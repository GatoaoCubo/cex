---
pillar: P03
llm_function: REASON
phase_count: 3
version: 1.0.0
---

# Instructions: rag-source-builder

## Execution Protocol

### Phase 1: DISCOVER

**Goal**: Identify and qualify the external source before writing anything.

1. Extract the URL from user input. If absent, ask for it — no URL, no rag_source.
2. Validate URL format: must start with https:// or http://, contain a valid domain, no trailing spaces.
3. Determine the domain: what CEX domain does this source serve? (e.g., llm_providers, benchmarks, tooling).
4. Run brain_query [IF MCP]: `brain_query [IF MCP]("rag_source {domain} {url_domain}")` — check for existing entries to avoid duplicates.
5. Assess reliability: is this official docs? community content? API endpoint? Assign high/medium/low.
6. Identify format: html, json, api, pdf, or csv.
7. Generate source_slug: lowercase, underscores, max 30 chars. Example: anthropic_claude_api_docs.

**Checklist before Phase 2**:
- [ ] URL present and valid format
- [ ] domain identified
- [ ] no duplicate found in brain
- [ ] reliability and format assessed
- [ ] source_slug generated matching ^[a-z][a-z0-9_]+$

### Phase 2: COMPOSE

**Goal**: Produce the artifact using SCHEMA.md as ground truth.

1. Read SCHEMA.md — internalize all required fields and constraints.
2. Read OUTPUT_TEMPLATE.md — use as structural guide.
3. Fill frontmatter:
   - id: p01_rs_{source_slug}
   - kind: rag_source
   - pillar: P01
   - version: "1.0.0"
   - created + updated: today YYYY-MM-DD
   - author: who is producing this
   - url: validated URL from Phase 1
   - domain: from Phase 1
   - last_checked: today YYYY-MM-DD
   - quality: null (mandatory — never self-score)
   - tags: minimum 3, include "rag-source" and domain tag
   - tldr: <= 160 chars, dense summary of what this source provides
4. Write body sections:
   - **Source Description**: what is this source, what content does it contain, who maintains it
   - **Freshness Policy**: re-check frequency, staleness threshold, trigger conditions for refresh
   - **Extraction Notes**: recommended extraction method, format quirks, auth requirements if any
5. Check total byte count — must stay <= 1024 bytes in body.

### Phase 3: VALIDATE

**Goal**: Ensure all quality gates pass before delivering.

1. Read QUALITY_GATES.md.
2. Check all HARD gates sequentially:
   - H01: does the YAML frontmatter parse cleanly?
   - H02: does id match ^p01_rs_[a-z][a-z0-9_]+$?
   - H03: does id == filename stem?
   - H04: is kind exactly "rag_source"?
   - H05: is quality exactly null (not "null", not 0)?
   - H06: are all 5 required fields present (id, kind, url, domain, last_checked)?
   - H07: is body <= 1024 bytes?
3. Check SOFT gates and note any that fail.
4. Cross-check boundary: is this still a pointer? Does the body contain actual extracted content? If yes, remove it — rag_source is a pointer only.
5. If any HARD gate fails: fix before delivering. Do not deliver a failing artifact.
