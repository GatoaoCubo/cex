---
kind: config
id: bld_config_glossary_entry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: glossary_entry Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_gl_{term_slug}.yaml` | `p01_gl_kind.yaml` |
| Builder directory | kebab-case | `glossary-entry-builder/` |
| Frontmatter fields | snake_case | `related_terms`, `domain_specific` |
| Term slugs | snake_case, lowercase | `kind`, `knowledge_card`, `quality_gate` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P01_knowledge/examples/p01_gl_{term_slug}.yaml`
- Compiled: `cex/P01_knowledge/compiled/p01_gl_{term_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 512 bytes
- Total: ~800 bytes including frontmatter
- Definition: max 3 lines
- Density: >= 0.80

## Definition Rules
| Rule | Enforcement |
|------|-------------|
| Max 3 lines | HARD (H07) |
| No filler words | SOFT (S07) |
| Concrete, not abstract | SOFT (S05) |
| Include at least one example in definition | SOFT (S04) |

## Term Conventions
- Terms are lowercase unless proper noun
- Multi-word terms use snake_case in id, natural case in term field
- Abbreviations documented in abbreviation field
- Cross-pillar terms include pillar reference in disambiguation
