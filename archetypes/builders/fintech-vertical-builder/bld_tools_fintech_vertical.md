---
kind: tools
id: bld_tools_fintech_vertical
pillar: P04
llm_function: CALL
purpose: Tools available for fintech_vertical production
quality: 8.9
title: "Tools Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, tools]
tldr: "Tools available for fintech_vertical production"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools (fintech vertical)
| Tool | Purpose (fintech context) | When |
|---|---|---|
| cex_compile.py | Compile fintech_vertical artifact to YAML + validate frontmatter | After authoring |
| cex_score.py | Score artifact against H01-H08 gates and 7D SOFT dimensions | Before publish |
| cex_retriever.py | Retrieve similar SOC2/PCI-DSS/KYC artifacts from knowledge library | During research |
| cex_doctor.py | Health-check builder ISO completeness and frontmatter validity | QA pass |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_wave_validator.py | Validate all 13 ISOs in builder directory | Post-build |
| cex_hygiene.py | Enforce naming, frontmatter, ASCII rules | Pre-commit |

## External References
- PCI Security Standards Council (pcicomplianceguide.org) -- PCI-DSS v4.0 controls
- FATF (fatf-gafi.org) -- KYC/AML Travel Rule guidance
- OFAC SDN List API (ofac.treasury.gov) -- sanctions screening
