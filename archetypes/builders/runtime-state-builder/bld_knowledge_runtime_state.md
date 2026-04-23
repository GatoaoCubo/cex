---
kind: knowledge_card
id: bld_knowledge_card_runtime_state
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for runtime_state production — atomic searchable facts
sources: runtime-state-builder MANIFEST.md + SCHEMA.md, state machine theory, BDI architecture
quality: 9.1
title: "Knowledge Card Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_runtime_state
  - runtime-state-builder
  - p03_sp_runtime_state_builder
  - bld_collaboration_runtime_state
  - p11_qg_runtime_state
  - p03_ins_runtime_state
  - bld_architecture_runtime_state
  - bld_knowledge_card_mental_model
  - p01_kc_runtime_state
  - p03_ins_mental_model
---

# Domain Knowledge: runtime_state
## Executive Summary
Runtime states are mutable cognitive contexts that agents accumulate during execution — live routing rules, decision trees, priorities, and heuristics that evolve based on inputs and outcomes. Each runtime state captures ONE agent's current decision-making context with explicit state transitions and persistence scope. They differ from mental models (P02, static design-time blueprints), session states (ephemeral snapshots lost on session end), learning records (persistent cross-session experience), and axioms (immutable truths) by being mutable, accumulative decision contexts that can persist within or across sessions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| Kind | `runtime_state` (exact literal) |
| ID pattern | `p10_rs_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 9 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Persistence | within_session or cross_session |
| Key sections | Routing Rules, Decision Tree, Priorities, Heuristics, State Transitions |
## Patterns
| Pattern | Application |
|---------|-------------|
| Mutable state | Runtime state evolves during execution; design-time identity does not |
| Concrete routing conditions | Keywords as concrete nouns/verbs with confidence thresholds |
| Decision tree depth | Max 3 levels to avoid reasoning complexity |
| Ordered priorities | Explicit rank order; tie-breaking requires explicit rules |
| Explicit triggers | State transitions have named triggers, not implicit changes |
| Persistence declaration | within_session (default) or cross_session (requires justification) |
| Update frequency | Event-driven (on task completion) or polling (interval-based) |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `pillar: P02` on runtime_state | P02 is design-time; runtime_state is P10 |
| Mixing identity with state | Agent identity belongs in agent/mental_model, not runtime_state |
| No state transitions defined | State without transitions is a static snapshot, not runtime state |
| Implicit persistence | Must declare within_session or cross_session explicitly |
| Routing without confidence thresholds | Ambiguous dispatch; no fallback logic possible |
| cross_session without justification | Most state is session-scoped; persistence needs rationale |
## Application
1. Identify the target agent and its runtime decision requirements
2. Define routing_rules with keywords, actions, confidence thresholds
3. Define decision_tree with max 3 levels of if/then/else
4. Set priorities in explicit rank order
5. Write heuristics for edge cases specific to this agent's domain
6. Define state transitions with named triggers and conditions
7. Set persistence scope (within_session or cross_session)
8. Validate: 9 HARD + 10 SOFT gates, body <= 3072 bytes
## References
- runtime-state-builder SCHEMA.md v1.0.0
- Finite State Machine theory
- BDI architecture (Belief-Desire-Intention)
- Blackboard architecture (shared multi-agent state)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_runtime_state]] | downstream | 0.62 |
| [[runtime-state-builder]] | downstream | 0.59 |
| [[p03_sp_runtime_state_builder]] | downstream | 0.56 |
| [[bld_collaboration_runtime_state]] | downstream | 0.51 |
| [[p11_qg_runtime_state]] | downstream | 0.50 |
| [[p03_ins_runtime_state]] | downstream | 0.47 |
| [[bld_architecture_runtime_state]] | downstream | 0.44 |
| [[bld_knowledge_card_mental_model]] | sibling | 0.40 |
| [[p01_kc_runtime_state]] | sibling | 0.38 |
| [[p03_ins_mental_model]] | downstream | 0.34 |
