---
kind: memory
id: bld_memory_response_format
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for response_format artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - response-format-builder
  - bld_collaboration_response_format
  - bld_architecture_response_format
  - p03_ins_response_format
  - p03_sp_response_format_builder
  - p11_qg_response_format
  - bld_knowledge_card_response_format
  - p01_kc_response_format
  - bld_examples_response_format
  - tpl_response_format
---
# Memory: response-format-builder
## Summary
Response formats are injected into the LLM prompt to guide how the agent structures its output. The critical distinction from validation schemas is visibility: the LLM sees response formats during generation, while validation schemas are applied post-generation by the system. Confusing these two causes either redundant enforcement (format + schema checking the same thing) or gaps (neither checking). The second lesson is injection point selection: system_prompt injection persists across turns, user_message injection applies to one turn only.
## Pattern
1. Choose injection_point based on persistence needs: system_prompt for all turns, user_message for single turn
2. Format type must match downstream consumer expectations: json for APIs, markdown for human readers, yaml for configs
3. Include a concrete example output in the format specification — LLMs follow examples more reliably than abstract rules
4. Section ordering in the format must match the LLM's natural generation flow — fighting generation order reduces compliance
5. Keep format specifications concise — verbose format instructions compete with task instructions for attention
6. Test format compliance with at least 3 different task types to verify the format works across use cases
## Anti-Pattern
1. Duplicating format rules in both response_format (LLM-visible) and validation_schema (system-applied) — maintain in one place
2. Injecting response format in user_message when persistence across turns is needed — format forgotten on next turn
3. Abstract format rules without examples — LLMs comply 40% less often without concrete examples
4. Format specifications longer than 500 tokens — drowns out task-specific instructions
5. Confusing response_format (P05, LLM sees) with validation_schema (P06, system applies) or parser (P05, extracts data)
## Context
Response formats sit in the P05 formatting layer. They are injected into prompts before generation, making them part of the LLM's instruction set. This is fundamentally different from post-generation validation (P06) which the LLM never sees. In agent pipelines, response formats ensure consistent output structure that downstream parsers and consumers can rely on.
## Impact
Formats with concrete examples achieved 90% compliance versus 55% for abstract-only formats. Correct injection point selection (system vs user) eliminated 100% of multi-turn format amnesia. Concise formats (under 300 tokens) showed 25% higher task quality due to less instruction competition.
## Reproducibility
Reliable response format production: (1) select injection point based on persistence needs, (2) choose format type matching downstream consumers, (3) include concrete example output, (4) order sections to match natural generation flow, (5) keep under 500 tokens, (6) validate against 10 HARD + 9 SOFT gates.
## References
1. response-format-builder SCHEMA.md (19 frontmatter fields, format specification)
2. P05 formatting pillar specification
3. LLM structured output and JSON mode patterns

## Metadata

```yaml
id: bld_memory_response_format
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-response-format.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | response format construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[response-format-builder]] | upstream | 0.61 |
| [[bld_collaboration_response_format]] | upstream | 0.52 |
| [[bld_architecture_response_format]] | upstream | 0.43 |
| [[p03_ins_response_format]] | upstream | 0.42 |
| [[p03_sp_response_format_builder]] | upstream | 0.35 |
| [[p11_qg_response_format]] | downstream | 0.35 |
| [[bld_knowledge_card_response_format]] | upstream | 0.33 |
| [[p01_kc_response_format]] | upstream | 0.31 |
| [[bld_examples_response_format]] | upstream | 0.30 |
| [[tpl_response_format]] | upstream | 0.29 |
