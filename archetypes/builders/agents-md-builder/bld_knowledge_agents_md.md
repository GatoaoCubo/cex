---
kind: knowledge_card
id: bld_knowledge_card_agents_md
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for agents_md production
quality: 9.2
title: "Knowledge Card Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, knowledge_card]
tldr: "Domain knowledge for AGENTS.md production (AAIF spec, 60K-projects corpus)"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - agents-md-builder
  - p03_sp_agents_md_builder
  - bld_tools_agents_md
  - p10_lr_agents_md_builder
  - bld_instruction_agents_md
  - bld_collaboration_agents_md
  - bld_examples_agents_md
  - p02_qg_agents_md
  - atom_28_code_agents
  - bld_config_capability_registry
---

## Domain Overview
AGENTS.md is the AAIF/OpenAI standardized project-root manifest that instructs coding-agent tooling how to operate inside a repository. It was originated by OpenAI for the Codex CLI in August 2025, and by December 2025 had been adopted by 60,000+ open-source projects. Governance moved to the Agentic AI Foundation (AAIF) under the Linux Foundation in December 2025. The canonical specification lives at https://agents.md/.

The file lives at project-root, sibling to README.md, and is read on repo entry by Codex CLI, Claude Code, Aider, Cursor, Block goose, and every other AAIF-compliant agent. Where README.md addresses a human reader (pitch, screenshots, contributor credits), AGENTS.md addresses an autonomous coding-agent reader with imperative, copy-pasteable command blocks: setup-command, test-command, lint-command, pr-format, deploy-rule, plus conventions and security rules.

AGENTS.md is complementary to -- not a replacement for -- vendor-specific files. CLAUDE.md encodes Claude-Code-only directives (slash commands, skills). .cursorrules encodes Cursor-editor-only rules. AGENTS.md is the vendor-neutral intersection that every agent parses. MCP (Model Context Protocol) is complementary at the transport layer: AGENTS.md tells the agent what to do, MCP tells the agent how to reach external tools.

## Key Concepts
| Concept          | Definition                                                                             | Source |
|------------------|----------------------------------------------------------------------------------------|--------|
| AGENTS.md        | Project-root manifest instructing coding agents how to work in a repo                  | agents.md spec (AAIF) |
| AAIF             | Agentic AI Foundation, Linux Foundation sub-project, governs AGENTS.md (Dec 2025)      | linuxfoundation.org |
| coding-agent     | Autonomous LLM tool that reads/writes repo code (Codex, Claude Code, Aider, Cursor)    | OpenAI Codex CLI docs |
| setup-command    | Shell invocation that prepares a fresh clone (npm install, pip install, cargo build)   | AGENTS.md spec |
| test-command     | Shell invocation that runs the test suite (npm test, pytest, cargo test)               | AGENTS.md spec |
| lint-command     | Shell invocation that runs linters and formatters (eslint, ruff, clippy)               | AGENTS.md spec |
| pr-format        | Commit-message grammar, branch-naming convention, review requirements                  | Conventional Commits |
| deploy-rule      | Who approves, which environments, how to roll back                                     | SRE release-engineering |
| project-root     | The repo top-level directory where AGENTS.md lives alongside README.md                 | AAIF spec |
| 60K-projects     | Dec 2025 adoption corpus size -- 60,000+ public repos carry AGENTS.md                  | AAIF community report |

## Industry Standards
- AGENTS.md spec (AAIF, https://agents.md/)
- Conventional Commits 1.0.0 (commit grammar)
- Semantic Versioning 2.0.0 (version field in deploy-rule)
- OpenAI Codex CLI reference implementation (August 2025)
- Block goose AGENTS.md adoption guide
- MCP (Model Context Protocol) -- complementary transport, not a replacement
- ISO 8601 (dates in frontmatter)

## Common Patterns
1. Place AGENTS.md at project-root alongside README.md -- never in docs/ or .github/.
2. Write imperative commands addressed to the coding-agent, not prose addressed to humans.
3. Provide one fenced shell block per concern: setup-command, test-command, lint-command.
4. Keep vendor-neutral; push Claude-only rules to CLAUDE.md and Cursor-only to .cursorrules.
5. Enumerate forbidden operations explicitly (NEVER force-push, NEVER delete main).
6. Mirror CI invocations verbatim so agents and CI cannot drift.

## Pitfalls
- Duplicating README.md prose (project pitch, screenshots) -- AGENTS.md is for agents, not humans.
- Leaking vendor-specific directives into AGENTS.md -- they belong in CLAUDE.md / .cursorrules.
- setup-command or test-command drifting from actual CI -- breaks fresh-clone bootstrap.
- Omitting security rules -- agents will eventually force-push or delete a branch without them.
- Placing the file outside project-root -- AAIF-compliant agents will not find it.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agents-md-builder]] | downstream | 0.68 |
| [[p03_sp_agents_md_builder]] | downstream | 0.63 |
| [[bld_tools_agents_md]] | downstream | 0.54 |
| [[p10_lr_agents_md_builder]] | downstream | 0.48 |
| [[bld_instruction_agents_md]] | downstream | 0.48 |
| [[bld_collaboration_agents_md]] | downstream | 0.47 |
| [[bld_examples_agents_md]] | downstream | 0.43 |
| [[p02_qg_agents_md]] | downstream | 0.37 |
| [[atom_28_code_agents]] | sibling | 0.36 |
| [[bld_config_capability_registry]] | downstream | 0.29 |
