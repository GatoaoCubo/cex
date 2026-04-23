---
kind: output_template
id: bld_output_template_legal_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for legal_vertical production
quality: 8.8
title: "Output Template Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, output_template]
tldr: "Template with vars for legal_vertical production"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_legal_vertical
  - bld_output_template_govtech_vertical
  - bld_config_legal_vertical
  - p10_lr_compliance_framework_builder
  - bld_schema_govtech_vertical
  - bld_collaboration_compliance_framework
  - bld_instruction_compliance_framework
  - p03_sp_compliance_framework_builder
  - legal-vertical-builder
  - compliance-framework-builder
---

```markdown
---
id: p01_lv_{{legal_entity}}.md
pillar: P01
type: legal_vertical
quality: null
naming: p01_lv_{{legal_entity}}
required_fields:
  - compliance_framework
  - jurisdiction
  - regulatory_body
  - documentation_template
---
## Legal Vertical Compliance Framework

### Key Requirements
| Jurisdiction | Regulatory Body       | Required Documentation         |
|--------------|-----------------------|--------------------------------|
| {{jurisdiction}} | {{regulatory_body}} | {{documentation_template}}   |

### Sample Legal Clause
```yaml
compliance_framework:
  name: "{{compliance_framework}}"
  scope: "covers {{jurisdiction}} regulations"
  enforcement: "{{regulatory_body}} audits required"
```

<!-- jurisdiction: e.g., "EU", "US", "APAC" -->
<!-- regulatory_body: e.g., "ESMA", "SEC", "FCA" -->
<!-- documentation_template: e.g., "KYC Form v2.1", "AML Policy 2023" -->
<!-- compliance_framework: e.g., "MiFID II", "Dodd-Frank", "MAS 6" -->
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_legal_vertical]] | downstream | 0.33 |
| [[bld_output_template_govtech_vertical]] | sibling | 0.27 |
| [[bld_config_legal_vertical]] | downstream | 0.24 |
| [[p10_lr_compliance_framework_builder]] | downstream | 0.22 |
| [[bld_schema_govtech_vertical]] | downstream | 0.21 |
| [[bld_collaboration_compliance_framework]] | downstream | 0.20 |
| [[bld_instruction_compliance_framework]] | upstream | 0.20 |
| [[p03_sp_compliance_framework_builder]] | upstream | 0.19 |
| [[legal-vertical-builder]] | upstream | 0.18 |
| [[compliance-framework-builder]] | downstream | 0.17 |
