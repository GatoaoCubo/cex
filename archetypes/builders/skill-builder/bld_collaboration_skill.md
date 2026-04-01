---
kind: collaboration
id: bld_collaboration_skill
pillar: P12
llm_function: COLLABORATE
purpose: How skill-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: skill-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is this reusable skill — its trigger, phases, inputs, outputs, and boundary?"
I do not write agents. I do not define workflows or system prompts.
I produce skill definitions so downstream builders can integrate skills into agents and workflows.

## Crew Compositions

### Crew: "New Skill End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for skill expertise"
  2. skill-builder -> "skill definition (trigger + phases + reusable boundary)"
  3. instruction-builder -> "execution steps for skill usage"
  4. agent-builder -> "agent that uses this skill"
```

### Crew: "Skill Library Expansion"
```
  1. skill-builder -> "define the skill"
  2. schema-builder -> "input/output schema for skill"
  3. examples-builder -> "usage examples"
  4. quality-gate-builder -> "validation criteria"
```

## What I Receive
- Domain KC, pattern description, user intent
## What I Produce
- Skill definition: trigger, phases, inputs, outputs, boundary, anti-patterns
