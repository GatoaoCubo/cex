---
kind: output_template
id: bld_output_template_session_backend
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a session_backend artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_session_backend
  - bld_schema_session_backend
  - bld_architecture_session_backend
  - p11_qg_session_backend
  - session-backend-builder
  - p03_sp_session_backend_builder
  - bld_instruction_session_backend
  - p01_kc_session_backend
  - bld_config_session_backend
  - bld_knowledge_card_session_backend
---

# Output Template: session_backend
```yaml
id: p10_sb_{{backend_name}}
kind: session_backend
pillar: P10

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

backend: {{file|sqlite|redis|postgres}}
path: "{{filesystem_path_if_file_or_sqlite}}"
connection_string: "{{env_var_reference_if_redis_or_postgres}}"
ttl_hours: {{positive_number}}

max_sessions: {{positive_integer}}
serialization: {{json|msgpack|protobuf}}
encryption: {{none|basic|full}}
scoping: {{per_nucleus|per_agent|global}}

quality: null
tags: [session_backend, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_config_covers_max_200ch}}"

compaction: {{true|false}}
upgrade_path: "{{current_backend}} -> {{next_backend}} (when {{trigger}})"
```
## Backend Specification
`{{backend_type_description_and_rationale}}`
`{{connection_details_or_path_description}}`
`{{why_this_backend_fits_the_requirements}}`
## Session Lifecycle
1. **Create**: `{{when_and_how_sessions_are_created}}`
2. **Read**: `{{how_sessions_are_loaded}}`
3. **TTL**: `{{expiration_policy}}`
4. **Cleanup**: `{{how_expired_sessions_are_removed}}`
5. **Compaction**: `{{defragmentation_strategy}}`
6. **Max sessions**: `{{eviction_policy_when_max_reached}}`
## Serialization
`{{format_choice_and_rationale}}`
1. Trade-off: `{{size_vs_speed_vs_readability}}`
2. Schema evolution: `{{how_old_sessions_remain_readable}}`
## Security
1. Encryption: `{{encryption_level_and_rationale}}`
2. Access: `{{access_control_mechanism}}`
3. Credentials: `{{env_var_references_only}}`
## Scoping
1. Namespace: `{{key_prefix_convention}}`
2. Isolation: `{{how_cross_nucleus_contamination_is_prevented}}`
## Upgrade Path
`{{migration_steps_from_current_to_next_tier}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | session backend construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_session_backend]] | downstream | 0.55 |
| [[bld_schema_session_backend]] | downstream | 0.50 |
| [[bld_architecture_session_backend]] | downstream | 0.50 |
| [[p11_qg_session_backend]] | downstream | 0.48 |
| [[session-backend-builder]] | downstream | 0.47 |
| [[p03_sp_session_backend_builder]] | upstream | 0.47 |
| [[bld_instruction_session_backend]] | upstream | 0.42 |
| [[p01_kc_session_backend]] | downstream | 0.39 |
| [[bld_config_session_backend]] | downstream | 0.36 |
| [[bld_knowledge_card_session_backend]] | upstream | 0.35 |
