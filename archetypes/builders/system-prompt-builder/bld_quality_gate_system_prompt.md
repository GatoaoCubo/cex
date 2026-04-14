---
id: p11_qg_system_prompt
kind: quality_gate
pillar: P03
title: "Gate: System Prompt"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: system_prompt
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - system-prompt
  - identity
  - P03
tldr: "Validates LLM identity and persona prompts for specificity, safety constraints, and behavioral clarity."
llm_function: GOVERN
---
## Definition
A system prompt establishes the identity, rules, and behavioral boundaries of a language model for a specific domain or role. It is not a task instruction and not a template with placeholders. This gate ensures every system prompt is specific, safe, self-contained, and clearly separated from prompt templates and action prompts.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p03_sp_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `system_prompt` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `domain`, `persona`, `tone`, `knowledge_boundary` all defined and non-empty |
| H07 | Identity section present | Body contains a `## Identity` section with a specific role description |
| H08 | ALWAYS/NEVER rules present | Body contains explicit ALWAYS and NEVER behavioral rules |
| H09 | Output format specified | Body contains a `## Output Format` section describing expected response structure |
| H10 | No variable placeholders | Body contains no `{placeholder}` or `{{template_var}}` tokens |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Prompt is tight; no filler prose or redundant restatements |
| Persona is domain-specific | 1.0 | Identity describes a concrete role, not a generic "helpful assistant" |
| Rules have justification | 0.5 | Each ALWAYS/NEVER rule states why it exists |
| Knowledge boundary defined | 1.0 | `knowledge_boundary` field specifies what the model knows and does not know |
| Tone calibrated for domain | 0.5 | Tone matches the domain audience (technical, conversational, formal, etc.) |
| Tags include system-prompt | 0.5 | `tags` list contains `"system-prompt"` |
| Safety constraints present | 1.0 | Explicit constraints on harmful or out-of-scope outputs |
| Not a template | 1.0 | No unfilled placeholders; prompt works as-is without substitution |
| Behavior examples present | 0.5 | At least one example of expected model behavior in the body |
| Boundary with other prompt types | 0.5 | Body clarifies what belongs in action prompts vs. this system prompt |
| No task instructions | 1.0 | Body defines identity only; no step-by-step task instructions |
Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference system prompt |
| >= 8.0 | PUBLISH — safe to attach to production model configurations |
| >= 7.0 | REVIEW — usable but persona or constraints need sharpening |
| < 7.0 | REJECT — do not deploy; identity or safety gaps present |
## Bypass
| Field | Value |
|-------|-------|
| condition | Rapid prototyping in an isolated sandbox where the model has no external access |
| approver | Domain owner who defined the persona requirements |
| audit_log | Entry required in `.claude/bypasses/system_prompt_{date}.md` with sandbox proof |
| expiry | 7 days; prompt must reach PUBLISH score before moving out of sandbox |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
