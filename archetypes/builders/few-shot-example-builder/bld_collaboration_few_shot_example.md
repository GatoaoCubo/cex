---
pillar: P12
llm_function: COLLABORATE
purpose: How few-shot-example-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: few-shot-example-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what input/output pair best teaches this format?"
I do not evaluate quality. I do not test correctness.
I craft format-exemplifying pairs so prompts can teach LLMs the expected output shape.

## Crew Compositions

### Crew: "Prompt Quality Stack"
```
  1. context-doc-builder -> "domain context"
  2. action-prompt-builder -> "task-focused prompt"
  3. few-shot-example-builder -> "input/output examples for the prompt"
  4. golden-test-builder -> "quality reference for evaluation"
```

### Crew: "Format Teaching"
```
  1. input-schema-builder -> "input contract definition"
  2. few-shot-example-builder -> "examples that demonstrate the format"
  3. formatter-builder -> "output formatting rules"
```

## Handoff Protocol

### I Receive
- seeds: target format/artifact type, difficulty level (easy/medium/hard)
- optional: edge cases to cover, domain context, output schema

### I Produce
- few_shot_example artifact (.md + .yaml, max 1024 bytes)
- committed to: `cex/P01/examples/p01_fewshot_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- input-schema-builder: provides the format contract that examples must demonstrate

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| action-prompt-builder | Embeds few-shot examples in task prompts |
| chain-builder | Uses examples to calibrate chain step outputs |
| golden-test-builder | References examples as starting point for quality refs |
