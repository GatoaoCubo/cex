---
id: p01_kc_red_team_eval
kind: knowledge_card
type: kind
pillar: P07
title: "Red Team Eval — Deep Knowledge for red_team_eval"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: red_team_eval
quality: 9.1
tags: [red_team_eval, P07, GOVERN, kind-kc]
tldr: "Adversarial safety and robustness test probing LLM systems against jailbreaks, injection, and policy violations."
when_to_use: "Building, reviewing, or reasoning about red_team_eval artifacts"
keywords: [red-team, adversarial, safety, jailbreak, injection]
feeds_kinds: [red_team_eval]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Red Team Eval

## Spec
```yaml
kind: red_team_eval
pillar: P07
llm_function: GOVERN
max_bytes: 2048
naming: p07_redteam.md
core: false
```

## What It Is
An adversarial evaluation protocol targeting security, safety, and robustness vulnerabilities—prompt injection, jailbreaks, policy violations, data leakage, and hallucination under adversarial prompts. NOT e2e_eval (tests functional correctness under normal inputs, not attacks). Treats the system as an adversary would: trying to elicit unsafe, unintended, or policy-violating behavior.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Custom adversarial dataset | Manual attack test cases |
| LlamaIndex | GuardrailsEvaluator | Policy violation detection |
| CrewAI | Safety guardrail test | Agent output safety check |
| DSPy | Adversarial assert | Assert model refuses attack prompts |
| Haystack | ContentFilterEvaluator | Built-in safety content filter |
| OpenAI | Red teaming guidelines | OpenAI red teaming framework |
| Anthropic | Constitutional AI eval | Harmlessness + helpfulness evaluation |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| attack_types | list[str] | required | More types = thorough but time-intensive |
| severity | enum | high | high = block on any fail, medium = log |
| automated | bool | false | Auto attacks miss creative exploits |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Jailbreak sweep | Test system prompt extraction | p07_redteam.md with jailbreak_types |
| Injection probe | Test against prompt injection | User input containing role overrides |
| Data leakage check | Test for PII or secret exposure | attack_types: [pii_leak, secret_exposure] |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Only automated attacks | Misses creative human exploits | Include manual review of attack surface |
| Conflating with e2e_eval | Normal inputs != adversarial | Keep red_team in separate test run |
| No attack documentation | Can't reproduce or update attacks | Document each attack_type with examples |

## Integration Graph
```
[attack_types catalog] --> [red_team_eval] --> [safety report]
[validator (safety)] -----> [red_team_eval]         |
                                 |-----------> [quality_gate (P11)]
```

## Decision Tree
- IF testing functional correctness under normal use THEN e2e_eval or unit_eval
- IF testing security, safety, robustness under attack THEN red_team_eval
- DEFAULT: red_team_eval for any public-facing LLM system before production

## Quality Criteria
- GOOD: attack_types documented, severity set, pass criteria defined
- GREAT: Mix of automated + manual attacks, linked to validator (P06), severity tiered
- FAIL: Only happy-path safety check, no attack documentation, no severity rating
