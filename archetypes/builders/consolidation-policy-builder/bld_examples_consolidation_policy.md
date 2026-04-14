---
kind: examples
id: bld_examples_consolidation_policy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of consolidation_policy artifacts
quality: null
title: "Examples Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, examples]
tldr: "Golden and anti-examples of consolidation_policy artifacts"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
title: "PyTorch Memory Consolidation Policy for Large Language Models"
kind: consolidation_policy
vendor: Meta
version: 1.13.1
description: "Memory lifecycle management for PyTorch-based LLM inference workloads"

body:
  memory_retention:
    - stage: "inference"
      duration: "session_lifetime"
      strategy: "reference_counting"
  eviction:
    - trigger: "memory_pressure"
      threshold: "90% GPU utilization"
      action: "evict_low_priority_tensors"
  garbage_collection:
    - interval: "every 100ms"
    - strategy: "mark_and_sweep"
  logging:
    - level: "debug"
    - metrics: ["resident_memory", "cached_tensors", "eviction_rate"]
```

## Anti-Example 1: Confusing with Memory Scope
```yaml
title: "Incorrect Memory Scope Policy"
kind: consolidation_policy
vendor: HuggingFace
version: 4.28.0
description: "Access control for model parameters"

body:
  access:
    - role: "inference"
      permissions: ["read", "write"]
    - role: "training"
      permissions: ["read", "write", "modify"]
```
## Why it fails
Mixes memory access rules (memory_scope) with lifecycle management. Consolidation_policy should handle retention/eviction, not access permissions.

## Anti-Example 2: Missing Critical Policies
```yaml
title: "Incomplete Memory Policy"
kind: consolidation_policy
vendor: Google
version: 2.5.0
description: "Basic memory management for TPU workloads"

body:
  garbage_collection:
    - interval: "every 5s"
```
## Why it fails
Lacks essential policies for memory retention, eviction strategies, and monitoring metrics. A complete policy must define full lifecycle management from allocation to deallocation.
