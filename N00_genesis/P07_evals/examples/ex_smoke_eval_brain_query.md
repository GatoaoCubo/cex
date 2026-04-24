---
id: p07_se_brain_query
kind: smoke_eval
8f: F7_govern
pillar: P07
title: "Smoke Eval: Brain MCP Query"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [smoke, eval, brain, mcp, search]
tldr: "30-second sanity check for brain MCP — verify BM25+FAISS hybrid search returns relevant results within 3s"
max_bytes: 1024
density_score: 0.88
source: organization-core/CLAUDE.md (BRAIN SEARCH section) + records/core/brain/mcp-organization-brain/
linked_artifacts: null
related:
  - p10_bi_organization_brain
  - bld_examples_smoke_eval
  - p07_ue_brain_query_accuracy
  - bld_examples_component_map
  - p04_plug_brain_search
  - p04_mcp_organization_brain
  - bld_examples_instruction
  - bld_knowledge_card_knowledge_index
  - p05_parser_brain_query
  - p01_rs_brain_faiss_index
---

# Smoke Eval: Brain MCP Query

## Purpose

Quick sanity check to verify brain MCP is operational. Run after FAISS index rebuild or agent_group boot to confirm hybrid search returns relevant results before executing knowledge-intensive tasks.

## Runtime

< 30 seconds

## Checks

| Check | Input | Expected | Fail Condition |
|-------|-------|----------|----------------|
| BM25 fallback | `brain_query("spawn agent_group")` | >= 3 results | 0 results |
| FAISS semantic | `brain_query("agent for web scraping")` | web_scraper in top 5 | wrong agent returned |
| Hybrid accuracy | `brain_query("skill for continuous batching")` | continuous_batching in top 3 | missing entirely |
| Response time | any query | < 3s | > 10s (Ollama timeout) |

## Execution

```python
# Run in knowledge_agent/orchestrator terminal
from mcp_organization_brain import brain_query

result = brain_query("agent for web scraping")
assert len(result) >= 3, f"Expected 3+ results, got {len(result)}"
assert any("web_scraper" in r.get("path","") for r in result), "web_scraper not found"
print(f"PASS: {len(result)} results in {result[0].get('elapsed_ms',0)}ms")
```

## Fallback Detection

```python
# Check if Ollama is down (BM25-only fallback mode)
result = brain_query("semantic test knowledge extraction")
if result[0].get("search_mode") == "bm25_only":
    print("WARN: Ollama down — BM25 fallback (~50% accuracy)")
    # Trigger rebuild: python build_indexes_ollama.py --scope all
```

## Success Criteria

- At least 3 results returned for each query
- No `search_mode: error` in response
- Response time < 3s (Ollama running) or < 0.5s (BM25-only)

## Fail Actions

| Failure | Action |
|---------|--------|
| 0 results | Run `python build_indexes_ollama.py --scope all` (~20 min) |
| Timeout > 10s | Check Ollama service: `ollama list` |
| Wrong results | Verify index scope: `brain_status()` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_bi_organization_brain]] | downstream | 0.46 |
| [[bld_examples_smoke_eval]] | related | 0.35 |
| [[p07_ue_brain_query_accuracy]] | related | 0.34 |
| [[bld_examples_component_map]] | related | 0.34 |
| [[p04_plug_brain_search]] | upstream | 0.29 |
| [[p04_mcp_organization_brain]] | upstream | 0.28 |
| [[bld_examples_instruction]] | related | 0.27 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.26 |
| [[p05_parser_brain_query]] | upstream | 0.26 |
| [[p01_rs_brain_faiss_index]] | related | 0.25 |
