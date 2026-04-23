---
kind: tools
id: bld_tools_learning_record
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for learning_record production
quality: 9.0
title: "Tools Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_pattern
  - bld_tools_retriever_config
  - bld_tools_axiom
  - bld_tools_cli_tool
  - bld_tools_workflow
  - bld_tools_validator
  - bld_tools_input_schema
  - bld_tools_prompt_version
  - bld_tools_output_validator
---

# Tools: learning-record-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing learning_records | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| memory_bridge.py | Sync learning to framework memory | Post-production | ACTIVE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for P10 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: topic, outcome, pattern, score |
| Learning memory | records/core/learning/memory/ | Existing patterns |
| Signal history | .claude/signals/ | Agent_group completion signals |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
- [ ] YAML frontmatter parses without error
- [ ] id matches `p10_lr_` pattern
- [ ] kind == "learning_record"
- [ ] quality == null
- [ ] outcome in [SUCCESS, PARTIAL, FAILURE]
- [ ] score is numeric 0.0-10.0
- [ ] pattern section has concrete steps (not vague advice)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.60 |
| [[bld_tools_pattern]] | sibling | 0.60 |
| [[bld_tools_retriever_config]] | sibling | 0.57 |
| [[bld_tools_axiom]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.57 |
| [[bld_tools_workflow]] | sibling | 0.56 |
| [[bld_tools_validator]] | sibling | 0.56 |
| [[bld_tools_input_schema]] | sibling | 0.56 |
| [[bld_tools_prompt_version]] | sibling | 0.55 |
| [[bld_tools_output_validator]] | sibling | 0.55 |
