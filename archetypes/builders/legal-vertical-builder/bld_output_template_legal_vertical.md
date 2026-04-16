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
