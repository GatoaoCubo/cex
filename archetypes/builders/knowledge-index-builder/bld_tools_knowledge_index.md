---
kind: tools
id: bld_tools_knowledge_index
pillar: P04
llm_function: CALL
purpose: Tools available for knowledge_index production
quality: 9.1
title: "Tools Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_response_format
  - bld_tools_golden_test
  - bld_tools_validation_schema
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_runtime_state
  - bld_tools_input_schema
  - bld_tools_unit_eval
  - bld_tools_path_config
---

# Tools: knowledge-index-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing knowledge_indexes | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for knowledge_index |
| CEX Examples | P10_memory/examples/ | Existing knowledge_index artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P10_knowledge_index seeds |
| FAISS Docs | faiss.ai | Index types, parameters, performance characteristics |
| BM25 Theory | Robertson & Zaragoza 2009 | BM25 parameters and scoring |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p10_bi_ prefix
3. [ ] algorithm in [bm25, faiss, hybrid]
4. [ ] corpus_type in [text, vector, structured]
5. [ ] rebuild_schedule valid enum

## Metadata

```yaml
id: bld_tools_knowledge_index
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-knowledge-index.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_response_format]] | sibling | 0.61 |
| [[bld_tools_golden_test]] | sibling | 0.61 |
| [[bld_tools_validation_schema]] | sibling | 0.60 |
| [[bld_tools_retriever_config]] | sibling | 0.59 |
| [[bld_tools_memory_scope]] | sibling | 0.59 |
| [[bld_tools_cli_tool]] | sibling | 0.58 |
| [[bld_tools_runtime_state]] | sibling | 0.58 |
| [[bld_tools_input_schema]] | sibling | 0.57 |
| [[bld_tools_unit_eval]] | sibling | 0.57 |
| [[bld_tools_path_config]] | sibling | 0.57 |
