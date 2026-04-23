---
kind: output_template
id: bld_output_template_cohort_analysis
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for cohort_analysis production
quality: 8.7
title: "Output Template Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, output_template]
tldr: "Template with vars for cohort_analysis production"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_ab_test_config
  - bld_output_template_collaboration_pattern
  - bld_examples_cohort_analysis
  - cohort-analysis-builder
  - bld_config_cohort_analysis
  - bld_instruction_cohort_analysis
  - bld_output_template_usage_report
  - p10_mem_cohort_analysis_builder
  - p03_sp_cohort_analysis_builder
  - bld_examples_workflow_node
---

```yaml
---
id: p07_ca_{{name}}.yaml <!-- Insert cohort name here -->
name: {{name}} <!-- Insert cohort name here -->
pillar: P07
quality: null
description: {{description}} <!-- Insert cohort description here -->
start_date: {{start_date}} <!-- YYYY-MM-DD -->
end_date: {{end_date}} <!-- YYYY-MM-DD -->
---
```

| patient_id | enrollment_date | outcome |
|------------|----------------|---------|
| 12345      | 2023-01-15     | 1       |
| 67890      | 2023-02-20     | 0       |

```python
# Example analysis code
import pandas as pd

data = pd.read_csv("cohort_data.csv")
summary = data.groupby("outcome").size()
print(summary)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_ab_test_config]] | sibling | 0.28 |
| [[bld_output_template_collaboration_pattern]] | sibling | 0.25 |
| [[bld_examples_cohort_analysis]] | downstream | 0.24 |
| [[cohort-analysis-builder]] | downstream | 0.22 |
| [[bld_config_cohort_analysis]] | downstream | 0.21 |
| [[bld_instruction_cohort_analysis]] | upstream | 0.21 |
| [[bld_output_template_usage_report]] | sibling | 0.20 |
| [[p10_mem_cohort_analysis_builder]] | downstream | 0.20 |
| [[p03_sp_cohort_analysis_builder]] | upstream | 0.20 |
| [[bld_examples_workflow_node]] | downstream | 0.18 |
