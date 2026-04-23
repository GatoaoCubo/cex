---
quality: 7.6
quality: 7.3
id: bld_schema_domain_vocabulary
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
tags: [domain_vocabulary, schema, ubiquitous-language]
title: "Schema Domain Vocabulary"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_sandbox_spec
  - bld_schema_eval_metric
  - bld_schema_search_strategy
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

## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.61 |
| [[bld_schema_benchmark_suite]] | related | 0.60 |
| [[bld_schema_usage_report]] | related | 0.59 |
| [[bld_schema_integration_guide]] | related | 0.58 |
| [[bld_schema_quickstart_guide]] | related | 0.57 |
| [[bld_schema_dataset_card]] | related | 0.57 |
| [[bld_schema_pitch_deck]] | related | 0.57 |
| [[bld_schema_sandbox_spec]] | related | 0.55 |
| [[bld_schema_eval_metric]] | related | 0.55 |
| [[bld_schema_search_strategy]] | related | 0.55 |
