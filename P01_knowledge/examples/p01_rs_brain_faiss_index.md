---
id: p01_rs_brain_faiss_index
type: rag_source
url: records/core/brain/mcp-codexa-brain/src/indexes/
domain: knowledge_retrieval
last_checked: 2026-03-24
---

# Brain MCP FAISS Index

Hybrid retrieval index combining BM25 lexical search with FAISS semantic vectors.

## Index Specs

| Field | Value |
|-------|-------|
| Embedding model | nomic-embed-text (Ollama) |
| Dimensions | 768 |
| Chunk size | 2048 tokens |
| Chunk overlap | 128 tokens |
| Indexed docs | ~4000 (agents, skills, pool, KCs) |
| Search method | BM25 + FAISS hybrid (weighted merge) |
| Accuracy | ~88% hybrid, ~50% BM25-only fallback |
| Rebuild time | ~20 min full scope |

## Scopes Indexed

- `records/agents/*/README.md` - agent overviews
- `records/skills/*/SKILL.md` - skill definitions
- `records/pool/**/*.md` - knowledge cards, prompts, workflows

## Usage

```python
brain_query("agent for SEO marketplace")  # hybrid search
brain_list(scope="agents", limit=10)      # filtered listing
```
