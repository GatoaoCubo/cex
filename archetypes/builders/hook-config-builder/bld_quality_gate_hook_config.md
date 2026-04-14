---
id: p11_qg_hook_config
kind: quality_gate
pillar: P11
title: "Gate: hook_config"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "builder_agent"
domain: "hook lifecycle configuration for builder execution"
quality: 9.0
tags: [quality-gate, hook-config, P04]
tldr: "Pass/fail gate for hook_config artifacts: required fields, id pattern, body sections, hook declaration completeness."
density_score: 0.90
llm_function: GOVERN
---
# Gate: hook_config
## Definition
| Field | Value |
|---|---|
| metric | hook_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: hook_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_hookconf_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `hook_config` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Hooks or ## Lifecycle or ## Integration |
| H08 | Body <= 4096 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Hook completeness | 1.0 | All hooks have phase, event, action, condition (no placeholders) |
| Condition quality | 1.0 | Each hook condition is specific and testsble |
| Phase coverage | 1.0 | Hooks cover relevant 8F phases for the target builder |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "hook_config", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Hooks and events specific to declared target builder |
| Testability | 0.5 | Hook declarations can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
