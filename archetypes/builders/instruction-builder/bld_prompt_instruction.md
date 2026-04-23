---
kind: instruction
id: bld_instruction_instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for instruction
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_input_schema
  - bld_instruction_action_prompt
  - bld_instruction_context_doc
  - bld_schema_instruction
  - bld_instruction_golden_test
  - bld_instruction_output_validator
  - bld_knowledge_card_instruction
  - bld_instruction_handoff
  - bld_instruction_handoff_protocol
  - bld_instruction_memory_scope
---

# Instructions: How to Produce an instruction
## Phase 1: RESEARCH
1. Identify the task: state exactly what must happen, who executes it, and in what context
2. Determine the executor: name the agent or role that will follow this recipe
3. List prerequisites — each must be verifiable ("Python 3.10+ installed" not "environment ready")
4. Define the input contract: every variable the executor receives, with type and required/optional status
5. Define the output contract: what the executor produces and in what format
6. Assess complexity to choose phase count: 3 phases for simple tasks, 4-5 for multi-stage operations
7. Check existing instructions via brain_query [IF MCP] for the same task — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 15 required fields + 7 recommended fields (null is acceptable for recommended)
4. Set quality: null — never self-score
5. Write the Context section (15-20% of doc): background, input/output contracts, every $variable defined with type and required/optional status
6. Write the Phases section (40-50% of doc): 3-5 phases following the Analyze -> Generate -> Validate pattern; each phase is atomic with one primary action; include pseudocode for complex logic
7. Write the Output Contract section (5-10% of doc): a literal template using `{{variable}}` placeholders — not a prose description
8. Write the Validation section (8-12% of doc): quality gates with numeric thresholds, formatted as a checklist
9. Write the Metacognition section (recommended): a Does / Does NOT block plus chaining notation showing upstream -> THIS -> downstream
10. Verify phases_count in frontmatter matches the actual number of Phase sections in the body
11. Verify body is within 8192 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p03_ins_[a-z][a-z0-9_]+`
   - kind == instruction
   - phases_count matches actual Phase section count in body
   - prerequisites are verifiable statements, not vague conditions
   - every $variable is defined with type and required/optional
   - output uses a literal `{{variable}}` template, not prose
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - each phase contains exactly one primary action
   - pseudocode present for any complex logic step
   - Context section is 15-20% of total doc
   - Phases section is 40-50% of total doc
   - Metacognition section present with Does / Does NOT block
4. Cross-check scope boundaries:
   - operational recipe, not an agent identity document (system_prompt)?
   - not a one-shot task prompt (action_prompt)?
   - not an orchestration plan (workflow, P12)?
   - no persona or identity content leaked into the body?
5. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | sibling | 0.45 |
| [[bld_instruction_action_prompt]] | sibling | 0.45 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[bld_schema_instruction]] | downstream | 0.36 |
| [[bld_instruction_golden_test]] | sibling | 0.36 |
| [[bld_instruction_output_validator]] | sibling | 0.35 |
| [[bld_knowledge_card_instruction]] | upstream | 0.35 |
| [[bld_instruction_handoff]] | sibling | 0.34 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.34 |
| [[bld_instruction_memory_scope]] | sibling | 0.33 |
