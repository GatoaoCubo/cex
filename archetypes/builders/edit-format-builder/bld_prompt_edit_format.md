---
kind: instruction
id: bld_instruction_edit_format
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for edit_format
quality: 8.9
title: "Instruction Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, instruction]
tldr: "Step-by-step production process for edit_format"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_instruction_playground_config
  - bld_instruction_judge_config
  - p10_lr_edit_format_builder
  - bld_instruction_planning_strategy
  - bld_instruction_benchmark_suite
  - bld_instruction_transport_config
  - bld_instruction_search_strategy
  - bld_instruction_reward_model
  - bld_instruction_white_label_config
  - bld_instruction_input_schema
---

## Phase 1: RESEARCH  

This ISO specifies an edit format: how diffs or patches are expressed and applied.
1. Analyze existing LLM-to-host communication protocols for file change syntax.  
2. Identify constraints from P06 (e.g., security, versioning, error handling).  
3. Survey use cases for edit_format (e.g., code patches, config updates).  
4. Determine required syntax elements (e.g., diff format, metadata fields).  
5. Evaluate tooling compatibility (e.g., Git, JSON, YAML parsers).  
6. Document research findings into a preliminary specification draft.  

## Phase 2: COMPOSE  
1. Define schema structure in SCHEMA.md (e.g., `operation`, `file_path`, `content`).  
2. Map each schema field to corresponding OUTPUT_TEMPLATE.md placeholders.  
3. Specify syntax rules (e.g., line endings, escaping characters).  
4. Add constraints (e.g., max file size, allowed operations).  
5. Write template examples for common operations (e.g., `replace`, `append`).  
6. Align template with SCHEMA.md using cross-references.  
7. Include error codes and handling procedures per P06.  
8. Add versioning metadata to both schema and template.  
9. Finalize artifact with review checklists from Phase 3.  

## Phase 3: VALIDATE  
- [ ] Validate schema against 10+ example edits using SCHEMA.md.  
- [ ] Test OUTPUT_TEMPLATE.md with edge cases (e.g., binary files).  
- [ ] Confirm tooling compatibility (e.g., parsers, validators).  
- [ ] Ensure all P06 constraints are explicitly addressed.  
- [ ] Perform peer review for clarity and completeness.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_playground_config]] | sibling | 0.31 |
| [[bld_instruction_judge_config]] | sibling | 0.29 |
| [[p10_lr_edit_format_builder]] | downstream | 0.28 |
| [[bld_instruction_planning_strategy]] | sibling | 0.27 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.26 |
| [[bld_instruction_transport_config]] | sibling | 0.26 |
| [[bld_instruction_search_strategy]] | sibling | 0.24 |
| [[bld_instruction_reward_model]] | sibling | 0.24 |
| [[bld_instruction_white_label_config]] | sibling | 0.24 |
| [[bld_instruction_input_schema]] | sibling | 0.24 |
