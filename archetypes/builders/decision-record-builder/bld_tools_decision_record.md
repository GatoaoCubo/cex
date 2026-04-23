---
kind: tools
id: bld_tools_decision_record
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for decision_record production
quality: 9.0
title: "Tools Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_collaboration_decision_record
  - bld_tools_memory_scope
  - bld_tools_prompt_version
  - bld_tools_path_config
  - bld_tools_output_validator
  - bld_tools_handoff_protocol
  - bld_tools_runtime_rule
  - bld_knowledge_card_decision_record
---

# Tools: decision-record-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing decision_record artifacts to avoid duplication and find supersession candidates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator — checks HARD gates | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| adr-tools CLI | External CLI for managing ADR collections (auto-increment, supersede) | Optional integration | EXTERNAL |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions, decision_record kind |
| CEX ADR Index | P08_architecture/adrs/ADR_INDEX.md | Existing ADRs, status, supersession chains |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P08_decision_record |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| brain_query pool | [MCP] | All indexed decision_record artifacts |
## adr-tools Integration (External)
adr-tools (github.com/npryce/adr-tools) manages numbered ADR sequences.
CEX uses slug-based IDs instead of sequence numbers, but adr-tools patterns apply:
- `adr new "Title"` — creates new ADR from template
- `adr supersede N "New title"` — marks ADR N as superseded and creates replacement
- `adr list` — lists all ADRs with status
CEX equivalent: use brain_query to find existing ADRs, manually set supersedes/superseded_by fields.
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id matches p08_adr_ pattern, status is
valid enum, context and decision fields non-empty, all 4 body sections present, at least
2 options documented, at least 1 negative consequence, quality == null.
If status == superseded: confirm superseded_by is populated with a valid id.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_cli_tool]] | sibling | 0.47 |
| [[bld_tools_retriever_config]] | sibling | 0.46 |
| [[bld_collaboration_decision_record]] | downstream | 0.46 |
| [[bld_tools_memory_scope]] | sibling | 0.46 |
| [[bld_tools_prompt_version]] | sibling | 0.45 |
| [[bld_tools_path_config]] | sibling | 0.44 |
| [[bld_tools_output_validator]] | sibling | 0.44 |
| [[bld_tools_handoff_protocol]] | sibling | 0.44 |
| [[bld_tools_runtime_rule]] | sibling | 0.44 |
| [[bld_knowledge_card_decision_record]] | upstream | 0.44 |
