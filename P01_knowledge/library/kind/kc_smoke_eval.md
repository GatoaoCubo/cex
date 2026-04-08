---
id: p01_kc_smoke_eval
kind: knowledge_card
type: kind
pillar: P07
title: "Smoke Eval — Deep Knowledge for smoke_eval"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: smoke_eval
quality: 9.1
tags: [smoke_eval, P07, GOVERN, kind-kc]
tldr: "Fast <30s sanity check confirming a pipeline starts and returns a non-empty, structurally valid output."
when_to_use: "Building, reviewing, or reasoning about smoke_eval artifacts"
keywords: [smoke, sanity, fast-check, startup, deploy-gate]
feeds_kinds: [smoke_eval]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["smoke test", "sanity check", "health check", "startup test", "deploy gate"]
user_says: ["quick sanity check", "verificacao rapida", "is it alive", "run a smoke test", "check if it starts"]
long_tails: ["I just deployed and need to verify the system is alive", "run a fast check to confirm the API responds before running full tests", "make sure the agent boots and returns something valid in under 30 seconds", "create a deploy gate that checks basic functionality"]
cross_provider:
  langchain: "chain.invoke('test') + non-null check"
  llamaindex: "query_engine.query('test') + exists check"
  crewai: "crew.kickoff({'input':'test'}) + output check"
  dspy: "program('test') + output check"
  openai: "chat.completions.create(minimal) + role check"
  anthropic: "messages.create(minimal) + content check"
  haystack: "pipeline.run({'query':'test'}) + key check"
---

# Smoke Eval

## Spec
```yaml
kind: smoke_eval
pillar: P07
llm_function: GOVERN
max_bytes: 3072
naming: p07_se_{{scope}}.md
core: false
```

## What It Is
A minimal, fast-running test that confirms the system starts, responds, and returns structurally valid output in under 30 seconds. Tests THAT something works, not HOW WELL. NOT unit_eval—unit_eval tests deep correctness with scoring; smoke_eval only checks "is it alive?". NOT benchmark—benchmark tracks performance distribution; smoke_eval is a single-shot sanity check.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | chain.invoke("test") | Minimal invocation + non-null check |
| LlamaIndex | query_engine.query("test") | Basic query + response exists check |
| CrewAI | crew.kickoff({"input":"test"}) | Single kickoff, output is not None |
| DSPy | program("test") | Single forward pass + output check |
| Haystack | pipeline.run({"query":"test"}) | Minimal run + output key check |
| OpenAI | chat.completions.create(minimal) | Single call + role/content check |
| Anthropic | messages.create(minimal) | Single call + content block check |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| max_seconds | int | 30 | Lower = faster CI, may miss slow starts |
| assertions | list[str] | [not_empty] | More assertions = slower, more coverage |
| scope | str | required | "api", "agent", "pipeline", "tool" |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Deploy gate | Run after deploy to verify live | p07_se_api.md -> check /health + /invoke |
| Agent startup | Confirm agent boots + responds | p07_se_agent_boot.md |
| CI fast path | First gate before slow unit_evals | Smoke -> unit_eval -> e2e_eval |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Deep assertions in smoke | Defeats <30s purpose, becomes unit_eval | Only structural/non-empty checks |
| No time limit | Hangs in CI on broken deploys | Always set max_seconds: 30 |
| Skipping smoke, running e2e | Slow, expensive, hard to debug | Always smoke first |

## Integration Graph
```
[deployment] --> [smoke_eval] --> [pass: proceed to unit_eval]
                     |----------> [fail: alert + rollback trigger]
                     |----------> [quality_gate (P11) minimal]
```

## Decision Tree
- IF verifying system is alive after deploy (<30s) THEN smoke_eval
- IF testing correctness of one agent in depth THEN unit_eval
- IF testing full pipeline THEN e2e_eval
- DEFAULT: smoke_eval as first gate in any CI/CD pipeline

## Quality Criteria
- GOOD: Runs in <30s, checks non-empty output, scope defined
- GREAT: Checks structural validity, used as CI first gate, named by scope
- FAIL: Takes >60s, includes scoring logic, asserts on content quality not structure
