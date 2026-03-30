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
INPUT: "Create entity memory for Firecrawl — the web scraping API service used by research_agent agent_node"
OUTPUT:
```yaml
id: p10_em_firecrawl
kind: entity_memory
pillar: P10
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
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
  - entity: "p10_em_shaka_agent_node"
    relation: "used_by"
  - entity: "p10_em_organization_core"
    relation: "integrated_into"
confidence: 0.92
last_referenced: "2026-03-29"
expiry: "2027-01-01"
quality: null
tags: [entity_memory, service, firecrawl, scraping, P10]
tldr: "Firecrawl: $19/mo web scraping service, 3000 credits/mo, REST API, used by research_agent for research enrichment."
description: "Firecrawl web scraping service — structured extraction, markdown output, 3000 monthly credits, integrated into research_agent agent_node."
```
## Overview
Firecrawl is a web scraping service used by research_agent to enrich product research with live marketplace data. Tracks pricing, credits, API details, and integration status.
## Attributes
| Key | Value | Source |
|-----|-------|--------|
| provider | Mendable / Firecrawl Inc | official site |
| pricing_tier | $19/mo | pricing page |
| monthly_credits | 3000 | MEMORY.md |
| api_endpoint | https://api.firecrawl.dev/v1 | docs |
| integration_status | active | MEMORY.md |
## Relationships
| Entity | Relation | Notes |
|--------|----------|-------|
| p10_em_shaka_agent_node | used_by | research_agent uses Firecrawl for research |
| p10_em_organization_core | integrated_into | API key stored in Railway env |
## Update Policy
Policy: overwrite — pricing and credit values change with plan changes.
Conflict: latest confirmed value wins; set confidence 0.9 only if from official source.
Staleness: re-verify pricing tier at expiry 2027-01-01.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p10_em_` pattern (H02 pass)
- kind: entity_memory (H04 pass)
- entity_type: service (H08 pass)
- 10 attributes — above minimum 3 (H07 pass)
- relationships: 2 typed links (S04 pass)
- confidence: 0.92 from primary source (S05 pass)
- update_policy: overwrite — matches volatile nature (S06 pass)
- expiry set (S07 pass)
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
3. entity_type: "ai_model" not in enum (use "tool" or "service") -> H08 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. attributes: 1 vague description, not a fact map -> S01 FAIL
6. tags: only 1 item, missing "entity_memory" -> H09 FAIL
7. Missing required fields: pillar, version, created, updated, author, tldr -> H06 FAIL
8. Body missing Overview, Attributes table, Relationships, Update Policy -> structure FAIL
9. Attribute value is an opinion, not a verifiable fact -> S02 FAIL
