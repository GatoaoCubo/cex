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
related:
  - p01_kc_schema_validation
  - p01_kc_qa_validation
  - p01_kc_input_hydration
  - p01_kc_spawn_patterns
  - p01_kc_context_scoping
  - p01_kc_workflow_orchestration
  - p05_fmt_artifact_creation_report
  - p01_kc_governance_patterns
  - p01_kc_test_automation
  - bld_examples_response_format
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_schema_validation]] | sibling | 0.37 |
| [[p01_kc_qa_validation]] | sibling | 0.36 |
| [[p01_kc_input_hydration]] | sibling | 0.35 |
| [[p01_kc_spawn_patterns]] | sibling | 0.33 |
| [[p01_kc_context_scoping]] | sibling | 0.33 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.32 |
| [[p05_fmt_artifact_creation_report]] | downstream | 0.31 |
| [[p01_kc_governance_patterns]] | sibling | 0.30 |
| [[p01_kc_test_automation]] | sibling | 0.30 |
| [[bld_examples_response_format]] | downstream | 0.29 |
