---
id: p01_gl_TERM_SLUG
kind: glossary_entry
pillar: P01
version: 1.0.0
title: "Template — Glossary Entry"
tags: [template, glossary, terminology, taxonomy]
tldr: "Canonical definition for a domain term. Links synonyms, usage context, and disambiguation to ensure consistent terminology across the knowledge base."
term: "[TERM]"
definition: "[SHORT_DEFINITION]"
synonyms: ["[SYNONYM_1]", "[SYNONYM_2]"]
quality: 9.0
updated: "2026-04-07"
domain: "knowledge management"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.89
---

# Glossary Entry: [TERM]

## Definition
[SHORT_DEFINITION_IN_1_TO_3_LINES — what this term means in the CEX context]

## Usage
- **Context**: [WHERE_TERM_APPEARS — which pillars, artifacts, or workflows]
- **Example**: "[SENTENCE_USING_TERM in a real scenario]"
- **Avoid confusion with**: [SIMILAR_TERM] — [WHY_DIFFERENT]

## Relationships

| Relation | Term | Notes |
|----------|------|-------|
| parent | [BROADER_TERM] | This term is a specialization of... |
| sibling | [RELATED_TERM] | Often co-occurs in same context |
| child | [NARROWER_TERM] | More specific variant |

## Domain Scope
- **Pillars**: P[XX] — [which pillars use this term]
- **Kinds**: [which artifact kinds reference this term]
- **Frequency**: [high | medium | low] — how often it appears

## Canonical Source
- Reference: [URL or document where this term is authoritatively defined]
- CEX adoption date: [YYYY-MM-DD]

## Quality Gate
- [ ] Definition ≤ 3 lines
- [ ] At least 1 synonym listed
- [ ] Usage example is concrete, not abstract
- [ ] No circular definitions (term used in its own definition)
- [ ] Total size ≤ 512 bytes (frontmatter) + 2048 bytes (body)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `glossary entry`
- **Artifact ID**: `p01_gl_TERM_SLUG`
- **Tags**: [template, glossary, terminology, taxonomy]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `glossary entry` | Artifact type |
| Pipeline | 8F (F1→F8) |
