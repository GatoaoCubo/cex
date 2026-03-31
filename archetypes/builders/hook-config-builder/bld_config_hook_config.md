---
kind: config
id: bld_config_hook_config
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
---
# Config: hook_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_hookconf_{slug}.md` | `p04_hookconf_agent_builder.md` |
| Builder directory | kebab-case | `hook-config-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `agent_builder` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_execution/examples/p04_hookconf_{slug}.md`
- Compiled: `cex/P04_execution/compiled/p04_hookconf_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5120 bytes
- Density: >= 0.8 (no filler)
