---
lp: P01
llm_function: INJECT
purpose: Standards and domain knowledge for knowledge_card production
sources: validate_kc.py v2.0 + 63 real examples + _schema.yaml + golden KC analysis
---

# Domain Knowledge: knowledge_card

## Foundational Principle
Knowledge cards are ATOMIC SEARCHABLE FACTS. One card = one concept.
Inspired by Zettelkasten (Luhmann), adapted for LLM retrieval pipelines.
Cards must be self-contained — readable without external context.

## Core Properties
| Property | Value | Why |
|----------|-------|-----|
| Atomicity | 1 concept per card | Retrieval precision: 1 query = 1 card |
| Density | >= 0.80 | No filler — every byte carries information |
| Max size | 5120 bytes | Fits in single LLM context chunk |
| Min bullets | 3 | Ensures substantive content |
| Searchability | keywords + long_tails + axioms | Powers BM25 + semantic retrieval |

## Body Structures (2 variants)

### domain_kc (subject-matter knowledge)
Sections: quick_reference, conceitos_chave, strategy_phases, regras_de_ouro, visual_flow, comparativo, artefatos
Use for: technical topics, methodologies, domain expertise

### meta_kc (system/spec knowledge)
Sections: executive_summary, spec_table, patterns, anti_patterns, application, references
Use for: CEX internals, architecture specs, process documentation

## Quality Tiers (from validate_kc.py)
| Tier | Score | Meaning |
|------|-------|---------|
| GOLDEN | >= 9.5 | Exemplary — reference for other builders |
| PUBLISH | >= 8.0 | Production-ready for pool |
| ACCEPTABLE | >= 7.0 | Usable but improvable |
| NEEDS_WORK | < 7.0 | Requires revision |
| REJECTED | HARD fail | Cannot publish — fix blockers first |

## Density Optimization Techniques
- Replace prose with tables (3x denser)
- Replace paragraphs with bullets (2x denser)
- Use code blocks for flows/diagrams (visual + dense)
- Cut filler: "it is worth noting" -> delete entire phrase
- Max 80 chars per bullet — forces concision

## Retrieval Optimization
- keywords: 2+ terms that match BM25 lexical search
- long_tails: 1+ natural-language queries users would type
- axioms: 1+ actionable rules (SEMPRE/NUNCA format)
- tags: 3+ categorical labels for filtering
- tldr: < 160 chars, standalone (no self-reference)

## References
- CEX _schema.yaml: P01_knowledge/_schema.yaml
- Validator: _tools/validate_kc.py v2.0
- Template: P01_knowledge/templates/tpl_knowledge_card.md
- 63+ real examples: P01_knowledge/examples/
