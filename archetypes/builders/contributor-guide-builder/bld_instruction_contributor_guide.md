---
kind: instruction
id: bld_instruction_contributor_guide
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for contributor_guide
quality: null
title: "Instruction Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, instruction]
tldr: "Step-by-step production process for contributor_guide"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing OSS CONTRIBUTING.md files for structure and common sections.  
2. Document current dev setup steps (dependencies, build tools, test environments).  
3. Map PR workflow from fork → branch → commit → push → open PR.  
4. Audit coding standards (linting, formatting, naming conventions).  
5. Define review process (criteria, timelines, required approvals).  
6. Verify CLA requirements (individual vs. corporate, signing流程).  

## Phase 2: COMPOSE  
1. Outline sections per SCHEMA.md: dev setup, PR flow, coding standards, review process, CLA.  
2. Write dev setup: OS, tools, installation steps, environment variables.  
3. Detail PR flow: branch naming, commit message format, squashing guidelines.  
4. Specify coding standards: language rules, file structure, API conventions.  
5. Describe review process: initial checks, feedback loops, merge criteria.  
6. Explain CLA: link to agreement, enforcement policy, exceptions.  
7. Use OUTPUT_TEMPLATE.md for section headers, bullet points, and code blocks.  
8. Cross-reference schema requirements to ensure completeness.  
9. Finalize with examples: sample PR, compliant commit message, CLA sign-off.  

## Phase 3: VALIDATE  
1. [ ] ✅ All required sections (dev setup, PR flow, etc.) present.  
2. [ ] ✅ Compliance with SCHEMA.md structure and OUTPUT_TEMPLATE.md format.  
3. [ ] ✅ Clear, actionable steps with no ambiguous language.  
4. [ ] ✅ CLA section aligns with legal team’s requirements.  
5. [ ] ✅ Review process matches actual team workflows.
