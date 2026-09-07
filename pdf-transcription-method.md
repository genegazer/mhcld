# Transcribing codebook PDFs: method notes

Written up from the MH-CLD 2021 job so it can be repeated. The companion
script is `samhsa_codebook_to_md.py`.

The short version: **diagnose before you reach for OCR**, parse tables by
*position* rather than by eye, and **prove the output is right with
arithmetic** instead of spot-checking it.

---

## Step 1. Find out what you actually have

Never start with OCR. Run this first — it takes seconds and decides
everything downstream:

```bash
pdfinfo   file.pdf     # pages, producer, size
pdffonts  file.pdf     # THE key question: is there a text layer?
pdfimages -list file.pdf   # is the page a scanned photograph?
pdftotext -layout -f 8 -l 8 file.pdf - | head -30   # sample a real page
```

Read `pdffonts` like this:

| What you see | What it means | What to do |
|---|---|---|
| Fonts listed, `emb: yes`, `uni: yes` | Born-digital, exact text | Extract directly. **Do not OCR.** |
| Empty table, `pdfimages` shows one big image per page | Scanned | OCR with Tesseract |
| Fonts listed but `emb: no`, "Custom" or Identity-H encoding with no map | Text layer may be garbled | Sample it; if mojibake, rasterize + OCR |

For the MH-CLD file: 57 pages, producer `SAS Institute Inc.`, every font
embedded with Unicode maps, and `pdfimages` returned **zero** images. That is
a born-digital PDF. Its text layer is the original characters, not a guess.

**Why this matters so much here.** Running OCR on a file like this makes the
result *worse*. Nearly every page is a table of six- and seven-digit counts,
and OCR is exactly where digits get misread — `6,516,527` becoming `6,516,627`
is silent, plausible, and fatal to an analysis. Tesseract was available and
would have run happily. Checking `pdffonts` first is what avoids that.

## Step 2. Extract with the right tool for the job

Two tools, used for different things:

- **`pdftotext -layout`** — preserves column alignment as fixed-width text.
  Good for regular tables (the `Value / Label / Frequency / %` blocks) where
  you can match rows with a regex.
- **`pdfplumber`** — gives each word an `x0` coordinate. Reach for it when
  column positions are irregular.

The `-layout` flag is not optional. Without it, multi-column tables collapse
into unusable word order.

## Step 3. Parse tables by coordinate, not by character offset

This is the one real trap.

The obvious approach for a three-column table is slicing by character
position: `line[:32]`, `line[32:67]`, `line[67:]`. It worked on the first
page of Appendix B and silently corrupted the rest — **the column offsets
shift from page to page.** Character offsets in `-layout` output depend on
the widest content on that page, so they are not stable across a document.

Word x-coordinates are stable. Dump them to find the real column bands:

```python
import pdfplumber
with pdfplumber.open(path) as pdf:
    page = pdf.pages[55]
    rows = {}
    for w in page.extract_words():
        rows.setdefault(round(w["top"] / 3), []).append(w)   # cluster into lines
    for k in sorted(rows)[:6]:
        ws = sorted(rows[k], key=lambda w: w["x0"])
        print(" | ".join(f'{round(w["x0"])}:{w["text"]}' for w in ws))
```

That printed clean bands for this template: variable `< 200pt`, original
codes `200–370pt`, recodes `≥ 370pt`. Two further rules handle wrapped cells:

- A **numeric** token at a column's left edge starts a new entry.
- Anything further right continues the previous label.

That second rule is what correctly rejoins `Self-contained special education`
+ `class` into one cell, and it must check *numeric* — otherwise a text cell
with no code, like AGE's `Continuous (0–85)`, gets mistaken for a code.

## Step 4. Detect structure instead of hardcoding it

The first pass hardcoded page numbers and a list of section headings. That
works once and breaks on the next file. The rewritten script derives
everything:

- **Headings** — in this template they are bold Arial in blue
  `(0.122, 0.255, 0.604)` while body text is black Times. Scan
  `page.chars` for that fill colour. This adapts to whatever sections a
  given codebook contains.
- **Variable pages** — first line matches `^[A-Z][A-Z0-9_]{1,20}:\s+(.+)$`.
- **Appendices** — first line matches `^Appendix ([A-Z])\.`, running until
  the next appendix starts.
- **Variables spanning two pages** — merge consecutive pages whose variable
  name repeats. (STATEFIP does this; its 50 rows are split across two pages
  and a naive parser keeps only the second half.)

## Step 5. Prove it, don't eyeball it

Spot-checking a 57-page numeric document tells you almost nothing. Two
checks did the real work:

**Arithmetic reconciliation.** Every frequency table has a printed total.
Sum the parsed rows and compare. If a row was dropped, misparsed, or
duplicated, the sum diverges. All 39 tables reconciled to 6,516,527.

```python
summed = sum(int(f.replace(",", "")) for _, f in rows)
assert summed == int(printed_total.replace(",", ""))
```

**Number-preservation audit.** Pull every comma-formatted number out of the
raw PDF text and confirm each appears in the output. Catches whole sections
silently dropped. 226 of 226 survived.

```python
nums = set(re.findall(r"\b\d{1,3}(?:,\d{3})+\b", raw_text))
missing = [n for n in nums if n not in markdown]
```

Both are built into the script, which exits non-zero if either fails.

## Bugs this process caught

Every one of these produced output that *looked* fine:

| Bug | Symptom | Cause |
|---|---|---|
| Truncated `EMPLOY` title | Label ended mid-phrase | Title wraps to a second line |
| Appendix A rows missing | 6 of 40 variables | Rows on one page have a leading space, the next page doesn't |
| Appendix B scrambled | Codes and labels interleaved | Character-offset slicing; offsets shift per page |
| Flattened sub-bullets | RACE nesting lost | `.strip()` applied before checking indentation |
| Headings swallowed | Four sections vanished into a paragraph | Headings aren't separated from body text by a blank line |
| Table rows skipped | Appendix B nearly empty | Page-number regex `\d{1,3}` also matched code cells like `12` |

The last one is the cautionary tale: a filter meant for page furniture
matched real data. Guard such filters on the line having a *single* token.

## Reusing this

```bash
python3 samhsa_codebook_to_md.py input.pdf output.md
```

It should work as-is on other CBHSQ/SAMHSA codebooks — TEDS-A, TEDS-D,
N-SSATS, other MH-CLD years — since they share this template. Check the
validation report it prints; if a different template moves the columns,
re-run the coordinate dump in Step 3 and update the four constants at the
top of the script (`HEADING_RGB`, `COL_VARIABLE`, `COL_ORIGINAL`,
`CODE_EDGE_*`).

If the numbers don't reconcile, do not use the output.

## Applying this to a scanned PDF instead

If `pdffonts` comes back empty, the process changes shape:

```bash
pdftoppm -png -r 300 file.pdf /tmp/page     # 300 DPI, not 150, for small type
tesseract /tmp/page-01.png out --psm 6      # psm 6 = uniform block of text
```

Two things to know. Raise DPI to 300+ for dense numeric tables; 150 is fine
for prose but loses thin digits. And OCR output cannot be trusted the way a
text layer can — the arithmetic reconciliation in Step 5 stops being a nice
check and becomes mandatory, because digit substitution is the characteristic
OCR failure and it is invisible on inspection.
