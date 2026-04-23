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
related:
  - bld_tools_user_journey
  - bld_tools_cohort_analysis
  - bld_tools_github_issue_template
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_playground_config
  - bld_tools_app_directory_entry
  - bld_tools_white_label_config
  - bld_tools_integration_guide
  - bld_tools_code_of_conduct
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_user_journey]] | sibling | 0.51 |
| [[bld_tools_cohort_analysis]] | sibling | 0.49 |
| [[bld_tools_github_issue_template]] | sibling | 0.41 |
| [[bld_tools_rbac_policy]] | sibling | 0.38 |
| [[bld_tools_usage_quota]] | sibling | 0.37 |
| [[bld_tools_playground_config]] | sibling | 0.36 |
| [[bld_tools_app_directory_entry]] | sibling | 0.36 |
| [[bld_tools_white_label_config]] | sibling | 0.35 |
| [[bld_tools_integration_guide]] | sibling | 0.35 |
| [[bld_tools_code_of_conduct]] | sibling | 0.33 |
