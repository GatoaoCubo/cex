---
kind: collaboration
id: bld_collaboration_edit_format
pillar: P12
llm_function: COLLABORATE
purpose: How edit_format-builder works in crews with other builders
quality: 9.0
title: "Collaboration Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, collaboration]
tldr: "How edit_format-builder works in crews with other builders"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p03_sp_edit_format_builder
  - bld_collaboration_response_format
  - bld_architecture_edit_format
  - bld_memory_response_format
  - p03_ins_response_format
  - response-format-builder
  - bld_tools_edit_format
  - bld_architecture_response_format
  - bld_examples_edit_format
  - bld_collaboration_system_prompt
---

## Crew Role

This ISO specifies an edit format: how diffs or patches are expressed and applied.

Defines the wire format specification that LLMs use to express file edits. Owns the syntax
contract between LLM output and host application tools. Receives format requirements from
upstream orchestration; produces format specs consumed by LLM system prompts, host appliers,
and validation pipelines.

## Receives From

| Builder | What | Format |
|---------|------|--------|
| diff_strategy_builder | Matching strategy constraints (affects which format_types are safe) | KC reference |
| code_executor_builder | Tool compatibility requirements (which formats the executor can apply) | config |
| prompt_template_builder | LLM instruction context (how format spec is injected into prompts) | prompt |
| agent_card_builder | Agent capability declaration (which formats the agent supports) | YAML |

## Produces For

| Builder | What | Format |
|---------|------|--------|
| system_prompt_builder | Format rules injected into LLM system prompt | Markdown section |
| diff_strategy_builder | Declared format_type informs which matching strategy is needed | reference |
| code_executor_builder | Format spec enables applier to validate and execute edits | spec |
| output_validator_builder | Validation rules for checking LLM edit output conformance | rules |
| prompt_template_builder | Compatible_tools list and syntax examples for prompt injection | data |

## Boundary

Does NOT own:
- Diff algorithm selection or matching logic (diff_strategy_builder)
- Code style, indentation, formatting of changed content (formatter_builder)
- Conflict resolution between concurrent edits (diff_strategy_builder)
- Semantic analysis of whether the edit is correct (code_executor_builder)
- File system operations, git commits, backup (operations layer)

Owns:
- The exact delimiter/marker syntax for each format_type
- Application rules (what MUST happen when applying each format)
- Validation rules (what constitutes a conforming LLM response)
- Compatible tools mapping

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_edit_format_builder]] | upstream | 0.39 |
| [[bld_collaboration_response_format]] | sibling | 0.36 |
| [[bld_architecture_edit_format]] | upstream | 0.34 |
| [[bld_memory_response_format]] | upstream | 0.33 |
| [[p03_ins_response_format]] | upstream | 0.33 |
| [[response-format-builder]] | upstream | 0.31 |
| [[bld_tools_edit_format]] | upstream | 0.29 |
| [[bld_architecture_response_format]] | upstream | 0.27 |
| [[bld_examples_edit_format]] | upstream | 0.27 |
| [[bld_collaboration_system_prompt]] | sibling | 0.25 |
