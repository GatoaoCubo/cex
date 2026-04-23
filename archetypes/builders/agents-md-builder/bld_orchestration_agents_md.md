---
kind: collaboration
id: bld_collaboration_agents_md
pillar: P12
llm_function: COLLABORATE
purpose: How agents_md-builder works in crews with other builders
quality: 8.9
title: "Collaboration Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, collaboration]
tldr: "How agents_md-builder works in crews with other builders"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - agents-md-builder
  - bld_knowledge_card_agents_md
  - p03_sp_agents_md_builder
  - p10_lr_agents_md_builder
  - bld_instruction_agents_md
  - p02_qg_agents_md
  - bld_examples_agents_md
  - bld_architecture_kind
  - bld_collaboration_agent_computer_interface
  - bld_tools_agents_md
---

## Crew Role
Authors the vendor-neutral AGENTS.md at project-root, synthesizing setup-command / test-command / lint-command / pr-format / deploy-rule blocks from CI reality so every AAIF-compliant coding-agent (Codex, Claude Code, Aider, Cursor, goose) can bootstrap on fresh clone.

## Receives From
| Builder            | What                               | Format       |
|--------------------|------------------------------------|--------------|
| N05 operations     | CI invocations + deploy-rule facts | YAML / shell |
| N04 knowledge      | Repo overview + conventions        | Markdown     |
| readme-builder     | Project summary paragraph          | Markdown     |

## Produces For
| Builder               | What                                | Format    |
|-----------------------|-------------------------------------|-----------|
| Project-root          | AGENTS.md manifest                  | Markdown  |
| claude-md-builder     | Vendor-neutral baseline to extend   | Markdown  |
| cursorrules-builder   | Vendor-neutral baseline to extend   | Markdown  |
| N05 CI pipeline       | Validation target for ci_mirror_check | Markdown |

## Boundary
Does NOT author CLAUDE.md (handled by `claude_md-builder`, Claude-specific directives), README.md (handled by `readme-builder`, human-facing docs), or .cursorrules (handled by `cursorrules-builder`, Cursor-editor rules). AGENTS.md is the vendor-neutral AAIF standard; the three above are complementary vendor-specific siblings at project-root.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agents-md-builder]] | upstream | 0.48 |
| [[bld_knowledge_card_agents_md]] | upstream | 0.46 |
| [[p03_sp_agents_md_builder]] | upstream | 0.45 |
| [[p10_lr_agents_md_builder]] | upstream | 0.37 |
| [[bld_instruction_agents_md]] | upstream | 0.33 |
| [[p02_qg_agents_md]] | upstream | 0.32 |
| [[bld_examples_agents_md]] | upstream | 0.30 |
| [[bld_architecture_kind]] | upstream | 0.29 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.29 |
| [[bld_tools_agents_md]] | upstream | 0.27 |
