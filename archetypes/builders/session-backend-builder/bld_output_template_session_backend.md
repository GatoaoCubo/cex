---
kind: output_template
id: bld_output_template_session_backend
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a session_backend artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{backend_type_description_and_rationale}}
{{connection_details_or_path_description}}
{{why_this_backend_fits_the_requirements}}
## Session Lifecycle
- **Create**: {{when_and_how_sessions_are_created}}
- **Read**: {{how_sessions_are_loaded}}
- **TTL**: {{expiration_policy}}
- **Cleanup**: {{how_expired_sessions_are_removed}}
- **Compaction**: {{defragmentation_strategy}}
- **Max sessions**: {{eviction_policy_when_max_reached}}
## Serialization
{{format_choice_and_rationale}}
- Trade-off: {{size_vs_speed_vs_readability}}
- Schema evolution: {{how_old_sessions_remain_readable}}
## Security
- Encryption: {{encryption_level_and_rationale}}
- Access: {{access_control_mechanism}}
- Credentials: {{env_var_references_only}}
## Scoping
- Namespace: {{key_prefix_convention}}
- Isolation: {{how_cross_nucleus_contamination_is_prevented}}
## Upgrade Path
{{migration_steps_from_current_to_next_tier}}
## References
- {{reference_1}}
- {{reference_2}}
