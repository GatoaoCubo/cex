---
pillar: P12
llm_function: COLLABORATE
purpose: How pattern-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: pattern-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the named, reusable solution for this recurring problem?"
I do not mandate rules. I do not execute workflows.
I DESCRIBE proven solutions so architects and builders can make informed decisions.

## Crew Compositions

### Crew: "Architecture Design"
```
  1. pattern-builder -> "reusable solution (p08_pat_*)"
  2. satellite-spec-builder -> "satellite spec referencing applicable patterns"
  3. law-builder [PLANNED] -> "mandatory rule derived from proven pattern"
  4. diagram-builder [PLANNED] -> "visual representation of pattern"
```

### Crew: "Knowledge to Architecture"
```
  1. learning-record-builder -> "experience record (what worked)"
  2. pattern-builder -> "formalized pattern (recurring solution)"
  3. axiom-builder -> "crystallized truth (if pattern proves universal)"
```

### Crew: "Pattern Catalog"
```
  1. pattern-builder -> "individual pattern"
  2. component-map-builder [PLANNED] -> "map of patterns and their relationships"
  3. knowledge-card-builder -> "KC summarizing pattern for brain search"
```

## Handoff Protocol

### I Receive
- seeds: problem description, domain, examples
- optional: forces, existing solutions, related patterns

### I Produce
- pattern artifact (markdown with YAML frontmatter)
- committed to: `cex/P08_architecture/examples/p08_pat_{slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- learning-record-builder: repeated learning reveals patterns (optional, not blocking)

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| satellite-spec-builder | Specs reference applicable patterns |
| law-builder [PLANNED] | Proven patterns may become mandatory laws |
| workflow-builder | Workflows implement pattern solutions |
| axiom-builder | Universal patterns may crystallize into axioms |
| knowledge-card-builder | KCs summarize patterns for brain search |
