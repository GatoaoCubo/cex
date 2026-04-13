---
kind: output_template
id: bld_output_template_vad_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for vad_config production
quality: null
title: "Output Template Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, output_template]
tldr: "Template with vars for vad_config production"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
name: {{name}}
description: {{description}}
version: {{version}}
kind: vad_config
pillar: P09

parameters:
  threshold: {{threshold}}
  sensitivity: {{sensitivity}}
  language: {{language}}

sections:
  - name: {{section1_name}}
    content: {{section1_content}}
  - name: {{section2_name}}
    content: {{section2_content}}

metadata:
  author: {{author}}
  date: {{date}}
```
