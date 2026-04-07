---
kind: config
id: bld_config_citation
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 15
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: citation Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_cit_{topic_slug}.md` | `p01_cit_anthropic_prompt_caching.md` |
| Builder directory | kebab-case | `citation-builder/` |
| Frontmatter fields | snake_case | `source_type`, `reliability_tier` |
| Topic slug | lowercase, underscores | `anthropic_prompt_caching`, `bm25_scoring` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `P01_knowledge/examples/p01_cit_{topic}.md`
2. Compiled: `P01_knowledge/compiled/p01_cit_{topic}.yaml`
## Size Limits
1. Total file: max 2048 bytes
2. Excerpt: 1-3 sentences (concrete, with specifics)
3. tldr: <= 160 chars
## Source Type Rules
| Source | source_type | reliability_tier | Notes |
|--------|------------|-----------------|-------|
| Peer-reviewed paper | paper | tier_1 | Include DOI |
| Official documentation | web | tier_2 | Include version |
| Blog/tutorial | web | tier_3 | Include date_accessed |
| Internal CEX artifact | internal | tier_2 | Include artifact id |
| API reference | api | tier_2 | Include endpoint version |

## Metadata

```yaml
id: bld_config_citation
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-citation.md
```
