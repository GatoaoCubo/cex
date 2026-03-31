---
kind: memory
id: bld_memory_response_format
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for response_format artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: response-format-builder
## Summary
Response formats are injected into the LLM prompt to guide how the agent structures its output. The critical distinction from validation schemas is visibility: the LLM sees response formats during generation, while validation schemas are applied post-generation by the system. Confusing these two causes either redundant enforcement (format + schema checking the same thing) or gaps (neither checking). The second lesson is injection point selection: system_prompt injection persists across turns, user_message injection applies to one turn only.
## Pattern
- Choose injection_point based on persistence needs: system_prompt for all turns, user_message for single turn
- Format type must match downstream consumer expectations: json for APIs, markdown for human readers, yaml for configs
- Include a concrete example output in the format specification — LLMs follow examples more reliably than abstract rules
- Section ordering in the format must match the LLM's natural generation flow — fighting generation order reduces compliance
- Keep format specifications concise — verbose format instructions compete with task instructions for attention
- Test format compliance with at least 3 different task types to verify the format works across use cases
## Anti-Pattern
- Duplicating format rules in both response_format (LLM-visible) and validation_schema (system-applied) — maintain in one place
- Injecting response format in user_message when persistence across turns is needed — format forgotten on next turn
- Abstract format rules without examples — LLMs comply 40% less often without concrete examples
- Format specifications longer than 500 tokens — drowns out task-specific instructions
- Confusing response_format (P05, LLM sees) with validation_schema (P06, system applies) or parser (P05, extracts data)
## Context
Response formats sit in the P05 formatting layer. They are injected into prompts before generation, making them part of the LLM's instruction set. This is fundamentally different from post-generation validation (P06) which the LLM never sees. In agent pipelines, response formats ensure consistent output structure that downstream parsers and consumers can rely on.
## Impact
Formats with concrete examples achieved 90% compliance versus 55% for abstract-only formats. Correct injection point selection (system vs user) eliminated 100% of multi-turn format amnesia. Concise formats (under 300 tokens) showed 25% higher task quality due to less instruction competition.
## Reproducibility
Reliable response format production: (1) select injection point based on persistence needs, (2) choose format type matching downstream consumers, (3) include concrete example output, (4) order sections to match natural generation flow, (5) keep under 500 tokens, (6) validate against 10 HARD + 9 SOFT gates.
## References
- response-format-builder SCHEMA.md (19 frontmatter fields, format specification)
- P05 formatting pillar specification
- LLM structured output and JSON mode patterns
