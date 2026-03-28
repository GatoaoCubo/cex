---
kind: config
id: bld_config_lens
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: lens Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_lens_{perspective_slug}.yaml` | `p02_lens_cost_efficiency.yaml` |
| Builder directory | kebab-case | `lens-builder/` |
| Frontmatter fields | snake_case | `applies_to`, `perspective` |
| Perspective slugs | snake_case, lowercase | `cost_efficiency`, `security_posture` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P02_model/examples/p02_lens_{perspective_slug}.yaml`
- Compiled: `cex/P02_model/compiled/p02_lens_{perspective_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total: ~3000 bytes including frontmatter
- Density: >= 0.80

## Perspective Rules
| Rule | Enforcement |
|------|-------------|
| Non-empty perspective | HARD (H07) |
| applies_to >= 1 kind | HARD (H08) |
| Concrete filters | SOFT (S04) |
| Declared bias | SOFT (S08) |

## Composition Rules
- Multiple lenses can apply to the same artifact kind
- Weight field (0.0-1.0) controls influence in multi-lens scenarios
- Priority field (integer) controls evaluation order
- Conflicting lenses: higher priority wins, equal priority uses weight
