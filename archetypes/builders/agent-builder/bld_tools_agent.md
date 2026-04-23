---
kind: tools
id: bld_tools_agent
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for agent production
quality: 9.1
title: "Tools Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_boot_config
  - bld_tools_instruction
  - bld_tools_agent_package
  - bld_tools_prompt_version
  - bld_tools_retriever_config
  - bld_tools_handoff_protocol
  - bld_tools_action_prompt
  - bld_tools_cli_tool
  - bld_tools_path_config
---

# Tools: agent-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing agents to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| iso_scaffold.py | Generate agent_package skeleton (10 files) | Phase 2 (compose) | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions, kinds, constraints |
| Agent Examples | P02_model/examples/ | Real agent artifacts |
| framework Agents | records/agents/ | 118+ agents with complete agent_package |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_agent |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps, boundary |
| system-prompt-builder | archetypes/builders/system-prompt-builder/ | Upstream dependency reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == agent, quality == null,
agent_package lists >= 10 files, capabilities_count matches body, llm_function == BECOME.

## Builder Context

This ISO operates within the `agent-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: bld_tools_agent
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose bld_tools_agent.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.57 |
| [[bld_tools_boot_config]] | sibling | 0.56 |
| [[bld_tools_instruction]] | sibling | 0.55 |
| [[bld_tools_agent_package]] | sibling | 0.55 |
| [[bld_tools_prompt_version]] | sibling | 0.55 |
| [[bld_tools_retriever_config]] | sibling | 0.55 |
| [[bld_tools_handoff_protocol]] | sibling | 0.53 |
| [[bld_tools_action_prompt]] | sibling | 0.53 |
| [[bld_tools_cli_tool]] | sibling | 0.53 |
| [[bld_tools_path_config]] | sibling | 0.52 |
