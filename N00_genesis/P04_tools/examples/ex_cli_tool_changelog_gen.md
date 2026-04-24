---
id: p04_ct_changelog_gen
kind: cli_tool
8f: F5_call
pillar: P04
title: "Changelog Gen — Generate changelog from git log grouped by LP"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, product, changelog, git, release]
cli_command: "python _tools/changelog_gen.py"
cli_args:
  - name: "--since"
    type: string
    required: false
    description: "Git ref to start from (tag or commit). Auto-detects last tag if omitted."
  - name: "--dry-run"
    type: boolean
    required: false
    description: "Print changelog without writing to file"
inputs: ["git log history", "_meta/VERSION.yaml"]
outputs: ["formatted changelog entry grouped by LP", "appended to _meta/CHANGELOG.md"]
dependencies: ["pyyaml", "git"]
category: product
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_bump_version
  - p04_tool_taxonomy_builder
  - bld_tools_changelog
  - p04_ct_cex_pipeline
  - changelog-builder
  - kc_git_workflow_for_agents
  - bld_collaboration_changelog
  - bld_knowledge_card_changelog
  - p04_ct_fix_frontmatter
  - p04_ct_cex_compile
---

## Purpose
Reads git log since the last tag (or specified ref), groups commits by LP based on file paths, and generates a formatted changelog entry. Auto-detects the last git tag as starting point.

## Usage
```bash
# Auto-detect last tag, generate changelog
python _tools/changelog_gen.py

# From specific tag
python _tools/changelog_gen.py --since v1.2.0

# Preview without writing
python _tools/changelog_gen.py --dry-run
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--since` | string | no | Starting git ref (default: last tag) |
| `--dry-run` | flag | no | Print without writing |

## Pipeline Position
**8F Function**: COLLABORATE (F8) — communication and documentation.
**Stage**: Release documentation. Run after bump_version, before git tag. Reads git history to produce human-readable changelog.

## Dependencies
- Git repository with commit history
- `_meta/VERSION.yaml` for version header
- `_meta/CHANGELOG.md` for appending entries
- LP detection regex on file paths (P\d{2}_\w+)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_bump_version]] | sibling | 0.32 |
| [[p04_tool_taxonomy_builder]] | sibling | 0.27 |
| [[bld_tools_changelog]] | related | 0.26 |
| [[p04_ct_cex_pipeline]] | sibling | 0.24 |
| [[changelog-builder]] | upstream | 0.24 |
| [[kc_git_workflow_for_agents]] | upstream | 0.23 |
| [[bld_collaboration_changelog]] | downstream | 0.21 |
| [[bld_knowledge_card_changelog]] | upstream | 0.20 |
| [[p04_ct_fix_frontmatter]] | sibling | 0.19 |
| [[p04_ct_cex_compile]] | sibling | 0.19 |
