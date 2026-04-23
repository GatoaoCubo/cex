---
kind: quality_gate
id: p11_qg_context_map
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of context_map artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: context_map"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, context-map, P08, ddd, bounded-context]
tldr: "Pass/fail gate for context_map: id pattern, contexts table, relationships with DDD patterns, team coupling."
domain: "context map -- DDD BC relationship diagram"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_retriever_config
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_constraint_spec
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_effort_profile
  - p11_qg_hook_config
  - p11_qg_component_map
---

## Quality Gate

# Gate: context_map

## Definition

| Field | Value |
|---|---|
| metric | context_map artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: context_map` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p08_cm_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p08_cm_foo but file is p08_cm_bar.md |
| H04 | Kind equals literal `context_map` | kind: architecture_diagram or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | All relationships have upstream, downstream, pattern | Missing any of these three fields |
| H07 | Pattern values are valid DDD patterns | Using "integration" instead of ACL/OHS/etc. |
| H08 | contexts_count matches body count | Declared 5 but listed 3 |
| H09 | Body has all 4 required sections | Missing any of 4 sections |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| Pattern completeness | 1.0 | Every relationship has a valid DDD pattern |
| Integration type | 1.0 | sync/async/batch declared for all relationships |
| Team ownership | 1.0 | Owning team identified for each BC |
| Team coupling documented | 1.0 | Coupling level + risk + mitigation per relationship |
| ACL translation layers | 1.0 | ACL relationships identify the translator owner |
| OHS protocol reference | 1.0 | OHS relationships reference the published language/API |
| Conformist risk flag | 1.0 | Conformist relationships annotated with migration plan |
| System coverage | 1.0 | All BCs in the system are included |
| Boundary clarity | 1.0 | Explicitly NOT bounded_context, NOT component_map |
| tldr quality | 0.5 | tldr <= 160ch, includes system name and key patterns |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
