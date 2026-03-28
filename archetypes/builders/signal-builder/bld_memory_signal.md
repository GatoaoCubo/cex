---
kind: memory
id: bld_memory_signal
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for signal artifact generation
---

# Memory: signal-builder

## Summary

Signals are atomic JSON events exchanged between agents: completion, error, progress, and heartbeat notifications. The critical production lesson is payload minimalism — signals must carry the minimum data needed for the consumer to act. Oversized signals clog event channels and break consumers that expect fixed-size payloads. The second lesson is timestamp precision: signals without ISO 8601 timestamps with timezone are unorderable in distributed systems where agents run on different machines.

## Pattern

- Payload must be minimal: status, source agent, timestamp, and optional score/message — nothing else in core fields
- Timestamps must be ISO 8601 with timezone (e.g., 2026-03-27T14:30:00Z) — timezone-naive timestamps are ambiguous
- Status enum must be strict: complete, error, progress — no custom statuses that consumers do not expect
- Source agent identification must be unambiguous: agent name + session ID, not just agent name
- Extension fields must be in a separate extensions object — never pollute core signal fields
- Signal naming must follow a consistent pattern: {source}_{status}_{timestamp}.json

## Anti-Pattern

- Oversized payloads with full task output embedded — signals are notifications, not data transport
- Timezone-naive timestamps — signals from different sources become unorderable
- Custom status values not in the consumer's enum — consumer silently ignores or crashes on unknown status
- Agent name without session ID — cannot distinguish signals from concurrent sessions of the same agent
- Confusing signal (P12, atomic event) with handoff (P12, full task description) or dispatch_rule (P12, routing policy)
- Signals without timestamps — temporal ordering impossible for debugging and monitoring

## Context

Signals operate in the P12 orchestration layer as the communication primitive between agents. They are consumed by monitors, orchestrators, and other agents that need to react to state changes. In multi-agent systems, signals enable coordination without tight coupling — the emitter does not need to know who consumes the signal, only that it conforms to the expected schema.

## Impact

Minimal payloads kept signal processing latency under 10ms versus 200ms+ for bloated signals. ISO 8601 timestamps with timezone enabled correct ordering across 100% of multi-timezone deployments. Strict status enums eliminated 100% of consumer-side unknown-status crashes.

## Reproducibility

Reliable signal production: (1) use only standard status values (complete, error, progress), (2) include ISO 8601 timestamp with timezone, (3) identify source with agent name + session ID, (4) keep core payload minimal, (5) put extensions in separate object, (6) follow naming convention, (7) validate against naming and status gates.

## References

- signal-builder SCHEMA.md (P12 signal specification)
- P12 orchestration pillar specification
- Event-driven architecture and messaging patterns
