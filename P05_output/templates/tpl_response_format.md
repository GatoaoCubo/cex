---
id: tpl_response_format
kind: response_format
pillar: P05
version: 1.0.0
title: "Template — Response Format"
tags: [template, response, format, output, structure]
tldr: "Defines how an agent structures its output. Controls format type (JSON, markdown, structured), required fields, max length, and validation rules."
quality: 9.0
updated: "2026-04-07"
domain: "output formatting"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
---

# Response Format: [FORMAT_NAME]

## Purpose
[WHAT output this format governs — API responses, agent replies, artifact content]

## Format Specification
```yaml
type: [json | markdown | structured_text | yaml]
schema:
  required: [status, data]
  optional: [metadata, errors]
max_tokens: [500 | 1000 | 4000]
encoding: utf-8
```

## Structure

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | yes | "success" \| "error" \| "partial" |
| data | object | yes | Primary response payload |
| metadata | object | no | Timing, model, token count |
| errors | array | no | List of error objects |

## Format Examples

### JSON Response
```json
{
  "status": "success",
  "data": { "result": "...", "score": 8.8 },
  "metadata": { "model": "sonnet", "tokens": 450, "latency_ms": 1200 }
}
```

### Markdown Response
```markdown
## Result
[CONTENT]

## Sources
- [SOURCE_1]
- [SOURCE_2]

## Confidence
[HIGH | MEDIUM | LOW] — [REASONING]
```

## Validation Rules
- **Max length**: Truncate at `max_tokens`, add `[truncated]` marker
- **Required fields**: Reject response if missing (retry)
- **Type checking**: Ensure field types match schema
- **Encoding**: Must be valid UTF-8 (no surrogate pairs)

## Content Policy
- **No hallucinated citations**: All sources must be retrievable
- **No PII leakage**: Strip emails, phone numbers unless explicitly requested
- **Language**: Match input language (default: same as query)

## Quality Gate
- [ ] Format type specified (json/markdown/yaml)
- [ ] Required fields listed
- [ ] Max length defined
- [ ] At least 1 format example provided
