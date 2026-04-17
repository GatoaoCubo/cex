---
kind: config
id: bld_config_drift_detector
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits for drift_detector production
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: null
title: "Config Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, config]
tldr: "Naming, paths, size limits, and enum constraints for drift_detector production."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Config: drift_detector Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p11_dd_{scope}.md` | `p11_dd_nucleus_output_quality.md` |
| Builder directory | kebab-case | `drift-detector-builder/` |
| Frontmatter fields | snake_case | `detection_method`, `window_config`, `alert_rule` |
| Detector slug | snake_case, lowercase, no hyphens | `nucleus_output_quality`, `input_token_distribution` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `N05_operations/P11_feedback/p11_dd_{scope}.md`
- Compiled: `N05_operations/P11_feedback/compiled/p11_dd_{scope}.yaml`

## Size Limits
- Body: max 3072 bytes
- Total: ~6000 bytes
- Density: >= 0.80

## Detection Method Enum
| Value | Feature Type | Formula |
|-------|-------------|---------|
| psi | Numerical (binned) | PSI = sum((act-exp)*ln(act/exp)) |
| ks | Continuous numerical | KS statistic (max absolute difference in CDFs) |
| chi_square | Categorical | chi2 statistic on frequency tables |
| js_divergence | Categorical or discrete | JS = (KL(P||M) + KL(Q||M)) / 2 |
| embedding_distance | Text/embeddings | Cosine distance or MMD on embedding vectors |
| custom | Any | Document implementation in description |

## Threshold Guidelines
| Method | Warning | Critical |
|--------|---------|---------|
| PSI | 0.10 | 0.20 |
| KS | 0.05 | 0.10 |
| JS divergence | 0.05 | 0.10 |
| Custom | domain-specific | domain-specific |

## Alert Destination Options
| Value | When to use |
|-------|-------------|
| webhook | External monitoring platform integration |
| log | File-based alert for batch jobs |
| signal_file | CEX signal system integration |
| stdout | Development/debugging only |
