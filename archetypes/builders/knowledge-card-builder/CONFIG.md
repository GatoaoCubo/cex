---
lp: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: knowledge_card Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_kc_{topic_slug}.md` | `p01_kc_rag_fundamentals.md` |
| Builder directory | kebab-case | `knowledge-card-builder/` |
| Frontmatter fields | snake_case | `density_score`, `when_to_use` |
| Topic slug | lowercase, underscores, no spaces | `hybrid_search`, `prompt_caching` |
| YAML companion | `p01_kc_{topic_slug}.yaml` | `p01_kc_rag_fundamentals.yaml` |

Rule: id MUST equal filename stem (H02 gate checks this).

## File Paths
- Output: `cex/P01_knowledge/examples/p01_kc_{topic_slug}.md`
- Compiled: `cex/P01_knowledge/compiled/p01_kc_{topic_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: 200-5120 bytes (H08 gate)
- Total: max 5120 bytes
- Density: >= 0.80
- Bullets: max 80 chars each (S10 gate)
- Sections: min 3 non-empty lines each (S08 gate)
- Min sections: 4 (S06 gate)

## Tags Convention
- Always list, never string-in-list
- Min 3 tags
- Lowercase, underscores for multi-word
- Include domain tag + 2 topic-specific tags minimum

## Frontmatter Quoting
- Strings: quoted (`"value"`)
- Numbers: unquoted (`0.92`)
- Booleans: unquoted (`true`/`false`)
- null: unquoted (`null`)
- Lists: bracket syntax (`[tag1, tag2]`) or YAML list syntax

## Forbidden Content
- Internal paths: `records/`, `.claude/`, `/home/` (H09 gate)
- Self-reference: "this document", "this KC" (S02 gate)
- Filler phrases: "in summary", "it is worth noting" (S09 gate)
- Author STELLA (H10 gate — STELLA orchestrates, never authors)
