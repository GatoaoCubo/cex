---
kind: tools
id: bld_tools_expansion_play
pillar: P04
llm_function: CALL
purpose: Tools available for expansion_play production
quality: 9.0
title: "Tools Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, tools, upsell, NRR, Gainsight, Salesforce]
tldr: "Tools available for expansion_play production"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_churn_prevention_playbook
  - bld_knowledge_card_expansion_play
  - p03_sp_expansion_play_builder
  - bld_tools_api_reference
  - bld_tools_renewal_workflow
  - bld_instruction_expansion_play
  - expansion-play-builder
  - bld_tools_nps_survey
  - p10_mem_expansion_play_builder
  - bld_examples_expansion_play
---

## Production Tools
| Tool               | Purpose                                    | When                            |
|--------------------|--------------------------------------------|---------------------------------|
| cex_compile.py     | Compile expansion play YAML/MD artifacts   | After artifact generation       |
| cex_score.py       | Score NRR model and trigger completeness   | Post-generation quality check   |
| cex_retriever.py   | Fetch similar expansion plays for reference| During F3 INJECT phase          |
| cex_doctor.py      | Diagnose schema compliance issues          | Pre-validation checks           |
| cex_validator.py   | Enforce frontmatter schema rules           | Data ingestion and post-build   |

## Validation Tools
| Tool               | Purpose                                    | When                            |
|--------------------|--------------------------------------------|---------------------------------|
| val_check.py       | Verify trigger quantification completeness | Pre-deployment                  |
| val_audit.py       | Cross-reference NRR model components       | Quarterly RevOps reviews        |
| val_comparator.py  | Detect duplicate expansion plays           | Before creating new play        |

## External Integrations
| System             | Purpose                                    | Integration Type                |
|--------------------|--------------------------------------------|---------------------------------|
| Gainsight PX       | Health score + usage signal data source    | REST API / webhook              |
| Salesforce CRM     | Account ARR, contract, opportunity data    | REST API (v58.0+)               |
| Product Analytics  | WAU/MAU, feature adoption rate             | Data warehouse export / API     |
| Looker/Tableau     | NRR model visualization                   | Embedded analytics              |
| Outreach/Salesloft | Talk track sequencing and send             | Sequence automation API         |

## External References
- Gainsight API v2.0: health score and CTA automation
- Salesforce Platform API v58: opportunity and account management
- OpenView SaaS Metrics Calculator: NRR model validation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.34 |
| [[bld_knowledge_card_expansion_play]] | upstream | 0.31 |
| [[p03_sp_expansion_play_builder]] | upstream | 0.29 |
| [[bld_tools_api_reference]] | sibling | 0.29 |
| [[bld_tools_renewal_workflow]] | sibling | 0.28 |
| [[bld_instruction_expansion_play]] | upstream | 0.27 |
| [[expansion-play-builder]] | upstream | 0.26 |
| [[bld_tools_nps_survey]] | sibling | 0.26 |
| [[p10_mem_expansion_play_builder]] | downstream | 0.25 |
| [[bld_examples_expansion_play]] | downstream | 0.24 |
