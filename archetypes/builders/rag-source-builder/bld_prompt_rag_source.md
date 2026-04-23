---
id: p03_ins_rag_source
kind: instruction
pillar: P01
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: RAG Source Builder Instructions
target: "rag-source-builder agent"
phases_count: 4
prerequisites:
  - "A URL for the external source is available and syntactically valid"
  - "Caller has identified the domain this source serves (e.g. llm_providers, benchmarks, tooling)"
  - "Caller can estimate how frequently the source is updated (daily, weekly, monthly, static)"
validation_method: checklist
domain: rag_source
quality: 9.1
tags: [instruction, rag-source, P01, content, indexing, freshness, pointer]
idempotent: true
atomic: true
rollback: "Delete the produced pointer file. No content was fetched or stored."
dependencies: []
logging: true
tldr: "Catalog an external URL as an indexable rag_source pointer with freshness policy, reliability, and format — under 1024 bytes, no content."
density_score: 0.92
llm_function: REASON
related:
  - rag-source-builder
  - bld_architecture_rag_source
  - bld_knowledge_card_rag_source
  - p03_sp_rag_source_builder
  - bld_collaboration_rag_source
  - p11_qg_rag_source
  - p01_kc_rag_source
  - bld_schema_rag_source
  - bld_memory_rag_source
  - bld_examples_rag_source
---
## Context
A **rag_source** is a pointer record: it catalogs where authoritative external data lives so a retrieval pipeline can schedule crawls and index the content. The artifact contains metadata about the source — URL, domain, format, freshness schedule, reliability classification — but it does NOT contain any extracted content. The 1024-byte body limit enforces this constraint structurally.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `url` | string | Full URL of the external source |
| `domain` | string | CEX subject domain this source serves (e.g. `llm_providers`, `benchmarks`, `tooling`) |
| `description` | string | One sentence: what this source contains and why it is authoritative |
| `update_frequency` | string | How often the source publishes new content: `realtime`, `daily`, `weekly`, `monthly`, `static` |
**Output**
A single `.md` file with YAML frontmatter (5 required + optional recommended fields) and a minimal body. Total size must be <= 1024 bytes. Contains no extracted content from the source.
**Boundary rules**
- rag_source = pointer to external URL for crawling and indexing (this builder)
- knowledge_card = distilled content extracted from a source (different builder)
- context_doc = domain background context written for an agent to read at boot (different builder)
- embedding_config = configuration for how the vector index is built (different builder)
## Phases
### Phase 1: Discover — Qualify the Source
Identify, validate, and classify the source before writing anything.
```
URL validation:
  scheme must be https:// or http://  (reject ftp://, file://, data://)
  domain must be a public hostname    (reject localhost, 127.x, 192.168.x, 10.x)
  no authentication tokens in plaintext in the URL
Duplicate check:
  IF brain_query [IF MCP] available:
    brain_query("rag_source {{domain}} {{url_hostname}}")
    IF existing entry found for same URL: STOP and report duplicate
Format inference:
  url ends in .pdf                    -> format = pdf
  url ends in .csv or .tsv            -> format = csv
  url contains /api/ or /v1/ or /v2/  -> format = api
  url ends in .json                   -> format = json
  otherwise                           -> format = html
Reliability classification:
  high:    official government, academic, or primary-source domain
  medium:  established industry publication or known aggregator
  low:     user-generated content, forums, or unverified third parties
source_slug generation:
  lowercase, underscores, max 30 chars, describes the source
  must match: ^[a-z][a-z0-9_]+$
  example: anthropic_claude_api_docs, huggingface_model_hub
Staleness threshold (infer from update_frequency):
  realtime  -> "1h"
  daily     -> "24h"
  weekly    -> "7d"
  monthly   -> "30d"
  static    -> null (manual trigger only)
```
Checklist before proceeding to Phase 2:
- URL present and syntactically valid
- Domain identified
- No duplicate found in brain (or brain MCP unavailable — proceed with note)
- Format, reliability, and source_slug determined
### Phase 2: Classify — Boundary Check
Confirm this artifact is `rag_source` and not a sibling kind.
```
IF caller wants to store extracted or summarized content from the URL:
  RETURN "Route to knowledge-card-builder — distills content, not a pointer."
IF caller wants domain background context for an agent:
  RETURN "Route to context-doc-builder — writes agent context, not a source pointer."
IF caller wants to configure vectorization or embedding parameters:
  RETURN "Route to embedding-config-builder."
IF the source is an internal file, not a publicly accessible URL:
  RETURN "rag_source is for external URLs. Use a different kind for internal files."
IF URL is valid AND purpose is to register the source for crawling/indexing:
  PROCEED as rag_source
```
Deliverable: confirmed `kind: rag_source` with one-line justification.
### Phase 3: Compose — Build the Pointer Record
Assemble frontmatter and body. Stay within the 1024-byte body limit.
```
ID generation:
  id = "p01_rs_" + source_slug
  must match: ^p01_rs_[a-z][a-z0-9_]+$
  id must equal the filename stem (e.g. p01_rs_anthropic_claude_api_docs.md)
Frontmatter (5 required fields — MUST all be present):
  id:           p01_rs_{source_slug}
  kind:         rag_source
  url:          {validated_url}
  domain:       {domain}
  last_checked: {today YYYY-MM-DD}
Frontmatter (recommended additional fields):
  pillar:             P01
  version:            "1.0.0"
  created:            {today YYYY-MM-DD}
  updated:            {today YYYY-MM-DD}
  author:             {author}
  format:             {html|json|api|pdf|csv}
  reliability:        {high|medium|low}
  update_frequency:   {realtime|daily|weekly|monthly|static}
  staleness_threshold: {duration or null}
  quality:            null
  tags:               [rag-source, {domain}, {format}]  -- minimum 3 tags
  tldr:               {<= 160 chars summary of what this source provides}
Body (must stay within 1024 bytes total):
  ## Source Description
  What is this source? What content does it contain? Who maintains it?
  One short paragraph. Do NOT include extracted content.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[rag-source-builder]] | related | 0.43 |
| [[bld_architecture_rag_source]] | downstream | 0.43 |
| [[bld_knowledge_card_rag_source]] | related | 0.42 |
| [[p03_sp_rag_source_builder]] | downstream | 0.41 |
| [[bld_collaboration_rag_source]] | related | 0.40 |
| [[p11_qg_rag_source]] | downstream | 0.40 |
| [[p01_kc_rag_source]] | related | 0.39 |
| [[bld_schema_rag_source]] | downstream | 0.39 |
| [[bld_memory_rag_source]] | downstream | 0.36 |
| [[bld_examples_rag_source]] | downstream | 0.31 |
