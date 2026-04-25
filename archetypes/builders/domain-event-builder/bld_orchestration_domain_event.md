---
id: bld_rules_domain_event
kind: guardrail
pillar: P11
llm_function: COLLABORATE
version: 1.0.0
quality: 7.7
tags: [domain_event, rules, guardrail]
title: "Rules: domain_event Builder"
author: builder
tldr: "Domain Event feedback: workflow coordination, handoffs, and lifecycle management"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_signal
  - p03_sp_signal_builder
  - p03_sp_webhook_builder
  - p03_sp_system-prompt-builder
  - bld_knowledge_card_signal
  - p03_sp_kind_builder
  - bld_config_signal
  - p03_sp_context_window_config_builder
  - bld_instruction_hook
  - p03_sp_input_schema_builder
---
# Builder Rules: domain_event
## ALWAYS
- ALWAYS name events in past tense (OrderPlaced, UserRegistered, PaymentFailed)
- ALWAYS identify the aggregate root -- events belong to aggregates, not services
- ALWAYS set quality: null
- ALWAYS include occurred_at with ISO-8601 UTC timestamp
- ALWAYS populate payload with at least 1 typed field

## NEVER
- NEVER name an event as a command (ProcessOrder, CreateUser)
- NEVER include mutable state in payload (no foreign key lookups at read time)
- NEVER conflate domain_event with signal (signal = system, domain_event = business)
- NEVER conflate domain_event with audit_log (audit = compliance, event = domain model)
- NEVER assign an event to a service -- only aggregates emit domain events

## EDGE CASES
| Case | Rule |
|------|------|
| Event spans multiple aggregates | Split into N events, one per aggregate |
| Event carries sensitive PII | Add pii_fields list; note retention policy |
| Event schema changes | Increment event_version (v1 -> v2), keep old version alive |
| Saga spans multiple BCs | Use correlation_id to link related events |

## Naming Conventions
| Pattern | Example |
|---------|---------|
| Entity + past verb | OrderPlaced, UserDeactivated |
| With qualifier | PaymentFailedDueToFraud (only when ambiguous) |
| ID prefix in file | de_{aggregate}_{verb}.md |

## Size Budget
max_bytes: 3072 (payload schema + causal chain + consumers = ~2KB typical)
Payload table preferred over inline YAML for density.

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_signal]] | downstream | 0.34 |
| [[p03_sp_signal_builder]] | upstream | 0.32 |
| [[p03_sp_webhook_builder]] | upstream | 0.27 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.26 |
| [[bld_knowledge_card_signal]] | downstream | 0.23 |
| [[p03_sp_kind_builder]] | upstream | 0.21 |
| [[bld_config_signal]] | upstream | 0.21 |
| [[p03_sp_context_window_config_builder]] | upstream | 0.21 |
| [[bld_instruction_hook]] | upstream | 0.21 |
| [[p03_sp_input_schema_builder]] | upstream | 0.20 |
