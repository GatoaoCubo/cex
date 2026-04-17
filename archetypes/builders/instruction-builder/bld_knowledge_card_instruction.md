---
kind: knowledge_card
id: bld_knowledge_card_instruction
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for instruction production — operational step-by-step recipes
sources: SRE runbooks, IEC 62443 SOPs, operational procedure design, 5 production instructions
quality: 9.1
title: "Knowledge Card Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: instruction
## Executive Summary
Instructions are operational recipes that transform a defined start state into an end state through atomic, verifiable, reversible steps. From SRE runbooks and SOPs. Each step performs one action, has verifiable completion criteria, and supports rollback. Instructions differ from action prompts (concise task with I/O), system prompts (identity/persona), and workflows (multi-agent orchestration).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Frontmatter fields | 20 |
| Quality gates | 8 HARD + 11 SOFT |
| Phases | 3-5 (analyze → generate → validate) |
| Max body bytes | 4096 |
| Sweet spot | 200-350 lines, 3000-3500 tokens |
| Input vars | 3-6 with type hints |
## Patterns
- **7-section structure**: allocation by importance
| Section | Purpose | % of doc |
|---------|---------|----------|
| Title + Audience | Who + what | 2-3% |
| Context | Background, I/O contracts | 15-20% |
| Task | Objective, success criteria | 8-12% |
| Approach | Phased execution + pseudocode | 40-50% |
| Constraints | Quality gates, limits | 8-12% |
| Examples | Complete I/O demo | 10-15% |
| Output Template | Exact deliverable format | 5-10% |
- **Input/output contracts**: every variable has type hint + required/optional + default — without contracts, LLM guesses formats inconsistently
- **Phase structure** (3-5 phases): universal pattern is Analyze → Generate → Validate
- **Pseudocode guidance**: descriptive function names, clear conditions — guides LLM reasoning, not execution
- **Atomic steps**: one action per step — compound steps cause ambiguous failures
- **Verifiable prerequisites**: "Python 3.10+" not "environment ready"
- **Idempotent when possible**: explicit rollback procedure when not
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No input contract | LLM guesses variable types; inconsistent output |
| Compound steps | Two actions in one step; ambiguous failure point |
| Prose output description | Use literal template with `{{variables}}` instead |
| Missing validation phase | No quality check; output quality unverified |
| No examples | At least 1 complete I/O example required |
| Identity mixed with task | Identity = system_prompt; task = instruction |
| Qualitative gates ("ensure quality") | Unenforceable; use numeric thresholds |
## Application
1. Define audience and prerequisites (verifiable, specific)
2. Write input/output contracts: every var with type, required/optional, default
3. Design 3-5 phases: Analyze → Generate → Validate pattern
4. Write approach section (40-50%): pseudocode with descriptive names
5. Add constraints: numeric quality gates, not aspirational
6. Include >= 1 complete I/O example and output template
## References
- Google SRE: runbook design and operational procedures
- IEC 62443: industrial automation procedure standards
- Prompt engineering: structured instruction design for LLMs
- Operational excellence: atomic, verifiable, reversible step patterns
