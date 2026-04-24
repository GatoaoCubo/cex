---
id: ex-validator-inventory-invariants
kind: validator
8f: F7_govern
pillar: P06
title: Inventory Invariants Validator
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_RECONCILE_TOLERANCE
  - BRAND_BLING_DEPOSITS
tags: [commerce, template, distillation, validator, inventory, invariants]
density_score: 0.94
related:
  - p03_ins_validator
  - p11_qg_validator
  - p06_security_validation_schema
  - p03_sp_validator-builder
  - extraction_gate_severity
  - bld_memory_validator
  - bld_examples_validator
  - bld_knowledge_card_guardrail
  - validator-builder
  - p11_gr_{{SCOPE_SLUG}}
---

# Inventory Invariants Validator

## Purpose
Declarative rule set that the reconcile workflow runs before any write. Each rule checks a cross-channel or intra-row inventory invariant; a failure either downgrades the mode (auto -> propose) or aborts the run. These rules are what keep a bad sync from writing garbage into the ERP.

## When to use
- Consumed by `ex_workflow_inventory_reconcile.md` step 5.
- Invoked manually from the admin UI during incident response ("run invariants").
- Used in CI as a contract test on a golden-dataset fixture.

## Interface
```ts
validate(rows: NormalizedInventoryRow[]): {
  passed: Rule[],
  failed: RuleViolation[],
  warnings: RuleViolation[],
}
```
`RuleViolation = { rule_id, sku, channel_values, expected, actual, severity }`.

## Brand variables used
- `{{BRAND_NAME}}` -- labels per-violation row for operator reports.
- `{{BRAND_RECONCILE_TOLERANCE}}` -- referenced in rule `R3`.
- `{{BRAND_BLING_DEPOSITS}}` -- rule `R5` uses this list.

## Rules

### R1. No negative inventory
- **Check:** `supabase.quantity >= 0 AND bling.quantity >= 0 AND shopify.quantity >= 0`.
- **Severity:** hard-fail (abort run).
- **Why:** negative stock is always a bug, never a legitimate state.

### R2. Missing in ERP but present elsewhere
- **Check:** if a SKU has stock in Shopify OR Supabase but does not exist in Bling, flag.
- **Severity:** warning (reconcile skips this SKU; run continues).
- **Resolution:** route to `bling-create-missing` workflow.

### R3. Drift within tolerance is a warning, not a fix
- **Check:** if |delta| <= `{{BRAND_RECONCILE_TOLERANCE}}`, do not auto-correct.
- **Severity:** info (logged only).
- **Why:** constant small deltas are normal (in-flight orders); fixing them generates thrash.

### R4. Catastrophic drift triggers downgrade
- **Check:** if > 25% of catalog shows |delta| > tolerance, downgrade mode `auto_correct` to `propose`.
- **Severity:** soft-fail (mode downgrade).
- **Why:** systemic issue (bad Bling backfill, wrong deposit list) -- need human eyes.

### R5. Deposit list completeness
- **Check:** Bling response covers all deposits in `{{BRAND_BLING_DEPOSITS}}`; missing deposits -> skip SKU.
- **Severity:** warning.
- **Why:** partial data would yield wrong totals; better to skip than to push wrong numbers.

### R6. Stale data guard
- **Check:** channel data's `fetched_at` is within 15 min of run start.
- **Severity:** hard-fail if stale (abort; channel likely unreachable).

### R7. Monotonic-only corrections
- **Check:** when auto-correcting, refuse to write a number >2x the prior Supabase value without explicit operator confirmation.
- **Severity:** soft-fail (row held for review).
- **Why:** huge jumps (10 -> 10000) are usually a Bling data bug; better to pause than to overstock ads.

### R8. Zero-stock broadcast guard
- **Check:** if a correction would zero out a SKU currently advertised in a paid campaign (join `products.in_campaign`), require operator confirmation.
- **Severity:** soft-fail.
- **Why:** ad dollars on an out-of-stock SKU is wasted spend.

## Rule authoring notes
- Each rule is a pure function with no side effects.
- New rules require a golden-dataset case showing both a passing and failing example.
- Rules are versioned with the validator; breaking changes require a bumped `validator_version`.

## Related artifacts
- `ex_workflow_inventory_reconcile.md` -- primary consumer.
- `ex_interface_supabase_tables.md` -- row shape reference.
- `ex_dispatch_rule_multi_marketplace.md` -- authority rules invoked alongside invariants.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_validator]] | upstream | 0.25 |
| [[p11_qg_validator]] | related | 0.24 |
| [[p06_security_validation_schema]] | sibling | 0.23 |
| [[p03_sp_validator-builder]] | upstream | 0.22 |
| [[extraction_gate_severity]] | related | 0.22 |
| [[bld_memory_validator]] | downstream | 0.21 |
| [[bld_examples_validator]] | downstream | 0.21 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.19 |
| [[validator-builder]] | related | 0.19 |
| [[p11_gr_{{SCOPE_SLUG}}]] | downstream | 0.19 |
