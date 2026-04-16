---
kind: instruction
id: bld_instruction_prompt_technique
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prompt_technique
quality: 8.9
title: "Instruction Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, instruction]
tldr: "Step-by-step production process for prompt_technique"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify target domain (e.g., code generation, data analysis).  
2. Analyze existing prompting patterns for efficacy and edge cases.  
3. Evaluate injection points where technique can alter model behavior.  
4. Document observed patterns in successful vs. failed prompts.  
5. Refine technique based on A/B test results with domain experts.  
6. Ensure alignment with Pillar P03’s injection-specific constraints.  

## Phase 2: COMPOSE  
1. Define artifact structure using bld_schema_prompt_technique.md’s `prompt_technique` fields.
2. Align function (PRODUCE) with schema-defined parameters and outputs.
3. Write technique name (e.g., “Role Injection with Contextual Anchors”).
4. Describe mechanism: how the technique elicits desired model behavior.
5. Specify parameters (e.g., anchor phrases, context depth, domain tags).
6. Include example prompts from bld_output_template_prompt_technique.md’s `examples` section.
7. Format artifact with YAML headers per bld_schema_prompt_technique.md’s metadata rules.
8. Validate against bld_output_template_prompt_technique.md’s structure and syntax.
9. Finalize artifact with versioning and authorship metadata.  

## Phase 3: VALIDATE
- [ ] Artifact conforms to bld_schema_prompt_technique.md’s required fields and types.
- [ ] Example prompts produce expected outputs in target domain.
- [ ] Parameters are clearly defined and match schema.
- [ ] Technique adheres to P03 prompt-specific constraints.
- [ ] No conflicts with existing techniques in the same domain.
