---
id: p01_kc_output_formatting
kind: knowledge_card
type: domain
pillar: P01
title: Output Formatting -- Formatters, Naming, Response Structure
version: 1.0.0
created: '2026-03-29'
author: orchestrator
domain: output
origin: manual
quality: 9.0
tags:
- formatter
- naming
- response-format
- structured-output
tldr: 'Patterns for formatting LLM output: markdown/JSON formatters, naming conventions, response structure'
when_to_use: Configuring how LLM output is structured and named
feeds_kinds:
- formatter
- naming_rule
- response_format
density_score: 0.85
updated: "2026-04-07"
---

## Quick Reference
| Pattern | Framework | CEX Kind |
|---------|-----------|----------|
| StrOutputParser | LangChain | parser |
| JsonOutputParser | LangChain | response_format |
| response_format: json_object | OpenAI | response_format |
| Naming conventions | All | naming_rule |

## Key Concepts
- **Formatter**: transforms raw output into structured format (markdown, HTML, XML)
- **Naming Rule**: enforces consistent naming (snake_case, kebab-case, prefixes)
- **Response Format**: constrains decoder to produce specific structure (JSON mode)

## Patterns
| Trigger | Action |
|---------|--------|
| Output needs structure | Apply response_format |
| Output for humans | Apply formatter |
| Naming inconsistent | Apply naming_rule |

## Anti-Patterns
- Parsing free-text with regex instead of structured output
- Mixing formatting and validation (formatter != validator)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_output_formatting`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_output_formatting`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |
