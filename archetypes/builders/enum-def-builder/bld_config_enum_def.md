---
kind: config
id: bld_config_enum_def
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: enum_def Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_enum_{slug}.md` | `p06_enum_publication_status.md` |
| Builder directory | kebab-case | `enum-def-builder/` |
| Frontmatter fields | snake_case | `descriptions`, `extensible`, `deprecated` |
| Enum slug | snake_case, lowercase, no hyphens | `publication_status`, `artifact_kind` |
| Value names | SCREAMING_SNAKE_CASE or lowercase — pick ONE, be consistent within an enum | `DRAFT` or `draft`, never mixed |
| GraphQL enum values | SCREAMING_SNAKE_CASE (required by GraphQL spec) | `DRAFT`, `PUBLISHED` |
| TypeScript union literals | lowercase string literals preferred | `"draft" \| "published"` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: all values within a single enum MUST use the same case convention.

## File Paths
- Output: `cex/P06_schema/examples/p06_enum_{slug}.md`
- Compiled: `cex/P06_schema/compiled/p06_enum_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)

## Value Count Guidelines
| Count | Signal |
|-------|--------|
| 1 | STOP — this is a constant, not an enum; use constant-builder |
| 2-5 | Ideal — tight domain with clear boundaries |
| 6-12 | Acceptable — complex domain; ensure all values are distinct |
| 13+ | Warning — consider splitting into sub-enums or using a taxonomy |

## Extensibility Rules
| extensible | Meaning | Version bump required to add value |
|------------|---------|-----------------------------------|
| false | Closed set — consumers may assume exhaustive match | YES — adding a value is a breaking change |
| true | Open set — consumers must handle unknown values | NO — new values are non-breaking |

## Deprecation Rules
| Rule | Detail |
|------|--------|
| Deprecated values MUST remain in `values` list | Removal is a breaking change |
| Deprecation reason MUST be documented | Note what to use instead |
| Removal only on major version bump | e.g., 1.x.x -> 2.0.0 |
| `deprecated: []` preferred over omitting field | Explicit empty set aids tooling |
