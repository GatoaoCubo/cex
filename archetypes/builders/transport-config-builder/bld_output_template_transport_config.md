---
kind: output_template
id: bld_output_template_transport_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for transport_config production
quality: null
title: "Output Template Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, output_template]
tldr: "Template with vars for transport_config production"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
name: {{name}}
kind: transport_config
pillar: P09
version: 1.0

transport_type: {{transport_type}}
protocols:
  - {{protocol_1}}
  - {{protocol_2}}

endpoints:
  - url: {{endpoint_url_1}}
    description: {{endpoint_desc_1}}
  - url: {{endpoint_url_2}}
    description: {{endpoint_desc_2}}

authentication:
  type: {{auth_type}}
  credentials:
    username: {{username}}
    password: {{password}}

timeout_seconds: {{timeout}}
notes: {{additional_notes}}
```
