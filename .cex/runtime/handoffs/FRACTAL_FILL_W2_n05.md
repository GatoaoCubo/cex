---
mission: FRACTAL_FILL_W2
nucleus: n05
wave: W2_KNOWLEDGE
created: 2026-04-16
model: gpt-5-codex
pillars: [P01, P10]
artifact_count: 9
---

# N05 -- Wave 2 KNOWLEDGE (9 artifacts: knowledge + memory)

## Mission

You are N05_operations (Gating Wrath sin lens). Fill P01 (knowledge) and P10 (memory)
pillars: 9 artifacts via the CEX 8F pipeline (.claude/rules/8f-reasoning.md).

## Context (READ THESE)

1. `N05_operations/architecture/nucleus_def_n05.md` -- identity + sin lens
2. `N05_operations/schemas/` + `N05_operations/config/` -- W1 output (contracts + runtime)
3. `archetypes/builders/{kind}-builder/` per kind
4. `P01_knowledge/library/kind/kc_{kind}.md` when present
5. `P01_knowledge/_schema.yaml`, `P10_memory/_schema.yaml`
6. Examples: `N0*/knowledge/`, `N0*/memory/` across nuclei

## Deliverables

### P01 (knowledge) -- 5 artifacts

1. `N05_operations/knowledge/kno_chunk_strategy_n05.md` -- kind=`chunk_strategy` -- Chunking strategy
2. `N05_operations/knowledge/kno_embedder_provider_n05.md` -- kind=`embedder_provider` -- Text embedding provider for vector search
3. `N05_operations/knowledge/kno_few_shot_example_n05.md` -- kind=`few_shot_example` -- Exemplo input/output pra prompt
4. `N05_operations/knowledge/kno_retriever_config_n05.md` -- kind=`retriever_config` -- Retrieval configuration (top_k, hybrid, reranker)
5. `N05_operations/knowledge/kno_vector_store_n05.md` -- kind=`vector_store` -- Vector database backend for similarity search

### P10 (memory) -- 4 artifacts

6. `N05_operations/memory/mem_entity_memory_n05.md` -- kind=`entity_memory` -- Memoria sobre entidades
7. `N05_operations/memory/mem_knowledge_index_n05.md` -- kind=`knowledge_index` -- Search index (BM25, FAISS config)
8. `N05_operations/memory/mem_learning_record_n05.md` -- kind=`learning_record` -- Learning record (what worked/failed)
9. `N05_operations/memory/mem_memory_summary_n05.md` -- kind=`memory_summary` -- Compressed memory summary

## Format

Standard frontmatter (id, kind, pillar, nucleus, title, version, quality: null, tags).
Body: structured markdown, min 80 lines, density >= 0.85, Properties table required.
Apply **Gating Wrath** lens to every artifact (domain focus, not decoration).

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

```html
<!-- 8F: F1=<kind/pillar> F2=<builder> F3=<refs> F4=<approach>
     F5=<tools> F6=<bytes> F7=<self-check> F8=<save path> -->
```

## ASCII rule: unaccented PT identifiers; emoji banned in code fields.

## On completion
1. Save files.  2. Print `=== COMPLETE === nucleus={nuc} wave=W2 count={total} ===`.
3. DO NOT commit (N07 commits).  4. Exit cleanly.
