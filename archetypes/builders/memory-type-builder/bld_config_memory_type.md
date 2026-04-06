---
kind: config
id: bld_config_memory_type
pillar: P09
llm_function: CONSTRAIN
effort: medium
max_turns: 15
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
---

# Config: memory_type

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_mt_{type_name}.md` → `.yaml` | `p10_mt_user.yaml` |
| Builder directory | kebab-case | `memory-type-builder/` |
| Frontmatter fields | snake_case | `observation_types`, `decay_rate` |

- output_dir: P10_memory/compiled/
- naming: p10_mt_{type_name}.md → p10_mt_{type_name}.yaml
- max_bytes: 2048
- machine_format: yaml
- id == filename stem
- One artifact per memory type (max 4 total)
