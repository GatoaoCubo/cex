---
kind: output_template
id: bld_output_template_data_residency
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for data_residency production
quality: 8.8
title: "Output Template Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, output_template]
tldr: "Template with vars for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_data_residency
  - p09_qg_data_residency
  - p09_kc_data_residency
  - bld_schema_data_residency
  - bld_knowledge_card_data_residency
  - data-residency-builder
  - bld_instruction_data_residency
  - bld_output_template_compliance_checklist
  - p03_sp_data_residency_builder
  - bld_config_audit_log
---

```yaml
---
id: p09_dr_{{name}}.md
name: {{name}}
description: {{description}}
regions: {{regions}}
compliance: {{compliance}}
data_ownership: {{data_ownership}}
encryption: {{encryption}}
audit_logs: {{audit_logs}}
quality: null
---
```

<!-- id: Generated filename following p09_dr_[a-z][a-z0-9_]+.yaml pattern -->
<!-- name: Short identifier for this data residency policy -->
<!-- description: Brief explanation of policy scope -->
<!-- regions: Array of ISO country codes where data resides -->
<!-- compliance: Array of regulatory standards (e.g., GDPR, CCPA) -->
<!-- data_ownership: Legal entity responsible for data -->
<!-- encryption: Boolean indicating if data is encrypted at rest -->
<!-- audit_logs: Boolean indicating if audit trails are enabled -->
<!-- quality: Always set to null -->

| Region | Compliance | Encryption | Audit Logs |
|--------|------------|------------|------------|
| EU     | GDPR       | true       | true       |
| US     | CCPA       | true       | false      |

```python
# Example data residency configuration
residency_config = {
    "regions": ["US", "EU"],
    "compliance": ["GDPR", "CCPA"],
    "data_ownership": "Acme Corp",
    "encryption": True,
    "audit_logs": False
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_data_residency]] | downstream | 0.38 |
| [[p09_qg_data_residency]] | downstream | 0.37 |
| [[p09_kc_data_residency]] | downstream | 0.35 |
| [[bld_schema_data_residency]] | downstream | 0.31 |
| [[bld_knowledge_card_data_residency]] | upstream | 0.31 |
| [[data-residency-builder]] | downstream | 0.28 |
| [[bld_instruction_data_residency]] | upstream | 0.27 |
| [[bld_output_template_compliance_checklist]] | sibling | 0.27 |
| [[p03_sp_data_residency_builder]] | upstream | 0.26 |
| [[bld_config_audit_log]] | downstream | 0.23 |
