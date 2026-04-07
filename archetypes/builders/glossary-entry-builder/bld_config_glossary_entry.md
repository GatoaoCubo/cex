---
kind: config
id: bld_config_glossary_entry
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
title: "Config Glossary Entry"
version: "1.0.0"
author: n03_builder
tags: [glossary_entry, builder, examples]
tldr: "Golden and anti-examples for glossary entry construction, demonstrating ideal structure and common pitfalls."
domain: "glossary entry construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: glossary_entry Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_gl_{term_slug}.yaml` | `p01_gl_kind.yaml` |
| Builder directory | kebab-case | `glossary-entry-builder/` |
| Frontmatter fields | snake_case | `related_terms`, `domain_specific` |
| Term slugs | snake_case, lowercase | `kind`, `knowledge_card`, `quality_gate` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P01_knowledge/examples/p01_gl_{term_slug}.yaml`
2. Compiled: `cex/P01_knowledge/compiled/p01_gl_{term_slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 512 bytes
2. Total: ~800 bytes including frontmatter
3. Definition: max 3 lines
4. Density: >= 0.80
## Definition Rules
| Rule | Enforcement |
|------|-------------|
| Max 3 lines | HARD (H07) |
| No filler words | SOFT (S07) |
| Concrete, not abstract | SOFT (S05) |
| Include at least one example in definition | SOFT (S04) |
## Term Conventions
1. Terms are lowercase unless proper noun
2. Multi-word terms use snake_case in id, natural case in term field
3. Abbreviations documented in abbreviation field
4. Cross-pillar terms include pillar reference in disambiguation

## Metadata

```yaml
id: bld_config_glossary_entry
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-glossary-entry.md
```
