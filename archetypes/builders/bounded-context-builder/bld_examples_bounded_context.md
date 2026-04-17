---
id: bld_examples_bounded_context
kind: few_shot_example
pillar: P03
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [bounded_context, examples, few-shot]
title: "Examples: bounded_context"
density_score: 1.0
updated: "2026-04-17"
---
# Examples: bounded_context
## Example 1: E-commerce Sales BC
```yaml
id: bc_sales
kind: bounded_context
pillar: P08
title: "Sales Bounded Context"
context_name: Sales
team_owner: sales-squad
scope_statement: "Customer purchase intent to confirmed order; pricing and discount rules apply here."
domain_vocabulary: dv_sales_vocabulary
quality: null
tags: [sales, ecommerce, bounded-context]
```
Aggregates: Order (manages purchase lifecycle), Cart (pre-confirmation state)
Integration: bc_billing (downstream, OHS -- Sales publishes OrderPlaced)
             bc_inventory (upstream, ACL -- Sales insulates from inventory model)
Business rules: Order.total must equal sum(line_items) + tax - discount

## Example 2: CEX Orchestration BC
```yaml
id: bc_cex_orchestration
kind: bounded_context
pillar: P08
title: "CEX Orchestration Bounded Context"
context_name: CexOrchestration
team_owner: n07-orchestrator
scope_statement: "Mission planning, nucleus dispatch, wave orchestration, and consolidation of results."
domain_vocabulary: dv_cex_core_vocabulary
quality: null
tags: [cex, orchestration, n07, bounded-context]
```
Aggregates: Mission (wave plan + dispatch state), HandoffRegistry (active handoffs)
Integration: all nucleus BCs (downstream, OHS -- N07 publishes handoffs)

## Anti-example (WRONG)
```yaml
id: api_gateway_service     # WRONG: this is a deployment component, not a BC
kind: bounded_context       # WRONG: technical boundary != semantic boundary
scope_statement: "handles HTTP requests"  # WRONG: technical, not domain model
```
