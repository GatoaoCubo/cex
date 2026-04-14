---
kind: instruction
id: bld_instruction_changelog
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for changelog
quality: null
title: "Instruction Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, instruction]
tldr: "Step-by-step production process for changelog"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify latest version using semver (e.g., `v1.2.3`).  
2. Extract feature additions from code commits and PRs.  
3. List bug fixes from issue trackers and test results.  
4. Document breaking changes affecting API/UX from release notes.  
5. Cross-reference with previous changelogs for consistency.  
6. Verify semver compliance (major/minor/patch) based on changes.  

## Phase 2: COMPOSE  
1. Create new changelog entry in SCHEMA.md format.  
2. Set version header (e.g., `## v1.2.3 - 2023-10-01`).  
3. Populate `Features` section with user-facing improvements.  
4. Detail `Fixes` with issue IDs and resolved problems.  
5. Highlight `Breaking Changes` with migration steps.  
6. Use OUTPUT_TEMPLATE.md for markdown syntax and structure.  
7. Ensure semver tags align with version header.  
8. Validate section headings match SCHEMA.md requirements.  
9. Proofread for clarity, grammar, and alignment with product goals.  

## Phase 3: VALIDATE  
- [ ] ✅ Semver format matches `vX.Y.Z` in header and tags.  
- [ ] ✅ All required sections (`Features`, `Fixes`, `Breaking Changes`) present.  
- [ ] ✅ Changes categorized correctly per impact (e.g., no fixes in features).  
- [ ] ✅ Template syntax (bold, links, lists) adheres to OUTPUT_TEMPLATE.md.  
- [ ] ✅ Peer review confirms accuracy and completeness.
