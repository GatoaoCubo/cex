---
kind: output_template
id: bld_output_template_trajectory_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for trajectory_eval production
quality: null
title: "Output Template Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, output_template]
tldr: "Template with vars for trajectory_eval production"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p07_te_{{id}}  # Use pattern: p07_te_[a-z][a-z0-9_]+
name: {{name}}     # Human-readable evaluation name
quality: null      # Must remain null
description: {{description}}  # Summary of evaluation purpose
parameters:
  {{param1}}: {{value1}}  # Example parameter
  {{param2}}: {{value2}}  # Another parameter
metrics:
  {{metric1}}: {{value}}  # Quantitative result
  {{metric2}}: {{value}}  # Another metric
version: {{version}}  # Schema version number
---
```

| Metric       | Value  | Unit   |
|--------------|--------|--------|
| Accuracy     | {{acc}}| %      |
| Latency      | {{lat}}| ms     |
| Throughput   | {{thr}}| req/s  |

```python
# Example trajectory data
trajectory = {
    "points": [{{x1}}, {{y1}}],  # X/Y coordinates
    "timestamp": {{ts}},        # Evaluation time
    "error": {{err}}           # Deviation from target
}
```
