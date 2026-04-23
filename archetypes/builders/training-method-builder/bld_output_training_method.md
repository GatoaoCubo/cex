---
kind: output_template
id: bld_output_template_training_method
pillar: P05
llm_function: PRODUCE
quality: 9.1
title: "Output Template Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, output_template, P05, builder]
tldr: "Canonical output template for training_method artifacts with all required sections."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_examples_training_method
  - training-method-builder
  - bld_instruction_training_method
  - bld_schema_training_method
  - p03_sp_training_method_builder
  - p02_qg_training_method
  - bld_knowledge_card_training_method
  - bld_collaboration_training_method
  - p10_lr_training_method_builder
  - bld_architecture_training_method
---

# Output Template: training_method

Copy this template and fill all fields. Remove placeholder text.

```markdown
---
id: p02_tm_{{domain}}
kind: training_method
pillar: P02
title: "{{Title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
domain: "{{domain}}"
learning_paradigm: "{{supervised|unsupervised|reinforcement|self_supervised|transfer|hybrid}}"
compute_intensity: "{{low|medium|high}}"
quality: null
tags: [training_method, {{domain}}, {{paradigm}}]
tldr: "{{One-sentence summary of training approach}}"
---

# Training Method: {{Title}}

## Overview
| Attribute | Value |
|-----------|-------|
| Target Task | {{classification/generation/alignment/detection/etc.}} |
| Base Model | {{model family or architecture}} |
| Paradigm Rationale | {{why this paradigm for this task}} |
| Compute Rationale | {{why this compute intensity}} |

## Learning Paradigm
| Attribute | Value |
|-----------|-------|
| paradigm | {{learning_paradigm}} |
| objective | {{loss function or reward signal}} |
| requires_labels | {{Yes/No/Reward signal}} |
| label_schema | {{field names or reward definition}} |

## Compute Profile
| Attribute | Value |
|-----------|-------|
| intensity | {{compute_intensity}} |
| hardware | {{GPU type and count}} |
| memory_per_gpu | {{GB}} |
| estimated_time | {{hours/days}} |
| parallelism | {{DDP/FSDP/pipeline/none}} |

## Hyperparameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| learning_rate | {{value}} | {{rationale}} |
| batch_size | {{value}} | {{effective if gradient accumulation}} |
| epochs | {{value}} | {{with early stopping criteria}} |
| optimizer | {{name}} | {{with weight_decay if applicable}} |
| scheduler | {{name}} | {{warmup_steps if applicable}} |

## Dataset Requirements
| Attribute | Value |
|-----------|-------|
| source | {{path or identifier}} |
| size | {{rows/samples}} |
| format | {{Alpaca/ShareGPT/Parquet/CSV/HF}} |
| field_mapping | {{instruction->input, output->label}} |
| preprocessing | {{tokenization, filtering, deduplication}} |
| language | {{en/pt/multilingual}} |

## Evaluation
| Metric | Target | Frequency |
|--------|--------|-----------|
| {{metric_1}} | {{target_value}} | {{every N steps/epoch}} |
| {{metric_2}} | {{target_value}} | {{final eval}} |
| convergence_criteria | {{condition to stop training}} | per epoch |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_training_method]] | downstream | 0.44 |
| [[training-method-builder]] | upstream | 0.40 |
| [[bld_instruction_training_method]] | upstream | 0.40 |
| [[bld_schema_training_method]] | downstream | 0.39 |
| [[p03_sp_training_method_builder]] | upstream | 0.38 |
| [[p02_qg_training_method]] | downstream | 0.36 |
| [[bld_knowledge_card_training_method]] | upstream | 0.32 |
| [[bld_collaboration_training_method]] | downstream | 0.31 |
| [[p10_lr_training_method_builder]] | downstream | 0.30 |
| [[bld_architecture_training_method]] | downstream | 0.29 |
