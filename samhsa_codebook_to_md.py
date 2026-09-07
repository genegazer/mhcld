#!/usr/bin/env python3
"""
Convert a SAMHSA-style PUF codebook PDF into structured Markdown.

Usage:
    python3 samhsa_codebook_to_md.py input.pdf [output.md]

Works on the CBHSQ/SAMHSA codebook template (MH-CLD, TEDS-A, TEDS-D,
N-SSATS, etc.). Nothing about page numbers, variable names or section
headings is hardcoded -- all of it is detected from the document.

Requires: poppler-utils (pdftotext) and pdfplumber.
"""
import re
import subprocess
import sys

# --- template constants -------------------------------------------------
# Section headings in this template are bold Arial in a distinctive blue.
HEADING_RGB = (0.122, 0.255, 0.604)
HEADING_TOL = 0.05
# Appendix B column bands, in PDF points, measured from the document itself.
COL_VARIABLE, COL_ORIGINAL, COL_RECODE = 200, 370, 999
CODE_EDGE_ORIG, CODE_EDGE_REC = 220, 390

PAGENUM = re.compile(r"^\s*(\d{1,3}|[ivxlc]+|[A-Z]-\d+)\s*$")
VARTITLE = re.compile(r"^([A-Z][A-Z0-9_]{1,20}):\s+(.+)$")
FREQ_ROW = re.compile(r"^\s{2,}(-?\d+)\s{2,}(.+?)\s{2,}([\d,]+)\s+([\d.]+%)\s*$")
FREQ_TOTAL = re.compile(r"^\s+Total\s+([\d,]+)\s+([\d.]+%)\s*$")
FREQ_HEAD = re.compile(r"^\s*Value\s+Label\s+Frequency\s+%\s*$")
META = re.compile(r"^(Width:|Variable type:|A frequency distribution)")
APPX_A_ROW = re.compile(
    r"^\s*([A-Z][A-Z0-9_]*)\s{2,}(Numeric|Character)\s+(\d+)\s{2,}(.+?)\s*$")


# --- extraction ---------------------------------------------------------
def layout_pages(path):
    """Fixed-width text, one string per page. Preserves column alignment."""
    out = subprocess.run(["pdftotext", "-layout", path, "-"],
                         capture_output=True, text=True, check=True).stdout
    return out.split("\f")


def detect_headings(pdf):
    """Return the set of section-heading strings, found by font colour.

    Beats a hardcoded list: it adapts to whatever sections a given
    codebook happens to contain.
    """
    found = set()
    for page in pdf.pages:
        rows = {}
        for c in page.chars:
            rows.setdefault(round(c["top"]), []).append(c)
        for _, chars in rows.items():
            first = chars[0]
            colour = first.get("non_stroking_color") or ()
            if len(colour) != 3:
                continue
            if all(abs(a - b) < HEADING_TOL for a, b in zip(colour, HEADING_RGB)):
                text = "".join(c["text"] for c in chars).strip()
                if text and not VARTITLE.match(text):
                    found.add(text)
    return found


def strip_furniture(page):
    """Drop page-number lines; keep indentation (nested bullets need it)."""
    return [l.rstrip() for l in page.split("\n") if not PAGENUM.match(l)]


# --- narrative text -----------------------------------------------------
def blocks(lines):
    """Group runs of non-blank lines."""
    out, cur = [], []
    for l in lines:
        if l.strip():
            cur.append(l)
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def render_body(lines):
    """Render one run of body lines as paragraphs and (nested) bullets."""
    out, buf, bullets = [], [], []

    def flush_para():
        if buf:
            out.append(" ".join(buf) + "\n")
            buf.clear()

    def flush_bullets():
        if bullets:
            out.extend(bullets)
            out.append("")
            bullets.clear()

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith(("•", "◦", "·")):
            flush_para()
            # Bullets indented in the source are sub-bullets.
            indent = "  " if len(line) - len(stripped) >= 5 else ""
            bullets.append(indent + "- " + stripped.lstrip("•◦· ").strip())
        elif bullets:
            bullets[-1] += " " + line.strip()      # wrapped bullet
        else:
            buf.append(line.strip())
    flush_para()
    flush_bullets()
    return out


def prose(lines, headings, level=2):
    """Render narrative text, promoting detected headings.

    Headings sit on their own line but are NOT always followed by a blank
    line, so a block must be split wherever a heading appears inside it.
    """
    out = []
    for block in blocks(lines):
        seg = []
        for line in block:
            if line.strip() in headings:
                if seg:
                    out.extend(render_body(seg))
                    seg = []
                out.append(f"\n{'#' * level} {line.strip()}\n")
            else:
                seg.append(line)
        if seg:
            out.extend(render_body(seg))
    return out


# --- variable pages -----------------------------------------------------
def parse_variable(lines):
    """Split a variable page into title, description, frequency rows, meta."""
    title = lines[0].strip()
    i = 1
    # A long title wraps; the continuation line begins in lower case.
    while i < len(lines) and lines[i].strip() and lines[i].lstrip()[0].islower():
        title += " " + lines[i].strip()
        i += 1

    desc, rows, total, meta = [], [], None, []
    in_table = False
    for line in lines[i:]:
        if FREQ_HEAD.match(line):
            in_table = True
            continue
        row, tot = FREQ_ROW.match(line), FREQ_TOTAL.match(line)
        if in_table and row:
            rows.append(row.groups())
        elif in_table and tot:
            total = tot.groups()
        elif META.match(line.strip()):
            meta.append(line.strip())
        elif not in_table:
            desc.append(line)
    return {"title": title, "desc": desc, "rows": rows,
            "total": total, "meta": meta}


def render_variable(v, headings):
    name, _, label = v["title"].partition(":")
    out = [f"\n## {name.strip()} — {label.strip()}\n"]
    out += prose(v["desc"], headings, level=3)
    if v["rows"]:
        out += ["| Value | Label | Frequency | % |", "|---:|---|---:|---:|"]
        for value, lab, freq, pct in v["rows"]:
            out.append(f"| {value} | {lab.strip()} | {freq} | {pct} |")
        if v["total"]:
            out.append(f"| | **Total** | **{v['total'][0]}** | **{v['total'][1]}** |")
        out.append("")
    if v["meta"]:
        out.append("*" + " ".join(v["meta"]) + "*\n")
    return out


# --- appendices ---------------------------------------------------------
def render_appendix_a(pages):
    out = ["| Variable | Type | Length | Label |", "|---|---|---:|---|"]
    for page in pages:
        for line in strip_furniture(page):
            m = APPX_A_ROW.match(line)
            if m:
                out.append("| {} | {} | {} | {} |".format(*m.groups()))
            elif (len(out) > 2 and line.strip()
                  and line.startswith(" " * 30)):
                out[-1] = out[-1][:-2] + " " + line.strip() + " |"   # wrapped
    return out + [""]


def render_appendix_b(pdf, page_indices):
    """Parse the three-column recode table using true word x-coordinates.

    Character-position slicing FAILS here: the column offsets shift from
    page to page. Word x-coordinates are stable.
    """
    entries, cur = [], None

    def add(col, words, code_edge):
        if not words:
            return
        first = words[0]
        if first["text"].isdigit() and first["x0"] < code_edge:
            col.append([first["text"], " ".join(w["text"] for w in words[1:])])
        else:                                   # wrapped label, or code-less cell
            text = " ".join(w["text"] for w in words)
            if col:
                col[-1][1] += " " + text
            else:
                col.append(["", text])

    for pno in page_indices:
        rows = {}
        for w in pdf.pages[pno].extract_words():
            rows.setdefault(round(w["top"] / 3), []).append(w)   # cluster by line
        for key in sorted(rows):
            ws = sorted(rows[key], key=lambda w: w["x0"])
            head = ws[0]["text"]
            # Page furniture is a line on its own -- a bare "12" at the start
            # of a row is a code value, not a page number.
            if head in ("Appendix", "Variable") or (len(ws) == 1 and PAGENUM.match(head)):
                continue
            c1 = [w for w in ws if w["x0"] < COL_VARIABLE]
            c2 = [w for w in ws if COL_VARIABLE <= w["x0"] < COL_ORIGINAL]
            c3 = [w for w in ws if COL_ORIGINAL <= w["x0"] < COL_RECODE]
            if c1:
                label = " ".join(w["text"] for w in c1)
                if re.fullmatch(r"[A-Z][A-Z0-9_]+", c1[0]["text"]):
                    cur = {"name": c1[0]["text"],
                           "sub": [label[len(c1[0]["text"]):].strip()],
                           "orig": [], "rec": []}
                    entries.append(cur)
                elif cur is not None:
                    cur["sub"].append(label)
            if cur is None:
                continue
            add(cur["orig"], c2, CODE_EDGE_ORIG)
            add(cur["rec"], c3, CODE_EDGE_REC)

    out = []
    for e in entries:
        sub = " ".join(s for s in e["sub"] if s).strip()
        out.append(f"\n### {e['name']}" + (f" — {sub}" if sub else "") + "\n")
        out += ["| Original code | Original label | Recode | Recoded label |",
                "|---:|---|---:|---|"]
        for i in range(max(len(e["orig"]), len(e["rec"]))):
            o = e["orig"][i] if i < len(e["orig"]) else ["", ""]
            r = e["rec"][i] if i < len(e["rec"]) else ["", ""]
            out.append(f"| {o[0]} | {o[1]} | {r[0]} | {r[1]} |")
        out.append("")
    return out


def render_exclusions(lines):
    """The 'States excluded' table: a year plus a wrapping list of states.

    Returns (markdown, remaining_lines) so the caller does not also render
    the raw table text as a paragraph.
    """
    out, rows, kept = [], [], []
    seen_head = False
    for line in lines:
        if re.match(r"^\s*Year\s+States\s*$", line):
            seen_head = True
            continue
        if not seen_head:
            kept.append(line)
            continue
        if not line.strip():
            continue
        m = re.match(r"^\s*(\d{4})\s+(.+)$", line)
        if m:
            rows.append([m.group(1), m.group(2).strip()])
        elif rows:
            rows[-1][1] += " " + line.strip()
        else:
            kept.append(line)
    if rows:
        out += ["| Year | States |", "|---|---|"]
        out += [f"| {y} | {s} |" for y, s in rows]
        out.append("")
    else:
        kept = lines
    return out, kept


# --- page classification ------------------------------------------------
def classify(pages):
    """Locate variable pages and appendices without hardcoding page numbers."""
    var_pages, appx = [], {}
    for i, page in enumerate(pages):
        lines = [l for l in page.split("\n") if l.strip()]
        if not lines:
            continue
        first = lines[0].strip()
        m = re.match(r"^Appendix ([A-Z])\.", first)
        if m:
            appx.setdefault(m.group(1), []).append(i)
        elif VARTITLE.match(first):
            var_pages.append(i)
    # An appendix continues onto pages that start no new appendix.
    for letter, starts in appx.items():
        start = starts[0]
        end = start
        while end + 1 < len(pages) and not re.match(
                r"^\s*Appendix [A-Z]\.",
                pages[end + 1].lstrip().split("\n")[0]):
            nxt = [l for l in pages[end + 1].split("\n") if l.strip()]
            if not nxt or VARTITLE.match(nxt[0].strip()):
                break
            end += 1
        appx[letter] = list(range(start, end + 1))
    return var_pages, appx


# --- validation ---------------------------------------------------------
def validate(md, pages):
    """Arithmetic and completeness checks. Prints a report; returns bool."""
    ok = True
    body = md.split("\n# Appendices")[0]
    checked = bad = 0
    for section in re.split(r"\n## ", body):
        rows = re.findall(r"^\| (-?\d+) \| .*? \| ([\d,]+) \| [\d.]+% \|$",
                          section, re.M)
        tot = re.search(r"\*\*Total\*\* \| \*\*([\d,]+)\*\*", section)
        if not rows or not tot:
            continue
        checked += 1
        summed = sum(int(f.replace(",", "")) for _, f in rows)
        printed = int(tot.group(1).replace(",", ""))
        if summed != printed:
            bad += 1
            ok = False
            print(f"  MISMATCH {section.splitlines()[0]}: "
                  f"rows={summed:,} vs printed total={printed:,}")
    print(f"  frequency tables: {checked} checked, {bad} mismatched")

    source = "\n".join(pages)
    nums = set(re.findall(r"\b\d{1,3}(?:,\d{3})+\b", source))
    missing = sorted(n for n in nums if n not in md)
    print(f"  large numbers: {len(nums)} in PDF, {len(missing)} missing from output")
    if missing:
        ok = False
        print(f"    missing: {missing[:10]}")
    return ok


# --- main ---------------------------------------------------------------
def convert(src, dest):
    import pdfplumber

    pages = layout_pages(src)
    with pdfplumber.open(src) as pdf:
        headings = detect_headings(pdf)
        var_pages, appx = classify(pages)
        first_var = min(var_pages)

        doc = []
        # Front matter: everything before the first variable page, minus the
        # cover and any section-divider pages.
        for i in range(1, first_var):
            lines = strip_furniture(pages[i])
            if len([l for l in lines if l.strip()]) <= 2:
                continue                      # divider page
            table, lines = render_exclusions(lines)
            doc += prose(lines, headings)
            doc += table
        if doc and doc[0].strip().startswith("## "):
            doc[0] = doc[0].replace("## ", "# ", 1)   # document title

        doc += ["\n# Variable Descriptions and Frequencies\n"]
        merged = []
        for i in var_pages:
            v = parse_variable(strip_furniture(pages[i]))
            name = v["title"].split(":")[0]
            if merged and merged[-1]["title"].split(":")[0] == name:
                merged[-1]["rows"] += v["rows"]        # variable spans pages
                merged[-1]["total"] = v["total"] or merged[-1]["total"]
                merged[-1]["meta"] = v["meta"] or merged[-1]["meta"]
            else:
                merged.append(v)
        for v in merged:
            doc += render_variable(v, headings)

        if appx:
            doc += ["\n# Appendices\n"]
        for letter in sorted(appx):
            idx = appx[letter]
            title = pages[idx[0]].lstrip().split("\n")[0].strip()
            doc.append(f"\n## {title}\n")
            if letter == "A":
                doc += render_appendix_a([pages[i] for i in idx])
            elif letter == "B":
                doc += render_appendix_b(pdf, idx)
            else:
                lines = strip_furniture(pages[idx[0]])[1:]
                for i in idx[1:]:
                    lines += strip_furniture(pages[i])
                doc += prose(lines, headings, level=3)

    md = re.sub(r"\n{3,}", "\n\n", "\n".join(doc)).strip() + "\n"
    with open(dest, "w") as f:
        f.write(md)

    print(f"wrote {dest} ({len(md):,} chars, "
          f"{len(merged)} variables, {len(appx)} appendices)")
    print("validation:")
    return validate(md, pages)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.pdf$", ".md", source)
    sys.exit(0 if convert(source, target) else 1)
