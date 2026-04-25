---
kind: output_template
id: bld_output_template_collaboration_pattern
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for collaboration_pattern production
quality: 8.7
title: "Output Template Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, output_template]
tldr: "Output template for collaboration pattern: frontmatter field guide, required body sections, filled example, and quality gate checklist for multi-agent coordination topology."
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_output_template_ab_test_config
  - bld_output_template_cohort_analysis
  - p06_is_marketing_data_model
  - bld_output_template_workflow_node
  - p06_is_campaign_performance_metrics
  - tpl_learning_record_autonomy
  - p04_function_def_NAME
---

```yaml
---
title: "{{name}} Collaboration"
description: "{{description}}"
participants: ["{{participant1}}", "{{participant2}}"]
scope: "{{scope}}"
start_date: "{{start_date}}"
end_date: "{{end_date}}"
status: "{{status}}"
---
## Objectives
{{objectives}}
## Key Activities
{{key_activities}}
## Success Metrics
{{success_metrics}}
## Next Steps
{{next_steps}}
```

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p12_collab_{{name}}.md pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 5120 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | collaboration pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_ab_test_config]] | sibling | 0.35 |
| [[bld_output_template_cohort_analysis]] | sibling | 0.28 |
| [[p06_is_marketing_data_model]] | downstream | 0.22 |
| [[bld_output_template_workflow_node]] | sibling | 0.18 |
| [[p06_is_campaign_performance_metrics]] | downstream | 0.17 |
| [[tpl_learning_record_autonomy]] | downstream | 0.17 |
| [[p04_function_def_NAME]] | upstream | 0.16 |
