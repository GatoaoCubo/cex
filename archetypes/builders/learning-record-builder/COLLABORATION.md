---
pillar: P12
llm_function: COLLABORATE
purpose: How learning-record-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: learning-record-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what did we learn from this experience, and how reproducible is it?"
I do not define immutable truths. I do not create decision maps.
I CAPTURE experiences so routing intelligence and future decisions improve over time.

## Crew Compositions

### Crew: "Memory System"
```
  1. axiom-builder -> "permanent truths (foundation)"
  2. learning-record-builder -> "experience records (evolving)"
  3. mental-model-builder -> "decision maps (derived from axioms + learning)"
```

### Crew: "Post-Execution Review"
```
  1. signal-builder -> "completion signal with status"
  2. learning-record-builder -> "structured learning from execution"
  3. quality-gate-builder -> "gate for learning_record quality"
  4. scoring-rubric-builder [PLANNED] -> "rubric for scoring learning impact"
```

### Crew: "Knowledge Upgrade"
```
  1. learning-record-builder -> "experience pattern captured"
  2. knowledge-card-builder -> "external fact validation"
  3. axiom-builder -> "crystallized truth (if pattern proves immutable)"
```

## Handoff Protocol

### I Receive
- seeds: topic, outcome, satellite context
- optional: signal data, session logs, execution metrics

### I Produce
- learning_record artifact (markdown with YAML frontmatter)
- committed to: `cex/P10_memory/examples/p10_lr_{slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- signal-builder: signals trigger learning capture (optional, not blocking)

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| mental-model-builder | Learning informs routing decisions |
| axiom-builder | Repeated learning may crystallize into axiom |
| knowledge-card-builder | Learning identifies knowledge gaps |
| quality-gate-builder | Learning validates gate effectiveness |
