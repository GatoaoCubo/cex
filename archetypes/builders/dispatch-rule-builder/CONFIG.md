---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: dispatch_rule Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_dr_{scope}.yaml` | `p12_dr_research.yaml` |
| Builder directory | kebab-case | `dispatch-rule-builder/` |
| Frontmatter fields | snake_case | `confidence_threshold`, `load_balance` |
| `id` field | `p12_dr_` prefix + snake_case scope | `p12_dr_build`, `p12_dr_marketing` |
| `satellite` values | lowercase slug | `edison`, `shaka`, `atlas` |
| `model` values | lowercase enum | `sonnet`, `opus`, `haiku`, `flash` |
| `scope` values | lowercase slug, no spaces | `build`, `research`, `orchestration` |
| `keywords` items | lowercase, no punctuation | `build`, `codigo`, `implementar` |

Rule: use `.yaml` only for this builder (frontmatter yaml + md body hybrid).

## File Paths
- Output: `cex/P12_orchestration/compiled/p12_dr_{scope}.yaml`
- Human reference: `cex/P12_orchestration/examples/p12_dr_{scope}.md`
- Template: `cex/P12_orchestration/templates/tpl_dispatch_rule.md`

## Size Limits
- Preferred file size: <= 1024 bytes
- Absolute max: 3072 bytes
- Body commentary should remain concise; routing logic is frontmatter only

## Field Restrictions
- `id` MUST match `^p12_dr_[a-z][a-z0-9_]+$`
- `quality` MUST be literal `null` — never a score at authoring time
- `priority` MUST be integer 1-10 (not float, not string)
- `confidence_threshold` MUST be float 0.0-1.0 (not percentage)
- `fallback` MUST differ from `satellite`
- `keywords` MUST be a list, even for a single keyword
- `model` MUST be one of: `sonnet`, `opus`, `haiku`, `flash`
- `routing_strategy` MUST be one of: `keyword_match`, `semantic`, `hybrid`

## Boundary Restrictions
- No task lists, scope fences, or commit instructions in the file
- No runtime status fields (`status`, `quality_score`, `timestamp`)
- No multi-step workflow graphs or dependency chains
- No hardcoded brand names, product names, or user-specific tokens in keywords
- `conditions` object must use generic keys; no runtime state references
