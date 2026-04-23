---
kind: tools
id: bld_tools_analyst_briefing
pillar: P04
llm_function: CALL
purpose: Tools available for analyst_briefing production
quality: 8.9
title: "Tools Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, tools]
tldr: "Tools available for analyst_briefing production"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_competitive_matrix
  - bld_knowledge_card_analyst_briefing
  - analyst-briefing-builder
  - bld_tools_roi_calculator
  - bld_tools_api_reference
  - bld_tools_case_study
  - bld_tools_quickstart_guide
  - p03_sp_analyst_briefing_builder
  - bld_tools_gpai_technical_doc
  - bld_tools_sdk_example
---

## Production Tools
| Tool               | Purpose                                      | When                        |
|--------------------|----------------------------------------------|-----------------------------|
| cex_compile.py     | Compile briefing to YAML + validate fields   | Post-production             |
| cex_score.py       | Score briefing against quality gate          | Pre-submission to analyst   |
| cex_retriever.py   | Fetch comparable briefing artifacts          | During Phase 1 RESEARCH     |
| cex_doctor.py      | Diagnose missing fields and schema issues    | Pre-validation              |
| cex_query.py       | Discover related knowledge cards             | During context assembly     |

## Validation Tools
| Tool               | Purpose                                      | When                        |
|--------------------|----------------------------------------------|-----------------------------|
| cex_wave_validator.py | Enforce HARD gates H01-H08               | Post-production             |
| cex_hooks.py       | Pre/post build hook execution                | Build lifecycle             |
| cex_sanitize.py    | Ensure ASCII compliance in code blocks       | Before commit               |

## External References
- Gartner Magic Quadrant Methodology (gartner.com/en/research/methodologies/magic-quadrants-research)
- Forrester Wave Methodology (forrester.com/policies/forrester-wave-methodology)
- IDC MarketScape Methodology (idc.com/getdoc.jsp?containerId=IDC_P14767)
- IIAR AR Best Practices (analystrelations.org/resources)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_competitive_matrix]] | sibling | 0.46 |
| [[bld_knowledge_card_analyst_briefing]] | upstream | 0.44 |
| [[analyst-briefing-builder]] | downstream | 0.36 |
| [[bld_tools_roi_calculator]] | sibling | 0.35 |
| [[bld_tools_api_reference]] | sibling | 0.33 |
| [[bld_tools_case_study]] | sibling | 0.32 |
| [[bld_tools_quickstart_guide]] | sibling | 0.31 |
| [[p03_sp_analyst_briefing_builder]] | upstream | 0.30 |
| [[bld_tools_gpai_technical_doc]] | sibling | 0.30 |
| [[bld_tools_sdk_example]] | sibling | 0.29 |
