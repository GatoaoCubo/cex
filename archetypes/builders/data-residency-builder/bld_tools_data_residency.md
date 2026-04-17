---
kind: tools
id: bld_tools_data_residency
pillar: P04
llm_function: CALL
purpose: Tools available for data_residency production
quality: 8.7
title: "Tools Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, tools]
tldr: "Tools available for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles data_residency artifact to .yaml | After each save |
| cex_score.py | Scores artifact against 5D quality dimensions | Post-production |
| cex_retriever.py | Retrieves similar residency specs and KCs | During F3 INJECT |
| cex_doctor.py | Validates builder ISO completeness and structure | During F7 GOVERN |
| cex_hygiene.py | Enforces frontmatter rules and naming conventions | During F7 GOVERN |

## External References
- GDPR Articles 44-50 (third-country transfers)
- Schrems II ruling (C-311/18) and EU-US Data Privacy Framework 2023
- ISO/IEC 27701:2019 (Privacy Information Management)
- AWS Data Residency, Azure Sovereign Regions (regional data plane references)
