---
kind: examples
id: bld_examples_thinking_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of thinking_config artifacts
quality: 8.9
title: "Examples Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, examples]
tldr: "Golden and anti-examples of thinking_config artifacts"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
```markdown
---
title: "Thinking Budget Configuration"
description: "Configures extended thinking with token budget limits"
version: "1.0"
author: "System Admin"
---

**thinking_budget**: 1000
**token_limits**: 
  - max_context: 500
  - max_response: 300
**dynamic_adjustment**: true
**fallback_strategy**: "truncate"
```

## Anti-Example 1: Missing Essential Fields
```markdown
---
title: "Incomplete Config"
description: "Missing thinking_budget parameter"
version: "0.5"
author: "Newbie"
---

**token_limits**: 
  - max_context: 500
  - max_response: 300
```
## Why it fails
Lacks required `thinking_budget` field, making resource allocation impossible.

## Anti-Example 2: Invalid Budget Values
```markdown
---
title: "Invalid Config"
description: "Uses non-numeric budget values"
version: "1.0"
author: "Mistake"
---

**thinking_budget**: "high"
**token_limits**: 
  - max_context: "unlimited"
  - max_response: 300
```
## Why it fails
Uses strings instead of numeric values for budget parameters, causing parsing errors.

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
