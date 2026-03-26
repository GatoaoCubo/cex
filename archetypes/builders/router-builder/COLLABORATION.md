---
pillar: P12
llm_function: COLLABORATE
purpose: How router-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: router-builder

## My Role in Crews
I am a DECISION ARCHITECT. I answer ONE question: "how should tasks be routed to destinations?"
I do not execute tasks. I do not define agent identities.
I DESIGN routing logic so dispatch systems can make informed decisions.

## Crew Compositions

### Crew: "Dispatch System" (standard)
```
  1. dispatch-rule-builder [PLANNED] -> "keyword-satellite mappings (simple hints)"
  2. router-builder                  -> "routing logic with confidence and fallback"
  3. agent-builder                   -> "agent identities at each destination"
  4. workflow-builder [PLANNED]      -> "orchestration using router decisions"
```

### Crew: "Resilient Routing"
```
  1. model-card-builder              -> "LLM capabilities for routing decisions"
  2. router-builder                  -> "task-to-destination routing logic"
  3. fallback-chain-builder          -> "model degradation when primary fails"
```

### Crew: "Full Orchestration"
```
  1. router-builder                  -> "where each task goes"
  2. spawn-config-builder [PLANNED]  -> "how to launch destination satellite"
  3. signal-builder                  -> "completion/failure signals from execution"
```

## Handoff Protocol

### I Receive
- seeds: routing domain, list of destinations, task patterns
- optional: dispatch_rules (keyword hints from P12)
- optional: model_cards (capabilities that inform routing decisions)

### I Produce
- router artifact: `cex/P02_model/examples/p02_router_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- dispatch-rule-builder [PLANNED]: provides keyword hints for pattern matching
- model-card-builder: provides model capabilities that may inform routing decisions

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| workflow-builder [PLANNED] | Uses router decisions within orchestration flows |
| spawn-config-builder [PLANNED] | Needs routing output to configure satellite spawn |
| fallback-chain-builder | May receive tasks that router cannot confidently route |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
fallback-chain-builder COLLABORATION.md lists router-builder as upstream (routing failures).
This file lists fallback-chain-builder as a downstream dependent.
The cross-reference is bidirectional.
