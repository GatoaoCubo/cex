---
kind: config
id: bld_config_handoff_protocol
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: handoff_protocol Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_handoff_{slug}.md` | `p02_handoff_example.md` |
| Builder directory | kebab-case | `handoff-protocol-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `example_config` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P02_model/examples/p02_handoff_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_handoff_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3048 bytes
- Density: >= 0.8 (no filler)
