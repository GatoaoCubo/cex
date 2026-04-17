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
