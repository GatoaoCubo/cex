---
mission: FRACTAL_FILL_W2
nucleus: n01
wave: W2_KNOWLEDGE
created: 2026-04-16
model: gpt-5-codex
pillars: [P01, P10]
artifact_count: 11
---

# N01 -- Wave 2 KNOWLEDGE (11 artifacts: knowledge + memory)

## Mission

You are N01_intelligence (Analytical Envy sin lens). Fill P01 (knowledge) and P10 (memory)
pillars: 11 artifacts via the CEX 8F pipeline (.claude/rules/8f-reasoning.md).

## Context (READ THESE)

1. `N01_intelligence/architecture/nucleus_def_n01.md` -- identity + sin lens
2. `N01_intelligence/schemas/` + `N01_intelligence/config/` -- W1 output (contracts + runtime)
3. `archetypes/builders/{kind}-builder/` per kind
4. `P01_knowledge/library/kind/kc_{kind}.md` when present
5. `P01_knowledge/_schema.yaml`, `P10_memory/_schema.yaml`
6. Examples: `N0*/knowledge/`, `N0*/memory/` across nuclei

## Deliverables

### P01 (knowledge) -- 8 artifacts

1. `N01_intelligence/knowledge/kno_chunk_strategy_n01.md` -- kind=`chunk_strategy` -- Chunking strategy
2. `N01_intelligence/knowledge/kno_citation_n01.md` -- kind=`citation` -- Structured source attribution with provenance, URL, date, and reliability metadata
3. `N01_intelligence/knowledge/kno_competitive_matrix_n01.md` -- kind=`competitive_matrix` -- Competitive feature matrix for sales battle cards and procurement evals
4. `N01_intelligence/knowledge/kno_embedder_provider_n01.md` -- kind=`embedder_provider` -- Text embedding provider for vector search
5. `N01_intelligence/knowledge/kno_few_shot_example_n01.md` -- kind=`few_shot_example` -- Exemplo input/output pra prompt
6. `N01_intelligence/knowledge/kno_ontology_n01.md` -- kind=`ontology` -- Formal taxonomy and ontology definitions (OWL, SKOS, schema.org patterns) for knowledge organization
7. `N01_intelligence/knowledge/kno_retriever_config_n01.md` -- kind=`retriever_config` -- Retrieval configuration (top_k, hybrid, reranker)
8. `N01_intelligence/knowledge/kno_vector_store_n01.md` -- kind=`vector_store` -- Vector database backend for similarity search

### P10 (memory) -- 3 artifacts

9. `N01_intelligence/memory/mem_entity_memory_n01.md` -- kind=`entity_memory` -- Memoria sobre entidades
10. `N01_intelligence/memory/mem_memory_summary_n01.md` -- kind=`memory_summary` -- Compressed memory summary
11. `N01_intelligence/memory/mem_runtime_state_n01.md` -- kind=`runtime_state` -- Estado mental variavel por sessao (routing, decisoes em runtime)

## Format

Standard frontmatter (id, kind, pillar, nucleus, title, version, quality: null, tags).
Body: structured markdown, min 80 lines, density >= 0.85, Properties table required.
Apply **Analytical Envy** lens to every artifact (domain focus, not decoration).

## 8F trace (HTML comment at top of each file)

```html
<!-- 8F: F1=<kind/pillar> F2=<builder> F3=<refs> F4=<approach>
     F5=<tools> F6=<bytes> F7=<self-check> F8=<save path> -->
```

## ASCII rule: unaccented PT identifiers; emoji banned in code fields.

## On completion
1. Save files.  2. Print `=== COMPLETE === nucleus={nuc} wave=W2 count={total} ===`.
3. DO NOT commit (N07 commits).  4. Exit cleanly.
