---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of glossary_entry in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: glossary_entry in the CEX

## Boundary
glossary_entry EH: definicao curta e concisa de um termo do dominio, max 3 linhas.

glossary_entry NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| knowledge_card (P01) | KC DESTILA conhecimento profundo (density >= 0.80). glossary DEFINE termo curto. | P01 knowledge_card |
| context_doc (P01) | context_doc CONTEXTUALIZA dominio. glossary DEFINE termo isolado. | P01 context_doc |
| few_shot_example (P01) | example DEMONSTRA input/output. glossary DEFINE significado. | P01 few_shot_example |
| naming_rule (P05) | naming_rule IMPOE padrao de nomenclatura. glossary EXPLICA termo. | P05 naming_rule |
| axiom (P10) | axiom GOVERNA com regra imutavel. glossary INFORMA significado. | P10 axiom |

Regra: "o que este termo significa?" -> glossary_entry.

## Position in Knowledge Flow

```text
new term encountered -> [glossary_entry] defines it -> knowledge_card deepens -> brain_index indexes
                              |
                        definition: max 3 lines, concise
```

glossary_entry is the ENTRY POINT to knowledge. Quick lookup before deep dive.

## Dependency Graph

```text
glossary_entry <--indexed_by-- brain_index (P10, searchable)
glossary_entry <--referenced_by-- knowledge_card (P01, links to glossary)
glossary_entry <--used_in-- system_prompt (P03, term reference)
glossary_entry --independent-- validator, interface, signal
```

## Fractal Position
Pillar: P01 (Knowledge — what the agent KNOWS)
Function: INJECT (provide term definitions into context)
Scale: L0 (content layer — glossary entries are the smallest knowledge unit)
Glossary entries are the lightest P01 kind — concise definitions for quick reference.

## Dependency Graph

```text
glossary_entry <--receives-- knowledge_card (P01) — source concepts to define
glossary_entry --produces_for--> system_prompt (P03) — terminology injection
glossary_entry --produces_for--> context_doc (P01) — term references
glossary_entry --independent-- rag_source, few_shot_example, signal
```

glossary_entry is TERMINOLOGY LAYER — canonical definitions
