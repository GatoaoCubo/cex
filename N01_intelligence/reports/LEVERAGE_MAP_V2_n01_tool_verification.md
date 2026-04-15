---
id: leverage_map_v2_n01_tool_verification
kind: knowledge_card
pillar: P04
title: LEVERAGE_MAP_V2 - N01 Tool Verification Cycle
version: 1.0
quality: null
tags: [leverage, tooling, n01, verification]
---

# N01 Intelligence - Tool Leverage Verification

## Verification

- Was the expected tool added? **YES.** `_tools/cex_web_fetch.py` exists in `_tools/` and is a standalone CLI fetcher.
- Evidence:
  - `Get-ChildItem _tools` shows `cex_web_fetch.py`
  - `_tools/cex_web_fetch.py` exposes `fetch()`, `html_to_text()`, and `arxiv_url()`
  - CLI surface: positional `url`, `--arxiv`, `--max-bytes`, `--raw`
- Does its API match N01's needs? **Partially.**
  - Matches the baseline need for live HTTP fetch and simple arXiv abstract retrieval.
  - Does not close the citation-validator gap.
  - Does not fetch PDF full text, render JavaScript, or extract structured metadata.

`rg -n "arxiv|web_fetch" _tools` also shows adjacent arXiv-related logic in `_tools/cex_source_harvester.py` and `_tools/cex_taxonomy_scout.py`, but those are not duplicate generic fetchers. They classify or scan sources; `cex_web_fetch.py` is the only minimal fetch-and-extract utility.

## New Wired Tools (since V1)

- `cex_web_fetch.py`
  - New capability: generic URL fetch with charset-aware decoding
  - New capability: HTML to plain-text reduction
  - New capability: `--arxiv` shortcut via `https://export.arxiv.org/abs/{id}`

This closes the "web search / ArXiv fetcher" gap only at a baseline ingestion level. It gives N01 a direct path to pull lightweight web content into research flows such as `cex_research.py`, but it does not yet turn fetched material into validated research evidence.

## Still Missing

- Citation validator
  - Still missing as a dedicated tool.
  - Current fetch output is unstructured text, so N01 still cannot check whether cited claims, authors, titles, venues, or source links are valid.
- PDF full-text extraction
  - `cex_web_fetch.py` targets HTML and arXiv abstract pages, not paper PDFs.
  - For N01, this is the main remaining blocker for paper-grade research.
- Metadata extraction
  - No structured parse of author, publish date, domain, DOI, venue, or citation list.
- Reliability controls
  - No retries, caching, rate limiting, or source provenance record in the fetcher itself.

## Next Iteration

1. Build `cex_citation_validator.py`
   - Priority: highest
   - Why: this is the gap explicitly left open by the previous cycle and the current fetcher does not address it.
2. Build `cex_pdf_extract.py`
   - Priority: high
   - Why: arXiv support is only partial until N01 can read paper bodies instead of just abstract pages.
3. Extend fetch output to emit structured provenance
   - Priority: medium
   - Why: N01 research artifacts need reusable metadata, not only raw plain text.

## 8F Trace

```text
=== 8F PIPELINE ===
F1 CONSTRAIN: mission=LEVERAGE_MAP_V2, output=N01_intelligence/reports/LEVERAGE_MAP_V2_n01_tool_verification.md
F2 BECOME: loaded N01 agent card + N01/routing rules
F3 INJECT: handoff, prior leverage-map report path, tool inventory, related _tools context
F4 REASON: verify existence, inspect API, check overlaps, then write evidence-based gap report
F5 CALL: used file reads, ripgrep, git status, compiler, signal writer
F6 PRODUCE: report drafted with Verification, New Wired Tools, Still Missing, Next Iteration
F7 GOVERN: corrected prior overclaim of "no duplicates" to "no duplicate generic fetcher"
F8 COLLABORATE: save, compile, commit, signal
===================
```
