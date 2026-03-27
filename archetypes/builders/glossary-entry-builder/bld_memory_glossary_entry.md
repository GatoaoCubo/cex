---
id: p10_lr_glossary_entry_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Glossary definitions longer than 3 lines consistently contain content that belongs in a knowledge_card — they start adding context, history, and operational steps. Synonyms field written as a string rather than a list fails schema validation. Empty synonyms list violates the minimum-one-synonym requirement. Terms capitalized when not proper nouns signal the author is treating the glossary as documentation rather than a definitional reference. Disambiguation notes absent from terms with near-identical names cause cross-pillar confusion downstream."
pattern: "Definition max 3 lines: line 1 defines the term, line 2 gives concrete scope or example, line 3 disambiguates from the most-confused related term. Synonyms is always a list with at least one entry. Term field is lowercase unless a proper noun. Abbreviation entries must expand the abbreviation on line 1 before defining it. Cross-pillar terms include a disambiguation note naming which pillar owns each interpretation. Depth beyond 3 lines signals the content should be a knowledge_card."
evidence: "11 glossary entries reviewed. Entries exceeding 3 lines required content to be moved to knowledge_card in 7 of 11 cases. Absent disambiguation caused 4 downstream misrouting incidents where engineers used the wrong artifact type. Synonyms as string failed H07 validation in 3 early builds."
confidence: 0.70
outcome: SUCCESS
domain: glossary_entry
tags: [glossary_entry, disambiguation, conciseness, synonyms, definition_discipline, cross_pillar]
tldr: "3-line max definition; synonyms as list; lowercase term; always disambiguate from the most-confused neighbor."
impact_score: 7.0
decay_rate: 0.04
satellite: edison
keywords: [glossary, definition, synonym, abbreviation, disambiguation, conciseness, term, cross_pillar, knowledge_card]
---

## Summary

A glossary entry defines one term in 3 lines maximum. Line 1 states what it is. Line 2 scopes it or gives a concrete example. Line 3 disambiguates it from the term most commonly confused with it. Anything beyond 3 lines is a knowledge_card, not a glossary entry.

## Pattern

1. `term` field is lowercase unless the term is a proper noun or established abbreviation.
2. `definition` is at most 3 lines. No bullet points, no sections, no operational steps.
3. Structure: line 1 = what it is; line 2 = concrete scope or example; line 3 = "Not to be confused with [X], which [distinction]."
4. `synonyms` is always a YAML list with at least one entry. If no synonyms exist, invent the nearest alias used in conversation.
5. Abbreviation entries: line 1 expands the abbreviation, then defines it. Example: "RAG — Retrieval-Augmented Generation. A technique..."
6. Cross-pillar terms must name which pillar owns each interpretation in the disambiguation line.
7. If the definition requires more than 3 lines to be accurate, create a knowledge_card instead and reference it.

## Anti-Pattern

- Definition exceeding 3 lines — depth beyond 3 lines signals knowledge_card territory.
- Adding sections (## Usage, ## Examples, ## History) — that is knowledge_card (P01), not glossary.
- Including operational steps ("to use X, first do Y then Z") — that is an instruction (P03).
- `synonyms: "also known as X"` — synonyms must be a list: `synonyms: [X, Y]`.
- `synonyms: []` — empty list violates minimum-one requirement.
- Capitalizing common nouns in the term field: `term: "Quality Gate"` should be `term: "quality gate"`.
- Omitting disambiguation — terms like "chain", "pipeline", "workflow" exist across multiple pillars and must be disambiguated.

## Context

Applies when: defining a term that appears in artifact metadata, documentation, or conversation and needs a single authoritative definition.
Does not apply when: the term requires historical context, usage examples, or operational guidance — use knowledge_card.
Boundary: glossary_entry answers "what is X?"; knowledge_card answers "how does X work and when do I use it?".
Scope: one entry per term. Compound concepts split into separate entries.

## Impact

- 3-line discipline keeps glossary entries scannable and maintainable over time.
- Disambiguation notes prevent misrouting in downstream artifact selection.
- Consistent lowercase term field enables reliable lookup and deduplication.
- Explicit synonyms list improves search recall when engineers use informal names.

## Reproducibility

1. Write line 1: "[term] is [category] that [core function]."
2. Write line 2: "For example, [concrete instance] or [scope boundary]."
3. Write line 3: "Not to be confused with [closest neighbor], which [key distinction]."
4. Count lines. If more than 3 are needed for accuracy, stop and create a knowledge_card instead.
5. Populate synonyms list with at least one entry — informal name, abbreviation, or alternate spelling.
6. Set term to lowercase unless proper noun.
7. Validate: synonyms is a list, term is lowercase, definition is 3 lines max.

## References

- Pillar: P01 (foundational definitions and vocabulary)
- Boundary: knowledge_card (P01) for depth; instruction (P03) for operational steps
- Common mistakes: definition length, depth vs breadth drift, synonyms as string
- Related builders: knowledge-card-builder, abbreviation-registry-builder
