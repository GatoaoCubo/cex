---
id: p01_kc_test_automation
kind: knowledge_card
type: domain
pillar: P01
title: "Test Automation for LLM Agent Systems"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: operations
quality: 9.0
tags: [testing, automation, pytest, tdd, quality-assurance]
tldr: "Test LLM systems at 3 levels: unit (tool functions), integration (pipeline chains), behavioral (output quality). pytest as universal runner."
when_to_use: "Establishing test coverage for agent tools and workflows"
keywords: [testing, pytest, tdd, unit-test, integration-test, behavioral-test]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_qa_validation
  - p01_kc_input_hydration
  - p01_kc_schema_validation
  - p01_kc_spawn_patterns
  - p01_kc_context_scoping
  - p01_kc_output_formatting
  - p01_kc_workflow_orchestration
  - p01_kc_eval_testing
  - p01_kc_governance_patterns
  - ex_knowledge_card_rag_fundamentals
---

# Test Automation for LLM Systems

## Three Levels

| Level | Tests | What | Speed |
|-------|-------|------|-------|
| Unit | Tool functions, parsers, validators | Deterministic logic | ms |
| Integration | Pipeline chains, file I/O, compilation | Component interaction | seconds |
| Behavioral | LLM output quality, format compliance | Non-deterministic | minutes |

## Testing Non-Deterministic Output
LLMs don't produce identical output twice. Test PROPERTIES, not exact strings:
- Output contains required sections
- JSON is valid / YAML parses
- Length within range
- Required fields present
- Quality score above threshold

## CEX Test Architecture
- `_tools/tests/` — pytest suite (400+ tests)
- Unit: tool functions (brand_validate, cex_intent, etc.)
- Integration: E2E pipeline (brand ingest → validate → propagate → audit)
- Structural: doctor (105 builders), compile (265 files)
- Pre-commit: `cex_hooks.py` validates staged .md files

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_test_automation`
- **Tags**: [testing, automation, pytest, tdd, quality-assurance]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_test_automation`
- **Tags**: [testing, automation, pytest, tdd, quality-assurance]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_qa_validation]] | sibling | 0.44 |
| [[p01_kc_input_hydration]] | sibling | 0.34 |
| [[p01_kc_schema_validation]] | sibling | 0.32 |
| [[p01_kc_spawn_patterns]] | sibling | 0.32 |
| [[p01_kc_context_scoping]] | sibling | 0.32 |
| [[p01_kc_output_formatting]] | sibling | 0.31 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.30 |
| [[p01_kc_eval_testing]] | sibling | 0.29 |
| [[p01_kc_governance_patterns]] | sibling | 0.28 |
| [[ex_knowledge_card_rag_fundamentals]] | sibling | 0.24 |
