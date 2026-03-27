---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for glossary_entry
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: glossary_entry

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_gl_{term}) | YES | - | Namespace compliance |
| kind | literal "glossary_entry" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| term | string | YES | - | The term being defined |
| definition | string, max 3 lines | YES | - | Concise definition |
| synonyms | list[string], len >= 1 | YES | - | At least one synonym |
| abbreviation | string or null | REC | null | Short form if exists |
| domain | string | YES | - | Where term is used |
| domain_specific | string or null | REC | null | CEX-specific meaning |
| context | string | REC | - | Where term appears |
| disambiguation | string or null | REC | null | Clarify vs similar terms |
| related_terms | list[string] | REC | [] | Cross-references |
| usage | string | REC | - | How term is used in practice |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "glossary" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern
Regex: `^p01_gl_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Definition` — the concise definition (max 3 lines)
2. `## Usage` — where and how the term appears
3. `## Disambiguation` — clarification vs similar terms (if needed)
4. `## Related Terms` — cross-references to other glossary entries

## Constraints
- max_bytes: 512 (body only)
- max_definition_lines: 3
- naming: p01_gl_{term}.yaml
- machine_format: yaml
- id == filename stem
- definition MUST be <= 3 lines
- synonyms MUST have at least 1 entry
- quality: null always
- glossary_entry is CONCISE — no deep analysis (that is knowledge_card)
