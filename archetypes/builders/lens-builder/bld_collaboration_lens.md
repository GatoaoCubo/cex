---
pillar: P02
llm_function: COLLABORATE
purpose: How lens-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: lens-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "through which lens should we analyze this artifact?"
I define focused analytical perspectives with declared bias, filter attributes, and applies_to scope. I do NOT define agent identity (agent-builder), routing decision trees (mental-model-builder), or LLM specifications (model-card-builder).

## Crew Compositions

### Crew: "Multi-Perspective Analysis"
```
  1. knowledge-card-builder  -> "provides domain facts as the subject of analysis"
  2. lens-builder            -> "defines the analytical perspective filter to apply"
  3. scoring-rubric-builder  -> "scores artifacts through the dimensions the lens exposes"
```

### Crew: "Model Selection"
```
  1. model-card-builder -> "documents LLM specs: pricing, context, capabilities"
  2. lens-builder       -> "applies cost/speed/quality perspective to compare models"
  3. agent-builder      -> "configures agent with the model selected via lens evaluation"
```

### Crew: "Agent Cognitive Stack"
```
  1. mental-model-builder  -> "defines routing rules and decision trees for the agent"
  2. lens-builder          -> "adds domain-specific perspective filters for analysis"
  3. system-prompt-builder -> "assembles mental model and lenses into agent instructions"
```

## Handoff Protocol

### I Receive
- seeds: perspective name, target artifact kinds (applies_to), domain, analytical focus
- optional: bias direction, filter attributes, relative weight, competing lenses to differentiate from

### I Produce
- lens artifact (YAML, 20 frontmatter fields, applies_to scope, declared bias, max 3KB)
- committed to: `cex/P02_model/examples/p02_lens_{perspective_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Lenses are INDEPENDENT — they can be built from a perspective seed alone.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| agent-builder          | agents may apply lenses to filter their domain analysis |
| mental-model-builder   | lenses are referenced as analysis filters within routing decision trees |
| scoring-rubric-builder | rubrics derive scoring dimensions from lens definitions |
| system-prompt-builder  | embeds lens perspectives into agent persona and analytical instructions |
