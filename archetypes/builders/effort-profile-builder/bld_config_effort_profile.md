---
kind: config
id: bld_config_effort_profile
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
# Config: effort_profile Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_effort_{slug}.md` | `p09_effort_n03_opus_high.md` |
| Builder directory | kebab-case | `effort-profile-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `n03_opus_high` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_effort_{slug}.md`
- Compiled: `cex/P09_config/compiled/p09_effort_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5120 bytes
- Density: >= 0.8 (no filler)
