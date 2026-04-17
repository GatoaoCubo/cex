---
id: p04_ct_cex_index
kind: cli_tool
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
