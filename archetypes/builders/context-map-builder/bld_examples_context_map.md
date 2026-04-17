---
kind: examples
id: bld_examples_context_map
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of context_map artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: null
title: "Examples Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, examples]
tldr: "Golden and anti-examples for context_map construction: BC inventory, relationships with DDD patterns, team coupling."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: context-map-builder

## Golden Example

INPUT: "Map the bounded contexts in our e-commerce platform"

WHY THIS IS GOLDEN:
- id matches `^p08_cm_[a-z][a-z0-9_]+$` -- H02 pass
- contexts_count matches actual count -- H03 pass
- All 4 required sections present -- H06 pass
- Every relationship has pattern, upstream, downstream -- H05 pass
- quality: null -- H01 pass
- integration_type declared for each relationship -- best practice
- team_coupling documented -- H07 pass

```yaml
id: p08_cm_ecommerce_platform
kind: context_map
pillar: P08
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
system_name: "E-Commerce Platform"
contexts_count: 5
quality: null
tags: [context_map, ecommerce, ddd, strategic-design]
tldr: "E-commerce platform: 5 BCs. Orders->Inventory ACL, Payments OHS, Catalog Conformist to Search."
```

## Bounded Contexts

| Context | Team | Core Domain? | Description |
|---------|------|-------------|-------------|
| Orders | Order Team | YES | Order lifecycle: placement, fulfillment, cancellation |
| Inventory | Warehouse Team | YES | Stock levels, reservation, replenishment |
| Payments | Payment Team | YES | Payment processing, refunds, reconciliation |
| Catalog | Content Team | SUPPORTING | Product data, descriptions, pricing |
| Search | Platform Team | GENERIC | Search index, faceting, ranking |

## Relationships

| Upstream (U) | Downstream (D) | Pattern | Integration Type | Notes |
|-------------|----------------|---------|-----------------|-------|
| Inventory | Orders | ACL | sync | Orders wraps Inventory calls through ACL; protects Order model from Inventory changes |
| Payments | Orders | OHS | sync | Payments exposes formal Payment API; Orders consumes it without translation |
| Catalog | Search | Conformist | async | Search adopts Catalog product model directly via Kafka events |
| Orders | Payments | Customer/Supplier | sync | Orders team negotiates payment requirements with Payments team |

## Integration Details

| Relationship | Translation Layer | Protocol | Sync/Async |
|-------------|-----------------|----------|-----------|
| Inventory -> Orders ACL | OrderInventoryTranslator (Orders-owned) | REST | sync |
| Payments -> Orders OHS | PaymentAPI v2 (published language) | REST | sync |
| Catalog -> Search | EventBus (Kafka topic: catalog.product.updated) | Kafka | async |
| Orders -> Payments C/S | PaymentRequestDTO (negotiated schema) | REST | sync |

## Team Coupling

| Relationship | Coupling Level | Risk | Mitigation |
|-------------|----------------|------|-----------|
| Inventory -> Orders (ACL) | Low | Inventory changes isolated by ACL | ACL translator owned by Orders team |
| Payments -> Orders (OHS) | Low | Formal versioned API | Payments team owns API versioning |
| Catalog -> Search (CF) | High | Search breaks if Catalog schema changes | Add ACL if Catalog evolves independently |
| Orders -> Payments (C/S) | Medium | Orders blocked on Payments backlog | Regular sync meetings; SLA for requests |

---

## Anti-Example

INPUT: "Map contexts for our system"
BAD OUTPUT:
```yaml
id: system-map
kind: architecture_diagram
relationships:
  - from: ServiceA
    to: ServiceB
    type: "integration"
quality: 9.0
```

FAILURES:
1. id: "system-map" has hyphens, no p08_cm_ prefix -> H02 FAIL
2. kind: "architecture_diagram" not "context_map" -> H04 FAIL
3. No DDD pattern declared (ACL/OHS/Conformist/etc.) -> H05 FAIL
4. quality: 9.0 (not null) -> H01 FAIL
5. Missing all 4 required sections -> H06 FAIL
6. Missing contexts table, integration_type, team_coupling -> incomplete
7. "from/to" instead of "upstream/downstream" -- wrong DDD terminology
