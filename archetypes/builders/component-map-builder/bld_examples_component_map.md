---
id: component-map-builder-examples
kind: examples
parent: component-map-builder
version: 1.0.0
---

# Examples — component-map-builder

## Golden Example

INPUT: "Map the CEX brain infrastructure components and connections"

OUTPUT (complete, 19+ fields):

```yaml
---
id: p08_cmap_brain_infrastructure
kind: component_map
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
domain: "infrastructure"
quality: null
tags: [component-map, brain, infrastructure, search, knowledge]
tldr: "Structured inventory of Brain search infrastructure: BM25, FAISS, Ollama, and 1957 pool artifacts"
scope: "CEX Brain search infrastructure — indexing, embedding, retrieval"
component_count: 6
connection_count: 8
components:
  - {name: "BM25 Index", role: "keyword search", owner: "PYTHA", status: "active"}
  - {name: "FAISS Index", role: "vector similarity search", owner: "PYTHA", status: "active"}
  - {name: "Ollama", role: "local embedding generation", owner: "system", status: "active"}
  - {name: "Pool", role: "artifact storage (1957 items)", owner: "system", status: "active"}
  - {name: "brain_query API", role: "hybrid search endpoint", owner: "PYTHA", status: "active"}
  - {name: "build_indexes_ollama.py", role: "index rebuilder", owner: "PYTHA", status: "active"}
connections:
  - {from: "Pool", to: "build_indexes_ollama.py", type: "data_flow"}
  - {from: "build_indexes_ollama.py", to: "BM25 Index", type: "produces"}
  - {from: "build_indexes_ollama.py", to: "FAISS Index", type: "produces"}
  - {from: "Ollama", to: "build_indexes_ollama.py", type: "dependency"}
  - {from: "brain_query API", to: "BM25 Index", type: "data_flow"}
  - {from: "brain_query API", to: "FAISS Index", type: "data_flow"}
  - {from: "satellites", to: "brain_query API", type: "data_flow"}
  - {from: "Ollama", to: "brain_query API", type: "dependency"}
keywords: [brain, search, bm25, faiss, ollama, knowledge, retrieval]
---

## Scope
CEX Brain search infrastructure: all components involved in indexing, embedding, and retrieving knowledge artifacts. Excludes individual artifact content, satellite internals, and API deployment.

## Components
| Component | Role | Owner | Status | Version |
|-----------|------|-------|--------|---------|
| BM25 Index | Keyword search (lexical) | PYTHA | active | - |
| FAISS Index | Vector similarity (semantic) | PYTHA | active | 140MB gitignored |
| Ollama | Local embedding (nomic-embed-text) | system | active | auto-start |
| Pool | Artifact storage | system | active | 1957 items |
| brain_query API | Hybrid search endpoint | PYTHA | active | ~88% accuracy |
| build_indexes_ollama.py | Index rebuilder | PYTHA | active | ~20 min full rebuild |

## Connections
| From | To | Type | Data | Direction |
|------|-----|------|------|-----------|
| Pool | build_indexes_ollama.py | data_flow | raw artifacts | unidirectional |
| build_indexes_ollama.py | BM25 Index | produces | keyword index | unidirectional |
| build_indexes_ollama.py | FAISS Index | produces | vector index | unidirectional |
| Ollama | build_indexes_ollama.py | dependency | embeddings | unidirectional |
| brain_query API | BM25 Index | data_flow | keyword results | unidirectional |
| brain_query API | FAISS Index | data_flow | vector results | unidirectional |
| satellites | brain_query API | data_flow | search queries | unidirectional |
| Ollama | brain_query API | dependency | runtime embeddings | unidirectional |

## Interfaces
| Boundary | Components | Contract | Status |
|----------|-----------|----------|--------|
| Search API | brain_query <-> satellites | MCP tool call, returns ranked results | active |
| Embedding | Ollama <-> indexer/API | nomic-embed-text model, 768d vectors | active |

## Dependencies
| Component | Depends On | Failure Impact |
|-----------|-----------|---------------|
| FAISS Index | Ollama | fallback to BM25-only (~50% accuracy) |
| brain_query API | BM25 + FAISS | no search if both down |
| build_indexes_ollama.py | Ollama + Pool | cannot rebuild indexes |

## Boundaries
Out of scope: individual artifact content, satellite boot sequences, Railway deployment, API authentication.
Adjacent maps: p08_cmap_satellite_network (satellite connections), p08_cmap_api_infrastructure (Railway/API).

## References
- CLAUDE.md BRAIN SEARCH section
- records/core/brain/mcp-codexa-brain/build_indexes_ollama.py
```

### Why This Is Golden

- `quality: null` (H05 pass)
- id matches `p08_cmap_` pattern (H02 pass)
- `kind: component_map` (H04 pass)
- 19 fields including all 15 required (H06 pass)
- scope clearly defined (H08 pass)
- `component_count: 6` >= 2 (H09 pass)
- `connection_count: 8` >= 1 (S02 pass)
- Components table with owner + status per row (S04 pass)
- Connections table with direction per row (S03 pass)
- No orphan components (S05 pass)
- Interfaces section present (S06 pass)
- All 7 body sections present (S07 pass)
- keywords present, len 7 (S10 pass)
- Dependencies with failure impact (S09 pass)

---

## Anti-Example

INPUT: "List brain components"

BAD OUTPUT:

```yaml
---
id: brain
kind: map
quality: 9.0
---

The brain has several components:
- BM25 for search
- FAISS for vectors
They work together to provide search functionality.
```

### Failures (10)

1. `id: brain` — no `p08_cmap_` prefix -> H02 FAIL
2. `kind: map` — not literal "component_map" -> H04 FAIL
3. `quality: 9.0` — self-assigned score -> H05 FAIL
4. Missing: pillar, version, created, updated, author, domain, tags, tldr, scope, component_count, connection_count, components -> H06 FAIL
5. No `scope` field defined -> H08 FAIL
6. No `component_count` field -> H09 FAIL
7. Components as bullet list, no table with role/owner/status -> S04 FAIL
8. No Connections table, no direction specified -> S03 FAIL
9. Body is prose filler ("several components", "work together") -> S08 FAIL
10. Missing all 7 body sections (Scope, Components, Connections, Interfaces, Dependencies, Boundaries, References) -> S07 FAIL
