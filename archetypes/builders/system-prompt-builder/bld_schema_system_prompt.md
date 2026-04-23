---
kind: schema
id: bld_schema_system_prompt
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for system_prompt
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 2.0.0
quality: 9.1
title: "Schema System Prompt"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_action_prompt
  - bld_schema_runtime_state
  - bld_schema_workflow
  - bld_schema_instruction
  - bld_schema_output_validator
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_reranker_config
  - bld_schema_constraint_spec
  - bld_schema_retriever_config
---

# Schema: system_prompt (v2)
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_sp_{agent_slug}) | YES | - | Namespace compliance. Regex: `^p03_sp_[a-z][a-z0-9_]+$` |
| kind | literal "system_prompt" | YES | - | Type integrity — invariant |
| pillar | literal "P03" | YES | - | Pillar assignment — invariant |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable system prompt name |
| target_agent | string | YES | - | Agent this prompt is for |
| persona | string | YES | - | One-line persona description |
| rules_count | integer | YES | - | Number of rules in body (must match actual count) |
| tone | enum: formal, technical, conversational, authoritative | YES | "technical" | Voice style — KNOWLEDGE confirms 4 tones work |
| knowledge_boundary | string | YES | - | What agent knows AND does NOT know (pair positive + negative scope) |
| domain | string | YES | - | Domain this agent operates in |
| quality | null | YES | null | Never self-score — invariant |
| tags | list[string], len >= 3 | YES | - | Must include "system_prompt" |
| safety_level | enum: standard, strict, permissive | REC | "standard" | Constraint strictness — not all prompts need explicit safety |
| tools_listed | boolean | REC | false | Whether tools section is included — optional in many prompts |
| output_format_type | enum: markdown, json, yaml, text, structured | REC | "markdown" | Response format |
| tldr | string <= 160ch | REC | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density metric |
**Required count**: 16 | **Recommended count**: 5
## ID Pattern
Regex: `^p03_sp_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Identity` — Who the agent is: name, domain expertise, core mission, persona voice. Format: `You are **{agent_name}**, a specialized {domain} agent focused on {core_mission}.` Front-loaded, always first.
2. `## Rules` — Numbered ALWAYS/NEVER statements grouped by concern (scope, quality, safety, comms). 5-12 ALWAYS + 3-8 NEVER. Binary constraints, not soft guidance. Brief "why" per group heading.
3. `## Output Format` — Response structure, format constraints, expected deliverable shape.
4. `## Constraints` — Knowledge boundary (positive + negative scope), delegation boundaries, what NOT to do.
## Size Calibration
| Metric | CEX Builders | Legacy System | Limit |
|--------|-------------|-------------------|-------|
| Avg body bytes | 1,620 | ~6,500 | - |
| Max body bytes | 2,842 | ~18,000 | - |
| **max_bytes** | **4,096** | exceeds (legacy) | **4,096** |
| Body tokens | 3,000-3,500 | varies | ~4,500 |
| Identity lines | 8-15 | varies | 25 |
| Rules count | 8-12 | varies | 20 |
> **Note**: max_bytes = 4096 applies to CEX-format artifacts. Legacy system prompts may exceed this — they predate the schema and are not subject to this constraint.
## Constraints
- max_bytes: 4096 (body only, CEX artifacts)
- naming: p03_sp_{agent_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- rules_count MUST match actual count of numbered rules in body
- Rules MUST use ALWAYS/NEVER pattern (binary > soft guidance)
- Identity section MUST be first, MUST define domain expertise
- Identity MUST NOT contain task instructions (that is instruction/action_prompt)
- quality: null always — invariant
- system_prompt defines identity — no task instructions, no conversation history, no training data

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_action_prompt]] | sibling | 0.58 |
| [[bld_schema_runtime_state]] | sibling | 0.54 |
| [[bld_schema_workflow]] | sibling | 0.54 |
| [[bld_schema_instruction]] | sibling | 0.54 |
| [[bld_schema_output_validator]] | sibling | 0.54 |
| [[bld_schema_smoke_eval]] | sibling | 0.53 |
| [[bld_schema_golden_test]] | sibling | 0.53 |
| [[bld_schema_reranker_config]] | sibling | 0.53 |
| [[bld_schema_constraint_spec]] | sibling | 0.53 |
| [[bld_schema_retriever_config]] | sibling | 0.53 |
