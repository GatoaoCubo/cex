---
id: p11_qg_context_map
kind: quality_gate
pillar: P11
title: "Gate: context_map"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "context map -- DDD BC relationship diagram"
quality: null
tags: [quality-gate, context-map, P08, ddd, bounded-context]
tldr: "Pass/fail gate for context_map: id pattern, contexts table, relationships with DDD patterns, team coupling."
density_score: 0.90
llm_function: GOVERN
---

# Gate: context_map

## Definition

| Field | Value |
|---|---|
| metric | context_map artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: context_map` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p08_cm_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p08_cm_foo but file is p08_cm_bar.md |
| H04 | Kind equals literal `context_map` | kind: architecture_diagram or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | All relationships have upstream, downstream, pattern | Missing any of these three fields |
| H07 | Pattern values are valid DDD patterns | Using "integration" instead of ACL/OHS/etc. |
| H08 | contexts_count matches body count | Declared 5 but listed 3 |
| H09 | Body has all 4 required sections | Missing any of 4 sections |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| Pattern completeness | 1.0 | Every relationship has a valid DDD pattern |
| Integration type | 1.0 | sync/async/batch declared for all relationships |
| Team ownership | 1.0 | Owning team identified for each BC |
| Team coupling documented | 1.0 | Coupling level + risk + mitigation per relationship |
| ACL translation layers | 1.0 | ACL relationships identify the translator owner |
| OHS protocol reference | 1.0 | OHS relationships reference the published language/API |
| Conformist risk flag | 1.0 | Conformist relationships annotated with migration plan |
| System coverage | 1.0 | All BCs in the system are included |
| Boundary clarity | 1.0 | Explicitly NOT bounded_context, NOT component_map |
| tldr quality | 0.5 | tldr <= 160ch, includes system name and key patterns |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
