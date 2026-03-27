---
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-builder works with other builders and runtime actors
pattern: each builder must know its role in a team, what it receives, and what it emits
---

# Collaboration: handoff-builder

## My Role in Crews
I am a TASK DELEGATION specialist.
I package complete execution briefs so satellites can work autonomously
with clear context, scope, and commit rules.

## Typical Collaboration Chain

```text
dispatch_rule selects -> handoff instructs -> execution -> signal reports
```

I sit between routing and execution, providing the complete instruction set.

## I Receive
- target satellite and mission name
- task descriptions and context
- scope constraints and quality targets

## I Produce
- one markdown handoff artifact with YAML frontmatter
- suitable for `.claude/handoffs/` or `P12_orchestration/compiled/`

## I Enable Downstream
- satellite execution with clear boundaries
- signal emission after work completes
- commit tracking via exact git commands

## Builders / Actors Adjacent to Me
| Actor | Relationship | Cross-ref |
|-------|--------------|-----------|
| dag-builder | provides dependency structure; one handoff per DAG node | dag-builder refs handoff-builder |
| signal-builder | produces completion events after my handoff executes | signal-builder refs handoff-builder |
| dispatch-rule-builder | routes tasks to satellites; I provide the execution detail | dispatch-rule-builder refs handoff-builder |
| spawn-config-builder | may derive spawn parameters from my handoff metadata | spawn-config-builder refs handoff-builder |
| workflow-builder | may include handoffs as steps in larger flows | workflow-builder refs handoff-builder |
| STELLA / orchestrators | create and consume my output for satellite delegation | runtime consumer |
