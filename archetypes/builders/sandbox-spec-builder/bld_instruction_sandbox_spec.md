---
kind: instruction
id: bld_instruction_sandbox_spec
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for sandbox_spec
quality: 8.8
title: "Instruction Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, instruction]
tldr: "Step-by-step production process for sandbox_spec"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify procurement gate requirements for enterprise pilot environments.  
2. Analyze security and compliance constraints for isolated sandbox deployment.  
3. Map stakeholder roles and access controls for sandbox governance.  
4. Document hardware/software dependencies for pilot procurement workflows.  
5. Evaluate existing infrastructure for sandbox isolation compatibility.  
6. Define success metrics for sandbox environment validation.  

## Phase 2: COMPOSE  
1. Define sandbox scope using SCHEMA.md's `environment_boundary` section.  
2. Align isolation parameters with P09 CONSTRAIN pillar requirements.  
3. Structure `resource_allocation` table per OUTPUT_TEMPLATE.md format.  
4. Specify network segmentation rules in `security_isolation` block.  
5. Embed compliance checklists from SCHEMA.md's `regulatory_gates` section.  
6. Outline procurement gate triggers in `workflow_triggers` JSON array.  
7. Reference approved tooling in `approved_tooling` list from schema.  
8. Apply schema validation rules to `sandbox_constraints` section.  
9. Finalize artifact using OUTPUT_TEMPLATE.md's `specification_summary` format.  

## Phase 3: VALIDATE  
[ ] [x] Verify schema alignment via `validate_schema.sh` script  
[ ] [x] Confirm compliance gates match SCHEMA.md's `regulatory_gates`  
[ ] [x] Test network isolation with `sandbox_isolation_test.py`  
[ ] [x] Validate procurement gate triggers against pilot workflows  
[ ] [x] Ensure OUTPUT_TEMPLATE.md formatting is fully adhered to
