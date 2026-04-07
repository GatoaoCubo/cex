---
kind: config
id: bld_config_interface
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: interface Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_iface_{contract_slug}.yaml` | `p06_iface_research_to_marketing.yaml` |
| Builder directory | kebab-case | `interface-builder/` |
| Frontmatter fields | snake_case | `backward_compatible`, `example_payloads` |
| Contract slugs | snake_case, lowercase | `research_to_marketing`, `brain_search` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P06_schema/examples/p06_iface_{contract_slug}.yaml`
2. Compiled: `cex/P06_schema/compiled/p06_iface_{contract_slug}.json`
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Total: ~4000 bytes including frontmatter
3. Density: >= 0.80
## Method Contract Rules
| Rule | Enforcement |
|------|-------------|
| Each method has name | HARD (H07) |
| Each method has input type | HARD (H07) |
| Each method has output type | HARD (H07) |
| Each method has description | SOFT (S05) |
| Methods list >= 1 entry | HARD (H07) |
## Versioning Policy
1. New interfaces start at 1.0.0
2. Breaking changes: bump major, set backward_compatible: false
3. Additive methods: bump minor, backward_compatible: true
4. Fix/doc changes: bump patch

## Metadata

```yaml
id: bld_config_interface
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-interface.md
```
