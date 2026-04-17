---
kind: output_template
id: bld_output_template_eval_metric
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for eval_metric production
quality: 8.7
title: "Output Template Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, output_template]
tldr: "Template with vars for eval_metric production"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p07_em_{{metric_name}}.md
name: {{metric_name}}
description: {{brief_description_of_metric}}
type: eval_metric
quality: null
parameters:
  - name: {{param1}}
    description: {{param1_description}}
examples:
  - {{example_usage}}
---
```

<!-- metric_name: Replace with lowercase alphanumeric name (e.g., 'accuracy') -->
<!-- brief_description_of_metric: 1-2 sentence summary of metric purpose -->
<!-- param1: First parameter name (e.g., 'threshold') -->
<!-- param1_description: Explanation of parameter's role -->
<!-- example_usage: Code snippet showing metric application -->

| Metric         | Description                  | Type      |
|----------------|------------------------------|-----------|
| p07_em_accuracy | Measures classification correctness | eval_metric |
