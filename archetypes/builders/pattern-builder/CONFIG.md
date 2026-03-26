---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: pattern Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_pat_{slug}.md` | `p08_pat_continuous_batching.md` |
| Builder directory | kebab-case | `pattern-builder/` |
| Frontmatter fields | snake_case | `related_patterns`, `anti_patterns` |
| Slug | lowercase + underscores | `continuous_batching` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P08_architecture/examples/p08_pat_{slug}.md`
- Compiled: `cex/P08_architecture/compiled/p08_pat_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total: ~5300 bytes (frontmatter + body)
- Density: >= 0.80

## Pattern-Specific Constraints
- Name: 2-5 words, Title Case (e.g., "Continuous Batching", "Signal Monitor")
- Problem recurrence: must describe a situation that happens repeatedly
- Forces minimum: at least 2 competing tensions
- Consequences balance: MUST include at least 1 cost/drawback alongside benefits
- Examples minimum: at least 2 concrete, named applications
- Solution concreteness: must describe HOW (steps or diagram), not just WHAT
- Anti-patterns: specific wrong approaches, not generic warnings
- No prescriptive language: "consider" not "you must" (patterns recommend, laws mandate)
