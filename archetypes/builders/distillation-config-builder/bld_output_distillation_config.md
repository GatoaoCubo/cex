---
kind: output_template
id: bld_output_distillation_config
pillar: P05
llm_function: PRODUCE
purpose: Template for producing a distillation_config artifact
quality: null
title: "Distillation Config Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, output]
tldr: "Output template for distillation config: frontmatter field guide, required body sections, filled example, and quality gate checklist for teacher-student model compression and knowledge distillation setup."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_distillation_config
---

# Output Template: distillation_config

```yaml
id: p02_dc_{{config_slug}}
kind: distillation_config
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
teacher_model: "{{teacher_model_id}}"
student_model: "{{student_model_id}}"
temperature: {{float}}
alpha: {{float}}
method: "{{logit_or_feature_or_progressive}}"
compression_ratio: {{float}}
domain: "{{domain_value}}"
quality: null
tags: [distillation, {{method_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Teacher
`{{teacher_model_params_and_performance}}`

## Student
`{{student_architecture_and_target_size}}`

## Training
`{{temperature_alpha_lr_epochs_schedule}}`

## Loss Function
`{{kd_loss_task_loss_composition}}`

## Evaluation
`{{checkpoints_quality_thresholds_regression}}`

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p02_dc_{{name}}.md + .yaml pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 4096 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | distillation config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
