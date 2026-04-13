---
kind: output_template
id: bld_output_template_threat_model
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for threat_model production
quality: null
title: "Output Template Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, output_template]
tldr: "Template with vars for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
name: {{name}}
description: {{description}}
author: {{author}}
date: {{date}}
version: {{version}}
```

## p11_tm_{{name}}_overview
{{overview_content}}

## p11_tm_{{name}}_assets
{{assets_content}}

## p11_tm_{{name}}_threats
{{threats_content}}

## p11_tm_{{name}}_mitigations
{{mitigations_content}}

## p11_tm_{{name}}_assumptions
{{assumptions_content}}

## p11_tm_{{name}}_open_issues
{{open_issues_content}}
