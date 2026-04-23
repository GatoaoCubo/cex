---
kind: knowledge_card
id: bld_knowledge_card_system_prompt
pillar: P03
llm_function: INJECT
purpose: Domain knowledge for system_prompt production — atomic searchable facts
sources: system-prompt-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card System Prompt"
version: "1.0.0"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_system-prompt-builder
  - bld_schema_system_prompt
  - system-prompt-builder
  - bld_collaboration_system_prompt
  - bld_memory_system_prompt
  - bld_examples_system_prompt
  - p11_qg_system_prompt
  - p03_sp__builder_builder
  - p03_sp_action_prompt_builder
  - p03_ins_system_prompt
---

# Domain Knowledge: system_prompt
## Executive Summary
System prompts define an LLM agent's permanent identity — who it is, what binary rules govern it, and how it responds. They transform a generic LLM into a focused specialist via persona, ALWAYS/NEVER constraints, knowledge boundaries, and output format definition. Unlike action_prompts (single-shot task execution) or instructions (step-by-step recipes), system prompts carry no task content — only identity, rules, and response shape.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 |
| Format | YAML (frontmatter) + Markdown (body) |
| Naming | `p03_sp_{agent_slug}.md` |
| ID regex | `^p03_sp_[a-z][a-z0-9_]+$` |
| Max body bytes | 4096 (CEX format) |
| Required frontmatter fields | 16 |
| Recommended frontmatter fields | 5: safety_level, tools_listed, output_format_type, tldr, density_score |
| Quality gates | 8 HARD + 12 SOFT |
| rules_count | MUST match actual numbered rules in body |
| tone enum | `formal` / `technical` / `conversational` / `authoritative` |
| safety_level enum | `standard` / `strict` / `permissive` |
| Rules volume | 5–12 ALWAYS + 3–8 NEVER |
| Identity lines | 8–15 lines (max 25) |
| quality field | null always — invariant |
## Patterns
| Pattern | Rule |
|---------|------|
| Identity first | Body ALWAYS opens with `## Identity` section — no exceptions |
| Persona formula | `You are **{name}**, a specialized {domain} agent focused on {mission}.` |
| ALWAYS/NEVER binary | Rules are binary constraints, not soft guidance ("always X" not "try to X") |
| Rules grouping | Group by concern: scope / quality / safety / comms |
| knowledge_boundary pair | State what agent knows AND what it does NOT know (positive + negative scope) |
| rules_count integrity | Count numbered rules in body; write that exact integer in frontmatter |
| No task instructions | system_prompt = identity only; task content belongs in action_prompt |
| id == filename stem | `p03_sp_scout.md` → `id: p03_sp_scout` |
- **Body sections**: Identity → Rules → Output Format → Constraints
- **Rules format**: numbered list, each prefixed ALWAYS or NEVER
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Task instructions in system prompt | Conflates identity with execution; breaks separation of concerns |
| Soft guidance rules ("try to", "consider") | LLM treats as optional; binary constraints required |
| rules_count mismatch | Hard gate failure; frontmatter integer must match actual rule count |
| Knowledge boundary missing negative scope | Agent attempts answers outside domain without guard |
| Identity section not first | Schema violation; Identity must be front-loaded in body |
| Body > 4096 bytes | CEX size limit exceeded; trim rules and identity prose |
| "You are" language in skill files | Persona belongs in system_prompt only |
| Omitting output_format_type | Consumer cannot predict response shape |
## Application
1. Research the target agent's domain to define expertise and knowledge boundaries
2. Write persona line: `You are **{name}**, a specialized {domain} agent focused on {mission}.`
3. Define `knowledge_boundary`: positive scope (what agent knows) + negative scope (what it does not)
4. Write 5–12 ALWAYS rules and 3–8 NEVER rules, grouped by concern
5. Count all numbered rules; write that integer into `rules_count` frontmatter field
6. Define `## Output Format`: response structure and format type
7. Write `## Constraints`: knowledge boundary, delegation rules, exclusions
8. Fill all 16 required frontmatter fields; set `quality: null`
9. Verify body ≤ 4096 bytes, `id` == filename stem
## References
- Schema: system_prompt SCHEMA.md (P06) v2.0
- Pillar: P03 (prompts)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_system-prompt-builder]] | related | 0.51 |
| [[bld_schema_system_prompt]] | downstream | 0.48 |
| [[system-prompt-builder]] | related | 0.37 |
| [[bld_collaboration_system_prompt]] | related | 0.36 |
| [[bld_memory_system_prompt]] | downstream | 0.35 |
| [[bld_examples_system_prompt]] | downstream | 0.34 |
| [[p11_qg_system_prompt]] | related | 0.33 |
| [[p03_sp__builder_builder]] | related | 0.31 |
| [[p03_sp_action_prompt_builder]] | related | 0.30 |
| [[p03_ins_system_prompt]] | related | 0.28 |
