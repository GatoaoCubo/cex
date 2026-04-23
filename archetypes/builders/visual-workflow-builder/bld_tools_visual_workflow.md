---
kind: tools
id: bld_tools_visual_workflow
pillar: P04
llm_function: CALL
purpose: Tools available for visual_workflow production
quality: 8.9
title: "Tools Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, tools]
tldr: "Tools available for visual_workflow production"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_multimodal_prompt
  - bld_tools_prompt_optimizer
  - bld_instruction_visual_workflow
  - bld_tools_legal_vertical
  - bld_tools_roi_calculator
  - bld_tools_workflow_node
  - bld_tools_customer_segment
  - bld_tools_white_label_config
  - bld_tools_pricing_page
  - bld_tools_changelog
---

## Production Tools
| Tool | Purpose | When |
|---|---|---|
| cex_compile.py | Compile visual_workflow artifact to YAML output | After F6 PRODUCE |
| cex_score.py | Score artifact against 5D quality dimensions | After generation |
| cex_retriever.py | Retrieve similar visual_workflow examples for F3 INJECT | During context assembly |
| cex_doctor.py | Validate builder ISO completeness and frontmatter | During F7 GOVERN |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_hooks.py | Pre-commit validation: ASCII check, frontmatter, schema | Before F8 COLLABORATE |
| cex_wave_validator.py | Validate all 13 ISOs in builder package | During audit cycles |

## Industry Reference Platforms
| Platform | Contribution to visual_workflow design |
|----------|---------------------------------------|
| Mermaid | Text-based diagram DSL -- node/edge schema reference |
| LangGraph Studio (LangChain) | Visual agent graph editor, state node pattern |
| Flowise | Open-source drag-and-drop LLM flow builder |
| n8n | Node-based workflow automation, trigger/action pattern |
| Dify | Visual LLM pipeline with typed input/output ports |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_multimodal_prompt]] | sibling | 0.36 |
| [[bld_tools_prompt_optimizer]] | sibling | 0.36 |
| [[bld_instruction_visual_workflow]] | upstream | 0.34 |
| [[bld_tools_legal_vertical]] | sibling | 0.30 |
| [[bld_tools_roi_calculator]] | sibling | 0.29 |
| [[bld_tools_workflow_node]] | sibling | 0.27 |
| [[bld_tools_customer_segment]] | sibling | 0.27 |
| [[bld_tools_white_label_config]] | sibling | 0.27 |
| [[bld_tools_pricing_page]] | sibling | 0.27 |
| [[bld_tools_changelog]] | sibling | 0.27 |
