---
kind: tools
id: bld_tools_model_architecture
pillar: P04
llm_function: CALL
quality: 8.9
title: "Tools Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, tools, P04, builder]
tldr: "Tools for model-architecture-builder: retriever, doctor, compiler, validator."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_tools_training_method
  - bld_architecture_model_architecture
  - bld_collaboration_model_architecture
  - p10_lr_model_architecture_builder
  - bld_tools_agent_computer_interface
  - validate
  - p11_qg_knowledge
  - doctor
  - p03_sp_model_architecture_builder
  - bld_tools_consolidation_policy
---

# Tools: model-architecture-builder

## Build-Time Tools
| Tool | Command | When to Use |
|------|---------|------------|
| Retriever | `python _tools/cex_retriever.py model_architecture` | Find similar architecture specs |
| Doctor | `python _tools/cex_doctor.py` | Verify builder completeness (13 ISOs) |
| Compiler | `python _tools/cex_compile.py {path}` | Compile artifact after save |
| Hooks | `python _tools/cex_hooks.py validate {path}` | Validate frontmatter |
| Score | `python _tools/cex_score.py --apply {path}` | Request quality score |

## Validation Tools
| Tool | Command | Purpose |
|------|---------|---------|
| Schema check | `python _tools/cex_hooks.py pre-save {path}` | Validate required fields |
| Size check | `wc -c {path}` | Verify <= 4096 bytes body |
| ASCII check | `python _tools/cex_sanitize.py --check {path}` | Verify ASCII in code blocks |

## Integration Points
| System | How | Purpose |
|--------|-----|---------|
| finetune_config | model_architecture -> finetune_config | Architecture defines model; finetune spec trains it |
| model_card | model_architecture -> model_card | Card documents the trained architecture |
| training_method | model_architecture -> training_method | Architecture constrains training approach |
| model_provider | model_architecture -> model_provider | Architecture determines serving requirements |
| benchmark | model_architecture -> benchmark | Architecture compared via benchmarks |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_training_method]] | sibling | 0.50 |
| [[bld_architecture_model_architecture]] | downstream | 0.35 |
| [[bld_collaboration_model_architecture]] | downstream | 0.35 |
| [[p10_lr_model_architecture_builder]] | downstream | 0.34 |
| [[bld_tools_agent_computer_interface]] | sibling | 0.30 |
| [[validate]] | downstream | 0.28 |
| [[p11_qg_knowledge]] | downstream | 0.28 |
| [[doctor]] | downstream | 0.27 |
| [[p03_sp_model_architecture_builder]] | upstream | 0.25 |
| [[bld_tools_consolidation_policy]] | sibling | 0.24 |
