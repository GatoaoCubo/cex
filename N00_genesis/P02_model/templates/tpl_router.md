---
id: p02_rt_SCOPE_SLUG
kind: router
pillar: P02
version: 1.0.0
title: "Template — Router"
tags: [template, router, dispatch, routing, classification]
tldr: "Routes incoming requests to the correct agent or handler based on conditions. Priority-ordered rules with a mandatory fallback. Prevents routing loops."
routes:
  - when: "[CONDITION_1]"
    send_to: "[TARGET_1]"
  - when: "[CONDITION_2]"
    send_to: "[TARGET_2]"
fallback: "[DEFAULT_TARGET]"
quality: 9.0
updated: "2026-04-07"
domain: "model configuration"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - bld_memory_router
  - p11_qg_router
  - bld_collaboration_router
  - p03_ins_router
  - p01_kc_dispatch_rule
  - bld_knowledge_card_dispatch_rule
  - bld_schema_dispatch_rule
  - p01_kc_router
  - bld_knowledge_card_router
  - router-builder
---

# Router: [SCOPE_SLUG]

## Routes
Order: most specific → most general. First match wins.

| Priority | Condition | Target | Confidence | Reason |
|----------|-----------|--------|------------|--------|
| 1 | [CONDITION_1] | [TARGET_1] | [0.9+] | [JUSTIFICATION] |
| 2 | [CONDITION_2] | [TARGET_2] | [0.8+] | [JUSTIFICATION] |
| 3 | [CONDITION_3] | [TARGET_3] | [0.7+] | [JUSTIFICATION] |

## Routing Logic
```
Input → Classify(intent) → Match(routes, priority_order) → Dispatch(target)
  └─ If no match: Fallback(default_target)
  └─ If confidence < threshold: Ask_Clarification || Fallback
```

## Fallback
- **Target**: [DEFAULT_TARGET]
- **Trigger**: No route matches OR confidence below [THRESHOLD]
- **Anti-loop**: Max [3] redirects per request. After that → error response.

## Classification Method
- **Type**: [rule_based | embedding_similarity | llm_classification]
- **Model**: [N/A for rules | model_name for ML]
- **Confidence threshold**: [0.7 — below this, use fallback]

## Observability
```yaml
log_fields:
  router_id: "[SCOPE_SLUG]"
  input_hash: "[SHA256[:8]]"
  matched_route: "[PRIORITY_N]"
  target: "[TARGET]"
  confidence: [FLOAT]
  latency_ms: [INT]
```

## Quality Gate
- [ ] At least 2 routes defined (1 route = no routing needed)
- [ ] Fallback defined (mandatory)
- [ ] Anti-loop limit set
- [ ] Routes ordered by specificity (most specific first)
- [ ] No overlapping conditions (deterministic matching)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_router]] | downstream | 0.35 |
| [[p11_qg_router]] | downstream | 0.34 |
| [[bld_collaboration_router]] | related | 0.33 |
| [[p03_ins_router]] | related | 0.32 |
| [[p01_kc_dispatch_rule]] | downstream | 0.32 |
| [[bld_knowledge_card_dispatch_rule]] | upstream | 0.31 |
| [[bld_schema_dispatch_rule]] | downstream | 0.29 |
| [[p01_kc_router]] | related | 0.27 |
| [[bld_knowledge_card_router]] | related | 0.27 |
| [[router-builder]] | related | 0.27 |
