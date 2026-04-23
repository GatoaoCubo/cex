---
kind: instruction
id: bld_instruction_personality
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for personality
pattern: 3-phase pipeline (design -> compose -> validate)
quality: 8.9
title: "Instruction: personality-builder"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, instruction, hermes_origin, hot_swap, persona]
tldr: "3-phase pipeline: design voice profile + compose persona spec + validate boundaries vs agent/agent_profile/system_prompt."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_enum_def
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_context_doc
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_env_config
---

# Instructions: How to Produce a personality

## Phase 1: DESIGN

1. Identify the persona name: what is this personality called? (e.g., "researcher", "coach", "casual")
2. Determine voice register: formal (precise, structured) | casual (friendly, approachable) | technical (jargon-rich) | playful (wit-forward)
3. Set verbosity: terse (short answers) | balanced (default) | verbose (elaborate explanations)
4. Calibrate humor: off (zero levity) | dry (subtle irony) | warm (genuine friendliness)
5. Select 3-5 core values: what does this persona prioritize? (e.g., accuracy, empathy, brevity, creativity, rigor)
6. Draft 3+ tone examples: real sample phrases this persona would say
7. List 3+ anti-patterns: phrases this persona would NEVER say (wrong register, wrong tone)
8. Set activation and deactivation cues: default is `/personality {{name}}` and `/personality default`
9. Confirm hot_swap_compatible: true (default) unless the persona requires full agent reload
10. Confirm name slug: snake_case or hyphen, lowercase, <= 30 chars

## Phase 2: COMPOSE

1. Read bld_schema_personality.md -- source of truth for all fields
2. Read bld_output_template_personality.md -- fill template variables following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null -- never self-score)
4. Write voice section: 3-column table (dimension, value, notes)
5. Write values section: bullet list of 3-5 core values with 1-sentence rationale each
6. Write tone_examples section: numbered list of 3+ verbatim sample phrases with context
7. Write anti_patterns section: numbered list of 3+ forbidden phrases with reason
8. Write activation section: activation_cue, deactivation_cue, hot_swap_compatible
9. Write related personalities section: sibling personas and contrast notes
10. Verify body <= 3072 bytes
11. Verify id matches `^per_[a-z][a-z0-9_-]+$`

## Phase 3: VALIDATE

1. Check bld_quality_gate_personality.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `per_` prefix
4. Confirm kind == personality
5. Confirm voice.register is one of: formal, casual, technical, playful
6. Confirm voice.verbosity is one of: terse, balanced, verbose
7. Confirm voice.humor is one of: off, dry, warm
8. Confirm values list has 3-5 items
9. Confirm tone_examples list has >= 3 items
10. Confirm anti_patterns list has >= 3 items
11. HARD gates: frontmatter valid, id pattern matches, voice fully specified, examples present
12. SOFT gates: score against quality gate -- target >= 8.0 before outputting
13. Cross-check kind boundaries:
    - Does NOT define tools or capabilities (that is agent)
    - Does NOT configure runtime parameters (that is agent_profile)
    - Does NOT contain a full system prompt text (that is system_prompt)
    - Does NOT define routing rules (that is lens)
14. Revise if score < 8.0 -- most common fix: missing anti_patterns or tone_examples below 3


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_enum_def]] | sibling | 0.43 |
| [[bld_instruction_output_validator]] | sibling | 0.42 |
| [[bld_instruction_retriever_config]] | sibling | 0.42 |
| [[bld_instruction_memory_scope]] | sibling | 0.41 |
| [[bld_instruction_context_doc]] | sibling | 0.41 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.40 |
| [[bld_instruction_prompt_version]] | sibling | 0.40 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.40 |
| [[bld_instruction_constraint_spec]] | sibling | 0.39 |
| [[bld_instruction_env_config]] | sibling | 0.37 |
