---
kind: config
id: bld_config_mental_model
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
title: "Config Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_mental_model
  - p03_ins_mental_model
  - p03_sp_mental_model_builder
  - bld_schema_mental_model
  - p11_qg_mental_model
  - bld_collaboration_mental_model
  - bld_config_system_prompt
  - mental-model-builder
  - bld_config_memory_scope
  - bld_tools_mental_model
---
# Config: mental_model Production Rules

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mm_{agent_slug}.yaml` | `p02_mm_scout_agent.yaml` |
| Builder directory | kebab-case | `mental-model-builder/` |
| Frontmatter fields | snake_case | `routing_rules`, `decision_tree` |
| Agent slug | snake_case, lowercase | `scout_agent`, `research_lead` |
Rule: id MUST equal filename stem.
Rule: file extension is .yaml (pure YAML artifact).
## File Paths
- Output: `cex/P02_model/examples/p02_mm_{agent_slug}.yaml`
- Compiled: `cex/P02_model/compiled/p02_mm_{agent_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total: ~3000 bytes
- Density: >= 0.80
## Routing Rules Requirements
- Minimum 3 routing rules
- Each rule: keywords (list), action (string), confidence (float 0.0-1.0)
- Keywords must be specific (not "everything", "anything", "general")
- Actions must be concrete verbs ("route to X", "execute Y", "defer to Z")
## Decision Tree Requirements
- Minimum 2 conditions
- Each condition: if/then structure, optional else
- Conditions must be evaluable (not vague)
- No circular references between conditions
## Personality Enum Values
| Field | Allowed Values |
|-------|---------------|
| tone | professional, casual, technical, empathetic, direct |
| verbosity | concise, moderate, verbose |
| risk_tolerance | low, medium, high |
## Pillar Disambiguation
This builder produces P02 mental_model (design-time blueprint).
P10 mental_model (runtime session state) is a DIFFERENT kind.
Never set pillar to P10 — that requires a different builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_mental_model]] | upstream | 0.40 |
| [[p03_ins_mental_model]] | upstream | 0.34 |
| [[p03_sp_mental_model_builder]] | upstream | 0.33 |
| [[bld_schema_mental_model]] | upstream | 0.33 |
| [[p11_qg_mental_model]] | downstream | 0.32 |
| [[bld_collaboration_mental_model]] | upstream | 0.31 |
| [[bld_config_system_prompt]] | sibling | 0.30 |
| [[mental-model-builder]] | upstream | 0.30 |
| [[bld_config_memory_scope]] | sibling | 0.29 |
| [[bld_tools_mental_model]] | upstream | 0.29 |
