---
pillar: P12
llm_function: COLLABORATE
purpose: How agent-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: agent-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "who is this agent, what can it do, what are its constraints, and how is it structured?"
I do not write system prompts. I do not define skills or model cards.
I produce agent definitions so downstream builders can configure, package, and deploy the agent.

## Crew Compositions

### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for agent expertise"
  2. agent-builder -> "agent definition (persona + capabilities + iso_vectorstore)"
  3. instruction-builder -> "execution steps for agent tasks"
  4. boot-config-builder -> "provider-specific initialization config"
  5. iso-package-builder -> "portable deployable package"
```

### Crew: "Agent Identity Stack"
```
  1. agent-builder -> "agent definition with capabilities"
  2. fallback-chain-builder -> "model degradation sequence"
  3. guardrail-builder -> "safety boundaries for agent behavior"
```

## Handoff Protocol

### I Receive
- seeds: agent name, domain, target capabilities, satellite assignment
- optional: existing persona sketch, tool list, routing keywords

### I Produce
- agent artifact with iso_vectorstore skeleton (10+ ISO files)
- committed to: `cex/P02/examples/p02_agent_{name}/`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- knowledge-card-builder: provides domain knowledge that shapes agent expertise

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| boot-config-builder | Needs agent identity to configure provider startup |
| iso-package-builder | Packages agent definition into portable bundle |
| dispatch-rule-builder | Creates routing rules that target this agent |
| guardrail-builder | Defines safety boundaries scoped to agent capabilities |
| interface-builder | Defines contracts between this agent and others |
