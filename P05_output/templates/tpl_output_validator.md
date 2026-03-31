---
id: p05_output_validator
kind: output_validator
pillar: P05
version: 1.0.0
title: "Template — Output Validator"
tags: [template, validator, output, quality, assertion]
tldr: "Validates LLM output against schema, content rules, and safety constraints. Defines validation pipeline: parse → schema check → content rules → safety filters."
quality: null
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
- **No hallucinated citations**: Every `[source]` must map to a real URL
- **No placeholder text**: Reject if contains `{{`, `TODO`, `FIXME`
- **Language consistency**: Body language matches frontmatter language
- **Structure**: At least 3 `##` sections in body

## Safety Filters
- **PII detection**: Flag emails, phone numbers, SSNs
- **Prompt injection**: Detect "ignore previous instructions" patterns
- **Harmful content**: Apply content policy (no violence, illegal advice)

## Validation Result
```yaml
result:
  valid: [true | false]
  errors: [{field, rule, message}]
  warnings: [{field, rule, message}]
  score: [0.0-1.0]  # Confidence in output quality
```

## Quality Gate
- [ ] Schema validation covers all required fields
- [ ] At least 2 content rules defined
- [ ] Safety filters configured
- [ ] Result includes errors AND warnings (not just pass/fail)
