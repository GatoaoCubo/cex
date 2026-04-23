---
id: bld_kc_bounded_context
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 7.4
tags: [bounded_context, ddd, context-map, knowledge]
title: "Knowledge: Bounded Context Pattern"
author: builder
density_score: 0.98
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_type_def
  - kc_model_context_protocol
  - bld_collaboration_model_card
---
# Domain Knowledge: bounded_context
## Core Facts
- Evans DDD 2003 ch.14: explicit boundary where a domain model applies
- Within a BC: terms are unambiguous; rules hold consistently; one team owns it
- Across BCs: same word (Account) can mean different things -- no shared global model
- Context Map (ch.14): diagram of all BCs and their integration relationships
- Anti-Corruption Layer: translator between two BCs' models (prevents vocabulary pollution)
- CEX maps each nucleus (N01-N07) to a bounded context with its own vocabulary

## Boundary vs. Similar Concepts
| Aspect | bounded_context | component_map | namespace |
|--------|----------------|---------------|----------|
| Boundary type | Semantic | Deployment | Code |
| Size | Team-sized | Service/pod | Package |
| Vocabulary | Has its own | No vocabulary | No vocabulary |
| Pattern | DDD | Infrastructure | OOP |

## Integration Pattern Decision Tree
- IF this BC must protect itself from upstream model -> ACL
- IF this BC wants to be reused by many consumers -> OHS
- IF this BC is small and can conform to upstream -> CF
- IF two BCs are co-owned by same team -> Partnership
- IF formalized schema needed for cross-BC data -> data_contract (Published Language)

## Anti-Patterns
| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| One model for entire enterprise | Multiple BCs; different models per boundary |
| BC = microservice | One BC may contain many services, or one service may implement parts of many |
| Ignoring context boundaries | Explicit ACL prevents vocabulary corruption |
| No context map | Always draw the map; invisible integration = invisible debt |

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_type_def]] | downstream | 0.17 |
| [[kc_model_context_protocol]] | sibling | 0.16 |
| [[bld_collaboration_model_card]] | downstream | 0.15 |
