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
related:
  - bld_collaboration_memory_benchmark
  - bld_collaboration_memory_type
  - memory-scope-builder
  - p01_kc_memory_scope
  - bld_collaboration_memory_scope
  - bld_output_template_benchmark_suite
  - bld_manifest_memory_type
  - bld_knowledge_card_memory_scope
  - bld_examples_memory_scope
  - memory-benchmark-builder
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_benchmark]] | downstream | 0.30 |
| [[bld_collaboration_memory_type]] | downstream | 0.29 |
| [[memory-scope-builder]] | upstream | 0.26 |
| [[p01_kc_memory_scope]] | upstream | 0.26 |
| [[bld_collaboration_memory_scope]] | downstream | 0.26 |
| [[bld_output_template_benchmark_suite]] | sibling | 0.25 |
| [[bld_manifest_memory_type]] | upstream | 0.24 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.23 |
| [[bld_examples_memory_scope]] | downstream | 0.22 |
| [[memory-benchmark-builder]] | downstream | 0.22 |
