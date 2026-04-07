---
kind: config
id: bld_config_handoff
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
# Config: handoff Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_ho_{task}.md` | `p12_ho_wave19_builders.md` |
| Builder directory | kebab-case | `handoff-builder/` |
| Frontmatter fields | snake_case | `quality_target`, `scope_fence` |
| Autonomy values | lowercase enum | `full`, `supervised`, `assisted` |
| Agent_group values | lowercase slug | `edison`, `atlas`, `shaka` |
Rule: use `.md` (YAML frontmatter + markdown body) for handoff artifacts.
## File Paths
- Primary output: `.claude/handoffs/p12_ho_{task}.md`
- Compiled output: `P12_orchestration/compiled/p12_ho_{task}.md`
- Human reference: `P12_orchestration/examples/p12_ho_{task}.md`
## Size Limits
- Preferred handoff size: <= 3072 bytes
- Absolute max: 4096 bytes
- Tasks should be concise and specific
## Content Restrictions
- Each task step must be one specific action (no compound steps)
- Scope fence must list both SOMENTE and NAO TOQUE
- Commit section must have exact git add and commit commands
- Signal section must reference a concrete completion mechanism
## Boundary Restrictions
- No prompt persona or response format constraints (belongs in action_prompt)
- No status events or quality scores (belongs in signal)
- No keyword routing tables (belongs in dispatch_rule)
- No step graphs with error handling (belongs in workflow)
- No dependency graph structure (belongs in dag)
- No multi-agent coordination protocol (belongs in crew)
