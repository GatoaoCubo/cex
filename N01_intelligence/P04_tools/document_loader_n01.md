---
id: document_loader_n01
kind: document_loader
pillar: P04
nucleus: n01
title: "N01 Multi-Source Document Loader"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [document_loader, ingestion, pdf, html, api, research, n01]
tldr: "Multi-format document ingestion for N01: PDF (academic papers, filings), HTML (web pages, news), JSON API responses, repo README files. Outputs normalized document chunks ready for synthesis."
density_score: 0.90
updated: "2026-04-17"
related:
  - bld_schema_api_reference
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - p04_document_loader_NAME
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_chunk_strategy
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
---

<!-- 8F: F1 constrain=P04/document_loader F2 become=document-loader-builder F3 inject=search_strategy_n01+api_reference_research_apis+sch_type_def_n01+chunk_strategy F4 reason=N01 must ingest documents from multiple formats without data loss F5 call=cex_compile F6 produce=document_loader_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Once `search_strategy_n01.md` identifies source URLs, this loader:
1. Fetches the raw document (respecting robots.txt and rate limits)
2. Extracts clean text from format-specific parsers
3. Normalizes to a canonical `DocumentChunk` schema
4. Outputs chunks ready for synthesis by `research_pipeline_n01.md`

## Supported Formats

| Format | Parser | Extraction Method | Quality Signal |
|--------|--------|------------------|----------------|
| HTML (web page) | BeautifulSoup / Playwright | `article`, `main`, `p` tag extraction | word count > 200 |
| PDF (paper/filing) | PyMuPDF / pdfplumber | text layer; OCR fallback | char count > 500 |
| JSON API response | native Python | field mapping per api_reference | non-null content |
| Markdown (.md) | native | strip frontmatter, extract body | heading count > 0 |
| Plain text (.txt) | native | strip excess whitespace | line count > 5 |
| GitHub repo | GitHub API | README.md + key source files | stars > 100 preferred |
| RSS / Atom feed | feedparser | item.summary + item.content | published_date present |

## DocumentChunk Schema

Output type (maps to `sch_type_def_n01.md` type `DocumentChunk`):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `chunk_id` | string | yes | `{source_domain}_{page}_{seq}` |
| `source_url` | string | yes | canonical source URL |
| `source_type` | enum | yes | html / pdf / json / md / txt / github / rss |
| `title` | string | yes | document or section title |
| `content` | string | yes | clean extracted text |
| `published_date` | ISO8601 | no | null if unavailable |
| `author` | string | no | null if unavailable |
| `word_count` | int | yes | len(content.split()) |
| `relevance_score` | float | yes | 0-1, from search source |
| `extraction_confidence` | float | yes | 0-1, parser success rate |
| `loaded_at` | ISO8601 | yes | ingestion timestamp |

## Extraction Pipeline

```
URL -> fetch(URL, timeout=30s)
  -> detect_format(response.headers, url_extension)
  -> parse(format, content)
  -> clean(text)              # strip nav, ads, boilerplate
  -> chunk(text, max=1500w)   # semantic chunking
  -> score(chunk)             # relevance + confidence
  -> filter(score > 0.5)
  -> return [DocumentChunk]
```

## Format-Specific Rules

### HTML

| Step | Rule |
|------|------|
| Fetch | Playwright for JS-heavy pages; requests for static |
| Extract | Priority: `<article>` > `<main>` > `<div class="content">` > `<body>` |
| Strip | nav, header, footer, sidebar, cookie banners, ads |
| Chunk | by heading (h2/h3 boundary) or 1500 words, whichever smaller |

### PDF

| Step | Rule |
|------|------|
| Fetch | direct download; check Content-Type: application/pdf |
| Extract | PyMuPDF text layer first; pdfplumber if empty; Tesseract OCR if both fail |
| Tables | detect with pdfplumber; output as markdown table |
| Chunk | by page (1 page = 1 chunk base) or 2000 chars |
| Metadata | extract title, author, year from PDF metadata or first-page heuristics |

### JSON API

| Step | Rule |
|------|------|
| Parse | field mapping defined in `api_reference_research_apis.md` per API |
| Normalize | all outputs -> DocumentChunk schema |
| Content | compose from: title + snippet/abstract + url |
| Dates | parse from API-specific date format -> ISO8601 |

## Rate Limiting

| Source Type | Delay Between Requests | Max Concurrent |
|-------------|----------------------|----------------|
| Web pages (HTML) | 1s | 3 |
| PDF downloads | 2s | 2 |
| API calls | per api_reference_research_apis.md | per API limit |
| GitHub API | 1s | 5 (authenticated) |

## Quality Filters

| Filter | Rule | Action on Fail |
|--------|------|----------------|
| Minimum content | word_count < 50 | discard chunk |
| Freshness | published_date > 90 days | tag as [STALE], include if no better |
| Extraction confidence | < 0.4 | discard; log warning |
| Duplicate URL | same source_url already in pool | skip |
| Paywall detected | content == subscription prompt | log, skip, try alternate source |

## Error Handling

| Error | Detection | Recovery |
|-------|-----------|---------|
| HTTP 403 / 429 | status code | wait 60s, retry once |
| Timeout | > 30s | skip URL, log |
| PDF parse failure | exception | OCR fallback, then discard |
| Empty extraction | word_count == 0 | discard, log |
| JS rendering failure | Playwright timeout | requests fallback |

## Comparison vs. Alternatives

| Tool | Formats | Cost | N01 Fit |
|------|---------|------|---------|
| LangChain loaders | HTML, PDF, many | free, complex | OK but heavy dependency |
| Firecrawl MCP | HTML, markdown | API cost | use for JS-heavy sites |
| This loader | HTML+PDF+JSON+MD+GitHub+RSS | no API cost | optimal for N01 scope |
| Jina Reader | HTML | API cost | good fallback for HTML |

## Integration

```
search_strategy_n01  -> [URLs]
  -> document_loader_n01  -> [DocumentChunks]
    -> research_pipeline_n01  -> synthesis -> output
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_api_reference]] | downstream | 0.35 |
| [[bld_schema_integration_guide]] | downstream | 0.34 |
| [[bld_schema_reranker_config]] | downstream | 0.33 |
| [[p04_document_loader_NAME]] | sibling | 0.33 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.31 |
| [[bld_schema_dataset_card]] | downstream | 0.31 |
| [[bld_schema_pitch_deck]] | downstream | 0.31 |
| [[bld_schema_chunk_strategy]] | downstream | 0.31 |
| [[bld_schema_usage_report]] | downstream | 0.30 |
| [[bld_schema_quickstart_guide]] | downstream | 0.30 |
