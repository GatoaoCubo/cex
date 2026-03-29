---
kind: config
id: bld_config_constraint_spec
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: constraint_spec Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_constraint_{slug}.md` | `p03_constraint_example.md` |
| Builder directory | kebab-case | `constraint-spec-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `example_config` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P03_prompt/examples/p03_constraint_{slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_constraint_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3048 bytes
- Density: >= 0.85 (no filler)
