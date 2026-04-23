---
kind: instruction
id: bld_instruction_red_team_eval
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for red_team_eval
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - p11_qg_red_team_eval
  - bld_instruction_handoff_protocol
  - bld_instruction_enum_def
  - bld_instruction_constraint_spec
  - bld_instruction_eval_dataset
---

# Instructions: How to Produce a red_team_eval
## Phase 1: RESEARCH
1. Identify the target: which specific agent, system prompt, or pipeline component is under test
2. Map the threat model: what could go wrong if this system is attacked? What data does it have access to?
3. Select attack_types from the approved enum (at minimum 2; prefer 3-5 for coverage)
4. Map each attack_type to its OWASP LLM Top 10 reference (LLM01-LLM10)
5. Determine framework: Promptfoo (YAML config), Garak (CLI probes), DeepEval (Python), Patronus (API), or costm
6. Define pass_criteria as observable model behavior — what does "safe" look like in a response?
7. Assess severity: critical/high/medium/low based on potential harm if attacks succeed
8. Check for existing red_team_eval artifacts to avoid duplicates
9. Confirm slug for id: snake_case, lowercase, no hyphens, prefix p07_rt_
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields and attack_type enum values
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what is being tested, threat model summary, who runs this eval and when
5. Write Attack Scenarios section: for each attack_type, provide:
   - Pattern description (placeholder-based, never real exploit strings)
   - Expected safe model response (observable behavior)
   - OWASP LLM reference
   - Framework-specific config snippet if applicable
6. Write Pass Criteria section: explicit, measurable definition of safe behavior per attack category
7. Write Configuration section: framework setup, env vars, how to execute, expected output format
8. Verify body <= 2048 bytes
9. Verify id matches `^p07_rt_[a-z][a-z0-9_]+$`
10. Verify attack_types in frontmatter match categories documented in Attack Scenarios section
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p07_rt_` prefix and pattern
4. Confirm kind == red_team_eval
5. Confirm attack_types list is non-empty and all values are from approved enum
6. Confirm target is specific (not "the system" or "the model")
7. Confirm pass_criteria is observable and measurable
8. Confirm no real PII or actual exploit payloads in body
9. HARD gates: frontmatter valid, id pattern matches, attack_types declared, pass_criteria offined, target named
10. SOFT gates: score against QUALITY_GATES.md
11. Cross-check boundary: is this testing BEFORE deployment (red_team_eval) or enforcing AT runtime (guardrail)? Is this adversarial (red_team_eval) or functional (e2e_eval)? Is this isolated unit logic (unit_eval)?
12. Revise if score < 8.0 before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_output_validator]] | sibling | 0.44 |
| [[bld_instruction_retriever_config]] | sibling | 0.43 |
| [[bld_instruction_memory_scope]] | sibling | 0.43 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.42 |
| [[bld_instruction_prompt_version]] | sibling | 0.42 |
| [[p11_qg_red_team_eval]] | downstream | 0.41 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.41 |
| [[bld_instruction_enum_def]] | sibling | 0.41 |
| [[bld_instruction_constraint_spec]] | sibling | 0.41 |
| [[bld_instruction_eval_dataset]] | sibling | 0.40 |
