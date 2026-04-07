---
id: p01_kc_guardrail
kind: knowledge_card
type: kind
pillar: P11
title: "Guardrail — Deep Knowledge for guardrail"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: guardrail
quality: 9.1
tags: [guardrail, P11, CONSTRAIN, kind-kc]
tldr: "Declarative safety boundary that blocks, flags, or rewrites outputs violating content, security, or ethics constraints"
when_to_use: "Building, reviewing, or reasoning about guardrail artifacts"
keywords: [safety, constraint, content-filter]
feeds_kinds: [guardrail]
density_score: null
---

# Guardrail

## Spec
```yaml
kind: guardrail
pillar: P11
llm_function: CONSTRAIN
max_bytes: 4096
naming: p11_gr_{{scope}}.yaml
core: true
```

## What It Is
A guardrail is a declarative constraint that wraps agent outputs or inputs with safety checks — blocking forbidden content, flagging policy violations, or rewriting outputs to comply with rules. It defines the violation type, detection method, on-failure action, and escalation. It is NOT permission (P09 — access control, who can do what) nor law (P08 — operational rule governing agent behavior; guardrails are safety-layer content filters).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Guardrails AI integration / `RunnableLambda` filter | Post-LLM validation layer via third-party or custom filter |
| LlamaIndex | Custom `QueryEngine` output filter | Wrap synthesizer output with validator before returning |
| CrewAI | `Task(guardrail=callable)` | Function that validates task output; returns (bool, feedback) |
| DSPy | `dspy.Assert` / `dspy.Suggest` | Assert = hard stop; Suggest = soft rewrite signal |
| Haystack | `ConditionalRouter` content filter branch | Route outputs to content filter component before delivery |
| OpenAI | Moderation API + system prompt safety instructions | `openai.moderations.create()` + refusal patterns in system |
| Anthropic | `system` message safety rules + harmlessness training | Harmlessness/helpfulness/honesty baked in; augment via system |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | output/input/both — wider scope = more coverage, more latency |
| on_failure | enum | block | block/rewrite/flag/escalate — block = safest; rewrite = most UX-friendly |
| detection_method | enum | pattern | pattern/llm-judge/classifier — pattern=fast; llm-judge=accurate |
| violation_types | list | required | List all constraint categories; incomplete list = blind spots |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Hard-block + escalate | PII, credentials, harmful content | `on_failure: block`, `escalation: security_team` |
| Soft-rewrite | Tone/style violations, minor policy issues | `on_failure: rewrite`, LLM rewrites removing violation |
| Layered guardrails | High-stakes outputs | Stack: fast pattern → LLM judge → human review |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Guardrail with no on_failure action | Violation detected but nothing happens | Always specify on_failure; minimum: flag |
| LLM-judge for low-latency paths | Adds 500ms+ per output; user-facing paths stall | Use pattern/regex for fast paths; LLM judge for async |
| Overly broad violation_types: [".*"] | Blocks legitimate content; agent becomes unusable | Define specific violation categories; test with known-good outputs |

## Integration Graph
```
[action_prompt] --> [guardrail] --> [output_parser]
[law] ------------^         |
                      [signal: violation]
```

## Decision Tree
- IF output contains PII/credentials THEN block immediately, escalate
- IF output violates style/tone policy THEN rewrite with LLM correction
- IF detection is latency-sensitive THEN use pattern method, not LLM-judge
- DEFAULT: on_failure: block for safety; on_failure: flag for audit trails

## Quality Criteria
- GOOD: Has scope, violation_types, detection_method, on_failure action, escalation path
- GREAT: Layered detection (fast pattern + LLM judge); violation_types are specific; tested against known cases
- FAIL: No on_failure action; violation_types too broad; no escalation path; blocks without logging

## Production Reference: OpenClaude Guardrails
OpenClaude's guardrail architecture spans two levels:

**Level 1 — System prompt behavioral rules** (getActionsSection):
- Binary blast-radius checklist: reversible? local? visible? destructive? authorized?
- Scope-limited authorization: approval once != approval always
- Root cause over shortcut: do not bypass safety checks
- CEX equivalent: p11_gr_action_reversibility

**Level 2 — Dedicated safety instruction** (cyberRiskInstruction.ts):
- 3 concise rules covering assist/refuse/dual-use boundaries
- Enforcement: warn (not block) for security context nuance
- Bypass: only with clear authorization context
- CEX equivalent: p11_gr_cyber_risk

**Key architectural insight**: OpenClaude separates behavioral guardrails (in the system
prompt, always loaded) from safety guardrails (separate instruction, conditionally loaded).
CEX mirrors this: p03_ins_action_protocol (behavioral, in identity) vs p11_gr_* (safety,
injected for CALL/PRODUCE/COLLABORATE functions).

## New Guardrail Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Binary checklist | Yes/no questions, any "no" triggers enforcement | Blast radius checklist |
| Scope-limited auth | Approval is per-instance, not permanent | Action reversibility |
| Dual-use handling | Same tool can be offensive or defensive, needs context | Cyber risk |
| Warn vs block | Security needs nuance (warn); destruction is absolute (block) | Two enforcement levels |
| Root cause mandate | "Fix the issue, don't bypass the check" | --no-verify anti-pattern |
