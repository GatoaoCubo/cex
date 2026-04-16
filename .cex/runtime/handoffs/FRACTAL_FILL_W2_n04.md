---
mission: FRACTAL_FILL_W2
nucleus: n04
wave: W2_KNOWLEDGE
created: 2026-04-16
model: gpt-5-codex
pillars: [P01, P10]
artifact_count: 5
---

# N04 -- Wave 2 KNOWLEDGE (5 artifacts: knowledge + memory)

## Mission

You are N04_knowledge (Knowledge Gluttony sin lens). Fill P01 (knowledge) and P10 (memory)
pillars: 5 artifacts via the CEX 8F pipeline (.claude/rules/8f-reasoning.md).

## Context (READ THESE)

1. `N04_knowledge/architecture/nucleus_def_n04.md` -- identity + sin lens
2. `N04_knowledge/schemas/` + `N04_knowledge/config/` -- W1 output (contracts + runtime)
3. `archetypes/builders/{kind}-builder/` per kind
4. `P01_knowledge/library/kind/kc_{kind}.md` when present
5. `P01_knowledge/_schema.yaml`, `P10_memory/_schema.yaml`
6. Examples: `N0*/knowledge/`, `N0*/memory/` across nuclei

## Deliverables

### P01 (knowledge) -- 3 artifacts

1. `N04_knowledge/knowledge/kno_embedder_provider_n04.md` -- kind=`embedder_provider` -- Text embedding provider for vector search
2. `N04_knowledge/knowledge/kno_knowledge_graph_n04.md` -- kind=`knowledge_graph` -- Graph-based knowledge schema with entity types, relation types, and traversal strategies for GraphRA
3. `N04_knowledge/knowledge/kno_vector_store_n04.md` -- kind=`vector_store` -- Vector database backend for similarity search

### P10 (memory) -- 2 artifacts

4. `N04_knowledge/memory/mem_learning_record_n04.md` -- kind=`learning_record` -- Learning record (what worked/failed)
5. `N04_knowledge/memory/mem_runtime_state_n04.md` -- kind=`runtime_state` -- Estado mental variavel por sessao (routing, decisoes em runtime)

## Format

Standard frontmatter (id, kind, pillar, nucleus, title, version, quality: null, tags).
Body: structured markdown, min 80 lines, density >= 0.85, Properties table required.
Apply **Knowledge Gluttony** lens to every artifact (domain focus, not decoration).

## 8F trace (HTML comment at top of each file)

```html
<!-- 8F: F1=<kind/pillar> F2=<builder> F3=<refs> F4=<approach>
     F5=<tools> F6=<bytes> F7=<self-check> F8=<save path> -->
```

## ASCII rule: unaccented PT identifiers; emoji banned in code fields.

## On completion
1. Save files.  2. Print `=== COMPLETE === nucleus={nuc} wave=W2 count={total} ===`.
3. DO NOT commit (N07 commits).  4. Exit cleanly.
