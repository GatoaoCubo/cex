---
id: p05_rf_builder_artifact
kind: response_format
pillar: P05
title: Response Format -- CEX Artifact
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [response-format, builder, N03]
tldr: Output format for all artifacts -- YAML frontmatter + Markdown body with open variables.
density_score: 0.88
---

# Response Format: CEX Artifact

## Structure

Every artifact follows:
1. YAML frontmatter between --- delimiters
2. Structured markdown body per builder output template

## Required Frontmatter Fields

| Field | Rule |
|-------|------|
| id | lowercase, underscored, pillar-prefixed |
| kind | must match kinds_meta.json entry |
| pillar | P01-P12 |
| title | descriptive, human-readable |
| version | semver (major.minor.patch) |
| created | ISO date |
| updated | ISO date |
| author | agent name or human |
| quality | float 0-10 or null |
| tags | lowercase list, max 10 |
| tldr | one sentence, max 120 chars |

## Body Rules

- Sections from bld_output_template for the kind
- Tables for structured data
- Lists for enumerable items
- No filler, no placeholder text
- Density >= 0.80
- Size <= max_bytes from kinds_meta.json
- Use {{open_variables}} for consumer-filled values

## Naming

File: {pillar_lower}_{kind}_{topic}.md
Compiled: {kind}_{topic}.yaml


## Response Format Constraints

Engineering outputs follow strict formatting rules to enable automated parsing:

- **Frontmatter mandatory**: every output starts with YAML frontmatter block
- **Machine-parseable sections**: key data in tables or YAML blocks, not prose
- **Deterministic structure**: heading hierarchy matches template exactly
- **Size bounds**: outputs stay within 1KB-50KB range; outliers trigger review

### Format Validation Pipeline

```yaml
# Post-generation validation
validation:
  frontmatter_check: strict
  heading_hierarchy: ordered
  table_parse: all_valid
  code_block_syntax: highlighted
  max_size_kb: 50
  min_size_kb: 1
```

| Format Element | Requirement | Failure Action |
|---------------|------------|----------------|
| YAML frontmatter | Valid YAML, required fields present | Block publication |
| Markdown headings | H2 > H3 ordering, no skips | Auto-fix if possible |
| Tables | Parseable, aligned pipes | Warn and flag |
| Code blocks | Language tag present | Auto-detect language |

