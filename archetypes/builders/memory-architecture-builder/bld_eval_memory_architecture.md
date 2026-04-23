---
kind: quality_gate
id: p10_qg_memory_architecture
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for memory_architecture
quality: 9.0
title: "Quality Gate: memory_architecture"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, quality_gate]
tldr: "HARD gates enforce artifact structure (schema, ID, layers, tier matrix). SOFT scoring weights domain accuracy, layer coverage, commercial differentiation, and architecture depth."
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_memory_architecture
  - p03_sp_memory_architecture_builder
  - bld_instruction_memory_architecture
  - memory-architecture-builder
  - p10_mem_memory_architecture_builder
  - p10_qg_consolidation_policy
  - bld_output_template_memory_architecture
  - bld_schema_memory_architecture
  - p10_qg_procedural_memory
  - bld_instruction_consolidation_policy
---

## Quality Gate
## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Required frontmatter fields | 100% | == | Artifact |
| Memory layers defined | >= 1 | >= | Artifact |
| Tier matrix present | true | == | Artifact |
| Industry reference cited | >= 1 | >= | Artifact |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches `^p10_marc_[a-z][a-z0-9_]+$` | ID absent or does not match pattern |
| H03 | kind field equals `memory_architecture` | kind field absent, wrong, or misspelled |
| H04 | layers field present and non-empty | layers field missing or empty list |
| H05 | working layer defined or excluded with justification | No working layer and no exclusion note |
| H06 | Commercial Tier Matrix section present | Section absent or empty |
| H07 | No hardware memory content (DRAM, DDR5, SRAM, cache latency ns) | Hardware memory terminology present |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D1 | Domain accuracy | 0.25 | 1.0 = all content is LLM agent memory; 0.0 = hardware/OS contamination |
| D2 | Layer coverage | 0.20 | 1.0 = all 4 layers defined with backend; 0.5 = working only; 0.0 = none |
| D3 | Commercial differentiation | 0.20 | 1.0 = FREE/PRO/ENTERPRISE table with 5+ features; 0.5 = partial; 0.0 = absent |
| D4 | Architecture depth | 0.20 | 1.0 = read+write pipelines + eviction + backends; 0.5 = partial; 0.0 = overview only |
| D5 | Industry grounding | 0.15 | 1.0 = 3+ systems cited with year; 0.5 = 1 citation; 0.0 = no citations |

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
| Emergency patching of agent production incident | N07 + N06 | Incident report with justification |
| Prototype with explicitly scoped working-only memory | N06 | Prototype annotation in frontmatter |

## Examples
## Golden Example: Customer Support Agent (PRO tier)
```yaml
---
id: p10_marc_customer_support_pro
kind: memory_architecture
pillar: P10
title: "Memory Architecture: Customer Support Agent (PRO)"
version: "1.0.0"
created: "2026-04-14"
updated: "2026-04-14"
author: n06_commercial
domain: "customer-support"
quality: null
tags: [memory_architecture, customer_support, pro]
tldr: "4-layer memory for B2C support agent: working context + episodic (pgvector) + semantic (Redis JSON) + procedural (Redis KV). PRO tier."
layers: [working, episodic, semantic, procedural]
tier: pro
system_ref: memgpt
retention_days: 90
consolidation_enabled: true
---
```

**Why golden**: all required frontmatter, 4 layers defined, tier=pro, system_ref cited,
retention_days set, consolidation_enabled. Body includes read/write pipelines, eviction
per layer, and FREE/PRO/ENTERPRISE tier matrix. No hardware memory content.

## Anti-Example 1: Hardware Memory Contamination (D04 domain hallucination)
```yaml
---
id: p10_marc_server_memory
kind: memory_architecture
title: "DDR5 Memory Architecture with CXL 3.0"
memory_type: DRAM
capacity: 4294967296
access_time: 50.0
---
```

**Why it fails**:
- `memory_type: DRAM` -- hardware memory field, not agent memory
- `capacity: bytes` -- byte capacity is for DRAM, not LLM context
- `access_time: nanoseconds` -- hardware latency, not retrieval latency
- No `layers` field, no `tier` field, no `system_ref`
- Content describes JEDEC DDR5, CXL interconnects -- wrong domain entirely

## Anti-Example 2: Flat Design with No Eviction Policy
```yaml
---
id: p10_marc_flat_no_eviction
kind: memory_architecture
title: "Agent Memory (everything stored forever)"
layers: [working]
---
## Memory
Store all conversations in a list. Never delete.
```

**Why it fails**:
- Only working layer -- no episodic/semantic persistence
- No eviction policy -- unbounded storage growth
- No tier matrix -- misses commercial differentiation
- No backend specified -- not implementable
- Fails H06 (no tier matrix) and scores 0.0 on D3 (commercial differentiation)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
