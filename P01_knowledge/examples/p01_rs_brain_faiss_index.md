---
id: p01_rs_brain_faiss_index
type: rag_source
url: records/core/brain/mcp-codexa-brain/src/indexes/
domain: knowledge_retrieval
last_checked: 2026-03-24
---

# RAG Source: brain_faiss_index

## URL
`records/core/brain/mcp-codexa-brain/src/indexes/` (local FAISS + BM25 indexes)

## Domain
Knowledge retrieval — serves all CODEXA satellites via brain_query MCP tool.

## Last Checked
2026-03-24. Rebuild: `python build_indexes_ollama.py --scope all` (~20 min).

## Indexing Notes
| Field | Value |
|-------|-------|
| Model | nomic-embed-text (768d, Ollama) |
| Chunks | 2048 tokens, 128 overlap |
| Docs indexed | ~4000 (agents, skills, pool, KCs) |
| Method | BM25 + FAISS hybrid (0.4/0.6 weight) |
| Accuracy | ~88% hybrid, ~50% BM25-only fallback |
| Index size | ~140MB (gitignored) |

Scopes: `agents/*/README.md`, `skills/*/SKILL.md`, `pool/**/*.md`
