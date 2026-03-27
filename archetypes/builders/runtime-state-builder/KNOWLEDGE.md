---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for runtime_state production
sources: [State Machine Theory, Decision Trees, Behavioral AI, CEX Architecture]
---

# Domain Knowledge: runtime_state

## Foundational Concepts
Runtime state captures an agent's LIVE decision-making context.
Unlike design-time mental models (static blueprints), runtime_state evolves
during execution based on inputs, outcomes, and environmental changes.
In CEX: declarative state definitions that agents use for routing, prioritization, and adaptation.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Finite State Machines | States, transitions, triggers | State Transitions section |
| Decision Trees | Branch conditions, outcomes | Decision Tree section |
| Behavior Trees | Priority-ordered task selection | Priorities + Heuristics |
| Blackboard Architecture | Shared state for multi-agent | Runtime state as shared context |
| Actor Model | Message-driven state changes | Update triggers per task |

## Key Principles
- Runtime state is MUTABLE (changes during execution)
- Design-time identity is IMMUTABLE (set at creation, never changes at runtime)
- Session state is EPHEMERAL (lost on session end)
- Runtime state ACCUMULATES within a session (or cross-session if persistence=cross_session)
- Routing rules need CONCRETE conditions and confidence thresholds
- State transitions need EXPLICIT triggers (not implicit)
- Priorities must be ORDERED (tie-breaking requires explicit rank)

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| routing_mode | How agent routes tasks | Decision tree type |
| persistence | State lifetime scope | Session vs cross-session |
| update_frequency | When state refreshes | Event-driven vs polling |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| mental_model (P02) | DESIGN-TIME identity (fixed, immutable) | Does NOT change at runtime |
| session_state (P10) | EPHEMERAL snapshot (reset each session) | Does NOT accumulate |
| learning_record (P10) | PERSISTENT across sessions (long-term memory) | Does NOT drive runtime decisions |
| axiom (P10) | IMMUTABLE fundamental rule | Does NOT evolve |
