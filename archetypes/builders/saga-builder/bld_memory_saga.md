---
id: bld_memory_saga
kind: knowledge_card
pillar: P10
title: "Memory: saga Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: 7.8
tags: [memory, saga, P12]
llm_function: INJECT
tldr: "Recalled patterns and corrections for saga builder sessions."
density_score: null
related:
  - p10_lr_instruction_builder
  - bld_memory_workflow
  - p11_qg_workflow
  - bld_knowledge_card_workflow
  - p10_lr_chain_builder
  - bld_instruction_chain
  - tpl_instruction
  - p03_ins_workflow
  - p01_kc_workflow
  - p11_qg_instruction
---

# Memory: saga Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| Every step MUST have compensating_action | HIGH | Gate H06 |
| Make compensating actions idempotent | HIGH | Retry safety |
| Rollback is reverse order of completed steps | HIGH | Saga invariant |
| steps_count must match list | HIGH | Gate H07 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User conflates with workflow | Teach: workflow has no compensation; saga does |
| User designs step without undo | Block: every step needs compensating_action |
| User sets compensating_action: null | Reject: must be idempotent undo action |
| User mixes choreography and orchestration | Choose one topology per saga |
| User exceeds 10 steps | Suggest splitting into sub-sagas |

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_instruction_builder]] | related | 0.28 |
| [[bld_memory_workflow]] | related | 0.26 |
| [[p11_qg_workflow]] | downstream | 0.26 |
| [[bld_knowledge_card_workflow]] | sibling | 0.24 |
| [[p10_lr_chain_builder]] | related | 0.23 |
| [[bld_instruction_chain]] | upstream | 0.23 |
| [[tpl_instruction]] | upstream | 0.21 |
| [[p03_ins_workflow]] | upstream | 0.21 |
| [[p01_kc_workflow]] | sibling | 0.20 |
| [[p11_qg_instruction]] | downstream | 0.20 |
