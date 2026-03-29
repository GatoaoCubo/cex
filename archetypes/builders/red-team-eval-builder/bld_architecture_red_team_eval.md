---
kind: architecture
id: bld_architecture_red_team_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of red_team_eval — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| attack_type | Named adversarial category defining what attack vector is tested | red_team_eval | required |
| target | The agent, prompt, or pipeline component under adversarial evaluation | red_team_eval | required |
| pass_criteria | Observable definition of safe model behavior that determines pass/fail | red_team_eval | required |
| attack_scenario | Concrete test case: placeholder payload + expected safe response + OWASP ref | red_team_eval | required |
| framework_config | Eval framework setup (Promptfoo YAML, Garak CLI, DeepEval Python, Patronus API) | red_team_eval | required |
| owasp_ref | OWASP LLM Top 10 identifier linking attack to industry taxonomy | red_team_eval | recommended |
| severity | Risk classification if attack succeeds (critical/high/medium/low) | red_team_eval | recommended |
| system_prompt | The prompt being tested — consumed by target agent at test time | P03 | external |
| guardrail | Runtime enforcement boundary — separate from eval; blocks attacks post-deploy | P11 | external |
| agent | Runtime agent under test — eval exercises it with adversarial inputs | P02 | consumer |
| eval_dataset | Dataset of adversarial inputs used to populate attack scenarios | P07 | external |
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
| From | To | Type | Data |
|------|----|------|------|
| system_prompt | target | depends | The prompt being adversarially tested |
| eval_dataset | attack_scenario | produces | Adversarial input cases |
| attack_type | attack_scenario | depends | Attack category scoping the scenario |
| attack_scenario | pass_criteria | depends | Scenario outcome graded against criteria |
| attack_scenario | owasp_ref | depends | Traceability to vulnerability taxonomy |
| framework_config | attack_scenario | depends | Execution config for the eval runner |
| agent | target | depends | Runtime system receiving adversarial inputs |
| guardrail | red_team_eval | follows | Guardrail deployment triggered after eval passes |
## Boundary Table
| red_team_eval IS | red_team_eval IS NOT |
|------------------|----------------------|
| Adversarial safety testing BEFORE deployment | A runtime enforcement boundary (that is guardrail, P11) |
| Tests for attack vulnerabilities with adversarial inputs | A functional end-to-end correctness test (that is e2e_eval) |
| Scoped to attack_types from approved adversarial enum | An isolated unit logic test (that is unit_eval) |
| Produces pass/fail per attack scenario with evidence | A quick sanity check that the system is alive (that is smoke_eval) |
| References OWASP LLM Top 10 vulnerability taxonomy | A comparative performance benchmark (that is benchmark) |
| Config artifact specifying how to run adversarial probes | An implementation of attack logic (that lives in the test runner) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| taxonomy | attack_type, owasp_ref | Classify and trace adversarial threat surface |
| specification | target, pass_criteria | Define what is tested and what safe looks like |
| scenarios | attack_scenario, eval_dataset | Concrete adversarial test cases with placeholder payloads |
| execution | framework_config, severity | Configure eval runner and prioritize risk |
| governance | guardrail | Post-eval runtime enforcement deployed after passing |
| consumers | agent, system_prompt | Runtime components exercised by the eval |
