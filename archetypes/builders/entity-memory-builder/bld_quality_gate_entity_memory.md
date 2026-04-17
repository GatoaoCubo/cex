---
id: p11_qg_entity_memory
kind: quality_gate
pillar: P11
title: "Gate: entity_memory"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "entity memory — structured facts about named entities (people, tools, concepts, organizations, projects, services)"
quality: 9.0
tags: [quality-gate, entity-memory, P10, memory, entity, attributes]
tldr: "Pass/fail gate for entity_memory artifacts: entity_type validity, non-empty attributes, update_policy, confidence scoring, and relationship integrity."
density_score: 0.90
llm_function: GOVERN
---
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
