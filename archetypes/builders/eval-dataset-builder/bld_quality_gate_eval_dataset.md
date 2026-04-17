---
id: p11_qg_eval_dataset
kind: quality_gate
pillar: P11
title: "Gate: eval_dataset"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "evaluation dataset — curated test case collections with declared schema, splits, and framework integration"
quality: 9.1
tags: [quality-gate, eval-dataset, P07, evals, splits, schema-fields]
tldr: "Pass/fail gate for eval_dataset artifacts: schema completeness, split integrity, size declaration, and framework integration."
density_score: 0.90
llm_function: GOVERN
---
# Gate: eval_dataset
## Definition
| Field | Value |
|---|---|
| metric | eval_dataset artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: eval_dataset` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p07_ds_[a-z][a-z0-9_]+$` | ID missing prefix, contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: p07_ds_foo` but file is `p07_ds_bar.md` |
| H04 | Kind equals literal `eval_dataset` | `kind: dataset` or `kind: golden_test` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `size`, `splits`, `schema_fields`, `name`, or `version` |
| H07 | schema_fields includes `input` and `expected_output` | Either field absent from schema_fields list |
| H08 | splits values sum to 1.0 | Sum deviates from 1.0 by more than 0.001 |
| H09 | size is a positive integer >= 1 | `size: 0`, `size: -5`, `size: "many"`, or field absent |
| H10 | Body has all 4 required sections | Missing `## Overview`, `## Schema`, `## Splits`, or `## Integration` |

## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Schema completeness | 1.0 | All schema_fields documented in ## Schema section with type and description |
| Split rationale | 1.0 | Each split has explicit rationale; eval-only datasets document why train is 0 |
| Framework integration | 1.0 | Loading pattern documented for target framework with code example |
| Source declaration | 1.0 | Data origin (human/synthetic/scraped/adversarial) declared with quality implication |
| Size credibility | 0.5 | Size is realistic for stated task type; growth strategy mentioned |
| Versioning strategy | 1.0 | Semver rules defined; schema migration path described for breaking changes |
| Task type specificity | 1.0 | Task type matches schema design (QA schema differs from classification schema) |
| Metadata richness | 0.5 | Optional fields (difficulty, category, tags) documented if present |
| Boundary clarity | 1.0 | Explicitly not a golden_test, benchmark, or scoring_rubric — collection contract stated |
| License declaration | 0.5 | Data license stated (especially for scraped or public data) |
| Refresh cadence | 0.5 | Update frequency declared or "frozen" status documented |
| Testability | 1.0 | Schema fields allow automated metric computation without additional context |

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
| conditions | Prototype dataset used only during local development, never shared or used in CI |
| approver | Author self-certification with comment explaining prototype-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — prototype datasets must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H08 (split math errors cause silent data leakage) |
