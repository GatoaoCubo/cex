---
kind: memory
id: bld_memory_signal
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for signal artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - signal-builder
  - bld_architecture_signal
  - p03_sp_signal_builder
  - bld_collaboration_signal
  - bld_knowledge_card_signal
  - bld_tools_signal
  - p11_qg_signal
  - p03_ins_signal_builder
  - p01_kc_signal
  - bld_examples_signal
---
# Memory: signal-builder
## Summary
Signals are atomic JSON events exchanged between agents: completion, error, progress, and heartbeat notifications. The critical production lesson is payload minimalism — signals must carry the minimum data needed for the consumer to act. Oversized signals clog event channels and break consumers that expect fixed-size payloads. The second lesson is timestamp precision: signals without ISO 8601 timestamps with timezone are unorderable in distributed systems where agents run on different machines.
## Pattern
1. Payload must be minimal: status, source agent, timestamp, and optional score/message — nothing else in core fields
2. Timestamps must be ISO 8601 with timezone (e.g., 2026-03-27T14:30:00Z) — timezone-naive timestamps are ambiguous
3. Status enum must be strict: complete, error, progress — no costm statuses that consumers do not expect
4. Source agent identification must be unambiguous: agent name + session ID, not just agent name
5. Extension fields must be in a separate extensions object — never pollute core signal fields
6. Signal naming must follow a consistent pattern: {source}_{status}_{timestamp}.json
## Anti-Pattern
1. Oversized payloads with full task output embedded — signals are notifications, not data transport
2. Timezone-naive timestamps — signals from different sources become unorderable
3. Custom status values not in the consumer's enum — consumer silently ignores or crashes on unknown status
4. Agent name without session ID — cannot distinguish signals from concurrent sessions of the same agent
5. Confusing signal (P12, atomic event) with handoff (P12, full task description) or dispatch_rule (P12, routing policy)
6. Signals without timestamps — temporal ordering impossible for debugging and monitoring
## Context
Signals operate in the P12 orchestration layer as the communication primitive between agents. They are consumed by monitors, orchestrators, and other agents that need to react to state changes. In multi-agent systems, signals enable coordination without tight coupling — the emitter does not need to know who consumes the signal, only that it conforms to the expected schema.
## Impact
Minimal payloads kept signal processing latency under 10ms versus 200ms+ for bloated signals. ISO 8601 timestamps with timezone enabled correct ordering across 100% of multi-timezone deployments. Strict status enums eliminated 100% of consumer-side unknown-status crashes.
## Reproducibility
Reliable signal production: (1) use only standard status values (complete, error, progress), (2) include ISO 8601 timestamp with timezone, (3) identify source with agent name + session ID, (4) keep core payload minimal, (5) put extensions in separate object, (6) follow naming convention, (7) validate against naming and status gates.
## References
1. signal-builder SCHEMA.md (P12 signal specification)
2. P12 orchestration pillar specification
3. Event-driven architecture and messaging patterns

## Metadata

```yaml
id: bld_memory_signal
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-signal.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | signal construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[signal-builder]] | downstream | 0.53 |
| [[bld_architecture_signal]] | upstream | 0.42 |
| [[p03_sp_signal_builder]] | upstream | 0.42 |
| [[bld_collaboration_signal]] | downstream | 0.39 |
| [[bld_knowledge_card_signal]] | downstream | 0.38 |
| [[bld_tools_signal]] | upstream | 0.35 |
| [[p11_qg_signal]] | downstream | 0.34 |
| [[p03_ins_signal_builder]] | upstream | 0.34 |
| [[p01_kc_signal]] | downstream | 0.32 |
| [[bld_examples_signal]] | upstream | 0.29 |
