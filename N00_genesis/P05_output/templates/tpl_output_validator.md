---
id: p05_output_validator
kind: output_validator
pillar: P05
version: 1.0.0
title: "Template — Output Validator"
tags: [template, validator, output, quality, assertion]
tldr: "Validates LLM output against schema, content rules, and safety constraints. Defines validation pipeline: parse → schema check → content rules → safety filters."
quality: 9.2
updated: "2026-04-07"
domain: "output formatting"
author: n03_builder
created: "2026-04-07"
density_score: 1.0
---

# Output Validator: [NAME]

## Purpose
Ensures LLM-generated output meets structural and content requirements before delivery.

## Validation Pipeline
```
Raw Output → Parse(format) → Schema(fields) → Content(rules) → Safety(filters) → Accept/Reject
```

## Schema Validation

| Field | Type | Required | Constraint |
|-------|------|----------|-----------|
| id | string | yes | matches `^[a-z][a-z0-9_]+$` |
| kind | string | yes | in known_kinds list |
| quality | null | yes | must be null, never a number |
| body | string | yes | ≥ 100 chars, ≤ max_bytes |

## Content Rules
1. **No hallucinated citations**: Every `[source]` must map to a real URL
2. **No placeholder text**: Reject if contains `{{`, `PENDING`, `NOTE`
3. **Language consistency**: Body language matches frontmatter language
4. **Structure**: At least 3 `##` sections in body

## Safety Filters
1. **PII detection**: Flag emails, phone numbers, SSNs
2. **Prompt injection**: Detect "ignore previous instructions" patterns
3. **Harmful content**: Apply content policy (no violence, illegal advice)

## Validation Result
```yaml
result:
  valid: [true | false]
  errors: [{field, rule, message}]
  warnings: [{field, rule, message}]
  score: [0.0-1.0]  # Confidence in output quality
```

## Quality Gate
1. [ ] Schema validation covers all required fields
2. [ ] At least 2 content rules defined
3. [ ] Safety filters configured
4. [ ] Result includes errors AND warnings (not just pass/fail)

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `output_validator` |
| Pillar | P05 |
| Domain | output formatting |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

# Output Validator: [NAME]

## Purpose
Ensures LLM-generated output meets structural and content requirements before delivery.

## Validation Pipeline
```
Raw Output → Parse(format) → Schema(fields) → Content(rules) → Safety(filters) → Accept/Reject
```

## Schema Validation

| Field | Type | Required | Constraint |
|-------|------|----------|-----------|
| id | string | yes | matches `^[a-z][a-z0-9_]+$` |
| kind | string | yes | in known_kinds list |
| quality | null | yes | must be null, never a number |
| body | string | yes | ≥ 100 chars, ≤ max_bytes |

## Content Rules
1. **No hallucinated citations**: Every `[source]` must map to a real URL
2. **No placeholder text**: Reject if contains `{{`, `PENDING`, `NOTE`
3. **Language consistency**: Body language matches frontmatter language
4. **Structure**: At least 3 `##` sections in body

## Safety Filters
1. **PII detection**: Flag emails, phone numbers, SSNs
2. **Prompt injection**: Detect "ignore previous instructions" patterns
3. **Harmful content**: Apply content policy (no violence, illegal advice)

## Validation Result
```yaml
result:
  valid: [true | false]
  errors: [{field, rule, message}]
  warnings: [{field, rule, message}]
  score: [0.0-1.0]  # Confidence in output quality
```

## Quality Gate
1. [ ] Schema validation covers all required fields
2. [ ] At least 2 content rules defined
3. [ ] Safety filters configured
4. [ ] Result includes errors AND warnings (not just pass/fail)

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `output_validator` |
| Pillar | P05 |
| Domain | output formatting |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

## Quality Enforcement

This artifact follows the CEX 3-layer quality model. Structural scoring
validates frontmatter completeness, content depth, and format diversity.
Rubric scoring checks dimension-specific criteria from the quality gate.
Semantic scoring provides LLM-based evaluation when layers one and two
average 8.5 or above.

All artifacts target quality 9.0 or higher. Below 8.0 triggers a rebuild.
Between 8.0 and 9.0, the evolve pipeline applies targeted improvements.
