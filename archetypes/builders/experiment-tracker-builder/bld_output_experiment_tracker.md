---
kind: output_template
id: bld_output_template_experiment_tracker
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for experiment_tracker production
quality: 8.9
title: "Output Template Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, output_template]
tldr: "Output template for experiment tracker: frontmatter field guide, required body sections, filled example, and quality gate checklist for experiment configuration and results tracking."
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_ch_{{PIPELINE_SLUG}}
  - bld_schema_experiment_tracker
  - pricing_experiment_tool
  - bld_output_template_user_journey
---

```yaml
id: {{experiment_id}}
name: {{experiment_name}}
pillar: P07
type: experiment_tracker
date: {{date}}
status: {{status}}
owner: {{owner}}
tags: [{{tags}}]
```

# Experiment: {{experiment_name}}

## 1. Objective
{{describe_the_primary_goal}}

## 2. Hypothesis
{{if_condition_then_outcome}}

## 3. Parameters & Setup
- **Variable A:** {{value_a}}
- **Variable B:** {{value_b}}
- **Environment:** {{environment_details}}

## 4. Execution Steps
1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

## 5. Results
| Metric | Target | Observed |
|--------|--------|----------|
| {{metric_1}} | {{target_1}} | {{actual_1}} |
| {{metric_2}} | {{target_2}} | {{actual_2}} |

## 6. Analysis
{{interpretation_of_observed_data}}

## 7. Conclusion & Next Steps
{{decision_to_scale_pivot_or_discard}}

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p07_et_{{name}}.md pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 4096 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | experiment tracker construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_{{PIPELINE_SLUG}}]] | upstream | 0.17 |
| [[bld_schema_experiment_tracker]] | downstream | 0.15 |
| [[pricing_experiment_tool]] | downstream | 0.15 |
| [[bld_output_template_user_journey]] | sibling | 0.15 |
