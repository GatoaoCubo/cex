---
kind: output_template
id: bld_output_template_healthcare_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for healthcare_vertical production
quality: 8.7
title: "Output Template Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, output_template]
tldr: "Template with vars for healthcare_vertical production"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_healthcare_vertical
  - bld_schema_healthcare_vertical
  - bld_output_template_cohort_analysis
  - p01_qg_healthcare_vertical
  - bld_architecture_ecommerce_vertical
  - bld_config_legal_vertical
  - healthcare-vertical-builder
---

```yaml
---
id: p01_hv_{{name}}.md
name: {{healthcare_vertical_name}}
pillar: P01
vertical: healthcare_vertical
quality: null
---
```

<!-- id: Generated filename (e.g., p01_hv_patient_data.md) -->
<!-- name: Healthcare vertical name (e.g., "patient_data") -->
<!-- pillar: Always "P01" -->
<!-- vertical: Always "healthcare_vertical" -->
<!-- quality: Always null -->

**Example Data Structure**
| Field        | Value              | Description                  |
|--------------|--------------------|------------------------------|
| patient_id   | {{patient_id}}     | Unique identifier            |
| condition    | {{medical_condition}} | Diagnosed condition        |
| treatment    | {{treatment_plan}} | Prescribed therapy           |

**Sample API Endpoint**
```python
def get_patient_data(patient_id):
    # Query healthcare database
    return {"id": patient_id, "condition": "hypertension", "treatment": "beta-blockers"}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_healthcare_vertical]] | downstream | 0.31 |
| [[bld_schema_healthcare_vertical]] | downstream | 0.22 |
| [[bld_output_template_cohort_analysis]] | sibling | 0.17 |
| [[p01_qg_healthcare_vertical]] | downstream | 0.17 |
| [[bld_architecture_ecommerce_vertical]] | downstream | 0.16 |
| [[bld_config_legal_vertical]] | downstream | 0.16 |
| [[healthcare-vertical-builder]] | upstream | 0.15 |
