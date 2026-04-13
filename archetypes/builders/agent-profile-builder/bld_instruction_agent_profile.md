---
kind: instruction
id: bld_instruction_agent_profile
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent_profile
quality: null
title: "Instruction Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, instruction]
tldr: "Step-by-step production process for agent_profile"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Define agent’s core purpose and domain expertise (e.g., healthcare, finance).  
2. Research target user personas and interaction patterns.  
3. Identify 3–5 key traits (e.g., empathy, precision) and 2–3 constraints (e.g., data privacy).  
4. Analyze existing agent benchmarks for role-specific capabilities.  
5. Map agent’s decision-making logic to domain workflows.  
6. Document ethical boundaries and compliance requirements.  

## Phase 2: COMPOSE  
1. Structure profile using SCHEMA.md fields: NAME, ROLE, TRAITS, CONSTRAINTS.  
2. Write NAME as a unique identifier (e.g., “Agent_Healthcare_001”).  
3. Define ROLE with 1–2 sentences describing primary function.  
4. List TRAITS as bullet points aligned with research phase.  
5. Specify CONSTRAINTS with actionable limitations (e.g., “No medical diagnosis”).  
6. Use OUTPUT_TEMPLATE.md to format examples and use cases.  
7. Embed domain-specific terminology (e.g., “ICU triage protocols”).  
8. Ensure BECOME function is reflected in transformation logic.  
9. Review for consistency with P02 pillar (identity construction).  

## Phase 3: VALIDATE  
- [ ] ✅ All schema fields populated per SCHEMA.md  
- [ ] ✅ Traits and constraints match research findings  
- [ ] ✅ Examples align with OUTPUT_TEMPLATE.md structure  
- [ ] ✅ No conflicting domain assumptions detected  
- [ ] ✅ Compliance with P02 identity construction standards
