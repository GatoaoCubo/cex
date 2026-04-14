---
id: p11_qg_effort_profile
kind: quality_gate
pillar: P11
title: "Gate: effort_profile"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "builder_agent"
domain: "effort and thinking level configuration for builder execution"
quality: 9.0
tags: [quality-gate, effort-profile, P09]
tldr: "Pass/fail gate for effort_profile artifacts: required fields, id pattern, body sections, configuration completeness."
density_score: 1.0
llm_function: GOVERN
---
# Gate: effort_profile
## Definition
| Field | Value |
|---|---|
| metric | effort_profile artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: effort_profile` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_effort_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `effort_profile` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing model, thinking_level, target_builder, quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Configuration or ## Levels or ## Integration |
| H08 | Body <= 4096 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Configuration completeness | 1.0 | Model + thinking level have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each configuration value has clear rationale |
| Level mapping | 1.0 | Correct model/thinking chosen for the builder complexity |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "effort_profile", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Model and thinking values specific to target builder |
| Testability | 0.5 | Configuration can be validated against dispatch system |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental effort and thinking level configuration for builder execution artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
