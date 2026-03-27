---
pillar: P12
llm_function: COLLABORATE
purpose: How chain-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: chain-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what prompts run in what order, and how does data flow between them?"
I do not orchestrate agents. I do not define individual task prompts.
I compose prompt pipelines so multi-step LLM tasks execute in correct sequence with typed data flow.

## Crew Compositions

### Crew: "Prompt Pipeline"
```
  1. action-prompt-builder -> "individual task prompts (steps)"
  2. chain-builder -> "sequential composition with data flow"
  3. input-schema-builder -> "typed contracts between chain steps"
```

### Crew: "Complex Task Decomposition"
```
  1. instruction-builder -> "step-by-step recipe for task"
  2. chain-builder -> "prompt chain that implements the recipe"
  3. e2e-eval-builder -> "end-to-end test of the full chain"
```

## Handoff Protocol

### I Receive
- seeds: task decomposition (list of steps), data flow description
- optional: error handling strategy, branching conditions, context passing rules

### I Produce
- chain artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_chain_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- action-prompt-builder: provides individual step prompts composed into the chain
- input-schema-builder: provides typed contracts for inter-step data flow

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| e2e-eval-builder | Tests the full chain from input to final output |
| dag-builder | May model chain dependencies in execution graphs |
