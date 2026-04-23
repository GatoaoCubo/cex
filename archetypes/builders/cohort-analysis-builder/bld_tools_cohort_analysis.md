---
kind: tools
id: bld_tools_cohort_analysis
pillar: P04
llm_function: CALL
purpose: Tools available for cohort_analysis production
quality: 8.9
title: "Tools Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, tools]
tldr: "Tools available for cohort_analysis production"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_user_journey
  - bld_tools_customer_segment
  - bld_tools_rbac_policy
  - bld_tools_github_issue_template
  - bld_tools_usage_quota
  - bld_tools_white_label_config
  - bld_knowledge_card_cohort_analysis
  - bld_tools_playground_config
  - bld_tools_api_reference
  - bld_tools_app_directory_entry
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
| cex_quality_monitor.py | Quality snapshots + regression detection | Post-wave monitoring |

## External References
- Mixpanel Cohort Analysis (cohort grouping by event)
- Amplitude Retention Chart (day-N retention curves: D1/D7/D30/D90)
- BG/NBD model (Fader & Hardie, 2009) for LTV prediction
- Kaplan-Meier survival analysis (standard churn modeling)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_user_journey]] | sibling | 0.55 |
| [[bld_tools_customer_segment]] | sibling | 0.54 |
| [[bld_tools_rbac_policy]] | sibling | 0.36 |
| [[bld_tools_github_issue_template]] | sibling | 0.36 |
| [[bld_tools_usage_quota]] | sibling | 0.35 |
| [[bld_tools_white_label_config]] | sibling | 0.32 |
| [[bld_knowledge_card_cohort_analysis]] | upstream | 0.32 |
| [[bld_tools_playground_config]] | sibling | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_app_directory_entry]] | sibling | 0.31 |
