---
id: p04_ct_cex_index
kind: cli_tool
8f: F5_call
pillar: P04
title: "CEX Index — SQLite indexer with wikilinks and frontmatter"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, governance, index, sqlite, search]
cli_command: "python _tools/cex_index.py"
cli_args:
  - name: "--query"
    type: string
    required: false
    description: "Query: field=value (e.g. type=knowledge_card)"
  - name: "--orphans"
    type: boolean
    required: false
    description: "Show files with no incoming wikilinks"
  - name: "--stats"
    type: boolean
    required: false
    description: "Show index statistics"
  - name: "--verbose"
    type: boolean
    required: false
    description: "Verbose output"
inputs: ["all .md/.yaml files in CEX repo"]
outputs: [".cex/index.db (SQLite)", "query results", "orphan reports", "statistics"]
dependencies: ["pyyaml", "sqlite3 (stdlib)"]
category: governance
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_cex_compile
  - p04_ct_cex_forge
  - p04_ct_fix_frontmatter
  - p04_ct_validate_schema
  - knowledge-index-builder
  - bld_collaboration_knowledge_index
  - validate
  - p04_ct_cex_doctor
  - p04_ct_distill
  - p06_arch_knowledge_graph
---

## Purpose
Scans all .md and .yaml files, parses YAML frontmatter and [[wikilinks]], stores metadata and edges in .cex/index.db (SQLite). Enables queries by any frontmatter field, orphan detection, and statistics about the knowledge graph.

## Usage
```bash
# Full index rebuild (scans all files)
python _tools/cex_index.py

# Query by frontmatter field
python _tools/cex_index.py --query "type=knowledge_card"

# Find orphan files (no incoming links)
python _tools/cex_index.py --orphans

# Show index statistics
python _tools/cex_index.py --stats
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--query` / `-q` | string | no | field=value query |
| `--orphans` | flag | no | Show unlinked files |
| `--stats` / `-s` | flag | no | Index statistics |
| `--verbose` / `-v` | flag | no | Verbose output |

No flags = full reindex.

## Pipeline Position
**8F Function**: INJECT (F3) — builds the searchable knowledge graph for context injection.
**Stage**: Infrastructure. Runs after batch creation or modification. Enables cex_forge and pipeline to discover artifacts.

## Dependencies
- Scans all directories except .git, .obsidian, __pycache__, node_modules, .cex
- Stores in `.cex/index.db` with tables: files (path, id, type, pillar, etc.), edges (source, target wikilinks)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_cex_compile]] | sibling | 0.30 |
| [[p04_ct_cex_forge]] | sibling | 0.25 |
| [[p04_ct_fix_frontmatter]] | sibling | 0.22 |
| [[p04_ct_validate_schema]] | sibling | 0.21 |
| [[knowledge-index-builder]] | downstream | 0.20 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.20 |
| [[validate]] | downstream | 0.20 |
| [[p04_ct_cex_doctor]] | sibling | 0.19 |
| [[p04_ct_distill]] | sibling | 0.18 |
| [[p06_arch_knowledge_graph]] | downstream | 0.18 |
