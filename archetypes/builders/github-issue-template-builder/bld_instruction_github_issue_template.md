---
kind: instruction
id: bld_instruction_github_issue_template
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for github_issue_template
quality: 8.9
title: "Instruction Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, instruction]
tldr: "Step-by-step production process for github_issue_template"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing GitHub issue templates in the project’s repository.  
2. Identify required fields (title, description, steps to reproduce, expected vs actual behavior).  
3. Categorize labels (bug, feature, question, blocked, enhancement).  
4. Review SCHEMA.md for field types, formats, and constraints.  
5. Audit OUTPUT_TEMPLATE.md for structure and placeholder syntax.  
6. Document domain-specific requirements (e.g., environment details, component names).  

## Phase 2: COMPOSE  
1. Create template file with `.md` extension and `issue_template` metadata.  
2. Define required fields using markdown headers and placeholder syntax (e.g., `{{field}}`).  
3. Assign labels based on categorization from Phase 1 (e.g., `bug`, `question`).  
4. Use SCHEMA.md to enforce field types (e.g., `textarea`, `checkbox`).  
5. Add optional fields for context (e.g., `screenshots`, `logs`).  
6. Reference OUTPUT_TEMPLATE.md for consistent formatting and structure.  
7. Embed validation rules (e.g., required fields must not be empty).  
8. Customize template for the project’s workflows (e.g., triage labels).  
9. Finalize with a `---` separator and metadata block.  

## Phase 3: VALIDATE  
- [ ] All required fields are present and labeled correctly.  
- [ ] Labels match predefined categories in SCHEMA.md.  
- [ ] Markdown syntax conforms to OUTPUT_TEMPLATE.md.  
- [ ] Placeholder syntax is consistent and functional.  
- [ ] Template renders correctly in GitHub (preview, submit).
