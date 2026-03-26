---
pillar: P12
llm_function: COLLABORATE
purpose: How system-prompt-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: system-prompt-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "who is this agent and what are its rules?"
I do not define tasks. I do not write step-by-step recipes.
I DEFINE IDENTITY so downstream agents and prompts have a stable persona to build on.

## Crew Compositions

### Crew: "Agent Bootstrap"
```
  1. knowledge-card-builder -> "domain knowledge for the agent"
  2. system-prompt-builder -> "agent identity, rules, format"
  3. action-prompt-builder [PLANNED] -> "task prompts the agent executes"
  4. instruction-builder [PLANNED] -> "operational recipes for the agent"
```

### Crew: "Full Agent Package"
```
  1. model-card-builder -> "LLM specs and routing decision"
  2. system-prompt-builder -> "persona and rules"
  3. skill-builder [PLANNED] -> "reusable capabilities"
  4. quality-gate-builder -> "validation criteria for agent output"
```

## Handoff Protocol

### I Receive
- seeds: target agent name, domain
- optional: mental_model, knowledge_cards, guardrails to internalize

### I Produce
- system_prompt artifact (YAML frontmatter + markdown body)
- committed to: `cex/P03_prompt/examples/p03_sp_{agent_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- knowledge-card-builder: provides domain knowledge to inject into identity
- model-card-builder: provides LLM capabilities to reference in constraints

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| action-prompt-builder [PLANNED] | Needs identity context to write aligned task prompts |
| instruction-builder [PLANNED] | References system_prompt rules for consistency |
| agent-builder [PLANNED] | Packages system_prompt into full agent definition |
