---
kind: config
id: bld_config_builder
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for the meta-builder
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: global
---
# Config: _builder-builder Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Meta-templates | `bld_meta_{iso_type}_builder.md` | `bld_meta_manifest_builder.md` |
| Builder directory | kebab-case + `-builder` suffix | `agent-builder/` |
| Frontmatter fields | snake_case | `llm_function`, `file_position` |
| builder specs | `bld_{iso_type}_{kind}.md` | `bld_manifest_agent.md` |

Rule: id MUST equal filename stem.
Rule: Every builder directory MUST contain exactly 13 builder spec files.

## File Paths
- Output: `archetypes/builders/{kind}-builder/bld_{iso}_{kind}.md`
- Meta-templates: `archetypes/builders/_builder-builder/bld_meta_{iso}_builder.md`

## Size Limits
- Standard ISOs: max 4096 bytes
- Instruction ISOs: max 6144 bytes
- Meta-templates: max 6144 bytes (include comments/examples)
- Density: >= 0.85

## Builder Generation Constraints
- MUST generate all 13 builder specs per builder (manifest, instruction, config, memory, tools, collaboration, architecture, schema, output_template, examples, quality_gate, knowledge_card, system_prompt)
- MUST include universal fields in generated ISOs (keywords, triggers, geo_description in manifest; memory_scope, observation_types in memory; effort, max_turns, hooks, permission_scope in config; Tool Permissions in tools)
- MUST respect non-default overrides table for specific builders
- NEVER generate ISOs that exceed size limits
- ALWAYS validate generated builder with cex_doctor.py before commit
