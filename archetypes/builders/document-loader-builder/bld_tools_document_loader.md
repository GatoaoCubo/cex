---
id: bld_tools_document_loader
kind: tools
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: CALL
quality: 9.1
tags: [tools, document_loader, ingestion, P04]
tldr: "Tools and data sources available to document_loader-builder during artifact production."
density_score: 1.0
title: Tools ISO - document_loader
related:
  - bld_tools_response_format
  - bld_tools_input_schema
  - bld_tools_retriever_config
  - bld_tools_function_def
  - bld_tools_golden_test
  - bld_tools_cli_tool
  - bld_tools_validation_schema
  - bld_tools_memory_scope
  - bld_tools_chunk_strategy
  - bld_tools_search_tool
---
# Tools: document_loader-builder

## Production Tools
| Tool | Purpose | When to Use |
|---|---|---|
| brain_query | Search CEX knowledge base for existing loaders and patterns | Before composing — check for duplicates and reference patterns |
| validate_artifact.py | Run HARD gate checks on produced artifact | After composing — verify H01-H10 before submission |
| cex_forge.py | Register artifact in CEX pool and routing index | After validation passes >= 7.0 |

## Data Sources
| Source | Content | Path |
|---|---|---|
| CEX Schema | SINGLE SOURCE OF TRUTH for document_loader fields | bld_schema_document_loader.md |
| CEX Examples | Golden and anti-examples with gate annotations | bld_examples_document_loader.md |
| SEED_BANK | Format seeds, parser references, chunking patterns | records/pool/seeds/ |
| TAXONOMY | Kind hierarchy — where document_loader sits vs retriever | records/core/docs/TAXONOMY.md |
| LangChain docs | 250+ loader implementations, splitter classes | https://python.langchain.com/docs/integrations/document_loaders/ |
| Unstructured.io | Auto-format detection, partition functions | https://unstructured-io.github.io/unstructured/ |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (Manual)
When validate_artifact.py is unavailable:
1. Copy frontmatter block into a YAML linter (yamllint.com) — must parse with zero errors.
2. Check id with regex `^p04_loader_[a-z][a-z0-9_]+$` — no uppercase, no missing prefix.
3. Count body bytes: `wc -c` on body section or paste into byte counter — must be <= 2048.
4. Verify formats_supported entries are valid MIME types (not file extensions like ".pdf").
5. Confirm chunk_strategy is exactly one of: fixed, recursive, semantic, sentence, paragraph.
6. Confirm output_format is exactly one of: langchain_doc, llamaindex_node, haystack_doc, raw_dict.
7. Check quality field is `null` (not a number, not a string).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_response_format]] | sibling | 0.45 |
| [[bld_tools_input_schema]] | sibling | 0.42 |
| [[bld_tools_retriever_config]] | sibling | 0.41 |
| [[bld_tools_function_def]] | sibling | 0.41 |
| [[bld_tools_golden_test]] | sibling | 0.41 |
| [[bld_tools_cli_tool]] | sibling | 0.40 |
| [[bld_tools_validation_schema]] | sibling | 0.40 |
| [[bld_tools_memory_scope]] | sibling | 0.40 |
| [[bld_tools_chunk_strategy]] | sibling | 0.40 |
| [[bld_tools_search_tool]] | sibling | 0.39 |
