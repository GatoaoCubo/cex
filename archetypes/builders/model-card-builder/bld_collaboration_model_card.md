---
kind: collaboration
id: bld_collaboration_model_card
pillar: P02
llm_function: COLLABORATE
purpose: How model-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: model-card-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what can this LLM do and how much does it cost?"
I produce technical specs for LLMs with pricing, context limits, capability booleans, and provider data. I do NOT handle boot configuration (boot-config-builder), agent definitions (agent-builder), benchmark design (benchmark-builder), or routing infrastructure (router-builder).

## Crew Compositions

### Crew: "Build New Agent from Scratch"
```
  1. model-card-builder   -> "LLM spec: pricing, context window, capability booleans"
  2. mental-model-builder -> "cognitive blueprint referencing model constraints"
  3. agent-builder        -> "complete agent definition selecting the documented model"
  4. system-prompt-builder -> "persona adapted to model capabilities and context limits"
  5. boot-config-builder  -> "initialization wired to model ID, temperature, and token limits"
```

### Crew: "Bootstrap New Satellite"
```
  1. model-card-builder    -> "spec for the model powering the satellite"
  2. satellite-spec-builder -> "satellite role, MCPs, and behavioral constraints"
  3. boot-config-builder   -> "startup configuration using model params from the card"
  4. system-prompt-builder -> "PRIME file adapted to documented model capabilities"
```

### Crew: "Model Comparison"
```
  1. model-card-builder    -> "produces cards for each candidate model"
  2. lens-builder          -> "applies cost/speed/quality perspective to compare them"
  3. scoring-rubric-builder -> "scores each model against target use case criteria"
```

## Handoff Protocol

### I Receive
- seeds: model name, provider (minimum required)
- optional: use case context (informs When to Use table), competing models to compare

### I Produce
- model_card artifact (Markdown, 26 frontmatter fields, capability booleans, normalized pricing, max 4KB)
- committed to: `cex/P02_model/examples/p02_mc_{provider}_{slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. model-card-builder is INDEPENDENT (layer 0 infrastructure).

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| agent-builder          | references model limits and capabilities in agent definition |
| boot-config-builder    | needs model ID, temperature range, and context limits for initialization |
| mental-model-builder   | uses model capability data to scope routing rules and decision thresholds |
| router-builder         | uses pricing and capability data to assign tasks to the right model |
| fallback-chain-builder | needs model specs to order fallback priority by cost and capability |
| iso-package-builder    | includes model_card as a deploy dependency in the packaged artifact |
