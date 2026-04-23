---
kind: config
id: bld_config_enum_def
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
title: "Config Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_enum_def
  - p10_lr_enum_def_builder
  - p11_qg_enum_def
  - bld_schema_enum_def
  - bld_instruction_enum_def
  - p03_sp_enum_def_builder
  - bld_examples_enum_def
  - bld_collaboration_enum_def
  - bld_config_prompt_version
  - bld_architecture_enum_def
---
# Config: enum_def Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_enum_{slug}.md` | `p06_enum_publication_status.md` |
| Builder directory | kebab-case | `enum-def-builder/` |
| Frontmatter fields | snake_case | `descriptions`, `extensible`, `deprecated` |
| Enum slug | snake_case, lowercase, no hyphens | `publication_status`, `artifact_kind` |
| Value names | SCREAMING_SNAKE_CASE or lowercase — pick ONE, be consistent within an enum | `DRAFT` or `draft`, never mixed |
| GraphQL enum values | SCREAMING_SNAKE_CASE (required by GraphQL spec) | `DRAFT`, `PUBLISHED` |
| TypeScript union literals | lowercase string literals preferred | `"draft" \| "published"` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: all values within a single enum MUST use the same case convention.

## File Paths
- Output: `cex/P06_schema/examples/p06_enum_{slug}.md`
- Compiled: `cex/P06_schema/compiled/p06_enum_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)

## Value Count Guidelines
| Count | Signal |
|-------|--------|
| 1 | STOP — this is a constant, not an enum; use constant-builder |
| 2-5 | Ideal — tight domain with clear boundaries |
| 6-12 | Acceptable — complex domain; ensure all values are distinct |
| 13+ | Warning — consider splitting into sub-enums or using a taxonomy |

## Extensibility Rules
| extensible | Meaning | Version bump required to add value |
|------------|---------|-----------------------------------|
| false | Closed set — consumers may assume exhaustive match | YES — adding a value is a breaking change |
| true | Open set — consumers must handle unknown values | NO — new values are non-breaking |

## Deprecation Rules
| Rule | Detail |
|------|--------|
| Deprecated values MUST remain in `values` list | Removal is a breaking change |
| Deprecation reason MUST be documented | Note what to use instead |
| Removal only on major version bump | e.g., 1.x.x -> 2.0.0 |
| `deprecated: []` preferred over omitting field | Explicit empty set aids tooling |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_enum_def]] | upstream | 0.51 |
| [[p10_lr_enum_def_builder]] | downstream | 0.47 |
| [[p11_qg_enum_def]] | downstream | 0.43 |
| [[bld_schema_enum_def]] | upstream | 0.41 |
| [[bld_instruction_enum_def]] | upstream | 0.40 |
| [[p03_sp_enum_def_builder]] | upstream | 0.38 |
| [[bld_examples_enum_def]] | upstream | 0.33 |
| [[bld_collaboration_enum_def]] | downstream | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_architecture_enum_def]] | upstream | 0.30 |
