---
kind: knowledge_card
id: bld_knowledge_card_action_prompt
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for action_prompt production
sources: OpenAI Chat API, Anthropic prompt guide, DSPy signatures, LangChain templates
quality: 9.1
title: "Knowledge Card Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - action-prompt-builder
  - p03_sp_action_prompt_builder
  - p01_kc_action_prompt
  - p11_qg_action_prompt
  - bld_instruction_action_prompt
  - bld_collaboration_action_prompt
  - bld_architecture_action_prompt
  - p01_kc_instruction
  - bld_schema_action_prompt
  - p10_lr_action-prompt-builder
---

# Domain Knowledge: action_prompt
## Executive Summary
Action prompts are task-focused messages injected at runtime that specify WHAT an LLM should do with defined input and WHAT output to produce. They function as typed function calls: input contract in, structured result out. The concept maps to OpenAI user messages, Anthropic Human turns, and DSPy Signatures.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| llm_function | BECOME (builder identity) |
| Core pattern | Verb-first task + typed I/O + validation criteria |
| Max steps | 3-7 (concise task, not detailed runbook) |
| Required sections | purpose, input_required, output_expected, edge_cases |
| Frontmatter fields | 21 |
| Quality gates | 8 HARD + 12 SOFT |
## Patterns
- **Verb-first framing**: "Extract metrics from log" not "Log metric extraction" — imperative voice activates task execution
- **Typed I/O contracts**: specify data types explicitly (list[string], JSON object) rather than vague descriptions
- **Structured output definition**: define format (JSON, table, markdown) with concrete example showing expected shape
- **Edge case enumeration**: minimum 2 known failure modes with handling guidance per action prompt
- **Validation criteria**: verifiable checks ("output contains >= 3 rows") not subjective ("output is good")
- **Purpose linkage**: every action_prompt states WHY it exists, connecting task to business reason
- **No identity mixing**: action_prompt assumes the agent already has identity from system_prompt
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague input ("some data") | LLM guesses types; outputs are unpredictable |
| Missing output format | Every run produces different structure |
| Subjective validation ("good quality") | Cannot be automatically verified |
| Identity instructions in action_prompt | Conflicts with system_prompt; role confusion |
| 10+ execution steps | That is an instruction (recipe), not an action prompt |
| No edge cases listed | First unusual input causes hallucination |
## Application
1. Start with the verb: what action does the LLM perform?
2. Define input_required with explicit types and examples
3. Define output_expected with format and concrete example
4. List 2+ edge cases with handling strategies
5. Add validation criteria that a script could verify
6. Confirm: is this a single task (action_prompt) or a multi-step recipe (instruction)?
## References
- OpenAI: Chat Completions API — user message best forctices
- Anthropic: Prompt engineering guide — Human turn design
- DSPy: Signatures — typed input/output contracts for LLM calls
- Zamfirescu-Pereira et al. 2023: "Why Johnny Can't Prompt"

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[action-prompt-builder]] | downstream | 0.46 |
| [[p03_sp_action_prompt_builder]] | downstream | 0.44 |
| [[p01_kc_action_prompt]] | sibling | 0.42 |
| [[p11_qg_action_prompt]] | downstream | 0.39 |
| [[bld_instruction_action_prompt]] | downstream | 0.38 |
| [[bld_collaboration_action_prompt]] | downstream | 0.37 |
| [[bld_architecture_action_prompt]] | downstream | 0.35 |
| [[p01_kc_instruction]] | sibling | 0.33 |
| [[bld_schema_action_prompt]] | downstream | 0.31 |
| [[p10_lr_action-prompt-builder]] | downstream | 0.30 |
