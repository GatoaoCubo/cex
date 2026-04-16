---
kind: tools
id: bld_tools_customer_segment
pillar: P04
llm_function: CALL
purpose: Tools available for customer_segment production
quality: 8.9
title: "Tools Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, tools]
tldr: "Tools available for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact YAML from source .md | After draft is written |
| cex_score.py | Peer-review scoring (hybrid 3-layer) | After artifact is saved |
| cex_retriever.py | TF-IDF similarity search across knowledge base | During F3 INJECT phase |
| cex_doctor.py | Builder health check -- validates ISOs and schema | Before dispatch |
| cex_hygiene.py | Artifact CRUD, enforce 8 hygiene rules | Ongoing quality control |
| cex_memory_select.py | Keyword + LLM memory injection | During F3 INJECT phase |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Structural ISO validation (frontmatter, kind, schema) | After each builder wave |
| cex_hooks.py | Pre/post commit validation + ASCII check | On git commit |
| cex_sanitize.py | ASCII-only check and auto-fix for code files | Before commit |

## External References
- ICP frameworks: Salesforce, HubSpot ICP documentation
- Firmographic data: Dun & Bradstreet, ZoomInfo, LinkedIn Sales Navigator
- Segmentation standards: SiriusDecisions Demand Unit Waterfall, Pragmatic Institute
