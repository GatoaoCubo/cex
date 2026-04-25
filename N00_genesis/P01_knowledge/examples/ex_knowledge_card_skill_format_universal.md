---
id: p01_kc_skill_format_universal
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Skill Format Universal — Frontmatter YAML + Markdown for LLM Agents"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: knowledge_engineering
quality: 9.2
tags: [skill-format, plugin-system, agent-skills, frontmatter, composable-skills]
tldr: "Skills use YAML frontmatter (name + description-trigger) + Markdown body with workflow, gates and integration — cross-platform"
when_to_use: "Create or evaluate skills for LLM agents on any platform"
keywords: [skill-format, frontmatter, trigger-condition, hard-gate, plugin-system]
long_tails:
  - "How to create a skill for Claude Code with YAML frontmatter"
  - "What is the universal skill format for LLM agents"
axioms:
  - "ALWAYS use description as trigger condition, NEVER as generic description"
  - "NEVER create monolithic skill without sub-files for complex techniques"
linked_artifacts:
  primary: p01_kc_skill_references
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://agentskills.io"
related:
  - bld_collaboration_skill
  - p01_kc_agentskills_spec
  - bld_architecture_skill
  - bld_system_prompt_skill
  - bld_memory_skill
  - p03_ins_skill_builder
  - bld_knowledge_card_procedural_memory
  - procedural-memory-builder
  - p01_kc_skill_references
  - skill-builder
---

## Summary

Skills for LLM agents follow a universal format: YAML frontmatter with `name` (kebab-case) and `description` (trigger condition) + structured Markdown body.
Works cross-platform: Claude Code, Codex, OpenCode, Cursor, Gemini.
The `description` field is the routing mechanism -- the agent reads this field to decide WHEN to invoke the skill automatically.

## Spec

| Field | Required | Format | Rule |
|-------|----------|--------|------|
| `name` | YES | kebab-case | Unique in plugin namespace |
| `description` | YES | Trigger condition | Condition for when to invoke |
| `model` | NO | string | `inherit` (default) or specific model |
| File | YES | `SKILL.md` | Inside `skills/{name}/` |
| Namespace | NO | `plugin:skill-name` | Qualified for registries |

Standard directory structure:

```
skills/{name}/
  SKILL.md                    # Entry point with frontmatter
  {sub-file}-prompt.md        # Prompts for sub-agents
  {technique}.md              # Support documents
```

Comparison between frameworks:

| Aspect | superpowers | agentskills.io |
|---------|-------------|----------------|
| Trigger | Campo `description` como condition | Campo `trigger` explicito |
| Namespace | `plugin:skill-name` | `namespace/skill` |
| Distribuicao | Plugin marketplace + git clone | Registry central |
| Cross-platform | Claude/Codex/Cursor/Gemini | Dependente da plataforma |

## Patterns

| Trigger | Action |
|---------|--------|
| Skill needs automatic invocation | Description as specific trigger condition |
| Critical workflow cannot skip steps | Hard gate with `<HARD-GATE>` tag |
| Complex decision with branches | Flowchart `dot` as algorithm |
| Skill uses or is used by others | Integration section with requires/called-by |
| Complex technique with many details | Sub-files in support folder |

## Anti-Patterns

- Vague description ("Skill for debugging") -- agent never invokes
- Monolithic skill (>200 lines) without support sub-files
- Missing hard gates in critical workflows (code before design)
- No Integration section -- skill isolated in capability graph
- Missing examples -- pattern stays abstract and ambiguous

## Code

<!-- lang: markdown | purpose: skill com trigger e hard gate -->
```markdown
---
name: systematic-debugging
description: "Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes"
---

# Systematic Debugging

## The Process
1. Read error and stacktrace
2. Form hypothesis about root cause
3. Verify with minimal reproduction test
4. Fix only after confirmation

<HARD-GATE>
Do NOT write fixes until root cause is confirmed.
</HARD-GATE>

## Integration
- requires: code-review
- called-by: feature-development
```

## References

- source: https://agentskills.io
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_skill_references
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_skill]] | downstream | 0.43 |
| [[p01_kc_agentskills_spec]] | sibling | 0.41 |
| [[bld_architecture_skill]] | downstream | 0.36 |
| [[bld_system_prompt_skill]] | downstream | 0.35 |
| [[bld_memory_skill]] | downstream | 0.35 |
| [[p03_ins_skill_builder]] | downstream | 0.34 |
| [[bld_knowledge_card_procedural_memory]] | sibling | 0.34 |
| [[procedural-memory-builder]] | downstream | 0.33 |
| [[p01_kc_skill_references]] | sibling | 0.33 |
| [[skill-builder]] | downstream | 0.33 |
