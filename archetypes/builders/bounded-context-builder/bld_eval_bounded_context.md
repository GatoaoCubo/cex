---
id: bld_qg_bounded_context
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 8.3
tags: [bounded_context, quality-gate, ddd]
title: "Quality Gate: bounded_context"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_agent_computer_interface
  - p11_qg_context_window_config
  - p11_qg_model_registry
  - p11_qg_orchestration_artifacts
  - p11_qg_golden_test
  - p11_qg_handoff
  - p11_qg_formatter
  - p11_qg_kind_builder
  - p11_qg_glossary_entry
  - p10_qg_consolidation_policy
---

## Quality Gate

# Quality Gate: bounded_context
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^bc_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | kind == "bounded_context" | Wrong kind |
| H04 | quality == null | Non-null value |
| H05 | context_name present (PascalCase) | Missing or snake_case |
| H06 | team_owner present and non-empty | Missing |
| H07 | scope_statement present (> 20 chars) | Missing or stub |
| H08 | Aggregates section with >= 1 aggregate | Missing section |
| H09 | scope_statement is SEMANTIC (not technical) | "handles HTTP" or "service that..." |
| H10 | Total file size <= 4096 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | Integration patterns documented | 1.0 | >= 1 pattern with rationale | Patterns listed, no rationale | Absent |
| S02 | domain_vocabulary referenced | 0.9 | dv_{context}_vocabulary present | Reference exists | Absent |
| S03 | Business rules stated | 0.8 | >= 1 invariant within BC | Implied by aggregates | Absent |
| S04 | Domain events published | 0.7 | Events listed with consumers | Events listed | Absent |
| S05 | Context map position | 0.6 | Upstream + downstream neighbors named | One direction | Absent |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Publish to architecture docs; add to context map |
| >= 7.0 | Use for planning; improve integration patterns |
| < 7.0 | Return: add scope statement, aggregates, integration patterns |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
