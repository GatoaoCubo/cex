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
| max_variables | 20 | Per template (practical limit; no hard schema cap) |
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
