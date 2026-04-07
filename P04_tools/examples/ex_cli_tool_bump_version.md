---
id: p04_ct_bump_version
kind: cli_tool
pillar: P04
title: "Bump Version — Increment LP or global version in VERSION.yaml"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, product, version, semver, release]
cli_command: "python _tools/bump_version.py"
cli_args:
  - name: "--lp"
    type: string
    required: false
    description: "LP to bump (e.g. P01). Omit for global only."
  - name: "--level"
    type: string
    required: false
    description: "Bump level: patch, minor, or major (default: patch)"
  - name: "--message"
    type: string
    required: false
    description: "Changelog entry message"
inputs: ["_meta/VERSION.yaml"]
outputs: ["updated VERSION.yaml", "changelog entry in _meta/CHANGELOG.md"]
dependencies: ["pyyaml"]
category: product
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
---

## Purpose
Increments semantic version (major.minor.patch) for a specific LP or the global CEX version. Updates _meta/VERSION.yaml and optionally appends a changelog entry to _meta/CHANGELOG.md.

## Usage
```bash
# Bump global patch version
python _tools/bump_version.py

# Bump specific LP minor version
python _tools/bump_version.py --lp P01 --level minor

# Major bump with changelog message
python _tools/bump_version.py --level major --message "Breaking: new schema format"
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--lp` | string | no | Target LP (omit for global) |
| `--level` | string | no | patch/minor/major (default: patch) |
| `--message` / `-m` | string | no | Changelog entry |

## Pipeline Position
**8F Function**: GOVERN (F7) — version governance.
**Stage**: Release management. Run before tagging a release. Downstream of all changes, upstream of changelog_gen.

## Dependencies
- `_meta/VERSION.yaml` with cex_version and lps sections
- `_meta/CHANGELOG.md` for appending entries
