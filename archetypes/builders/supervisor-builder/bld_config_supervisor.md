---
kind: config
id: bld_config_supervisor
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
quality: 9.0
title: "Config Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_director_builder
  - bld_knowledge_card_supervisor
  - bld_schema_supervisor
  - bld_instruction_supervisor
  - bld_examples_supervisor
  - supervisor-builder
  - bld_collaboration_supervisor
  - p11_qg_director
  - bld_output_template_supervisor
  - p01_kc_supervisor
---
# Config: supervisor Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `ex_director_{topic}.md` + `.yaml` | `ex_director_brand_launch.md` |
| Builder directory | kebab-case | `supervisor-builder/` |
| Frontmatter fields | snake_case | `dispatch_mode`, `signal_check` |
| Topic slug | snake_case, lowercase | `brand_launch`, `content_pipeline` |
Rule: id MUST equal filename stem.
## File Paths
- Output (canonical): `P08_architecture/examples/ex_director_{topic}.md`
- Compiled: `P08_architecture/compiled/ex_director_{topic}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3200 bytes
- Density: >= 0.85
## Dispatch Mode Enum
| Value | When to use |
|-------|-------------|
| sequential | Builders have strict ordering dependencies |
| parallel | Builders are independent — run simultaneously |
| conditional | Route to specific builders based on task content or signals |
## Wave Topology Rules
- Wave N+1 starts ONLY after all Wave N signals received (when signal_check: true)
- Each wave lists its builders by name and nucleus
- Fallback per builder: retry (1x), skip, substitute (name alternate), abort
## Body Requirements
- Identity: 2-4 sentences naming the mission, domain, and coordination strategy
- Builders: table or list of all dispatched builders with role and nucleus
- Wave Topology: ordered wave sequence with signal gates
- Dispatch Config: mode + signal_check + fallback_per_builder
- Routing: triggers + keywords + NOT-when exclusions (mandatory)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_director_builder]] | upstream | 0.49 |
| [[bld_knowledge_card_supervisor]] | upstream | 0.48 |
| [[bld_schema_supervisor]] | upstream | 0.44 |
| [[bld_instruction_supervisor]] | upstream | 0.42 |
| [[bld_examples_supervisor]] | upstream | 0.38 |
| [[supervisor-builder]] | upstream | 0.38 |
| [[bld_collaboration_supervisor]] | downstream | 0.38 |
| [[p11_qg_director]] | downstream | 0.37 |
| [[bld_output_template_supervisor]] | upstream | 0.33 |
| [[p01_kc_supervisor]] | upstream | 0.32 |
