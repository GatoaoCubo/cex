---
id: p10_bi_organization_brain
kind: knowledge_index
pillar: P10
title: "Brain Index: organization Knowledge Base"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [brain, index, bm25, faiss, search, memory]
tldr: "Hybrid search index: BM25 (keyword, ~50% accuracy) + FAISS/Ollama (semantic, ~88% accuracy) over 9916 MD files in organization-core"
max_bytes: 1024
density_score: 0.89
source: organization-core/CLAUDE.md (BRAIN SEARCH) + records/core/brain/mcp-organization-brain/
linked_artifacts:
  smoke_eval: p07_se_brain_query
---

# Brain Index: organization Knowledge Base

## Configuration

```yaml
knowledge_index:
  name: organization_knowledge_base
  version: current
  location: records/core/brain/mcp-organization-brain/

  corpus:
    total_files: ~9916
    primary: records/pool/knowledge/  # KCs
    secondary: records/agents/*/iso_vectorstore/
    tertiary: records/skills/*/SKILL.md

  search_backends:
    bm25:
      type: keyword
      accuracy: ~50%
      fallback: true  # activates when Ollama down
      rebuild_time: < 1min

    faiss:
      type: semantic
      model: nomic-embed-text  # via Ollama local
      accuracy: ~88%
      index_size: 140MB  # gitignored — must rebuild on fresh clone
      rebuild_time: ~20min
      rebuild_cmd: "python build_indexes_ollama.py --scope all"
```

## Hybrid Search Mode

```
Query → BM25 (keyword match) + FAISS (semantic match)
      → merge results (rank fusion)
      → return top-N with confidence scores

If Ollama DOWN:
  → BM25-only fallback (~50% accuracy)
  → search_mode: "bm25_only" in response
```

## Accuracy by Mode

| Mode | Accuracy | When |
|------|----------|------|
| Hybrid (BM25+FAISS) | ~88% | Ollama running |
| BM25-only | ~50% | Ollama down |

## Rebuild Protocol

```bash
# Check if rebuild needed (stale > 24h):
brain_status()  # returns last_rebuild timestamp

# Rebuild full index:
cd records/core/brain/mcp-organization-brain
python build_indexes_ollama.py --scope all

# Verify:
brain_query("test agent for web scraping")  # should return web_scraper
```

## Scope Mapping

| Query Pattern | Best Backend | Example |
|---------------|-------------|---------|
| `"agent for X"` | FAISS (semantic) | `"agent for security scanning"` |
| `"KC_knowledge_agent_*"` | BM25 (keyword) | `"KC_knowledge_agent_088"` |
| `"skill for X"` | FAISS | `"skill for continuous batching"` |
