---
pillar: P12
llm_function: COLLABORATE
purpose: How context-doc-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: context-doc-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what background context does this domain need for prompt hydration?"
I do not distill atomic facts. I do not define terms.
I document domain context so prompt builders can hydrate their prompts with relevant background.

## Crew Compositions

### Crew: "Content Foundation"
```
  1. context-doc-builder -> "domain context (scope, stakeholders, constraints)"
  2. knowledge-card-builder -> "atomic facts from the domain"
  3. glossary-entry-builder -> "term definitions for the domain"
  4. few-shot-example-builder -> "format examples grounded in context"
```

### Crew: "Prompt Hydration"
```
  1. context-doc-builder -> "domain background for injection"
  2. action-prompt-builder -> "task prompt hydrated with context"
  3. chain-builder -> "prompt pipeline with contextual grounding"
```

## Handoff Protocol

### I Receive
- seeds: domain name, scope description, target audience
- optional: stakeholder list, constraints, assumptions, dependencies

### I Produce
- context_doc artifact (.md + .yaml, max 2048 bytes)
- committed to: `cex/P01/examples/p01_context_{domain}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent builder (layer 0). Context docs are authored from domain analysis.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| action-prompt-builder | Injects context_doc into task prompts |
| knowledge-card-builder | Uses context scope to bound fact distillation |
| chain-builder | Hydrates chain steps with domain background |
| instruction-builder | Grounds execution recipes in domain context |
