---
pillar: P12
llm_function: COLLABORATE
purpose: How instruction-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: instruction-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the exact steps to do this?"
I do not define identity. I do not specify input/output contracts.
I DECOMPOSE TASKS into executable steps so agents can follow a clear recipe.

## Crew Compositions

### Crew: "Agent Bootstrap"
```
  1. knowledge-card-builder -> "domain knowledge for the task"
  2. system-prompt-builder -> "agent identity and rules"
  3. instruction-builder -> "step-by-step execution recipes"
  4. action-prompt-builder [PLANNED] -> "task prompts with I/O"
```

### Crew: "Operational Runbook"
```
  1. knowledge-card-builder -> "domain context and patterns"
  2. instruction-builder -> "step-by-step procedure"
  3. quality-gate-builder -> "validation criteria for output"
```

## Handoff Protocol

### I Receive
- seeds: task name, domain, target executor
- optional: knowledge_cards, system_prompt context, dependency list

### I Produce
- instruction artifact (YAML frontmatter + markdown body)
- committed to: `cex/P03_prompt/examples/p03_ins_{task_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- knowledge-card-builder: provides domain knowledge for step details
- system-prompt-builder: provides agent context to align instruction tone

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| skill-builder [PLANNED] | Skill phases reference instruction steps |
| workflow-builder [PLANNED] | Workflow steps may wrap instructions |
| action-prompt-builder | May reference instruction for detailed steps |
