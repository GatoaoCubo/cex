---
kind: output_template
id: bld_output_template_memory_benchmark
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for memory_benchmark production
quality: 8.8
title: "Output Template Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, output_template]
tldr: "Template with vars for memory_benchmark production"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p07_mb_{{name}}.md
name: {{benchmark_name}}
quality: null
description: <!-- Brief overview of the memory benchmark purpose -->
test_cases: <!-- List of test cases with memory metrics -->
---
```

## Test Cases
| Test Case         | Memory Usage (MB) |
|-------------------|-------------------|
| {{test_case_1}}   | {{value_1}}       |
| {{test_case_2}}   | {{value_2}}       |

## Sample Code
```python
def allocate_memory(size_mb):
    # Allocate and measure memory usage
    buffer = bytearray(size_mb * 1024 * 1024)
    return len(buffer) / (1024 * 1024)
```

<!-- Replace {{name}} with benchmark identifier following p07_mb_[a-z][a-z0-9_]+ pattern -->
<!-- {{benchmark_name}}: Human-readable benchmark title -->
<!-- {{test_case_1}}, {{value_1}}: Specific test scenario and measured memory -->
