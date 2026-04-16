---
kind: examples
id: bld_examples_consolidation_policy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of consolidation_policy artifacts
quality: 8.9
title: "Examples: consolidation_policy artifacts"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, examples]
tldr: "Golden example: MemGPT-style promotion + eviction + compliance. Anti-examples: OS GC (wrong domain) and missing promotion rules."
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Golden Example: Customer Support Agent (PRO tier)

```yaml
---
id: p10_cp_customer_support_pro
kind: consolidation_policy
pillar: P10
title: "Consolidation Policy: Customer Support Agent (PRO)"
version: "1.0.0"
created: "2026-04-14"
author: n06_commercial
domain: customer-support
quality: null
tags: [consolidation_policy, customer_support, pro]
tldr: "PRO tier: session-end episodic promotion, importance-gated semantic, 90-day TTL, LRU eviction."
tier: pro
eviction_strategy: hybrid
consolidation_async: true
importance_floor: 0.3
retention_days: 90
promotion_threshold: 0.7
audit_trail: false
---
```

**Why golden**: all required frontmatter, consolidation_async: true, tier=pro,
eviction_strategy=hybrid, importance_floor + promotion_threshold defined. Body includes
Promotion Rules table, Eviction Rules table, importance scoring formula, async job spec,
and FREE/PRO/ENTERPRISE tier matrix. No OS memory terminology.

## Anti-Example 1: OS/GC Domain Contamination (D04)

```yaml
---
id: p10_cp_pytorch_gc
kind: consolidation_policy
title: "PyTorch Memory Consolidation for LLM Inference"
vendor: Meta
version: 1.13.1
description: "Memory lifecycle for PyTorch inference with mark-and-sweep GC"
body:
  garbage_collection:
    interval: "every 100ms"
    strategy: "mark_and_sweep"
  eviction:
    trigger: "90% GPU utilization"
    action: "evict_low_priority_tensors"
---
```

**Why it fails**:
- Describes PyTorch tensor management and GPU memory -- NOT agent memory
- `garbage_collection: mark_and_sweep` is OS/GC terminology, wrong domain
- No `consolidation_async` field, no `importance_floor`, no `tier`
- No Promotion Rules (working->episodic) or Semantic Promotion
- Missing all required frontmatter fields (`pillar`, `quality`, `tags`, `tldr`)

## Anti-Example 2: Missing Promotion Rules

```yaml
---
id: p10_cp_minimal
kind: consolidation_policy
pillar: P10
tier: pro
consolidation_async: true
eviction_strategy: ttl
retention_days: 90
---
## Eviction Rules
Delete everything older than 90 days.
```

**Why it fails**:
- Has eviction but NO promotion rules: episodic -> semantic promotion is missing
- Eviction rule is a sentence, not a structured table
- No importance scoring section
- No Commercial Tier Matrix
- Missing required frontmatter: `quality`, `tags`, `tldr`, `domain`, `author`
- Fails H05 (Promotion Rules section absent), D2 (0.0), D3 (0.0)
