---
kind: tools
id: bld_tools_usage_report
pillar: P04
llm_function: CALL
purpose: Tools available for usage_report production
quality: 8.9
title: "Tools Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, tools]
tldr: "Tools available for usage_report production"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile usage_report artifact to YAML + register in index | After authoring |
| cex_score.py | Score artifact quality (5D + HARD gates) | After compile |
| cex_retriever.py | Find similar usage report artifacts for template reuse | During F3 INJECT |
| cex_doctor.py | Validate all ISOs in builder for structural health | Post-build audit |
| cex_wave_validator.py | Batch-validate full usage-report-builder (39 ISOs) | CI gate |
| cex_hygiene.py | Enforce 8 hygiene rules (frontmatter, density, IDs) | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit hook: block schema violations + ASCII errors | On git add |
| cex_sanitize.py | ASCII sanitize .py/.ps1 in builder scope | After code edits |
| cex_feedback.py | Track quality trends and archive low-score artifacts | After scoring |

## External References
- Apache Airflow (orchestration for usage data pipelines)
- Snowflake (data share for cross-org usage reporting)
- Metabase / Looker (dashboard embedding for CFO/showback reports)
- GDPR Article 30 (data lineage and retention requirements)
- FinOps Foundation (chargeback vs. showback framework terminology)
