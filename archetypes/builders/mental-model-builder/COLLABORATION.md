---
pillar: P12
llm_function: COLLABORATE
purpose: How mental-model-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: mental-model-builder

## My Role in Crews
I am a COGNITIVE ARCHITECT. I answer ONE question: "how does this agent route, decide, and prioritize?"
I do not define agents. I do not write system prompts. I do not manage runtime state.
I DESIGN cognitive maps so agents have structured reasoning when loaded.

## Crew Compositions

### Crew: "Agent Design" (standard)
```
  1. knowledge-card-builder -> "domain knowledge informing decisions"
  2. mental-model-builder   -> "cognitive map with routing and decisions"
  3. agent-builder          -> "complete agent integrating mental model"
```

### Crew: "Full Agent Pipeline"
```
  1. knowledge-card-builder -> "domain facts"
  2. model-card-builder     -> "LLM capabilities for routing"
  3. mental-model-builder   -> "cognitive blueprint"
  4. system-prompt-builder [PLANNED] -> "persona and voice"
  5. agent-builder          -> "complete agent definition"
  6. boot-config-builder    -> "provider initialization"
```

### Crew: "Cognitive Audit"
```
  1. mental-model-builder (read mode) -> "parse existing mental model"
  2. quality-gate-builder              -> "score routing/decision quality"
  3. knowledge-card-builder            -> "distill audit findings"
```

## Handoff Protocol

### I Receive
- seeds: agent name, domain, observed routing patterns
- optional: knowledge_cards (from knowledge-card-builder) for domain context
- optional: agent artifact (from agent-builder) for identity scoping

### I Produce
- mental_model artifact: `cex/P02_model/examples/p02_mm_{agent_slug}.yaml`
- committed to: `cex/P02_model/examples/`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On

| Builder | Why | Wave |
|---------|-----|------|
| knowledge-card-builder | Domain facts inform routing rules and heuristics | Upstream |
| agent-builder | Agent identity scopes what the mental model covers | Upstream (optional) |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| agent-builder | Integrates mental model as cognitive component |
| boot-config-builder | Uses routing info for boot constraints |
| quality-gate-builder | Validates mental model artifacts |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
agent-builder ARCHITECTURE.md lists mental-model-builder as upstream dependency.
This file lists agent-builder as both upstream (optional) and downstream consumer.
The cross-reference is bidirectional.
