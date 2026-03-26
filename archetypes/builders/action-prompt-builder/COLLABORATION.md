---
pillar: P12
llm_function: COLLABORATE
purpose: How action-prompt-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: action-prompt-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what prompt injects this task into the agent?"
I do not define identity. I do not write detailed recipes.
I DEFINE TASKS with typed I/O so agents know exactly what to do and what to produce.

## Crew Compositions

### Crew: "Agent Bootstrap"
```
  1. knowledge-card-builder -> "domain knowledge for the agent"
  2. system-prompt-builder -> "agent identity, rules, format"
  3. instruction-builder -> "operational step-by-step recipes"
  4. action-prompt-builder -> "task prompts with typed I/O"
```

### Crew: "Task Pipeline"
```
  1. action-prompt-builder -> "task prompt A (extract)"
  2. action-prompt-builder -> "task prompt B (transform)"
  3. chain-builder [PLANNED] -> "compose A->B into pipeline"
  4. quality-gate-builder -> "validation for pipeline output"
```

## Handoff Protocol

### I Receive
- seeds: action verb phrase, input types, output format, domain
- optional: system_prompt context, knowledge_cards, edge case hints

### I Produce
- action_prompt artifact (YAML frontmatter + markdown body)
- committed to: `cex/P03_prompt/examples/p03_ap_{task_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- system-prompt-builder: provides identity context for task alignment
- knowledge-card-builder: provides domain knowledge for input/output design

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| chain-builder [PLANNED] | Chains compose multiple action_prompts |
| workflow-builder [PLANNED] | Workflows may wrap action_prompts as task steps |
| instruction-builder | May reference action_prompts for task context |
