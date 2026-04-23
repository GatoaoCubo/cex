---
quality: 8.2
quality: 7.8
kind: tools
id: bld_tools_working_memory
pillar: P04
llm_function: CALL
purpose: Tools for working_memory production
title: "Tools Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, tools]
tldr: "Tools for working_memory production: discovery, scoring, compilation."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_response_format
  - bld_tools_function_def
  - bld_tools_memory_summary
  - bld_tools_input_schema
  - bld_tools_validation_schema
  - bld_tools_search_tool
  - bld_tools_hitl_config
  - bld_tools_cli_tool
  - bld_tools_learning_record
---

# Tools: working-memory-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Find existing working_memory artifacts | Phase 1 | CONDITIONAL |
| cex_retriever.py | Semantic search for similar memory specs | Phase 1 | AVAILABLE |
| cex_score.py | Score artifact quality | Phase 3 | AVAILABLE |
| cex_compile.py | Compile .md to .yaml | Phase 3 | AVAILABLE |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Kind definitions |
| LangChain docs | docs.langchain.com/memory | Buffer window memory patterns |
| LangGraph docs | langchain-ai.github.io/langgraph | AgentState patterns |

## Slot Type Reference
```
Valid types: string, int, float, bool, list[string], list[int], json
Use json only when structure is truly nested; prefer typed primitives
```

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | |

## Validation Checks
id `^p10_wm_`, task_id non-empty, context_slots typed, capacity_limit numeric + unit,
expiry declared, clear_on_complete in enum, quality == null, body <= 3072 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.42 |
| [[bld_tools_response_format]] | sibling | 0.42 |
| [[bld_tools_function_def]] | sibling | 0.41 |
| [[bld_tools_memory_summary]] | sibling | 0.41 |
| [[bld_tools_input_schema]] | sibling | 0.40 |
| [[bld_tools_validation_schema]] | sibling | 0.39 |
| [[bld_tools_search_tool]] | sibling | 0.39 |
| [[bld_tools_hitl_config]] | sibling | 0.39 |
| [[bld_tools_cli_tool]] | sibling | 0.38 |
| [[bld_tools_learning_record]] | sibling | 0.38 |
