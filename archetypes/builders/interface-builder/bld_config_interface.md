---
kind: config
id: bld_config_interface
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: interface Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_iface_{contract_slug}.yaml` | `p06_iface_research_to_marketing.yaml` |
| Builder directory | kebab-case | `interface-builder/` |
| Frontmatter fields | snake_case | `backward_compatible`, `example_payloads` |
| Contract slugs | snake_case, lowercase | `research_to_marketing`, `brain_search` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P06_schema/examples/p06_iface_{contract_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_iface_{contract_slug}.json`

## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80

## Method Contract Rules
| Rule | Enforcement |
|------|-------------|
| Each method has name | HARD (H07) |
| Each method has input type | HARD (H07) |
| Each method has output type | HARD (H07) |
| Each method has description | SOFT (S05) |
| Methods list >= 1 entry | HARD (H07) |

## Versioning Policy
- New interfaces start at 1.0.0
- Breaking changes: bump major, set backward_compatible: false
- Additive methods: bump minor, backward_compatible: true
- Fix/doc changes: bump patch
