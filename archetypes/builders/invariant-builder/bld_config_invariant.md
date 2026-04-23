---
id: bld_config_invariant
kind: config
pillar: P08
parent: invariant-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
tags: [config, invariant-builder, naming, paths, P08]
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
title: "Config Invariant"
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_knowledge_card_invariant
  - bld_schema_invariant
  - p03_ins_law
  - p11_qg_law
  - bld_examples_invariant
  - bld_tools_invariant
  - bld_collaboration_invariant
  - bld_memory_invariant
  - p03_sp_law_builder
  - bld_output_template_invariant
---
# invariant-builder — CONFIG
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_law_{number}.md` | `p08_law_5.md` |
| Compiled output | `p08_law_{number}.yaml` | `p08_law_5.yaml` |
| Builder directory | kebab-case | `invariant-builder/` |
| Frontmatter id | `p08_law_{number}` | `p08_law_5` |
| Frontmatter fields | snake_case | `enforcement`, `rationale`, `created` |
| Number format | plain integer | `5` (not `05`, not `five`, not `5.0`) |
Rule: `id` MUST equal filename stem. File `p08_law_5.md` MUST have `id: p08_law_5`.
## File Paths
| Purpose | Path |
|---------|------|
| Output (examples) | `cex/P08_architecture/examples/p08_law_{number}.md` |
| Compiled YAML | `cex/P08_architecture/compiled/p08_law_{number}.yaml` |
| Builder location | `cex/archetypes/builders/invariant-builder/` |
| CEX schema ref | `cex/P08_architecture/_schema.yaml` |
| Existing laws ref | `records/framework/docs/LAWS_v3_PRACTICAL.md` |
## Size Limits
| Constraint | Value | Scope |
|-----------|-------|-------|
| max_bytes (body) | 3072 | Body sections only (after frontmatter) |
| max_bytes (total) | ~4200 | Frontmatter + body combined |
| density_min | 0.80 | No filler phrases |
| tldr max chars | 160 | Frontmatter field |
| statement | 1 sentence | Imperative, no compound sentences |
## Law-Specific Constraints
| Field | Constraint | Rationale |
|-------|-----------|-----------|
| statement | One imperative sentence using MUST/SHALL/NEVER/ALWAYS | RFC 2119 compliance; laws mandate, not suggest |
| number | Positive integer, unique, sequential | Identification and collision prevention |
| enforcement | Must name detection mechanism explicitly | Unenforced laws are wishes, not laws |
| exceptions | Explicit list or "None" — never omit field | Prevents ambiguity and "well technically" bypasses |
| scope | One of: system, agent_group, domain | Precise applicability boundary |
| priority | Integer 1-10 (10 = highest) | Conflict resolution when laws compete |
| quality | Always null | H05 gate; no self-scoring ever |
| advisory language | PROHIBITED | "should", "consider", "recommended" belong in patterns/instructions |
## Prohibited in Law Artifacts
| Pattern | Why prohibited | Use instead |
|---------|---------------|-------------|
| `quality: 8.5` | Self-scoring (H05) | `quality: null` |
| `statement: "try to..."` | Advisory language (H09) | `statement: "MUST..."` |
| `kind: rule` | Wrong kind (H04) | `kind: law` |
| Multi-sentence statement | Violates single-mandate rule | Split into multiple laws |
| Missing enforcement | Unenforced law (S03) | Add mechanism + detection |
| Omitted exceptions field | Ambiguity risk (S04) | Add `exceptions: []` or list conditions |
| `id: law_5` | Wrong prefix (H02) | `id: p08_law_5` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_invariant]] | related | 0.58 |
| [[bld_schema_invariant]] | related | 0.51 |
| [[p03_ins_law]] | upstream | 0.47 |
| [[p11_qg_law]] | downstream | 0.38 |
| [[bld_examples_invariant]] | related | 0.37 |
| [[bld_tools_invariant]] | related | 0.35 |
| [[bld_collaboration_invariant]] | related | 0.34 |
| [[bld_memory_invariant]] | downstream | 0.32 |
| [[p03_sp_law_builder]] | upstream | 0.29 |
| [[bld_output_template_invariant]] | related | 0.28 |
