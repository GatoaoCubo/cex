---
kind: tools
id: bld_tools_case_study
pillar: P04
llm_function: CALL
purpose: Tools available for case_study production
quality: 8.9
title: "Tools Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, tools]
tldr: "CEX tools available for case_study production and validation"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml sidecar | After write |
| cex_score.py | Score case study against quality gate dimensions | Pre-publish |
| cex_retriever.py | Find existing case studies for pattern reference | Research phase |
| cex_doctor.py | Validate frontmatter fields, ID pattern, kind compliance | Pre-publish |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Check all builder ISOs for schema compliance | Post-build |
| cex_hooks.py | Pre-commit YAML validation and quality gate enforcement | On git commit |

## External References
- G2 testimonial verification guidelines (quote attribution standards)
- Gartner customer reference program (enterprise case study methodology)
- AWS case study template (challenge/solution/outcome structure reference)
- Snowflake customer stories (before/after KPI table format reference)
