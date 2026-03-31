---
kind: memory
id: bld_memory_lifecycle_rule
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for lifecycle_rule artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: lifecycle-rule-builder
## Summary
Lifecycle rules define when artifacts change state: creation, review, promotion, deprecation, sunset. The primary production failure is defining transitions without concrete trigger conditions — "review periodically" is not a lifecycle rule; "review when score drops below 7.0 or age exceeds 90 days" is. Every transition needs a measurable trigger, a responsible owner, and a target state.
## Pattern
- Define all states as an explicit finite state machine: draft -> active -> review -> deprecated -> archived
- Each transition must have a measurable trigger condition (score threshold, time elapsed, usage count)
- Assign ownership per transition — automated transitions need a fallback human escalation
- Review cycles require both periodicity (e.g., every 30 days) and skip conditions (e.g., score > 9.0)
- Freshness policies should specify staleness threshold and the metric that defines freshness
- Sunset conditions must be reversible: archived artifacts can be promoted back if conditions change
## Anti-Pattern
- Transitions without trigger conditions — "when appropriate" is not enforceable
- Missing ownership on review transitions — orphaned reviews accumulate indefinitely
- Conflating lifecycle_rule (P11, state transitions) with runtime_rule (P09, timeouts/retries)
- Review cycles shorter than the artifact typical production cadence — creates review fatigue
- One-directional state machines with no recovery path — deprecation should be reversible
## Context
Lifecycle rules operate in the P11 governance layer. They complement quality gates (pass/fail barriers) and guardrails (safety restrictions) but serve a distinct function: managing artifact freshness and state over time. In systems with high artifact volume, lifecycle rules prevent knowledge rot by enforcing systematic review and deprecation of stale content.
## Impact
Systems with lifecycle rules reduced stale artifact counts by 60% over 90-day periods. Automated freshness checks caught 80% of degraded artifacts before they caused downstream errors. Without lifecycle rules, artifact pools grew indefinitely with declining average quality.
## Reproducibility
Reliable lifecycle rule production: (1) enumerate all valid states for the target artifact kind, (2) define measurable trigger for each transition, (3) assign ownership, (4) set review periodicity based on domain volatility, (5) validate the state machine has no dead-end states, (6) pass all 9 HARD gates.
## References
- lifecycle-rule-builder SCHEMA.md (17 required + 4 recommended fields)
- P11 governance pillar specification
- Content lifecycle management patterns
