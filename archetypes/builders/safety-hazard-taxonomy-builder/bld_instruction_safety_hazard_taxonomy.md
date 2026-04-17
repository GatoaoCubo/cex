---
kind: instruction
id: bld_instruction_safety_hazard_taxonomy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for safety_hazard_taxonomy
quality: 8.9
title: "Instruction Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, instruction, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template]
tldr: "Step-by-step production process for safety_hazard_taxonomy"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify the taxonomy scope: full AILuminate v1.0 (12 categories) or domain-restricted subset.
2. Retrieve MLCommons AILuminate v1.0 hazard category definitions and boundary conditions.
3. Map categories to Llama Guard 4 output label equivalents for implementation alignment.
4. Gather organizational context: deployment domain, user population, regional legal constraints.
5. Identify severity escalation thresholds relevant to deployment context (e.g., consumer vs. enterprise API).
6. Collect existing response templates or refusal patterns from the organization's safety system.

## Phase 2: COMPOSE
1. Reference SCHEMA for required fields (taxonomy scope, version, hazard-category table, severity-level definitions).
2. For each of 12 hazard categories, define: category name, AILuminate code, formal definition, boundary conditions.
3. Assign severity-level per category variant: low (informational query), medium (borderline), high (explicit harm), critical (imminent/CBRN).
4. Map each category to Llama Guard 4 output label (e.g., S1=Violent Crimes, S13=Elections).
5. Write response-template for each severity level per category: refusal text, safe-completion path, escalation trigger.
6. Document boundary conditions distinguishing adjacent categories (e.g., Violent Crimes vs. Hate Speech).
7. Add false-positive risk notes per category (common benign queries that trigger the category).
8. Include MLCommons AILuminate v1.0 reference and Llama Guard 4 model card citation.
9. Tag each category with applicable jurisdictional regulations (GDPR, CSAM laws, CBRN export controls).

## Phase 3: VALIDATE
- [ ] All 12 AILuminate hazard categories present with formal definitions.
- [ ] Each category has 4 severity levels (low/medium/high/critical) defined.
- [ ] Llama Guard 4 label mapping present for each category.
- [ ] Response-template provided for each hazard category at minimum high severity.
- [ ] Boundary conditions documented between adjacent hazard categories.
- [ ] CBRN category includes specific sub-categories (Chemical/Biological/Radiological/Nuclear).
- [ ] MLCommons AILuminate v1.0 and Llama Guard 4 sources cited.
- [ ] taxonomy-scope field declares coverage (full-12 or subset with justification).
