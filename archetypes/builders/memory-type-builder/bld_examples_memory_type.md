---
kind: examples
id: bld_examples_memory_type
pillar: P07
llm_function: GOVERN
quality: 9.0
title: "Examples Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Examples: memory_type

## Golden: Correction

| Field | Value |
|-------|-------|
| id | p10_mt_correction |
| type_name | correction |
| decay_rate | 0.00 |
| preserve_on_compact | true |
| tldr | User-corrected facts -- permanent, zero decay |

Definition: Explicit user overrides. "No, YAML not JSON." Zero decay = ground truth.
Decay: 0.00 -- never loses confidence. Verified by authoritative source.
Storage: Append to bld_memory. Never overwrite. Always preserve. Confidence 1.0.
Examples: (1) "pt-BR not en-US" (2) "API /v2 not /v1" (3) "voice warm, not clinical"
Anti-ex: (1) "prefer bullets" = PREFERENCE (2) "we use tabs" = CONVENTION

## Golden: Context

| Field | Value |
|-------|-------|
| type_name | context |
| decay_rate | 0.05 |
| preserve_on_compact | false |
| tldr | Session-bound situational facts -- fast decay |

Definition: Time-bound facts. "Debugging auth module now." Fast decay after session.
Storage: Session memory. First to drop on compaction (Wire 6).
Examples: (1) "working on auth today" (2) "file open: router.py" (3) "sprint 14"
Anti-ex: (1) "always use auth middleware" = CONVENTION (repeatable pattern)

## Anti-Example: Misclassified

| Field | Wrong Value | Correct Value | Why |
|-------|------------|---------------|-----|
| type_name | correction | context | "Today working on X" is temporal, no override |
| decay_rate | 0.00 | 0.05 | Session-bound, not permanent |
| preserve | true | false | No long-term value after session |

Rule: If observation contains "today/now/currently" WITHOUT contradicting agent, it is CONTEXT not CORRECTION.
