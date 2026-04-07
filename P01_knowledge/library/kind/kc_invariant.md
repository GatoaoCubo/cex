---
id: p01_kc_invariant
kind: knowledge_card
type: kind
pillar: P08
title: "Law — Deep Knowledge for law"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: law
quality: 9.1
tags: [law, P08, CONSTRAIN, kind-kc]
tldr: "law is an inviolable operational rule with a unique number, severity, scope, and rationale — it cannot be overridden by instruction, context, or convenience."
when_to_use: "Building, reviewing, or reasoning about law artifacts"
keywords: [operational_law, inviolable_rule, constraint]
feeds_kinds: [law]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Invariant

## Spec
```yaml
kind: invariant
pillar: P08
llm_function: CONSTRAIN
max_bytes: 3072
naming: p08_law_{{number}}.md
core: true
```

## What It Is
A law is an inviolable operational rule — once accepted, it cannot be violated regardless of context, instruction, or convenience. It differs from an instruction (P03, flexible guidance that may be overridden) and a guardrail (P11, safety-focused content boundary) in that it governs operational system behavior at the architecture level and is always binary: violated or not.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Callbacks (`OnLLMError`/`OnToolError`) | Hooks enforce behavior but are not inviolable |
| LlamaIndex | `Settings` constraints | Global config constraints; not formally inviolable |
| CrewAI | `guardrail` param on `Task` | Validation function post-task — soft law equivalent |
| DSPy | `dspy.Assert` / `dspy.Suggest` | Assert = hard constraint; Suggest = soft — closest analog |
| Haystack | `ConditionalRouter` | Routes to error handler on violation; not truly inviolable |
| OpenAI | System prompt hard instructions | Hard constraints in system message; model may still deviate |
| Anthropic | System prompt + `tool_choice: none` | Constitutional constraints; strongest provider enforcement |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| number | int | required | Unique, never reused even after deprecation |
| severity | enum | hard | hard (never violate) vs soft (strong default) |
| scope | enum | system | system/agent_group/agent — wider = more agents constrained |
| rationale | string | required | Why drives correct edge-case decisions; missing = ignored |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Safety law | Prevent destructive operations | LAW-01: Never delete files without backup confirmation |
| Routing law | Enforce agent_group specialization | LAW-07: orchestrator orchestrates, never executes tasks |
| Quality law | Minimum output threshold | LAW-12: score < 7.0 → redo; never ship below threshold |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Vague law | "Be careful with data" is not enforceable | Laws must be binary: violated or not — no gray area |
| Law creep | Every guideline promoted to law | Laws are inviolable; preferences belong in instructions |
| No rationale | Laws without rationale get ignored on edge cases | Always document why — drives correct novel-case reasoning |

## Integration Graph
```
decision_record, pattern --> [law] --> agent_card, workflow, permission
                                  |
                             guardrail, instruction, runtime_rule
```

## Decision Tree
- IF violation leads to catastrophic/irreversible outcome THEN hard law
- IF violation degrades quality but is recoverable THEN soft law
- IF applies to all agents in system THEN scope: system
- DEFAULT: hard law, scope: system, numbered sequentially, never renumbered

## Quality Criteria
- GOOD: number, severity, scope, rationale all present; statement unambiguous and binary
- GREAT: violation examples documented, enforcement mechanism named, linked to ADR
- FAIL: vague statement, missing number, no rationale, soft law masquerading as hard
