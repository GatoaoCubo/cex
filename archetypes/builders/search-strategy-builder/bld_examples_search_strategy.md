---
kind: examples
id: bld_examples_search_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of search_strategy artifacts
quality: 9.0
title: "Examples Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, examples]
tldr: "Golden and anti-examples of search_strategy artifacts"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "Dynamic Resource Allocation for Query Complexity"
author: "AI Systems Team"
date: "2023-10-01"
keywords: search_strategy, compute_allocation, inference_optimization
---

**Strategy**: Allocate compute resources based on query complexity during inference.  
**Implementation**:  
1. Preprocess queries to estimate complexity (e.g., length, entity count).  
2. Use a tiered compute budget:  
   - Low complexity: 1 GPU core, 2 threads.  
   - Medium: 2 GPU cores, 4 threads.  
   - High: 4 GPU cores, 8 threads.  
3. Monitor latency and adjust budgets dynamically using feedback loops.  
**Parameters**: `max_threads`, `gpu_cores_per_tier`, `latency_threshold`.  
**Benefits**: Balances speed and accuracy, adapts to workload variations.
```

## Anti-Example 1: Confusing with Reasoning Strategy
```markdown
---
title: "Prompt-Based Compute Allocation"
author: "Novice Developer"
date: "2023-09-15"
keywords: reasoning_strategy, prompt_tuning
---

**Strategy**: Use prompts like "Use more compute" to influence model behavior.  
**Implementation**:  
- Insert instruction: "Allocate maximum resources for this query."  
**Parameters**: None.  
**Benefits**: "Simplifies" resource management through natural language.
```
## Why it fails: This is a reasoning_strategy (prompt technique), not a search_strategy. It relies on model interpretation of text, not explicit compute allocation logic.

## Anti-Example 2: Vague Allocation Rules
```markdown
---
title: "Generic Compute Strategy"
author: "Unspecified"
date: "2023-08-20"
keywords: search_strategy
---

**Strategy**: "Use more resources when needed."  
**Implementation**:  
- "Sometimes increase GPU usage."  
**Parameters**: None.  
**Benefits**: "Flexible" approach.
```
## Why it fails: No actionable rules or metrics for determining "need." Lacks parameters, tiers, or feedback mechanisms, making it unimplementable.
