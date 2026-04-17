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
