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
