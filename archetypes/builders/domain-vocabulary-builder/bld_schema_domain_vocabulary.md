---
id: bld_schema_domain_vocabulary
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
quality: null
tags: [domain_vocabulary, schema, ubiquitous-language]
title: "Schema Domain Vocabulary"
---
# Schema: domain_vocabulary
## Frontmatter Fields (Required)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (dv_{context}_vocabulary) | YES | One per bounded context |
| kind | literal "domain_vocabulary" | YES | — |
| pillar | literal "P01" | YES | — |
| title | string | YES | "{Context} Domain Vocabulary" |
| version | semver | YES | Increment on term additions |
| quality | null | YES | Never self-score |
| bounded_context | string | YES | BC name this vocabulary governs |
| governed_agents | list[string] | YES | Agent IDs that must load this |
| term_count | integer | YES | Total active terms |
| tags | list[string] | YES | >= 3 tags |

## Terms Section Structure (Required in body)
```markdown
## Terms

### {TermName}
| Field | Value |
|-------|-------|
| definition | {canonical definition} |
| industry_standard | {Evans/NIST/ISO ref or "CEX-internal"} |
| anti_patterns | [{what NOT to call it}] |
| status | proposed|active|deprecated |
| replaces | {old_term or null} |
| replaced_by | {new_term or null} |
```

## ID Pattern
`^dv_[a-z][a-z0-9_]+_vocabulary$`
Example: dv_sales_vocabulary, dv_billing_vocabulary, dv_cex_core_vocabulary

## Constraints
- max_bytes: 5120
- min 3 active terms in terms section
- each term must have definition + status
- deprecated terms must have replaced_by
