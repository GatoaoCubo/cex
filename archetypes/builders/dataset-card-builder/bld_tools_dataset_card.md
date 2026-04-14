---
kind: tools
id: bld_tools_dataset_card
pillar: P04
llm_function: CALL
purpose: Tools available for dataset_card production
quality: null
title: "Tools Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, tools]
tldr: "Tools available for dataset_card production"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Aggregates metadata | Finalizing card |
| cex_score.py | Calculates quality | Post-processing |
| cex_retriever.py | Fetches schema | Data ingestion |
| cex_doctor.py | Checks integrity | Pre-deployment |
| cex_formatter.py | Standardizes MD | Post-compilation |

## Validation Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| schema_validator.py | Schema compliance | Build time |
| lint_card.py | Markdown linting | Review stage |
| integrity_check.py | Link verification | Deployment |

## External References
* Hugging
