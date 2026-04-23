---
kind: knowledge_card
id: bld_knowledge_card_skill
pillar: P04
llm_function: INJECT
purpose: Domain knowledge for skill production — atomic searchable facts
sources: skill-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Skill"
version: "1.0.0"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill-builder
  - p11_qg_skill
  - bld_schema_skill
  - p03_ins_skill_builder
  - bld_config_skill
  - p01_kc_skill
  - bld_architecture_skill
  - bld_system_prompt_skill
  - bld_collaboration_skill
  - bld_examples_skill
---

# Domain Knowledge: skill
## Executive Summary
Skills are reusable, phase-structured capabilities with a defined trigger — the bridge between a raw LLM and a repeatable workflow. Each skill has an ordered phase list (discover/configure/execute/validate) and a precise invocation pattern. Unlike agents (which carry identity/persona) or action_prompts (single-shot task text), skills are stateless capability definitions with no "You are" language and no task instructions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 |
| Format | YAML (frontmatter) + Markdown (body) |
| Naming | `p04_skill_{name}.md` + `.yaml` |
| ID regex | `^p04_skill_[a-z][a-z0-9_]+$` |
| Max body bytes | 5120 |
| Required frontmatter fields | 16 |
| Optional frontmatter fields | 4: references_dir, sub_skills, platforms, stack_default |
| Quality gates | 7 HARD + 10 SOFT |
| description max | 120 characters |
| Minimum phases | 2 |
| Maximum phases | 6 |
| quality field | null always — invariant |
## Patterns
| Pattern | Rule |
|---------|------|
| Phase alignment | `phases` list in frontmatter MUST match `## Workflow Phases` subsections in body (1:1) |
| Slash command trigger | `user_invocable: true` REQUIRES trigger to start with `/` |
| Agent-invoked trigger | `user_invocable: false` + keyword or event trigger (no slash) |
| No persona | Skills NEVER contain "You are" — capability only, not identity |
| Parallel lists | `when_to_use` and `when_not_to_use` MUST be at the same abstraction level |
| id == filename stem | `p04_skill_deploy.md` → `id: p04_skill_deploy` |
| Sub-skills | Delegate to other skill IDs via `sub_skills` list; never re-implement inline |
| Canonical phases | discover → configure → execute → validate |
- **Body sections**: Purpose → Workflow Phases → Anti-Patterns → Metrics
- **Per-phase structure**: input / action / output clearly named
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| "You are an expert…" in skill body | Skills have no persona; identity belongs in system_prompt |
| phases list mismatched to body subsections | Hard gate failure; names must be 1:1 with body |
| `user_invocable: true` with non-slash trigger | Schema violation; slash command required for user-invocable |
| Single monolithic phase | Loses phase contract; minimum 2 distinct phases with named boundaries |
| Missing `when_not_to_use` | Routing ambiguity; consumers cannot exclude skill correctly |
| Task instructions embedded in skill | Skill defines capability shape, not execution content |
| God skill (8+ unrelated actions) | Split into focused sub_skills |
## Application
1. Define the single reusable capability domain
2. Decompose into 2–6 ordered phases (minimum: execute + validate)
3. Write frontmatter: all 16 required fields, set `user_invocable` and `trigger` correctly
4. If `user_invocable: true`, set trigger to `/skill-name` slash command
5. Write body: Purpose → one `###` subsection per phase (input/action/output) → Anti-Patterns → Metrics
6. Verify `phases` list matches body subsection names exactly
7. Set `quality: null`
8. Check body ≤ 5120 bytes
## References
- Schema: skill SCHEMA.md (P06)
- Pillar: P04 (skills + hooks)
- Boundary: system_prompt (identity), action_prompt (single-shot task), hook (event-driven, not phase-based)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill-builder]] | related | 0.59 |
| [[p11_qg_skill]] | downstream | 0.52 |
| [[bld_schema_skill]] | downstream | 0.49 |
| [[p03_ins_skill_builder]] | upstream | 0.48 |
| [[bld_config_skill]] | downstream | 0.48 |
| [[p01_kc_skill]] | sibling | 0.46 |
| [[bld_architecture_skill]] | downstream | 0.46 |
| [[bld_system_prompt_skill]] | upstream | 0.39 |
| [[bld_collaboration_skill]] | downstream | 0.39 |
| [[bld_examples_skill]] | downstream | 0.38 |
