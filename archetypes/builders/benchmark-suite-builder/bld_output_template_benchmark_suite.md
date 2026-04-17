---
kind: output_template
id: bld_output_template_benchmark_suite
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for benchmark_suite production
quality: 8.8
title: "Output Template Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, output_template]
tldr: "Template with vars for benchmark_suite production"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
id: p07_bs_{{name}}.md
name: {{benchmark_name}}
description: {{benchmark_description}}
quality: null
tags: ["{{tag1}}", "{{tag2}}"]
---
```

<!-- Benchmark overview -->
## Overview

This benchmark evaluates {{benchmark_purpose}}.

### Key Metrics
| Metric          | Value       | Unit  |
|-----------------|-------------|-------|
| Throughput      | {{throughput}} | TPS   |
| Latency         | {{latency}}   | ms    |
| Error Rate      | {{error_rate}}| %     |

<!-- Example test script -->
```python
# Sample Test Script
import {{library_name}}

def run_test():
    client = {{library_name}}.Client()
    results = client.run_benchmark(
        duration={{duration}},
        concurrency={{concurrency}}
    )
    return results
```

<!-- Notes -->
## Notes
- {{implementation_details}}
- {{constraints}}
```
