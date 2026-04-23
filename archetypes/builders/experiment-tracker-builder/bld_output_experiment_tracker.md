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
tldr: "Template with vars for experiment_tracker production"
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_{{PIPELINE_SLUG}}]] | upstream | 0.17 |
| [[bld_schema_experiment_tracker]] | downstream | 0.15 |
| [[pricing_experiment_tool]] | downstream | 0.15 |
| [[bld_output_template_user_journey]] | sibling | 0.15 |
