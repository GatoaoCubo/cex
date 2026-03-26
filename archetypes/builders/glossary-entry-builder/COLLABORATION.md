---
pillar: P12
llm_function: COLLABORATE
purpose: How glossary-entry-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: glossary-entry-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what does this term mean in this domain?"
I do not analyze deeply. I do not provide operational context.
I DEFINE terms so knowledge-card-builder and other consumers have clear terminology.

## Crew Compositions

### Crew: "Knowledge Onboarding"
```
  1. glossary-entry-builder -> "defines key terms (quick reference)"
  2. knowledge-card-builder -> "deep-dives into domain knowledge"
  3. context-doc-builder [PLANNED] -> "provides domain background"
```

### Crew: "Domain Standardization"
```
  1. glossary-entry-builder -> "standardizes term definitions"
  2. naming-rule-builder [PLANNED] -> "enforces naming conventions"
  3. validator-builder -> "validates term usage in artifacts"
```

## Handoff Protocol

### I Receive
- seeds: term to define, domain context
- optional: existing definitions, synonyms, related terms

### I Produce
- glossary_entry artifact (YAML)
- committed to: `cex/P01_knowledge/examples/p01_gl_{term_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Glossary entries are INDEPENDENT — they can be built from a term alone.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| knowledge-card-builder | References glossary terms for consistency |
| system-prompt-builder [PLANNED] | Uses glossary for agent vocabulary |
| context-doc-builder [PLANNED] | Links to glossary for term definitions |
