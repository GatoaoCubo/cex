---
kind: knowledge_card
id: bld_knowledge_card_path_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for path_config production — atomic searchable facts
sources: path-config-builder MANIFEST.md + SCHEMA.md, XDG Base Directory, Windows Known Folders
quality: 9.1
title: "Knowledge Card Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: path_config
## Executive Summary
Path configs are filesystem path catalogs that define every directory and file path a system scope needs — with platform support, default values, expandable variables, and creation order. Each config scopes paths to ONE system area with portable defaults using expandable variables instead of hardcoded absolutes. They differ from env configs (all environment variables), permissions (access control), feature flags (on/off toggles), and runtime rules (behavioral settings) by being the single source of truth for filesystem layout.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (configuration) |
| Kind | `path_config` (exact literal) |
| ID pattern | `p09_path_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min path entries | 3 |
| Path types | dir, file, glob |
| Platform field | required (target OS or list of supported OS) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Expandable variables | Use $HOME, `{{USER_DIR}}`, $XDG_DATA_HOME — never hardcoded user paths |
| Platform normalization | Define with forward slashes; resolve per-platform at runtime |
| Directory hierarchy | base_dir -> {data, config, cache, logs, temp} as tree |
| Required vs optional | Required paths block startup if missing; optional created on demand |
| Relative preference | Prefer relative to base_dir; absolute only for system-level paths |
| Explicit defaults | Every path has a default value (null acceptable if documented) |
| Creation order | Document which paths must exist before others |
### XDG Mapping Reference
| XDG Variable | Purpose | Windows Equivalent |
|-------------|---------|-------------------|
| $XDG_DATA_HOME | User data | %APPDATA% |
| $XDG_CONFIG_HOME | User config | %APPDATA% |
| $XDG_CACHE_HOME | Cache files | %LOCALAPPDATA%\cache |
| $XDG_STATE_HOME | State data | %LOCALAPPDATA% |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Hardcoded user paths (/home/john/) | Breaks on any other machine |
| No platform field | Paths are platform-dependent; undeclared = silent breakage |
| Missing defaults | Forces manual config on every installation |
| Fewer than 3 path entries | Doesn't justify a config artifact |
| Mixed separators (/ and \\) | Inconsistent; pick one and resolve at runtime |
| No creation order | Dependencies between paths cause race conditions |
## Application
1. Define scope: which system area does this path config govern?
2. List all paths with name, type (dir/file/glob), and default value
3. Set platform field (target OS or supported OS list)
4. Use expandable variables for all user-specific absolute paths
5. Mark each path as relative_or_absolute explicitly
6. Document directory hierarchy (parent-child relationships)
7. Specify creation_order for initialization from scratch
8. Validate: 8 HARD + 10 SOFT gates, body <= 3072 bytes
## References
- path-config-builder SCHEMA.md v1.0.0
- XDG Base Directory Specification
- Windows Known Folder IDs (MSDN)
- Python pathlib documentation
