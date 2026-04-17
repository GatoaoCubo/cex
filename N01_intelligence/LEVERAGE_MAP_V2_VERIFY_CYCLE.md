---
id: leverage_map_v2_verify_cycle
title: N01 Leverage Map V2 — Verification Cycle Report
kind: knowledge_card
pillar: P01_knowledge
nucleus: N01
created: 2026-04-15
version: 2.0.1
quality: 9.1
tags: [leverage, tools, gap-analysis, n01-intel]
density_score: 1.0
---

# N01 Intelligence — Leverage Map V2 Verification Cycle

## Verification

### Was the expected tool added? (YES/NO + evidence)

**YES.** `_tools/cex_web_fetch.py` is present and functional.

**Evidence:**
- File exists: `{{USER_HOME}}\Documents\GitHub\cex\_tools\cex_web_fetch.py` ✓
- Implements HTTP fetch with HTML→text conversion ✓
- Supports both generic URLs and arXiv shortcuts ✓
- Handles charset detection and truncation ✓
- ASCII-only, per `.claude/rules/ascii-code-rule.md` ✓

### Does its API match N01's needs?

**PARTIALLY.** The tool is sufficient for *fetching* but insufficient for *validating* what was fetched.

#### API Capabilities (✓ = present, ✗ = missing)

| Feature | Status | Implementation |
|---------|--------|-----------------|
| HTTP GET with user-agent | ✓ | `fetch(url, timeout=20)` |
| Charset auto-detection | ✓ | Parses `Content-Type` header |
| HTML→plaintext conversion | ✓ | Regex strip scripts/styles/tags |
| ArXiv URL shortcut | ✓ | `arxiv_url(arxiv_id)` + `--arxiv` flag |
| Size limiting | ✓ | `--max-bytes` (default 20KB) |
| Raw HTML fallback | ✓ | `--raw` flag for JS-heavy sites |
| Timeout handling | ✓ | Configurable timeout (default 20s) |
| **Citation extraction** | ✗ | MISSING |
| **Metadata parsing** | ✗ | MISSING (author, date, venue) |
| **Citation validation** | ✗ | MISSING (DOI/ISBN/arXiv authenticity) |
| **Broken link detection** | ✗ | MISSING (HTTP status inference) |
| **Citation formatting** | ✗ | MISSING (APA/MLA/Chicago/BibTeX) |

---

## New Wired Tools (since V1)

### Primary New Tool
**`cex_web_fetch.py`** (72 lines, minimal deps)
- Fetch URL content for N01 research
- Output: plaintext with truncation
- Integration points: `cex_research.py`, `cex_taxonomy_scout.py` already use similar fetch patterns
- Maturity: Production-ready for basic fetch, not for citation work

### Secondary Integration Points
**`cex_taxonomy_scout.py`** (existing, now has fetch dependency)
- Uses urllib.request for source discovery (now can delegate to cex_web_fetch)
- Scans GitHub, arXiv, IETF, W3C, community sources
- Output: candidate kinds + evidence

**`cex_source_harvester.py`** (existing, now complementary)
- Extracts source references (URLs, arXiv, RFC, DOI) from repo
- Deduplicates via URL canonicalization + fuzzy matching
- Output: `.cex/P09_config/taxonomy_sources.yaml`

**`cex_research.py`** (existing, now has fetch foundation)
- Generates research prompts for taxonomy extraction
- Pipeline: research.py → cex_web_fetch.py → src_*.md → distill.py → kc_*.md
- Integrates with official docs fetching

---

## Still Missing (Leverage Gaps)

### Gap 1: Citation Extraction & Validation
**Why this matters:** N01 research outputs (KCs, briefs, analyses) cite sources. Without automated validation, citations are **unmaintained** — links break, DOI format drifts, metadata goes stale.

**What's needed:**
1. **Citation parser** — extract citations from fetched HTML/plaintext
   - Regex patterns for DOI, arXiv, ISBN, GitHub slugs, URLs
   - Support both implicit (URL in text) and explicit (citation blocks)
   - Example: "See [Liu et al. 2023](https://arxiv.org/abs/2303.18223)" → `{authors: [...], year: 2023, arxiv: 2303.18223}`

2. **Metadata extractor** — pull author, date, venue from fetched pages
   - Open Graph meta tags (og:title, og:author, og:publication_date)
   - Schema.org structured data (ScholarArticle, BlogPosting)
   - arXiv API (faster than scraping)
   - Fallback heuristics (h1/h2 for title, footer for date)

3. **Validation engine** — check citations for authenticity/liveness
   - HTTP HEAD to detect broken links (304, 404, 410, 451)
   - arXiv API lookup (verify ID format, retraction status)
   - DOI resolution (crossref.org API)
   - ISBN validation (checksum + OpenLibrary)

### Gap 2: Citation Formatting & Normalization
**Why this matters:** N01 outputs need consistent citation formats (APA, MLA, Chicago, BibTeX). Current solution: manual. Opportunity: generative.

**What's needed:**
1. **Citation formatter** — convert parsed citation objects to standard formats
   - Input: `{authors: [...], title, year, venue, doi, arxiv, url}`
   - Output: APA, MLA, Chicago, BibTeX, CSL-JSON
   - Validation: check that output is structurally valid (APA requires period, etc.)

2. **Template library** — per-format rules (author order, punctuation, abbreviations)
   - APA: "(Author, Year)" for in-text, full list at end
   - MLA: (Author Page) for in-text
   - Chicago: superscript numbers or author-date
   - BibTeX: raw LaTeX-safe fields

### Gap 3: Knowledge Base Linkage
**Why this matters:** N01's research feeds into P01_knowledge library. Citations should auto-link to existing KCs or flag new KC opportunities.

**What's needed:**
1. **Citation→Kind mapping** — when N01 cites a paper on "tokenization," auto-suggest that it feeds `kc_tokenization.md` in P01
2. **Missing KC detector** — if citation is novel (not mapped to existing KC), flag for N04 to create
3. **Citation aging** — track when each source was last accessed, flag stale references for refresh

### Gap 4: Multimodal Fetch (Low Priority)
**Why this matters:** arXiv PDFs, GitHub README.md rendering, social media embeds add richness to research.

**What's needed:**
1. **PDF extraction** (pypdf, pdfplumber) — extract text from arXiv PDFs instead of HTML
2. **Markdown rendering** — GitHub/GitLab README render to plaintext for better extraction
3. **Rate limiting** — respect API quotas (arXiv, GitHub, Crossref all have limits)

---

## Wiring Summary (V1 → V2)

| Layer | V1 Status | V2 Status | Tool |
|-------|-----------|-----------|------|
| **Fetch** | Manual (research.py requests) | ✓ Automated | `cex_web_fetch.py` |
| **Research** | ✓ Prompt template | ✓ Same | `cex_research.py` |
| **Taxonomy Scout** | ✓ Basic fetch | ✓ Enhanced | `cex_taxonomy_scout.py` |
| **Source Harvesting** | ✓ Regex extraction | ✓ Same | `cex_source_harvester.py` |
| **Citation Parsing** | ✗ MISSING | ✗ Still missing | — |
| **Citation Validation** | ✗ MISSING | ✗ Still missing | — |
| **Citation Formatting** | ✗ MISSING | ✗ Still missing | — |
| **Metadata Extraction** | ✗ MISSING | ✗ Still missing | — |

---

## Next Iteration (Prioritized)

### 1. **Citation Extractor (`cex_citation_parser.py`)** [CRITICAL]
**Purpose:** Parse fetched content and extract structured citations.

**Input:** Plaintext from `cex_web_fetch.py`

**Output:** JSON with parsed citations
```json
[
  {
    "authors": ["Liu, Z.", "Wang, X."],
    "title": "Attention Is All You Need",
    "year": 2017,
    "venue": "NeurIPS",
    "doi": "10.5555/3295222",
    "arxiv": "1706.03762",
    "url": "https://arxiv.org/abs/1706.03762"
  }
]
```

**Scope:** ~150 lines
- Regex for DOI: `\b10\.\d{4,}/\S+`
- Regex for arXiv: `\barxiv:\d{4}\.\d{4,}`
- Regex for URLs: `https?://[^\s)]+`
- Regex for author lists: `\b[A-Z][a-z]+(?:,| and) [A-Z]\.`
- Fallback heuristics for missing metadata

**Success criteria:**
- Extracts ≥80% of citations from academic papers (test vs. 10 arXiv papers)
- Zero false positives (random URLs should not be flagged as citations)
- Handles DOI, arXiv, ISBN, GitHub URLs

---

### 2. **Citation Validator (`cex_citation_validator.py`)** [HIGH]
**Purpose:** Check citations for authenticity, liveness, and completeness.

**Input:** Parsed citations from `cex_citation_parser.py`

**Output:** Validation status + metadata enrichment
```json
{
  "doi": "10.5555/3295222",
  "status": "valid",
  "http_status": 301,
  "metadata": {
    "authors": ["Vaswani, A.", ...],
    "title": "Attention Is All You Need",
    "year": 2017,
    "venue": "31st Conference on Neural Information Processing Systems"
  },
  "last_checked": "2026-04-15T12:34:56Z"
}
```

**Scope:** ~200 lines
- arXiv API: `https://export.arxiv.org/api/query?id_list={arxiv_id}`
- DOI resolution: `https://doi.org/{doi}` (follow 301 redirects)
- Crossref API: `https://api.crossref.org/works/{doi}` (metadata enrichment)
- HTTP HEAD for URL liveness
- ISBN checksum validation

**Success criteria:**
- Validates ≥95% of DOI/arXiv citations (test vs. 50 real citations)
- Detects broken links (404, 410) with zero false negatives
- Enriches metadata for ≥90% of academic papers

---

### 3. **Citation Formatter (`cex_citation_format.py`)** [MEDIUM]
**Purpose:** Convert parsed citations to standard formats (APA, MLA, Chicago, BibTeX).

**Input:** Validated citations from `cex_citation_validator.py`

**Output:** Formatted citation strings per requested style
```
# APA
Vaswani, A., et al. (2017). Attention is all you need. In Advances in neural information processing systems (pp. 5998-6008).

# BibTeX
@inproceedings{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and others},
  booktitle={NeurIPS},
  year={2017}
}
```

**Scope:** ~250 lines
- Template-based formatting per style
- Author abbreviation rules (et al. for ≥4 authors)
- Punctuation & capitalization rules per style
- Validation that output matches style spec

**Success criteria:**
- Formats all citation types (book, journal, conference, web)
- Output matches citation style guide examples (test vs. official examples)
- BibTeX output is valid (no unescaped special chars)

---

## Integration Points

Once built, these tools should wire into:

1. **N01 Research Pipeline**
   - `cex_research.py` output (src_*.md) → auto-extract citations → store in `N01_intelligence/research/citations/`

2. **N04 Knowledge Base**
   - Citation validator flags new entities → suggest new KCs
   - Citation formatter generates formatted references for KC outputs

3. **Continuous Monitoring**
   - Nightly job: re-validate all citations in `.cex/P09_config/taxonomy_sources.yaml`
   - Report broken links + suggest archival (Wayback Machine) or removal

4. **Memory & Learning**
   - Track citation patterns per domain (ML papers cite arXiv, management cite LinkedIn, etc.)
   - Learn domain-specific citation formats for future generation

---

## Conclusion

**cex_web_fetch.py is 50% of the solution.** It handles data *ingestion*. The missing 50% is data *validation* and *formatting* — transforming raw fetched content into trustworthy, reusable research artifacts.

The 3-tool sequence (parser → validator → formatter) is a **high-ROI pattern** that will dramatically increase N01's research output reliability and N04's citation hygiene across the repo.

**Recommendation:** Implement in order (1 → 2 → 3) with tests against real data (arXiv, DOI, GitHub) before wiring into research pipeline.
