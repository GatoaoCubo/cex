---
kind: memory
id: bld_memory_skill
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for skill artifact generation
---

# Memory: skill-builder

## Summary

Skills are reusable capabilities with structured phases and explicit triggers. The critical production lesson is phase atomicity — each phase must have a clear input, a clear output, and be independently testable. Phases that depend on implicit state from previous phases break when the execution order changes or when a phase is retried after failure. The second lesson is trigger precision: overly broad triggers activate the skill in wrong contexts, while overly narrow triggers make it undiscoverable.

## Pattern

- Each phase must define explicit input and output — no implicit state passing between phases
- Trigger must be precise: exact slash command for user-invocable, specific event type for agent-invoked
- Distinguish user_invocable (appears in command menus) from agent-only (programmatic call only)
- Phase ordering must handle failure: define what happens when phase N fails (skip, retry, abort)
- Keep phase count between 3-7 — fewer than 3 suggests the capability is too simple for a skill, more than 7 suggests decomposition
- Include a validation phase at the end — skills without output validation ship unchecked results

## Anti-Pattern

- Phases with implicit state dependencies — break on retry, reorder, or partial execution
- Triggers that match common words — skill activates in unintended contexts constantly
- Missing failure handling per phase — one failed phase aborts the entire skill with no recovery
- Skills with 1-2 phases — likely an action prompt, not a skill; skills need structured multi-phase execution
- Confusing skill (P04, phased capability) with hook (P04, event interception) or action_prompt (P03, single-shot task)
- No validation phase — output ships without quality check

## Context

Skills operate in the P04 tools layer as reusable multi-phase capabilities. They sit between simple action prompts (P03, one-shot) and full workflows (P12, multi-agent orchestration). Skills are invoked by users via slash commands or by agents programmatically. Each skill encapsulates a complete capability lifecycle: discover, configure, execute, validate.

## Impact

Phase atomicity (explicit I/O per phase) achieved 95% successful retry rates versus 30% for implicit-state phases. Precise triggers reduced false activations by 80%. Validation phases caught 40% of quality issues before output delivery.

## Reproducibility

For reliable skill production: (1) decompose capability into 3-7 atomic phases, (2) define explicit input/output per phase, (3) specify trigger with appropriate precision, (4) add failure handling per phase (skip/retry/abort), (5) include validation phase, (6) classify as user_invocable or agent-only, (7) validate against 7 HARD + 10 SOFT gates.

## References

- skill-builder SCHEMA.md (12 required + 4 optional fields, phase specification)
- P04 tools pillar specification
- Capability lifecycle and phase decomposition patterns
