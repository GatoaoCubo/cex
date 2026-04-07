---
id: p04_fd_builder_toolkit
kind: function_def
pillar: P04
title: Function Definitions -- Builder Toolkit
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [function-def, builder, N03, tools]
tldr: 10 callable functions in the builder pipeline -- motor, runner, compiler, doctor, forge, indexer, feedback, register, nucleus, validate.
density_score: 0.90
---

# Builder Toolkit: 10 Functions

| # | Name | Script | Input | Output | Timeout |
|---|------|--------|-------|--------|---------|
| 1 | parse_intent | cex_8f_motor.py | intent (string) | verb, objects, classified_kinds | 10s |
| 2 | run_pipeline | cex_8f_runner.py | kind, context, dry_run | path, quality, compiled | 120s |
| 3 | compile_artifact | cex_compile.py | path | yaml_path, success | 30s |
| 4 | check_health | cex_doctor.py | (none) | pass, warn, fail counts | 60s |
| 5 | batch_forge | cex_forge.py | kinds list, domain | created, failed counts | 300s |
| 6 | rebuild_index | cex_index.py | (none) | total_indexed | 60s |
| 7 | apply_feedback | cex_feedback.py | path, feedback | updated, new_quality | 60s |
| 8 | register_kind | cex_kind_register.py | kind, pillar, function, desc | files_updated | 30s |
| 9 | build_nucleus | cex_nucleus_builder.py | nucleus, name, domain | pass, total | 600s |
| 10 | validate_registries | cex_kind_register.py --validate | (none) | in_sync, gaps | 10s |

## Invocation Pattern

All tools follow: python _tools/{script} [args]
All return exit code 0 on success, non-zero on failure.
All write structured output to stdout (JSON or human-readable).

## Composition

The 8F Runner (F02) internally calls F03-F06-F10 in sequence.
For full artifact creation: F01 > F02 (which runs F1-F8 internally).
For batch: F05 calls F02 in parallel.
For nucleus: F09 calls F02 sequentially for each kind.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Engineering artifacts follow CEX 8F pipeline from intent to publication
- Quality gates enforce minimum 8.0 threshold for all published artifacts
- Cross-nucleus references use explicit id-based linking, not path-based
- Version tracking enables rollback to any previous artifact state

### Usage Reference

```yaml
# function_def integration
artifact: function_def_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

