---
kind: collaboration
id: bld_collaboration_model_architecture
pillar: P12
llm_function: COLLABORATE
quality: 9.1
title: "Collaboration Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, collaboration, P12, builder]
tldr: "Collaboration patterns: upstream dependencies, downstream products, crew integration."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_collaboration_training_method
  - bld_architecture_model_architecture
  - bld_tools_model_architecture
  - p03_sp_model_architecture_builder
  - bld_architecture_training_method
  - bld_output_template_model_architecture
  - bld_collaboration_kind
  - p10_lr_model_architecture_builder
  - kc_intent_resolution_map
  - bld_knowledge_card_nucleus_def
---

# Collaboration: model-architecture-builder

## Upstream Dependencies
| Artifact | From | When |
|----------|------|------|
| knowledge_card (domain) | P01 / N04 | Domain-specific architecture conventions |
| training_method | P02 / N03 | Training approach constrains architecture choices |
| benchmark results | P07 / N05 | Prior architecture benchmarks inform design |

## Downstream Products
| Artifact | To | Purpose |
|----------|-----|---------|
| model_architecture | P02 | Structure specification for the neural network |
| Informs finetune_config | P02 / N03 | Concrete job uses this architecture |
| Informs model_card | P02 / N04 | Model docs reference architecture |
| Informs model_provider | P09 / N05 | Serving requirements derived from architecture |

## Crew Roles
| Nucleus | Role | Interaction |
|---------|------|------------|
| N03 Builder | Creates the artifact | Receives handoff with architecture domain + scale |
| N01 Intelligence | Provides research context | Architecture papers, SOTA benchmarks |
| N04 Knowledge | Provides domain KCs | Architecture patterns and conventions |
| N05 Operations | Validates and deploys | Doctor + hooks on final artifact |

## Handoff Format
When N07 dispatches to N03:
```
Build: model_architecture for [family/scale]
Kind: model_architecture
Pillar: P02
Context:
  - Architecture type: [transformer/cnn/etc.]
  - Scale: [parameter count]
  - Use case: [NLP/vision/etc.]
Read: archetypes/builders/model-architecture-builder/ (all 13 ISOs)
Output: P02_model/architectures/p02_ma_[name].md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_training_method]] | sibling | 0.47 |
| [[bld_architecture_model_architecture]] | upstream | 0.40 |
| [[bld_tools_model_architecture]] | upstream | 0.37 |
| [[p03_sp_model_architecture_builder]] | upstream | 0.26 |
| [[bld_architecture_training_method]] | upstream | 0.26 |
| [[bld_output_template_model_architecture]] | upstream | 0.25 |
| [[bld_collaboration_kind]] | sibling | 0.24 |
| [[p10_lr_model_architecture_builder]] | upstream | 0.23 |
| [[kc_intent_resolution_map]] | upstream | 0.23 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.23 |
