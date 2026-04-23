---
kind: tools
id: bld_tools_few_shot_example
pillar: P04
llm_function: CALL
purpose: Tools available to few-shot-example-builder
quality: 9.0
title: "Tools Few Shot Example"
version: "1.0.0"
author: n03_builder
tags: [few_shot_example, builder, examples]
tldr: "Golden and anti-examples for few shot example construction, demonstrating ideal structure and common pitfalls."
domain: "few shot example construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_context_doc
  - bld_tools_retriever_config
  - bld_tools_rag_source
  - bld_tools_prompt_version
  - bld_tools_golden_test
  - bld_tools_response_format
  - bld_tools_validation_schema
  - bld_tools_system_prompt
  - bld_tools_chunk_strategy
  - bld_tools_action_prompt
---

# Tools: few-shot-example-builder
## Primary Tools
### brain_query
**Purpose**: Check for existing few_shot_examples before creating duplicates
**Usage**: `brain_query("few_shot_example [domain] [topic]")`
**When**: Phase 1 DESIGN — always check before composing
**Expected**: Returns existing examples for domain; if none found, proceed
### validate_artifact.py [PLANNED]
**Purpose**: Automated validation against QUALITY_GATES.md
**Usage**: `python validate_artifact.py --kind few_shot_example --file p01_fse_{topic}.md`
**When**: Phase 3 VALIDATE — after composing
**Status**: PLANNED — use manual gate checklist in INSTRUCTIONS.md until available
## Data Sources
### P01_knowledge/_schema.yaml
**Purpose**: Source of truth for few_shot_example field definitions
**Path**: `cex/_schemas/p01_schema.yaml` or `cex/P01_knowledge/_schema.yaml`
**When**: Phase 1 — confirm required fields before composing
### Existing few_shot_examples
**Purpose**: Reference for format and difficulty calibration
**Path**: `cex/P01_knowledge/examples/p01_fse_*.md`
**When**: Phase 1 — understand existing coverage before adding
### P03_prompt templates
**Purpose**: Understand what formats are being taught to LLMs
**Path**: `cex/P03_prompt/`
**When**: Phase 1 — identify which prompt patterns need few-shot support
## Interim Workflow (until validate_artifact.py ships)
1. brain_query for duplicates
2. Compose using OUTPUT_TEMPLATE.md
3. Manual checklist against QUALITY_GATES.md
4. Peer review if score uncertain

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_context_doc]] | sibling | 0.45 |
| [[bld_tools_retriever_config]] | sibling | 0.44 |
| [[bld_tools_rag_source]] | sibling | 0.44 |
| [[bld_tools_prompt_version]] | sibling | 0.43 |
| [[bld_tools_golden_test]] | sibling | 0.43 |
| [[bld_tools_response_format]] | sibling | 0.43 |
| [[bld_tools_validation_schema]] | sibling | 0.43 |
| [[bld_tools_system_prompt]] | sibling | 0.42 |
| [[bld_tools_chunk_strategy]] | sibling | 0.42 |
| [[bld_tools_action_prompt]] | sibling | 0.42 |
