---
kind: config
id: bld_config_axiom
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: axiom Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_ax_{slug}.md` | `p10_ax_quality_never_self_scored.md` |
| Builder directory | kebab-case | `axiom-builder/` |
| Frontmatter fields | snake_case | `linked_artifacts`, `density_score` |
| Slug | lowercase + underscores | `quality_never_self_scored` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P10_memory/examples/p10_ax_{slug}.md`
- Compiled: `cex/P10_memory/compiled/p10_ax_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes (frontmatter + body)
- Density: >= 0.80
## Axiom-Specific Constraints
- Rule atomicity: ONE sentence, no conjunctions ("and", "or", "but")
- Immutability test: if the rule could change in 5 years, it is a law, not an axiom
- Scope precision: must name domain boundary (e.g., "all CEX artifacts" not "the system")
- No operational details: axiom states WHAT, never HOW
- Dependencies: only reference other axioms (never laws, guardrails, or instructions)
