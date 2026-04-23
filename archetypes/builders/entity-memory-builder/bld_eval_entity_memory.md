---
kind: quality_gate
id: p11_qg_entity_memory
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of entity_memory artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: entity_memory"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, entity-memory, P10, memory, entity, attributes]
tldr: "Pass/fail gate for entity_memory artifacts: entity_type validity, non-empty attributes, update_policy, confidence scoring, and relationship integrity."
domain: "entity memory — structured facts about named entities (people, tools, concepts, organizations, projects, services)"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_entity_memory
  - bld_instruction_entity_memory
  - entity-memory-builder
  - bld_architecture_entity_memory
  - p03_sp_entity_memory_builder
  - bld_schema_entity_memory
  - bld_collaboration_entity_memory
  - p11_qg_chunk_strategy
  - bld_knowledge_card_entity_memory
  - bld_output_template_entity_memory
---

## Quality Gate

# Gate: entity_memory
## Definition
| Field | Value |
|---|---|
| metric | entity_memory artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: entity_memory` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p10_em_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, or missing prefix |
| H03 | ID equals filename stem | `id: p10_em_stripe` but file is `p10_entity_stripe.md` |
| H04 | Kind equals literal `entity_memory` | `kind: memory` or `kind: learning_record` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `entity_type`, `attributes`, `name`, `tldr` |
| H07 | Attributes map is non-empty | `attributes: {}` or attributes field absent |
| H08 | entity_type is one of declared enum values | `entity_type: module` or unrecognized value |
| H09 | Tags list has >= 3 items and includes "entity_memory" | Only 2 tags, or missing "entity_memory" tag |
| H10 | Artifact is entity memory, not learning_record | Contains outcome/lesson fields (impact_score, decay_rate) — wrong kind |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Attribute completeness | 1.0 | >= 3 meaningful attributes covering entity identity, status, and provenance |
| Attribute value quality | 1.0 | Values are specific facts, not vague descriptions; dates formatted YYYY-MM-DD |
| Entity type precision | 1.0 | entity_type matches actual nature of entity; not "concept" for a concrete tool |
| Relationship mapping | 1.0 | relationships field present with at least 1 link; relation type is a meaningful verb |
| Confidence scoring | 0.5 | confidence float present and in 0.0-1.0 range with plausible value |
| Update policy | 1.0 | update_policy declared and apownte for entity volatility |
| Source attribution | 0.5 | source field present; identifies where attributes came from |
| Expiry/staleness | 0.5 | expiry set for volatile entities (tools, services); null acceptable for stable concepts |
| Boundary clarity | 1.0 | Not a learning_record (no outcome/lesson), not session_state (no ephemeral runtime data) |
| tldr quality | 1.0 | <= 160 chars, includes entity name and 2+ key facts |
| Description quality | 0.5 | <= 200 chars, distinct from tldr, adds context |
| Tags relevance | 0.5 | Tags include entity_type value and domain keywords |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Stub entity record used as placeholder during active research; not yet published |
| approver | Author self-certification with comment noting stub status |
| audit_trail | Bypass note in frontmatter comment with resolution date |
| expiry | 7d — stubs must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H10 (wrong kind corrupts memory index) |

## Examples

# Examples: entity-memory-builder
## Golden Example
INPUT: "Create entity memory for Firecrawl — the web scraping API service used by research_agent agent_group"
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
  - entity: "p10_em_shaka_agent_group"
    relation: "used_by"
  - entity: "p10_em_organization_core"
    relation: "integrated_into"
confidence: 0.92
last_referenced: "2026-03-29"
expiry: "2027-01-01"
quality: 8.9
tags: [entity_memory, service, firecrawl, scraping, P10]
tldr: "Firecrawl: $19/mo web scraping service, 3000 credits/mo, REST API, used by research_agent for research enrichment."
description: "Firecrawl web scraping service — structured extraction, markdown output, 3000 monthly credits, integrated into research_agent agent_group."
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
| p10_em_shaka_agent_group | used_by | research_agent uses Firecrawl for research |
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
