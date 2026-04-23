---
id: bld_memory_domain_event
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 8.1
tags: [domain_event, memory, patterns]
title: "Memory Patterns: domain_event"
author: builder
density_score: 0.99
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_signal
  - p03_sp_signal_builder
  - bld_knowledge_card_signal
  - bld_instruction_hook
  - bld_tools_signal
  - p11_qg_signal
  - bld_output_template_webhook
  - bld_collaboration_hook
  - bld_collaboration_memory_scope
  - bld_memory_signal
---
# Memory Patterns: domain_event
## What to Remember
- Event naming: ALWAYS past tense. OrderPlaced NOT PlaceOrder
- Aggregate ownership: each event belongs to EXACTLY ONE aggregate root
- Payload immutability: record state AT occurrence_time, never current state
- Causation chain: event_id -> causation_id -> correlation_id (tracing backbone)

## Common Mistakes to Avoid
| Mistake | Correction |
|---------|-----------|
| Command as event name (ProcessPayment) | Past tense (PaymentProcessed) |
| Missing aggregate_root | Always name the DDD aggregate |
| Mutable payload field | Snapshot only, freeze at occurred_at |
| Conflating with signal | Check: is it business-meaningful? -> domain_event |

## Cross-Kind Memory
- data_contract: publish domain_event schema to consumers via data_contract
- bounded_context: domain_events are scoped to their bounded_context
- workflow: domain_events trigger workflows (one-way dependency)
- audit_log: downstream consumers may convert domain_events to audit_log

## Reuse Signals
Search for existing domain_events before creating new ones:
- grep P12 for de_ prefix files
- check bounded_context event catalog if it exists

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
| [[p01_kc_signal]] | downstream | 0.25 |
| [[p03_sp_signal_builder]] | upstream | 0.22 |
| [[bld_knowledge_card_signal]] | downstream | 0.20 |
| [[bld_instruction_hook]] | upstream | 0.20 |
| [[bld_tools_signal]] | upstream | 0.18 |
| [[p11_qg_signal]] | downstream | 0.18 |
| [[bld_output_template_webhook]] | upstream | 0.18 |
| [[bld_collaboration_hook]] | downstream | 0.18 |
| [[bld_collaboration_memory_scope]] | downstream | 0.17 |
| [[bld_memory_signal]] | related | 0.17 |
