---
kind: tools
id: bld_tools_system_prompt
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for system_prompt production
quality: 9.0
title: "Tools System Prompt"
version: "1.0.0"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_instruction
  - bld_tools_action_prompt
  - bld_tools_prompt_version
  - bld_tools_workflow
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_constraint_spec
  - bld_tools_chain
  - bld_tools_cli_tool
  - bld_tools_output_validator
---

# Tools: system-prompt-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing system_prompts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, kinds |
| CEX Examples | P03_prompt/examples/ | Real system_prompt artifacts |
| PRIME files | records/agent_groups/*/PRIME_*.md | 7 existing system prompts |
| ISO Instructions | records/agents/*/agent_package/ISO_*_SYSTEM_INSTRUCTION.md | 101 agent system prompts |
| Rules files | .claude/rules/*.md | 10 operational rule sets |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_system_prompt |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | BashTool | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, rules_count match,
body has all 4 required sections, no task instructions leaked into identity.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_instruction]] | sibling | 0.68 |
| [[bld_tools_action_prompt]] | sibling | 0.68 |
| [[bld_tools_prompt_version]] | sibling | 0.65 |
| [[bld_tools_workflow]] | sibling | 0.63 |
| [[bld_tools_retriever_config]] | sibling | 0.62 |
| [[bld_tools_memory_scope]] | sibling | 0.62 |
| [[bld_tools_constraint_spec]] | sibling | 0.62 |
| [[bld_tools_chain]] | sibling | 0.62 |
| [[bld_tools_cli_tool]] | sibling | 0.62 |
| [[bld_tools_output_validator]] | sibling | 0.62 |
