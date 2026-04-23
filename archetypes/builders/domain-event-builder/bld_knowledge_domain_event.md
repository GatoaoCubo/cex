---
id: bld_kc_domain_event
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 7.6
tags: [domain_event, ddd, event-sourcing, knowledge]
title: "Knowledge: Domain Event Pattern"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_signal
  - bld_schema_audit_log
  - bld_instruction_hook
  - bld_knowledge_card_signal
  - bld_schema_hook
  - bld_collaboration_hook
  - bld_schema_action_paradigm
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_knowledge_card_hook_config
---
# Domain Knowledge: domain_event
## Core Facts
- DDD Domain Event (Evans 2003 ch.8): immutable record of domain-significant occurrence
- Named in past tense: OrderPlaced, PaymentFailed, CustomerUpgraded
- Carries snapshot payload -- data at time of occurrence, not current state
- Owned by aggregate root: Order emits OrderPlaced, not PaymentService
- Versioned independently (v1, v2) to support consumer schema evolution
- Three IDs: event_id (self), causation_id (what caused it), correlation_id (saga)

## Boundary vs. Similar Kinds
| Aspect | domain_event | signal | audit_log |
|--------|-------------|--------|-----------|
| Origin | Domain layer | Infrastructure | Compliance layer |
| Immutable | YES | YES | YES |
| Business meaning | YES | NO | PARTIAL |
| Consumer | Other BCs | Monitoring | Auditors |
| Pattern | DDD | Observability | SOX/GDPR |

## Event Schema Evolution Rules
- v1 -> v2: additive fields only (never remove, never rename)
- Breaking change requires new event type, not version bump
- Consumers must handle unknown fields (schema registry pattern)

## Anti-Patterns
| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| Mutable event (update payload after fact) | Events are immutable; emit corrective event |
| System event as domain event (HeartbeatReceived) | signal kind, not domain_event |
| Command disguised as event (PlaceOrder) | Events are past tense; commands are imperative |

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_signal]] | sibling | 0.34 |
| [[bld_schema_audit_log]] | downstream | 0.27 |
| [[bld_instruction_hook]] | downstream | 0.25 |
| [[bld_knowledge_card_signal]] | sibling | 0.24 |
| [[bld_schema_hook]] | downstream | 0.23 |
| [[bld_collaboration_hook]] | downstream | 0.22 |
| [[bld_schema_action_paradigm]] | downstream | 0.21 |
| [[bld_schema_search_strategy]] | downstream | 0.21 |
| [[bld_schema_reranker_config]] | downstream | 0.21 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.21 |
