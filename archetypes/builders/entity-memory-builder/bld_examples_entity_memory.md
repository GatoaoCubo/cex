---
kind: examples
id: bld_examples_entity_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of entity_memory artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: entity-memory-builder
## Golden Example
INPUT: "Create entity memory for Firecrawl — the web scraping API service used by SHAKA satellite"
OUTPUT:
```yaml
id: p10_em_firecrawl
kind: entity_memory
pillar: P10
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "Firecrawl"
entity_type: service
attributes:
  provider: "Mendable / Firecrawl Inc"
  pricing_tier: "$19/mo"
  monthly_credits: "3000"
  api_endpoint: "https://api.firecrawl.dev/v1"
  primary_use: "web scraping and structured extraction"
  supported_formats: "markdown, extract, screenshot"
  credit_per_scrape_shopee: "3"
  credit_per_scrape_standard: "1"
  integration_status: "active"
  key_env_var: "FIRECRAWL_API_KEY"
update_policy: overwrite
source: "MEMORY.md + Firecrawl official docs"
relationships:
  - entity: "p10_em_shaka_satellite"
    relation: "used_by"
  - entity: "p10_em_codexa_core"
    relation: "integrated_into"
confidence: 0.92
last_referenced: "2026-03-29"
expiry: "2027-01-01"
quality: null
tags: [entity_memory, service, firecrawl, scraping, P10]
tldr: "Firecrawl: $19/mo web scraping service, 3000 credits/mo, REST API, used by SHAKA for research enrichment."
description: "Firecrawl web scraping service — structured extraction, markdown output, 3000 monthly credits, integrated into SHAKA satellite."
```
## Overview
Firecrawl is a web scraping and structured data extraction service used by the SHAKA satellite to enrich product research with live marketplace data. Tracks pricing, credits, API details, and integration status.
## Attributes
| Key | Value | Type | Source |
|-----|-------|------|--------|
| provider | Mendable / Firecrawl Inc | string | official site |
| pricing_tier | $19/mo | string | pricing page |
| monthly_credits | 3000 | string | MEMORY.md |
| api_endpoint | https://api.firecrawl.dev/v1 | url | docs |
| integration_status | active | enum | MEMORY.md |
## Relationships
| Entity | Relation | Direction | Notes |
|--------|----------|-----------|-------|
| p10_em_shaka_satellite | used_by | outbound | SHAKA uses Firecrawl for research |
| p10_em_codexa_core | integrated_into | outbound | API key stored in Railway env |
## Update Policy
Policy: overwrite — pricing and credit values change with plan changes.
Conflict: latest confirmed value wins; update confidence to 0.9 only if from official source.
Staleness: check expiry 2027-01-01; re-verify pricing tier annually.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p10_em_` pattern (H02 pass)
- kind: entity_memory (H04 pass)
- entity_type: service — correct for SaaS API (H08 pass)
- 10 attributes — well above minimum 3 (H07 pass, S01 high)
- relationships: 2 links with typed relation verbs (S04 pass)
- confidence: 0.92 from primary+verified source (S05 pass)
- update_policy: overwrite — matches volatile pricing nature (S06 pass)
- expiry set — service pricing can change (S07 pass)
- tldr: 96 chars <= 160, includes name + 3 key facts (S08 pass)
- tags: 5 items, includes "entity_memory" (H09 pass)
## Anti-Example
INPUT: "Create entity memory for Claude"
BAD OUTPUT:
```yaml
id: claude-ai
kind: memory
name: Claude AI
entity_type: ai_model
attributes:
  description: "A very good AI assistant made by Anthropic that helps with many tasks"
quality: 8.5
tags: [ai]
```
Claude is an AI assistant.
FAILURES:
1. id: "claude-ai" has hyphens and no `p10_em_` prefix -> H02 FAIL
2. kind: "memory" not "entity_memory" -> H04 FAIL
3. entity_type: "ai_model" not in enum (should be "tool" or "service") -> H08 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. attributes: 1 vague description, not a fact map -> H07 borderline, S01 FAIL
6. tags: only 1 item, missing "entity_memory" -> H09 FAIL
7. Missing required fields: pillar, version, created, updated, author, tldr -> H06 FAIL
8. Body missing Overview, Attributes table, Relationships, Update Policy -> structure FAIL
9. Attribute value is an opinion/description, not a verifiable fact -> S02 FAIL
10. No update_policy declared -> S06 FAIL
