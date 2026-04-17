---
kind: config
id: bld_config_backpressure_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
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
quality: 7.8
title: "Config Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, config]
tldr: "Naming: p09_bp_{scope}.md. Threshold: 0.7-0.8. Watermarks required. Strategy enum enforced."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Config: backpressure_policy Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_bp_{scope_slug}.md` | `p09_bp_llm_job_queue.md` |
| Builder directory | kebab-case | `backpressure-policy-builder/` |
| Frontmatter fields | snake_case | `overflow_strategy`, `buffer_size`, `shed_threshold` |
| Scope slug | snake_case, lowercase, no hyphens | `llm_job_queue`, `event_ingest` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `N0X_{domain}/P09_config/p09_bp_{scope_slug}.md`
- Compiled: `N0X_{domain}/P09_config/compiled/p09_bp_{scope_slug}.yaml`

## Size Limits
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)

## Overflow Strategy Reference
| Strategy | Enum Value | Data Loss |
|----------|-----------|-----------|
| Drop newest | DROP_LATEST | Yes |
| Drop oldest | DROP_OLDEST | Yes |
| Accumulate | BUFFER | No (until full) |
| Slow producer | THROTTLE | No |
| Raise exception | ERROR | Caller-defined |

## Threshold Guidance by Pipeline Type
| Pipeline Type | shed_threshold | buffer_size | overflow_strategy |
|--------------|----------------|-------------|-------------------|
| LLM job queue | 0.7-0.8 | 50-200 | DROP_LATEST or ERROR |
| Metrics/telemetry | 0.8-0.9 | 1000-10000 | DROP_LATEST |
| Event streaming | 0.7 | 500-5000 | BUFFER or THROTTLE |
| Audit log | 0.5-0.6 | 100-500 | ERROR or THROTTLE |
| Real-time sensor | 0.9 | 10000+ | DROP_OLDEST |

## Watermark Constraints
- high_watermark MUST be <= buffer_size
- low_watermark MUST be < high_watermark
- Hysteresis gap (high - low) SHOULD be >= 20% of buffer_size
- Invalid: low_watermark == high_watermark (causes oscillation)
