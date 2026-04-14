---
kind: output_template
id: bld_output_template_sandbox_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sandbox_config production
quality: null
title: "Output Template Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, output_template]
tldr: "Template with vars for sandbox_config production"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
sandbox_config:
  metadata:
    name: {{name}}
    version: {{version}}
    creator: {{creator}}
    description: {{description}}
  sandbox:
    type: {{sandbox_type}}
    isolation_level: {{isolation_level}}
    resource_limits:
      cpu: {{cpu_limit}}
      memory: {{memory_limit}}
      storage: {{storage_limit}}
    network:
      allowed_ports: {{allowed_ports}}
      firewall_rules: {{firewall_rules}}
  environment:
    variables:
      {{env_var_name}}: {{env_var_value}}
  dependencies:
    - {{dependency_1}}
    - {{dependency_2}}
```
