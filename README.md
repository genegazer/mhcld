# mhcld — MH-CLD codebook transcription tools and output

This repository contains a small tool and supporting documentation for converting SAMHSA-style PUF codebook PDFs into structured Markdown, plus a transcription of the MH-CLD 2021 codebook.

Public-domain notice
This document is a markdown conversion of SAMHSA's MH-CLD manual, a U.S. Government work in the public domain (17 U.S.C. §105). No new copyright is claimed in this conversion.

Contents
- samhsa_codebook_to_md.py — Script that converts SAMHSA-style PUF codebook PDFs to Markdown.
- pdf-transcription-method.md — Method notes and best practices used when transcribing the codebook PDFs.
- MH-CLD-2021-codebook.md — Markdown transcription of the MH-CLD 2021 codebook (PUF).
- (optionally) LICENSE — Not included; content is public-domain per the notice above.

Quick summary
- The converter uses `pdftotext -layout` for column-preserving extraction and `pdfplumber` for coordinate-aware parsing (Appendix B recodes).
- It detects headings by font color, finds variable pages, merges multi-page variables, and validates outputs using arithmetic reconciliation and a number-preservation audit.
- The script exits nonzero if validation fails.

Dependencies
- poppler-utils (provides `pdftotext`)
- Python 3.8+
- pdfplumber (`pip install pdfplumber`)

Usage
```bash
python3 samhsa_codebook_to_md.py input.pdf [output.md]