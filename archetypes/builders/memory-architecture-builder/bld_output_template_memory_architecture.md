---
kind: output_template
id: bld_output_template_memory_architecture
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for memory_architecture production
quality: null
title: "Output Template Memory Architecture"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_architecture, builder, output_template]
tldr: "Template with vars for memory_architecture production"
domain: "memory_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p10_marc_{{name}}.md
name: {{name}}
pillar: P10
kind: memory_architecture
quality: null
description: {{description}}
tags: {{tags}}
---
```

<!-- id: Unique identifier following pattern p10_marc_[a-z][a-z0-9_]+.md -->
<!-- name: Human-readable name of the memory architecture -->
<!-- pillar: Always "P10" for this template -->
<!-- kind: Always "memory_architecture" for this template -->
<!-- quality: Always null -->
<!-- description: Brief overview of the architecture -->
<!-- tags: List of relevant keywords -->

### Example Memory Hierarchy
| Level | Type   | Capacity | Access Time |
|-------|--------|----------|-------------|
| L1    | SRAM   | 32KB     | 1ns         |
| L2    | SRAM   | 256KB    | 5ns         |
| L3    | DRAM   | 4GB      | 50ns        |

```c
// Pseudocode for memory access
void fetch_data(address) {
    if (L1.contains(address)) {
        return L1.read(address);
    } else if (L2.contains(address)) {
        return L2.read(address);
    } else {
        return L3.read(address);
    }
}
```
