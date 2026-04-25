---
id: p01_kc_agentskills_spec
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "AgentSkills.io — Open Standard for Reusable AI Agent Skills"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [agentskills, skill-format, agent-interop, markdown-skills, cross-platform]
tldr: "AgentSkills.io packages knowledge as reusable SKILL.md consumable by any agent — Claude Code, Codex CLI, OpenCode"
when_to_use: "Design portable skills across LLM platforms or understand the SKILL.md standard"
keywords: [agentskills-io, skill-md, agent-skills, cross-platform-skills]
long_tails:
  - "How to create reusable skills for AI agents"
  - "What is the standard SKILL.md format for LLM agents"
axioms:
  - "ALWAYS separate interface (SKILL.md) from depth (references/)"
  - "NEVER create a monolithic SKILL.md with all documentation"
linked_artifacts:
  primary: null
  related: [p01_kc_brand_skill, p01_kc_csv_as_knowledge]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - p01_kc_skill_format_universal
  - p01_kc_skill_references
  - bld_collaboration_skill
  - bld_memory_skill
  - p01_kc_lp04_tools
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - bld_architecture_skill
  - bld_system_prompt_skill
  - skill-builder
---

## TL;DR

Open standard that packages specialized knowledge as Markdown files consumable by any AI agent. Each skill has SKILL.md (lightweight interface) + references/ (on-demand depth). Automatic discovery via `description` field in frontmatter.

## Core Concept

AgentSkills.io solves the problem of knowledge portability between agents. A skill is a directory with a SKILL.md file containing YAML frontmatter (name + description) and a Markdown body with workflow and references. The `description` field acts as a trigger rule — the agent reads this field to decide whether to activate the skill. Cross-platform by design: Claude Code, Codex CLI, and OpenCode consume the same format without adaptation.

The interface/depth separation is fundamental: SKILL.md loads fast (~1KB), while references/ contains examples, schemas, and complete docs that the agent loads on demand. This optimizes context usage — only loads what is needed.

## Architecture/Patterns

| Component | Role | Size |
|-----------|------|------|
| SKILL.md | Main interface, trigger rule | Lightweight (~1KB) |
| references/EXAMPLES.md | Concrete usage examples | On-demand |
| references/FUNCTIONS_REF.md | Available APIs and functions | On-demand |
| references/*.md | Specialized docs by topic | On-demand |

Mandatory frontmatter format:

```yaml
---
name: skill-name        # kebab-case, unique identifier
description: "Use when..." # trigger rule for the agent
---
```

Installation by platform:
- Claude Code: plugin marketplace or project commands directory
- Codex CLI: copy skills/ to `~/.codex/skills/`
- OpenCode: clone full repo to `~/.opencode/skills/`
- Universal: `npx skills add <repo-url>`

Discovery pattern: agent scans skills directories, reads `description` from each SKILL.md, activates when request context matches the trigger.

## Practical Examples

| Skill | Trigger | Domain |
|-------|---------|--------|
| obsidian-markdown | .md files, wikilinks, callouts | Obsidian editing |
| obsidian-bases | .base files, filters, formulas | Database views |
| json-canvas | .canvas files, mind maps | Visual mapping |
| defuddle | Extract markdown from URLs | Web content |

Effective description example:
```
"Create and edit Obsidian Bases (.base files)
with views, filters, formulas. Use when working
with .base files or database-like content."
```

The "Use when..." is the critical part — without it, the agent does not know when to activate.

## Anti-Patterns

- Monolithic SKILL.md with all documentation embedded
- Vague description field without activation context
- Copying only skills/ without repo structure (OpenCode)
- Confusing with MCP tools — agentskills is file-based
- Skills without references/ when the domain is complex
- Name with spaces or camelCase (must be kebab-case)

## References

- source: https://github.com/kepano/obsidian-skills
- related: p01_kc_brand_skill
- related: p01_kc_csv_as_knowledge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_skill_format_universal]] | sibling | 0.50 |
| [[p01_kc_skill_references]] | sibling | 0.44 |
| [[bld_collaboration_skill]] | downstream | 0.38 |
| [[bld_memory_skill]] | downstream | 0.38 |
| [[p01_kc_lp04_tools]] | sibling | 0.36 |
| [[procedural-memory-builder]] | downstream | 0.32 |
| [[bld_knowledge_card_procedural_memory]] | sibling | 0.32 |
| [[bld_architecture_skill]] | downstream | 0.32 |
| [[bld_system_prompt_skill]] | downstream | 0.31 |
| [[skill-builder]] | downstream | 0.31 |
