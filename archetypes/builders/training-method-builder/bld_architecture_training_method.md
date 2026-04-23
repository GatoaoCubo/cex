---
kind: architecture
id: bld_architecture_training_method
pillar: P08
llm_function: CONSTRAIN
quality: 9.1
title: "Architecture Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, architecture, P08, builder]
tldr: "Architecture of training-method-builder: pillar placement, naming conventions, size constraints, and 8F pipeline integration."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.86
related:
  - bld_architecture_model_architecture
  - bld_collaboration_training_method
  - bld_tools_training_method
  - p03_sp_training_method_builder
  - training-method-builder
  - p10_lr_training_method_builder
  - bld_knowledge_card_training_method
  - bld_config_kind
  - bld_output_template_training_method
  - bld_knowledge_card_kind
---
# Architecture: training_method

## Pillar Placement
| Attribute | Value |
|-----------|-------|
| Pillar | P02 (Model) |
| Rationale | training_method defines HOW a model learns -- belongs with model artifacts |
| Adjacent pillars | P07 (eval metrics), P01 (dataset knowledge), P11 (reward/feedback) |

## Naming Convention
| Component | Pattern | Example |
|-----------|---------|---------|
| Artifact ID | `p02_tm_[domain]` | `p02_tm_text_classification_bert` |
| File name | `p02_tm_[domain].md` | `p02_tm_text_classification_bert.md` |
| Builder ISOs | `bld_[type]_training_method.md` | `bld_instruction_training_method.md` |
| Directory | `P02_model/training_methods/` | standard pillar location |

## Size Constraints
| Component | Limit | Rationale |
|-----------|-------|-----------|
| Artifact body | 4096 bytes | Concise specification, not documentation |
| Instruction ISO | 8192 bytes | Detailed process guidance needs more space |
| Other ISOs | 6144 bytes | Standard ISO limit |
| Frontmatter | No hard limit | YAML is compact |

## 8F Pipeline Integration
| Stage | training_method Role |
|-------|---------------------|
| F1 CONSTRAIN | kind=training_method, pillar=P02, schema loaded |
| F2 BECOME | training-method-builder loaded (13 ISOs) |
| F3 INJECT | kc_training_method + similar artifacts + domain KCs |
| F4 REASON | plan sections: overview + paradigm + compute + hyperparams + dataset + eval |
| F5 CALL | retriever finds existing specs, doctor verifies builder completeness |
| F6 PRODUCE | generate complete artifact with all required sections |
| F7 GOVERN | validate 10 HARD gates, density >= 0.85 |
| F8 COLLABORATE | save to P02, compile, commit, signal |

## Relationship Map
```
training_method
  |-- extends  --> model_architecture (neural net structure)
  |-- uses     --> finetune_config (specific job implementation)
  |-- informs  --> model_card (documentation of trained model)
  |-- integrates --> reward_model (RL training reward signal)
  |-- validates_via --> benchmark (evaluation methodology)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_model_architecture]] | sibling | 0.53 |
| [[bld_collaboration_training_method]] | downstream | 0.42 |
| [[bld_tools_training_method]] | upstream | 0.36 |
| [[p03_sp_training_method_builder]] | upstream | 0.34 |
| [[training-method-builder]] | upstream | 0.32 |
| [[p10_lr_training_method_builder]] | downstream | 0.31 |
| [[bld_knowledge_card_training_method]] | upstream | 0.28 |
| [[bld_config_kind]] | downstream | 0.28 |
| [[bld_output_template_training_method]] | upstream | 0.28 |
| [[bld_knowledge_card_kind]] | upstream | 0.27 |
