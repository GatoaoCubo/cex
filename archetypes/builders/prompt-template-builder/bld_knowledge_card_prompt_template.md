---
kind: knowledge_card
id: bld_knowledge_card_prompt_template
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for prompt_template production — atomic searchable facts
sources: prompt-template-builder MANIFEST.md + SCHEMA.md, LangChain, Mustache, Jinja2
quality: 9.1
title: "Knowledge Card Prompt Template"
version: "1.0.0"
author: n03_builder
tags: [prompt_template, builder, examples]
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
domain: "prompt template construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: prompt_template
## Executive Summary
Prompt templates are parameterized text molds where fixed structure and dynamic content are separated via typed `{{variable}}` slots filled at invocation time. The same template produces N distinct prompts by substituting different variable values — this is the core reuse contract. They differ from system prompts (fixed identity, no slots), user prompts (one-time tasks), few-shot examples (fixed examples), and meta-prompts (which generate other prompts) by being reusable molds with declared, typed variable slots.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Kind | `prompt_template` (exact literal) |
| ID pattern | `p03_pt_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min variables | 1 (at least one `{{variable}}` slot) |
| Injection point | `system` or `user` |
| Tier-1 syntax | `{{variable}}` (Mustache-compatible) |
| Tier-2 syntax | `[VARIABLE]` (when Mustache conflicts) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Uniform syntax | All {{}} Mustache OR all [] bracket — never mixed in one template |
| Typed variables | Declare type (string, list, integer, boolean, object) for validation |
| Required vs optional | Required variables have no default; optional carry default value |
| Injection point | Declare system or user — determines where in conversation template lands |
| Composability | Template designed for embedding in larger templates via partials |
| Idempotency | Same template + same variables MUST always produce same rendered prompt |
| Variable-body match | Every `{{variable}}` in body must be declared in Variables section |
| Rendering pipeline | Template -> variable substitution -> rendered prompt -> LLM call |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No `{{variable}}` in body | Not a template — it's a fixed prompt |
| Undeclared variable in body | Variable present in body but missing from Variables section |
| Mixed syntax ({{}} and []) | Inconsistent; tools cannot reliably extract all variables |
| Hardcoded content in variable slots | Slots must be empty placeholders only |
| No injection_point declared | Consumer doesn't know where to place rendered text |
| Variables without constraints | No type/enum/regex means any value accepted — fragile |
| Template with side effects | Templates must be pure text transformation, no side effects |
## Application
1. Identify the reuse contract: what varies between invocations?
2. Extract variables: name, type, required/optional, constraints
3. Choose syntax tier: `{{variable}}` (tier-1) or [VARIABLE] (tier-2)
4. Set injection_point: system or user
5. Write template body with all variable slots as empty placeholders
6. Provide at least one complete invocation example with all slots filled
7. Declare output format (what rendered template produces)
8. Validate: all body vars declared, 8 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- prompt-template-builder SCHEMA.md v1.0.0
- LangChain PromptTemplate / ChatPromptTemplate
- Mustache specification (logic-less templates)
- Jinja2 template engine documentation
