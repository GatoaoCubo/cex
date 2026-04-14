---
kind: output_template
id: bld_output_template_quantization_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for quantization_config production
quality: null
title: "Output Template Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, output_template]
tldr: "Template with vars for quantization_config production"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
id: {{id}}
version: {{version}}
pillar: P09
name: p09_qc_{{name}}
type: quantization_config

quantization_settings:
  method: {{method}}
  precision:
    bits: {{bits}}
    dtype: {{dtype}}
  parameters:
    group_size: {{group_size}}
    scale_type: {{scale_type}}
    zero_point: {{zero_point}}
  hardware_target:
    architecture: {{arch}}
    optimization_level: {{opt_level}}
```
