---
kind: config
id: bld_config_validator_builder_codex
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: validator Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_val_{rule}.md` | `p06_val_frontmatter_required.md` |
| Compiled files | `p06_val_{rule}.yaml` | `p06_val_frontmatter_required.yaml` |
| Builder directory | kebab-case | `validator-builder-codex/` |
| Frontmatter fields | snake_case | `action_on_fail`, `density_score` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_val_{rule}.md`
- Compiled: `cex/P06_schema/compiled/p06_val_{rule}.yaml`
## Size Limits
- Total artifact: <= `3072` bytes compiled
- Markdown body: prefer <= `2200` bytes
- Density: >= `0.80`
## Validator-Specific Constraints
- use only approved trigger enum values
- use only approved severity enum values
- `action_on_fail` must align with severity
- conditions must be deterministic, not aspirational
- prefer one validator per rule family; split oversized mixed concerns
