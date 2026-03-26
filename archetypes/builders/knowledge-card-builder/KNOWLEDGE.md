---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for knowledge_card production
sources: validate_kc.py v2.0 + _schema.yaml v4.0 + 63 real examples
---

# Domain Knowledge: knowledge_card

## Foundational Concept
Knowledge cards are ATOMIC SEARCHABLE FACTS — the smallest unit of knowledge
in the CEX system. Each card answers ONE question about ONE topic.
Density > 0.80 means >80% of content is concrete data (no filler, no narrative).

## CEX Knowledge Card Principles
| Principle | Rule | Why |
|-----------|------|-----|
| Atomicity | One topic per card | Brain search retrieves whole cards |
| Density | >= 0.80 ratio of data to prose | LLM context is expensive |
| Searchability | tldr + keywords + long_tails | Brain hybrid search (BM25 + FAISS) |
| Versionability | semver, created/updated dates | Knowledge evolves |
| Linkability | linked_artifacts (adw, agent, hop) | Knowledge connects to action |

## Two Body Structures

### domain_kc (external knowledge)
For real-world topics: technologies, patterns, APIs, protocols.
Sections: Quick Reference, Key Concepts, Strategy Phases, Golden Rules, Flow, Comparativo, References.

### meta_kc (CEX-internal knowledge)
For CEX system topics: architecture, patterns, processes.
Sections: Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References.

## Quality Tiers (validate_kc.py v2.0)
| Tier | Score | Requirements |
|------|-------|-------------|
| GOLDEN | >= 9.5 | All 10 HARD + 95% of 20 SOFT gates |
| PUBLISH | >= 8.0 | All 10 HARD + 80% SOFT |
| ACCEPTABLE | >= 7.0 | All 10 HARD + 70% SOFT |
| NEEDS_WORK | < 7.0 | All HARD pass, SOFT insufficient |
| REJECTED | — | Any HARD gate fails |

## Density Calculation
```
density = (data_lines) / (total_non_empty_lines)
data_line = bullet, table row, code line, yaml value
non_data_line = heading, empty prose, transition sentence
Target: >= 0.80 (ideally 0.85-0.95)
```

## Key Differences from model_card
| Aspect | knowledge_card | model_card |
|--------|---------------|------------|
| LP | P01 (Knowledge) | P02 (Model) |
| Purpose | Atomic fact about any topic | LLM spec (capabilities, cost) |
| Size limit | 5120 bytes | 4096 bytes (body) |
| Density gate | >= 0.80 | >= 0.85 |
| Body structure | 2 variants (domain/meta) | 1 fixed structure |
| Validator | validate_kc.py (ACTIVE) | validate_artifact.py [PLANNED] |
| Naming | p01_kc_{topic}.md | p02_mc_{provider}_{slug}.md |
| quality field | null (never self-score) | null (never self-score) |
