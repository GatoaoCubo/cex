---
kind: tools
id: bld_tools_interactive_demo
pillar: P04
llm_function: CALL
purpose: Tools available for interactive_demo production
quality: 8.9
title: "Tools Interactive Demo"
version: "1.0.1"
author: n02_marketing
tags: [interactive_demo, builder, tools]
tldr: "Tools available for interactive_demo production"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_product_tour
  - bld_knowledge_card_interactive_demo
  - bld_tools_pitch_deck
  - bld_tools_rbac_policy
  - bld_tools_api_reference
  - bld_tools_usage_quota
  - interactive-demo-builder
  - bld_tools_playground_config
  - bld_tools_customer_segment
  - bld_tools_quickstart_guide
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles interactive_demo artifact and validates frontmatter | After draft complete |
| cex_score.py | Scores demo script against quality gate dimensions | After each draft |
| cex_retriever.py | Fetches comparable demo scripts and talk track KCs | Research phase |
| cex_doctor.py | Validates structural integrity and required sections | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit gate: ASCII check + frontmatter validation | On git add |
| cex_hygiene.py | Artifact CRUD enforcement: naming, kind, quality=null | Post-generation |

## External References (informational, not CEX tools)
| Resource | Purpose |
|----------|---------|
| Demostack / Reprise / Navattic | Guided tour platform patterns: step triggers, branching, presales flows |
| Arcade / Supademo | Click-through demo structure: screenshot-based walkthroughs, CTA placement |
| Presales SE Playbook | Talk track structure: discovery questions, objection maps, proof points |
| MEDDIC / MEDDPIC | Qualification framework for demo script targeting |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_product_tour]] | sibling | 0.38 |
| [[bld_knowledge_card_interactive_demo]] | upstream | 0.35 |
| [[bld_tools_pitch_deck]] | sibling | 0.35 |
| [[bld_tools_rbac_policy]] | sibling | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_usage_quota]] | sibling | 0.30 |
| [[interactive-demo-builder]] | downstream | 0.30 |
| [[bld_tools_playground_config]] | sibling | 0.29 |
| [[bld_tools_customer_segment]] | sibling | 0.29 |
| [[bld_tools_quickstart_guide]] | sibling | 0.29 |
