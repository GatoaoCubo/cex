---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for glossary_entry production
sources: [IEEE glossary standards, ISO 1087 terminology, CEX knowledge layer]
---

# Domain Knowledge: glossary_entry

## Foundational Concept
Glossary entries are concise, authoritative term definitions: one term, one definition,
maximum clarity. Rooted in ISO 1087 (Terminology), IEEE glossary standards, and
technical writing best practices. In CEX, glossary_entries sit in the content layer
of P01 — they define terms, not deep knowledge or operational context.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| ISO 1087 | Terminology science — term/concept/designation | term + definition + synonyms |
| IEEE Glossary | Technical term standardization | Domain-specific term definitions |
| W3C Glossary | Web standards terminology | Abbreviated definitions with cross-refs |
| Wikipedia disambiguation | Multiple meanings of same term | disambiguation field |
| API docs glossary | Developer-facing term reference | Usage context and abbreviations |

## Key Patterns
- Definitions are CONCISE: max 3 lines, no prose padding
- Each entry defines ONE term (not a cluster of related concepts)
- Synonyms are EXPLICIT: listed even if partial matches
- Domain context is SCOPED: where and how the term is used
- Disambiguation resolves CONFUSION: similar terms clarified
- Entries are ATOMIC: self-contained, no external dependencies
- Abbreviations are DOCUMENTED: full form and short form linked
- Related terms are REFERENCED: cross-linking for navigation

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| domain_specific | CEX terms may differ from industry standard | W3C "context" |
| disambiguation | Terms overlap across pillars/satellites | Wikipedia disambiguation |
| related_terms | Cross-reference within CEX glossary | W3C "see also" |
| usage | Where/how the term appears in practice | IEEE "usage notes" |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT glossary_entry |
|------|------------|----------------------------|
| knowledge_card (P01) | Dense research fact (density >= 0.80) | KCs are deep; glossary is surface definition |
| context_doc (P01) | Scoped domain context | Context docs provide background; glossary defines terms |
| few_shot_example (P01) | Input/output pair for prompts | Examples demonstrate; glossary defines |
| axiom (P10) | Immutable fundamental rule | Axioms govern; glossary informs |
| naming_rule (P05) | Naming convention enforcement | Naming rules constrain; glossary explains |

## References
- ISO 1087:2019 — Terminology work — Vocabulary
- IEEE Standard Glossary of Software Engineering Terminology
- Plain Language Action and Information Network (PLAIN)
