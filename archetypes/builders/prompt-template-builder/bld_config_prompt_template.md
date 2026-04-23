---
id: config_prompt_template_builder
kind: config
pillar: P09
llm_function: CONSTRAIN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [config, prompt-template, P03, naming, constraints]
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Prompt Template"
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
related:
  - p03_ins_prompt_template
  - bld_knowledge_card_prompt_template
  - bld_collaboration_prompt_template
  - bld_memory_prompt_template
  - prompt-template-builder
  - schema_prompt_template_builder
  - p03_sp_prompt_template_builder
  - p01_kc_prompt_template
  - tools_prompt_template_builder
  - bld_architecture_prompt_template
---
# Config — prompt-template-builder
## Naming Convention
**Pattern**: `p03_pt_{topic_slug}.md`
| Component | Rule |
|---|---|
| `p03` | Pillar prefix — always P03 for prompt layer |
| `pt` | Kind abbreviation — always `pt` for prompt_template |
| `{topic_slug}` | Lowercase, underscored, 2-5 words describing the template purpose |
| `.md` | Always markdown |
**Valid examples**:
- `p03_pt_knowledge_card_production.md`
- `p03_pt_research_synthesis.md`
- `p03_pt_code_review_checklist.md`
- `p03_pt_marketing_copy_generator.md`
**Invalid examples**:
- `prompt_template_knowledge.md` — missing pillar prefix
- `p03_knowledge_card.md` — missing kind abbreviation `pt`
- `p03_pt_KnowledgeCard.md` — uppercase not allowed
- `p03_pt_k.md` — topic_slug too short (min 2 chars after pt_)
## File Paths
| Context | Path |
|---|---|
| Pool artifacts | `records/pool/prompts/p03_pt_{topic_slug}.md` |
| Draft / WIP | `records/pool/drafts/p03_pt_{topic_slug}.md` |
| Builder reference | `archetypes/builders/prompt-template-builder/` |
## Size Limits
| Limit | Value | Scope |
|---|---|---|
| max_bytes | 8192 | Per artifact file |
| max_variables | 20 | Per template (forctical limit; no hard schema cap) |
| max_body_lines | 80 | Recommended; keep templates scannable |
| min_variables | 1 | A template with zero variables is a user_prompt, not a template |
## Variable Syntax Rules
### Tier-1: Mustache (default)
```
{{variable_name}}
```
Use for: all new templates. Compatible with Mustache, Handlebars, Anthropic prompt libraries, and most CEX renderers.
**Conditional blocks** (Mustache):
```
{{#boolean_var}}
  Content shown when boolean_var is true
{{/boolean_var}}
```
**List iteration** (Mustache):
```
{{#items}}
  - {{.}}
{{/items}}
```
### Tier-2: Bracket (fallback)
```
[VARIABLE_NAME]
```
Use for: templates targeting systems where `{{}}` is reserved syntax (e.g., Vue.js templates, some shell scripts, Go HTML templates).
### Mixing Tiers
NEVER mix tier-1 and tier-2 syntax in the same template. Set `variable_syntax` to either `mustache` or `bracket` and use exclusively.
## Version Increment Rules
| Change type | Version bump |
|---|---|
| Add new optional variable | patch (1.0.0 → 1.0.1) |
| Add new required variable | minor (1.0.0 → 1.1.0) |
| Remove or rename variable | major (1.0.0 → 2.0.0) |
| Change template body structure | minor (1.0.0 → 1.1.0) |
| Fix typo or formatting | patch (1.0.0 → 1.0.1) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_prompt_template]] | upstream | 0.43 |
| [[bld_knowledge_card_prompt_template]] | upstream | 0.40 |
| [[bld_collaboration_prompt_template]] | upstream | 0.40 |
| [[bld_memory_prompt_template]] | downstream | 0.39 |
| [[prompt-template-builder]] | upstream | 0.37 |
| [[schema_prompt_template_builder]] | upstream | 0.36 |
| [[p03_sp_prompt_template_builder]] | upstream | 0.33 |
| [[p01_kc_prompt_template]] | upstream | 0.31 |
| [[tools_prompt_template_builder]] | upstream | 0.30 |
| [[bld_architecture_prompt_template]] | upstream | 0.29 |
