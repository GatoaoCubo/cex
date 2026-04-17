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
