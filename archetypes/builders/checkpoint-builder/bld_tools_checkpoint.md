---
kind: tools
id: bld_tools_checkpoint
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for checkpoint production
quality: 9.1
title: "Tools Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_workflow
  - bld_tools_prompt_version
  - bld_tools_output_validator
  - bld_tools_path_config
  - bld_tools_handoff_protocol
  - bld_tools_chunk_strategy
  - bld_tools_runtime_rule
---

# Tools: checkpoint-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing checkpoint artifacts and workflow refs in pool | Phase 1 (check duplicates, find workflow_ref) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, checkpoint kind |
| CEX Examples | P12_orchestration/examples/ | Real checkpoint artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_checkpoint |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Workflow artifacts | P12_orchestration/examples/p12_wf_*.md | workflow_ref lookup |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `p12_ck_`, workflow_ref non-empty,
step non-empty, tags includes "checkpoint", body has 4 sections, body <= 2048 bytes, quality == null.
## workflow_ref Lookup
Before composing, verify the workflow_ref exists:
1. Search pool: `brain_query("workflow {domain_keyword}")`
2. Check: `cex/P12_orchestration/examples/p12_wf_{slug}.md`
3. If workflow artifact does not exist yet: use provisional id and add comment noting dependency

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.57 |
| [[bld_tools_memory_scope]] | sibling | 0.56 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_workflow]] | sibling | 0.56 |
| [[bld_tools_prompt_version]] | sibling | 0.55 |
| [[bld_tools_output_validator]] | sibling | 0.54 |
| [[bld_tools_path_config]] | sibling | 0.54 |
| [[bld_tools_handoff_protocol]] | sibling | 0.54 |
| [[bld_tools_chunk_strategy]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
