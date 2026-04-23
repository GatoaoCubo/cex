---
kind: instruction
id: bld_instruction_code_of_conduct
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for code_of_conduct
quality: 8.9
title: "Instruction Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, instruction]
tldr: "Step-by-step production process for code_of_conduct"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - p05_qg_code_of_conduct
  - bld_knowledge_card_code_of_conduct
  - p03_sp_code_of_conduct_builder
  - code-of-conduct-builder
  - bld_examples_code_of_conduct
  - p10_mem_code_of_conduct_builder
  - bld_schema_code_of_conduct
  - bld_output_template_code_of_conduct
  - bld_instruction_input_schema
  - bld_instruction_context_doc
---

## Phase 1: RESEARCH
1. Identify the project type (solo OSS, foundation-backed, corporate-sponsored).
2. Determine enforcement capacity (maintainer count, response bandwidth).
3. Confirm reporting channel (contact email, dedicated moderation team).
4. Review existing community norms or prior conduct incidents.
5. Select base standard: Contributor Covenant v2.1 (default) or project-specific adaptation.
6. Identify which spaces the CoC covers (GitHub issues, forums, chat, events).

## Phase 2: COMPOSE
1. Reference bld_schema_code_of_conduct.md for required frontmatter fields.
2. Write the pledge section: "We as members, contributors, and leaders pledge..."
3. List positive standards (welcoming language, respect, constructive feedback).
4. List unacceptable behaviors (harassment, trolling, doxxing, discrimination).
5. Define enforcement responsibilities (maintainers, moderators).
6. Specify scope: online (repo, issues, PR comments) + offline (events, meetups).
7. Compose enforcement ladder with 4 levels: Correction, Warning, Temporary Ban, Permanent Ban.
8. Add reporting instructions with contact email and confidentiality statement.
9. Include attribution line referencing Contributor Covenant v2.1.
10. Add contact email placeholder with instruction to replace before publishing.

## Phase 3: VALIDATE
- [x] All required frontmatter fields present per bld_schema_code_of_conduct.md.
- [x] Pledge section present with inclusive commitment language.
- [x] Standards of conduct section lists at least 5 positive behaviors.
- [x] Unacceptable behaviors section lists at least 5 prohibited actions.
- [x] Enforcement ladder has all 4 levels (Correction, Warning, Temp Ban, Perm Ban).
- [x] Reporting channel (contact email) present and actionable.
- [x] Scope covers both online and offline spaces.
- [x] Attribution to Contributor Covenant present.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_qg_code_of_conduct]] | downstream | 0.46 |
| [[bld_knowledge_card_code_of_conduct]] | upstream | 0.45 |
| [[p03_sp_code_of_conduct_builder]] | related | 0.42 |
| [[code-of-conduct-builder]] | downstream | 0.40 |
| [[bld_examples_code_of_conduct]] | downstream | 0.38 |
| [[p10_mem_code_of_conduct_builder]] | downstream | 0.36 |
| [[bld_schema_code_of_conduct]] | downstream | 0.31 |
| [[bld_output_template_code_of_conduct]] | downstream | 0.28 |
| [[bld_instruction_input_schema]] | sibling | 0.21 |
| [[bld_instruction_context_doc]] | sibling | 0.21 |
