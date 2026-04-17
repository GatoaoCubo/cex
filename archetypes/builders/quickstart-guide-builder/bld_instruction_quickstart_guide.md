---
kind: instruction
id: bld_instruction_quickstart_guide
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for quickstart_guide
quality: 8.8
title: "Instruction Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, instruction]
tldr: "Step-by-step production process for quickstart_guide"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH (quickstart guide scoping)
1. Identify target audience for the quickstart guide (developers, admins, etc.)  
2. Gather API endpoints, SDKs, and authentication methods  
3. Collect prerequisite tools (CLI, SDK versions, dependencies)  
4. Outline 5-minute onboarding workflow (setup → config → first call)  
5. Review existing documentation for gaps or redundancies  
6. Validate technical feasibility with engineering teams  

## Phase 2: COMPOSE  
1. Use bld_schema_quickstart_guide.md to define structure: title, audience, prerequisites, steps  
2. Write intro: purpose, time estimate, success metrics  
3. List prerequisites (software, account setup, API keys)  
4. Step-by-step: install CLI, configure env vars, first API call  
5. Embed code snippets (language-specific: Python/JavaScript)  
6. Add troubleshooting: common errors, mitigation steps  
7. Format with bld_output_template_quickstart_guide.md: bullet points, code blocks, warnings  
8. Reference API docs for accuracy (version, rate limits, auth)  
9. Proofread for conciseness: remove jargon, ensure 5-minute completion  

## Phase 3: VALIDATE  
[ ] All steps complete in <5 minutes with no blockers  
[ ] Code samples execute without errors in test environments  
[ ] Prerequisites align with current SDK/CLI versions  
[ ] Language and terminology match target audience (e.g., "endpoint" vs "URL")  
[ ] Schema and template compliance checked via automated linter
