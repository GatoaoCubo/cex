---
id: p01_rs_brain_faiss_index
kind: rag_source
url: records/core/brain/mcp-organization-brain/src/indexes/
domain: knowledge_retrieval
last_checked: 2026-03-24
quality: 9.0
title: "Rag Source Brain Faiss Index"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for knowledge, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# RAG Source: brain_faiss_index

## URL
`records/core/brain/mcp-organization-brain/src/indexes/` (local FAISS + BM25 indexes)

## Domain
Knowledge retrieval — serves all organization agent_groups via brain_query MCP tool.

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

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: p01_rs_brain_faiss_index
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p01-rs-brain-faiss-index.md
```

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
