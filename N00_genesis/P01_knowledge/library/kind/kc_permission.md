---
id: p01_kc_permission
kind: knowledge_card
type: kind
pillar: P09
title: "Permission — Deep Knowledge for permission"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: permission
quality: 9.1
tags: [permission, P09, GOVERN, kind-kc]
tldr: "permission is a structured access control rule binding a subject (agent/agent_group) to allowed actions (read/write/execute/spawn) on resources — with explicit deny rules overriding allows."
when_to_use: "Building, reviewing, or reasoning about permission artifacts"
keywords: [access_control, RBAC, agent_permissions]
feeds_kinds: [permission]
density_score: null
---

# Permission

## Spec
```yaml
kind: permission
pillar: P09
llm_function: GOVERN
max_bytes: 3072
naming: p09_perm_{{scope}}.yaml
core: true
```

## What It Is
A permission is a structured access control rule specifying who (subject) can do what (actions) on which resources — with explicit deny rules that override allows. It is NOT a guardrail (P11, which is a safety/content boundary), NOT a feature_flag (which is binary capability on/off without subject-resource binding).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Tool callbacks (`OnToolStart`) | Can block tool invocation — approximate permission |
| LlamaIndex | N/A | No formal permission; tool access via agent config only |
| CrewAI | `allow_delegation` flag | Boolean per-agent delegation permission |
| DSPy | N/A | No permission system; access controlled by code structure |
| Haystack | Pipeline topology | Component access implicit in connect() wiring |
| OpenAI | `tool_choice: none` | Disables all tool access per-request; coarse-grained |
| Anthropic | `tool_choice` + system prompt | Restrict tool use per-request; enforcement via system block |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | system/agent_group/agent — wider = harder to audit |
| subject | string | required | Who — never use wildcard `*` without explicit justification |
| actions | list[enum] | required | read/write/execute/spawn/delete — minimum viable set |
| deny | list[PermRule] | [] | Explicit denies override all allows — missing = no exceptions |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Agent_group isolation | Agent_group writes only to its own signal/output paths | `subject: atlas, actions: [write], resources: [records/signals/atlas*]` |
| Tool whitelist | Agent may only call approved tools | `subject: scout, actions: [execute], resources: [glob, grep, read]` |
| Spawn gate | Only orchestrator may spawn agent_groups | `subject: stella, actions: [spawn], resources: [*]` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| God permissions | `subject: *, actions: [*]` is security theater | Always scope to minimum required per subject |
| No deny rules | Permissions without denies cannot express exceptions | Model deny-over-allow when exceptions exist |
| Unenforced permission | Permission config not wired to runtime check | Must link to runtime_rule or law with enforcement mechanism |

## Integration Graph
```
law, feature_flag --> [permission] --> agent_card, runtime_rule, path_config
                           |
                      guardrail, env_config, law
```

## Decision Tree
- IF controlling filesystem read/write THEN path_config + permission together
- IF controlling which tools an agent may call THEN permission on `actions: [execute]`
- IF controlling agent spawn rights THEN permission on `actions: [spawn]`
- DEFAULT: whitelist model (deny all, allow specific); minimum viable actions per subject

## Quality Criteria
- GOOD: subject, actions, resources all explicit; no unjustified wildcards
- GREAT: deny rules documented, enforcement mechanism named, audit trail specified
- FAIL: `subject: *`, wildcard resources without justification, no deny rules, no enforcement link
