---
id: n00_glossary_entry_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Glossary Entry -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, glossary_entry, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Glossary Entry defines a term with its canonical definition, synonyms, domain context, and usage examples. It is the atomic unit of a controlled vocabulary that ensures consistent terminology across nuclei and artifacts. Glossary entries are consumed by the metaphor dictionary, knowledge cards, and agent prompts to enforce terminology alignment.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `glossary_entry` |
| pillar | string | yes | Always `P01` |
| title | string | yes | The term being defined |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| term | string | yes | Canonical term (preferred form) |
| definition | string | yes | Precise, concise definition |
| domain | string | yes | Field this term belongs to |
| synonyms | list | no | Alternative names or phrasings |
| antonyms | list | no | Opposing or contrasting terms |
| see_also | list | no | Related terms in the glossary |

## When to use
- When introducing a new term into the CEX vocabulary
- When resolving terminology conflicts between nuclei
- When building a controlled vocabulary for a client domain

## Builder
`archetypes/builders/glossary_entry-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind glossary_entry --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 or N07)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- all nuclei and human collaborators
- `{{DOMAIN_CONTEXT}}` -- technical, business, or domain-specific vocabulary

## Example (minimal)
```yaml
---
id: glossary_entry_intent_resolution
kind: glossary_entry
pillar: P01
nucleus: n04
title: "Intent Resolution"
version: 1.0
quality: null
---
term: intent resolution
definition: "The process of mapping ambiguous user input to a structured action tuple (kind, pillar, nucleus, verb)."
domain: NLU / CEX orchestration
synonyms: [query rewriting, intent classification, transmutation]
see_also: [prompt_compiler, transmutation]
```

## Related kinds
- `knowledge_card` (P01) -- broader atomic facts that use glossary terms
- `context_doc` (P01) -- domain context that references glossary
- `ontology` (P01) -- formal taxonomy that builds on glossary entries
