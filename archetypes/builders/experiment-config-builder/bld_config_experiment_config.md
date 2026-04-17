---
kind: config
id: bld_config_experiment_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for experiment_config
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, config, P09]
tldr: "Naming conventions, paths, size limits, and enum values for experiment_config production."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---
# Config: experiment_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_ec_{name_slug}.yaml` | `p09_ec_code_review_prompt_style.yaml` |
| Builder directory | kebab-case | `experiment-config-builder/` |
| Frontmatter fields | snake_case | `traffic_split`, `primary_metric` |
| Name slug | snake_case, lowercase, no hyphens | `code_review_prompt_style`, `llm_judge_v2` |
| Variant names | snake_case, lowercase | `control`, `concise_prompt`, `treatment_a` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: first variant MUST be "control". Any other name = HARD FAIL.

## File Paths
1. Output: `P09_config/examples/p09_ec_{name_slug}.md`
2. Compiled: `P09_config/compiled/p09_ec_{name_slug}.yaml`
3. Builder ISOs: `archetypes/builders/experiment-config-builder/`

## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5500 bytes
3. Density: >= 0.85 (no filler)

## Status Enum
| Value | Meaning | When to use |
|-------|---------|-------------|
| draft | Spec complete; not yet launched | Default for new experiments |
| running | Traffic flowing; collecting data | After launch |
| paused | Guardrail breach or operational hold | After incident or anomaly |
| concluded | Decision made; winner documented | After significance + min runtime |

## Traffic Split Rules
| Rule | Value |
|------|-------|
| Must sum to | 100 (integer percentages only) |
| Preferred split | 50/50 for two-variant experiments |
| Minimum arm size | 10% (below this, statistical power degrades severely) |
| Maximum arms | 5 (more than 5 variants requires separate Bonferroni correction) |

## Statistical Defaults
| Parameter | Default | Notes |
|-----------|---------|-------|
| significance_threshold | 0.05 | alpha = 5pct; two-tailed |
| power | 0.80 | 80pct power (standard industry default) |
| duration_days (minimum) | 7 | Novelty effect mitigation |
| duration_days (maximum) | 28 | Prevents indefinite experiments |

## Segment Conventions
| Segment | When to use |
|---------|-------------|
| all | No audience restriction (default) |
| power_users | Users with >= N sessions/month |
| new_users | Users in first 7 days |
| returning_users | Users past first 7 days |
| custom_segment | Document segment definition explicitly |

## Metadata

```yaml
id: bld_config_experiment_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_experiment_config.md
```
