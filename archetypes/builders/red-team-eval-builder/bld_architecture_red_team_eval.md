---
kind: architecture
id: bld_architecture_red_team_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of red_team_eval — inventory, dependencies, and architectural position
quality: 9.0
title: "Architecture Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - red-team-eval-builder
  - p03_sp_red_team_eval_builder
  - p01_kc_red_team_eval
  - bld_instruction_red_team_eval
  - p11_qg_red_team_eval
  - bld_collaboration_red_team_eval
  - bld_schema_red_team_eval
  - bld_knowledge_card_red_team_eval
  - bld_examples_red_team_eval
  - bld_output_template_red_team_eval
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| attack_type | Named adversarial category defining attack vector | red_team_eval | required |
| target | Agent, prompt, or pipeline under adversarial evaluation | red_team_eval | required |
| pass_criteria | Observable definition of safe behavior (pass/fail) | red_team_eval | required |
| attack_scenario | Test case: placeholder payload + expected response + OWASP ref | red_team_eval | required |
| framework_config | Eval framework setup (Promptfoo/Garak/DeepEval/Patronus) | red_team_eval | required |
| owasp_ref | OWASP LLM Top 10 identifier linking attack to taxonomy | red_team_eval | recommended |
| severity | Risk classification if attack succeeds (critical/high/medium/low) | red_team_eval | recommended |
| system_prompt | Prompt under test — consumed by target at test time | P03 | external |
| guardrail | Runtime enforcement boundary — blocks attacks post-deploy | P11 | external |
| agent | Runtime agent under test | P02 | consumer |
| eval_dataset | Dataset of adversarial inputs populating attack scenarios | P07 | external |
## Dependency Graph
```
system_prompt    --depends-->  target
eval_dataset     --produces--> attack_scenario
attack_type      --depends-->  attack_scenario
attack_scenario  --depends-->  pass_criteria
attack_scenario  --depends-->  owasp_ref
framework_config --depends-->  attack_scenario
agent            --depends-->  target
target           --produces--> pass_criteria (graded against)
guardrail        --follows-->  red_team_eval (deployed after eval passes)
```
## Boundary Table
| red_team_eval IS | red_team_eval IS NOT |
|------------------|----------------------|
| Adversarial safety testing BEFORE deployment | Runtime enforcement boundary (guardrail, P11) |
| Tests attack vulnerabilities with adversarial inputs | Functional end-to-end correctness test (e2e_eval) |
| Scoped to attack_types from approved adversarial enum | Isolated unit logic test (unit_eval) |
| Produces pass/fail per attack scenario with evidence | Quick sanity check (smoke_eval) |
| References OWASP LLM Top 10 taxonomy | Comparative performance benchmark |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| taxonomy | attack_type, owasp_ref | Classify and trace adversarial threat surface |
| specification | target, pass_criteria | Define what is tested and what safe looks like |
| scenarios | attack_scenario, eval_dataset | Concrete adversarial test cases |
| execution | framework_config, severity | Configure eval runner and prioritize risk |
| governance | guardrail | Post-eval runtime enforcement |
| consumers | agent, system_prompt | Runtime components exercised by the eval |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[red-team-eval-builder]] | upstream | 0.55 |
| [[p03_sp_red_team_eval_builder]] | upstream | 0.50 |
| [[p01_kc_red_team_eval]] | upstream | 0.44 |
| [[bld_instruction_red_team_eval]] | upstream | 0.43 |
| [[p11_qg_red_team_eval]] | downstream | 0.42 |
| [[bld_collaboration_red_team_eval]] | downstream | 0.39 |
| [[bld_schema_red_team_eval]] | upstream | 0.36 |
| [[bld_knowledge_card_red_team_eval]] | upstream | 0.33 |
| [[bld_examples_red_team_eval]] | upstream | 0.32 |
| [[bld_output_template_red_team_eval]] | upstream | 0.30 |
