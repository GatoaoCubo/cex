---
pillar: P12
llm_function: COLLABORATE
purpose: How fallback-chain-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: fallback-chain-builder

## My Role in Crews
I am a RESILIENCE ENGINEER. I answer ONE question: "what model sequence ensures graceful degradation?"
I do not route tasks. I do not sequence prompts.
I DESIGN model fallback sequences so systems survive primary model failure.

## Crew Compositions

### Crew: "Resilient Agent" (standard)
```
  1. model-card-builder           -> "model specs for each step in the chain"
  2. fallback-chain-builder       -> "ordered degradation sequence with thresholds"
  3. agent-builder                -> "agent identity using the chain for resilience"
```

### Crew: "Full Dispatch Resilience"
```
  1. router-builder               -> "task routing to destinations"
  2. fallback-chain-builder       -> "model fallback when routing destination fails"
  3. signal-builder               -> "degradation and circuit-breaker signals"
```

### Crew: "Cost-Optimized Pipeline"
```
  1. model-card-builder           -> "pricing and capability per model"
  2. fallback-chain-builder       -> "cost-aware degradation with ceiling"
  3. quality-gate-builder         -> "quality thresholds that trigger fallback"
```

## Handoff Protocol

### I Receive
- seeds: model list (ordered by capability), domain, quality requirements
- optional: model_cards (pricing and capability data)
- optional: router output (routing failures that need model fallback)

### I Produce
- fallback_chain artifact: `cex/P02_model/examples/p02_fc_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- model-card-builder: provides model specs, pricing, and capability tiers

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| agent-builder | Agents reference fallback_chain for resilient model selection |
| router-builder | Router may delegate to fallback_chain when routing fails |
| signal-builder | Signals emitted on degradation events reference chain state |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
router-builder COLLABORATION.md lists fallback-chain-builder as downstream.
This file lists router-builder as a potential upstream source.
The cross-reference is bidirectional.
