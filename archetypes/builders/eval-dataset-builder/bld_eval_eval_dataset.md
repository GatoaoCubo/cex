---
kind: quality_gate
id: p11_qg_eval_dataset
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of eval_dataset artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Gate: eval_dataset"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, eval-dataset, P07, evals, splits, schema-fields]
tldr: "Pass/fail gate for eval_dataset artifacts: schema completeness, split integrity, size declaration, and framework integration."
domain: "evaluation dataset — curated test case collections with declared schema, splits, and framework integration"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_eval_dataset
  - bld_instruction_eval_dataset
  - p11_qg_chunk_strategy
  - p11_qg_function_def
  - p11_qg_vision_tool
  - p11_qg_constraint_spec
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p03_sp_eval_dataset_builder
  - p11_qg_document_loader
---

## Quality Gate

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

## Examples

# Examples: eval-dataset-builder
## Golden Example
INPUT: "Create eval dataset for testing CEX artifact quality gate validation — 200 cases covering all 10 HARD gate checks"
OUTPUT:
```yaml
id: p07_ds_artifact_quality_gate_eval
kind: eval_dataset
pillar: P07
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "CEX Artifact Quality Gate Evaluation Dataset"
size: 200
splits:
  test: 1.0
schema_fields:
  - input
  - expected_output
  - metadata
quality: 8.9
tags: [eval_dataset, quality-gate, artifact-validation, P07]
tldr: "200 test cases covering all 10 HARD gates for CEX artifact validation, eval-only split"
description: "Evaluation dataset for CEX artifact quality gate validation covering all hard gate failure modes"
source: "synthetic"
framework: "braintrust"
task_type: "classification"
language: "en"
license: "MIT"
refresh_cadence: "on-demand"
```
## Overview
Tests the CEX artifact quality gate validator across all 10 HARD gate conditions. Used by builder_agent to verify validation logic and by CI to catch regression in gate checks.
## Schema
### input
Type: dict. The artifact under evaluation — `frontmatter` (dict) and `body` (string).
Example: `{"frontmatter": {"id": "p04_cli_foo", "kind": "cli_tool", "quality": null}, "body": "## Commands\n..."}`
### expected_output
Type: dict. Expected gate result — `passed` (bool), `failures` (list[string]), `score` (float or null).
Example: `{"passed": false, "failures": ["H05: quality is not null"], "score": null}`
### metadata
Type: dict. Case-level annotations for filtering and analysis.
Values: `{gate_id: "H05", failure_mode: "quality_not_null", difficulty: "easy", artifact_kind: "cli_tool"}`
## Splits
| Split | Percentage | Cases |
|-------|-----------|-------|
| test | 100% | 200 |

Pure evaluation — no training use for a rule-based validator. All cases are test-only.
## Integration
Framework: braintrust. Loading: `project.datasets.create(name="p07_ds_artifact_quality_gate_eval")` — iterate cases, call `validate_artifact(case["input"]["frontmatter"], case["input"]["body"])`, compare to `case["expected"]`.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_ds_ pattern (H02 pass)
- kind: eval_dataset (H04 pass)
- schema_fields has input + expected_output (H07 pass)
- splits: test: 1.0 sums to 1.0 (H08 pass)
- size: 200 positive integer (H09 pass)
- body has all 4 sections: Overview, Schema, Splits, Integration (H10 pass)
## Anti-Example
INPUT: "Create eval dataset for testing my chatbot"
BAD OUTPUT:
```yaml
id: chatbot-eval
kind: dataset
pillar: evals
name: My Chatbot Eval
size: "a lot"
quality: 8.5
tags: [eval]
```
Some test cases for my chatbot.
## Cases
- Ask it about weather
- Ask it about sports
FAILURES:
1. id: "chatbot-eval" has hyphens and no `p07_ds_` prefix -> H02 FAIL
2. kind: "dataset" not "eval_dataset" -> H04 FAIL
3. pillar: "evals" not "P07" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. size: "a lot" not a positive integer -> H09 FAIL
6. Missing fields: splits, schema_fields, version, created, updated, author, tldr -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
