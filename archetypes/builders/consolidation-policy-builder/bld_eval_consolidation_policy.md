---
kind: quality_gate
id: p10_qg_consolidation_policy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for consolidation_policy
quality: 9.0
title: "Quality Gate: consolidation_policy"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, quality_gate]
tldr: "HARD gates enforce artifact structure (schema, ID, async flag, promotion rules). SOFT scoring weights domain accuracy, eviction completeness, commercial differentiation, and compliance."
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_consolidation_policy
  - bld_instruction_consolidation_policy
  - p10_qg_memory_architecture
  - p10_qg_procedural_memory
  - bld_schema_consolidation_policy
  - p03_sp_consolidation_policy_builder
  - bld_examples_memory_architecture
  - bld_output_template_consolidation_policy
  - bld_tools_consolidation_policy
  - p10_mem_consolidation_policy_builder
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Required frontmatter fields | 100% | == | Artifact |
| consolidation_async | true | == | Artifact |
| Promotion Rules section present | true | == | Artifact |
| Eviction Rules section present | true | == | Artifact |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches `^p10_cp_[a-z][a-z0-9_]+$` | ID absent or does not match pattern |
| H03 | kind field equals `consolidation_policy` | kind field absent, wrong, or misspelled |
| H04 | `consolidation_async: true` in frontmatter | Field absent or set to false |
| H05 | Promotion Rules section present with table | Section absent or table empty |
| H06 | Eviction Rules section present with table | Section absent or table empty |
| H07 | No OS memory management content (GC, slab, heap, TLB, fragmentation) | OS terminology present |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D1 | Domain accuracy | 0.25 | 1.0 = all content is LLM agent memory; 0.0 = OS/GC contamination |
| D2 | Promotion completeness | 0.20 | 1.0 = all tier transitions defined with conditions; 0.5 = partial; 0.0 = absent |
| D3 | Commercial differentiation | 0.20 | 1.0 = FREE/PRO/ENTERPRISE matrix with 5+ features; 0.5 = partial; 0.0 = absent |
| D4 | Eviction coverage | 0.20 | 1.0 = eviction defined per layer with trigger + action; 0.5 = partial; 0.0 = absent |
| D5 | Compliance coverage | 0.15 | 1.0 = retention_days + gdpr_erasure + audit_trail; 0.5 = partial; 0.0 = absent (enterprise penalized more) |

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- archive as gold standard example |
| >= 8.0 | PUBLISH -- merge to main |
| >= 7.0 | REVIEW -- surgical fix before merge |
| < 7.0 | REJECT -- rebuild required |

## Bypass

| Condition | Approver | Audit Trail |
|-----------|----------|------------|
| Emergency patching of agent memory incident | N07 + N06 | Incident report with justification |
| Free-tier artifact with no consolidation (correct behavior) | N06 | Tier=free annotation in frontmatter |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
