---
kind: collaboration
id: bld_collaboration_fallback_chain
pillar: P12
llm_function: COLLABORATE
purpose: How fallback-chain-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: fallback-chain-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what sequence of models should be tried when the primary fails?"
I do not sequence prompts. I do not define routing rules.
I design model degradation chains so systems remain available when primary models fail or exceed limits.
## Crew Compositions
### Crew: "Resilient Agent Deployment"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "provider configuration"
  3. fallback-chain-builder -> "model degradation sequence (e.g., opus -> sonnet -> haiku)"
  4. benchmark-builder -> "latency/cost baselines per model tier"
```
### Crew: "Full Dispatch Setup"
```
  1. dispatch-rule-builder -> "routing rules to primary target"
  2. fallback-chain-builder -> "degradation path when primary fails"
  3. guardrail-builder -> "safety boundaries during degradation"
```
## Handoff Protocol
### I Receive
- seeds: primary model, fallback models in order, quality threshold per step
- optional: timeout per step, circuit breaker config, cost budget, max retries
### I Produce
- fallback_chain artifact (.md + .yaml frontmatter)
- committed to: `cex/P02/examples/p02_fallback_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- benchmark-builder: provides latency/cost data to calibrate timeouts and thresholds
- boot-config-builder: provides provider constraints that affect fallback viability
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder | References fallback chain as alternative routing path |
| agent-package-builder | Includes fallback config in portable agent package |
