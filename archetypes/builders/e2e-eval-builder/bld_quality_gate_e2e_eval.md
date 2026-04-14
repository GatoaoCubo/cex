---
id: p11_qg_e2e_eval
kind: quality_gate
pillar: P11
title: "Gate: e2e_eval"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "e2e_eval — end-to-end pipeline tests verifying full flow from input to final output"
quality: 9.0
tags: [quality-gate, e2e-eval, pipeline-testing, integration-test, P11]
tldr: "Gates for e2e_eval artifacts: validates pipeline coverage, stage completeness, fixture validity, assertion specificity, and cleanup protocol."
density_score: 0.91
llm_function: GOVERN
---
# Gate: e2e_eval
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: e2e_eval` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p07_e2e_[a-z][a-z0-9_]+$` | "ID fails e2e_eval namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"e2e_eval"` | "Kind is not 'e2e_eval'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, pipeline, stages, data_fixtures, expected_output, cleanup, version, created, author, tags | "Missing required field(s)" |
| H07 | `stages` list contains >= 2 stages (single-stage is a unit test, not e2e) | "e2e_eval must have >= 2 stages" |
| H08 | Each stage has both `name` and `expected` fields | "Stage missing 'name' or 'expected' assertion" |
| H09 | `data_fixtures` is non-empty and each fixture has a resolvable path or inline value | "Fixtures empty or unresolvable" |
| H10 | `cleanup` block defines post-run teardown actions (not empty) | "No cleanup protocol defined" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Pipeline coverage | 1.0 | All named agents/steps in the pipeline appear in stages |
| Stage assertion quality | 1.0 | Assertions are specific (not just "non-empty output") |
| Fixture realism | 1.0 | Input fixtures represent real-world data, not trivial stubs |
| Intermediate output checking | 1.0 | Intermediate stage outputs verified, not just final output |
| Environment specification | 1.0 | Required environment (model, API keys, infra) documented |
| Failure scenario coverage | 1.0 | At least one negative test case (bad input, timeout, error) |
| Cleanup completeness | 0.5 | Teardown covers files, DB state, and API side effects |
| Reproducibility | 1.0 | Test can be run multiple times with identical results |
| Boundary clarity | 0.5 | Explicitly not unit_eval (single component) or benchmark (perf) |
| Execution time estimate | 0.5 | Expected runtime documented so CI can set apownte timeout |
| Documentation | 0.5 | tldr states which pipeline and what behavior is being verified |
Weight sum: 1.0+1.0+1.0+1.0+1.0+1.0+0.5+1.0+0.5+0.5+0.5 = 9.0 -> normalize to 100%
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Pipeline under active development where stages are not yet stable |
| approver | QA lead approval required with written justification |
| audit_trail | Bypass logged to `records/audits/e2e_eval_bypass_{date}.md` |
| expiry | 48h; eval must be stabilized before pipeline ships to production |
| never_bypass | H01 (YAML parse failure), H05 (quality null invariant), H07 (single-stage eval is by definition not e2e) |
