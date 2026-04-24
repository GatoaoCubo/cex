---
id: sch_validator_n06
kind: validator
8f: F7_govern
pillar: P06
nucleus: n06
title: Revenue Integrity Validator
version: 1.0
quality: 9.0
tags: [schema, validator, quality, pricing, revenue]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_thinking_config
  - bld_schema_pitch_deck
---

<!-- 8F: F1 constrain=P06/validator F2 become=validator-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_validator.md,kc_validator.md,P06_schema/_schema.yaml F4 reason=precommit_validator_for_revenue_integrity_and_density F5 call=apply_patch;python _tools/cex_compile.py F6 produce=5962_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/P06_schema/sch_validator_n06.md -->

# Revenue Integrity Validator

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define the pre-commit and quality-gate rule set that blocks commercially weak or structurally unsafe N06 artifacts |
| Business Lens | Strategic Greed tolerates aggressive monetization, but never sloppy accounting, hidden leakage, or vague offer logic |
| Primary Use | Validate schema and config artifacts before they influence pricing, funnel, or billing behavior |
| Failure Prevented | broken pricing assumptions, fake revenue metrics, under-protected premium flows, low-density boilerplate |
| Trigger | pre-commit, review gate, compile-time audit |
| Outcome | pass, warn, or block with corrective action |

## Schema

| Property | Type | Required | Constraint | Commercial Intent |
|----------|------|----------|------------|-------------------|
| validator_name | string | yes | `revenue_integrity_validator` | stable reference |
| scope | string | yes | `N06_commercial/{schemas,config}` | bounded enforcement |
| rule_type | string | yes | structural plus semantic | catches both form and business weakness |
| severity | string | yes | `error` default | poor monetization contracts must block |
| on_fail | string | yes | `block` | prevents bad config from shipping |
| checks | array | yes | 9 named checks | one validator, many atomic checks |
| bypass_policy | table | yes | explicit approver path | no silent bypass for commercial gates |
| evidence | table | yes | file,line,reason | auditability for review |

## Checks

| Check ID | Condition | Pass Rule | On Fail | Strategic Greed Reason |
|----------|-----------|-----------|---------|------------------------|
| RV01 | frontmatter completeness | required keys present and `quality: null` | block | prevents governance drift |
| RV02 | section completeness | Purpose, Schema or Values, Rationale, Example, Properties exist | block | forces usable commercial docs |
| RV03 | line density | file has >= 80 lines and table-heavy structure | block | rejects lazy filler that hides weak thinking |
| RV04 | ASCII discipline | identifiers and code blocks remain ASCII-only | block | avoids runtime and parsing risk |
| RV05 | monetization specificity | each artifact names pricing, revenue, funnel, margin, retention, or upsell logic | block | generic config is commercially useless |
| RV06 | enum and type consistency | references match declared N06 artifacts | block | avoids broken joins across pricing systems |
| RV07 | value realism | money, limits, and paths cannot be null without rationale | warn | greed needs explicit constraints |
| RV08 | premium defense | enterprise, scale, paid, or secret flows cannot use wildcard access or unlimited defaults | block | premium surfaces deserve tighter controls |
| RV09 | example validity | example must align with artifact rules | block | documentation must be executable in spirit |

## Evaluation Order

| Step | Check Group | Reason |
|------|-------------|--------|
| 1 | RV01 and RV02 | stop immediately if structure is broken |
| 2 | RV03 and RV04 | prevent low-quality or unsafe syntax from continuing |
| 3 | RV05 and RV06 | verify commercial meaning and cross-artifact integrity |
| 4 | RV07 to RV09 | catch realism, premium defense, and example accuracy |

## Bypass Policy

| Field | Rule |
|-------|------|
| Allowed Bypass | no for pre-commit, yes for emergency hotfix review only |
| Approver | N07 plus N06 owner together |
| Evidence Required | incident id, rollback plan, revenue impact estimate |
| Time Limit | 24 hours before full fix |
| Audit Record | mandatory in review note |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Error-first severity | Weak commercial contracts are expensive | blocks revenue mistakes early |
| Density check | Short fluffy docs hide missing constraints | pushes artifacts toward actionability |
| Premium defense rule | High-value accounts deserve stronger rules | protects enterprise margin |
| Example validity | teams copy examples into implementation | reduces monetization misfires |
| Realism warning | some values may vary by environment | still forces declared intent |
| No silent bypass | greed likes speed, but only with traceable risk | keeps aggressive execution auditable |

## Example

| File | Result | Reason |
|------|--------|--------|
| `sch_type_def_n06.md` | pass | has required sections, clear revenue fields, valid example |
| `con_permission_n06.md` | pass | scoped roles and deny rules protect premium resources |
| `draft_config.md` | block | missing Properties section and uses wildcard permissions |

```yaml
validator_name: revenue_integrity_validator
scope:
  - N06_commercial/schemas
  - N06_commercial/config
severity: error
on_fail: block
checks:
  - RV01
  - RV02
  - RV03
  - RV04
  - RV05
  - RV06
  - RV07
  - RV08
  - RV09
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Validator Type | structural_semantic_hybrid |
| Default Severity | error |
| Default Action | block |
| Check Count | 9 |
| Bypass Mode | dual approval only |
| Enforcement Target | schemas and config |
| Commercial Bias | protect margin, MRR, and premium flows |
| Audit Surface | pre-commit and review gate |
| Related Pillars | P06, P09, P11 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.34 |
| [[bld_schema_usage_report]] | related | 0.33 |
| [[bld_schema_benchmark_suite]] | related | 0.32 |
| [[bld_schema_quickstart_guide]] | related | 0.32 |
| [[bld_schema_integration_guide]] | related | 0.32 |
| [[bld_schema_sandbox_config]] | related | 0.31 |
| [[bld_schema_dataset_card]] | related | 0.31 |
| [[bld_schema_multimodal_prompt]] | related | 0.31 |
| [[bld_schema_thinking_config]] | related | 0.31 |
| [[bld_schema_pitch_deck]] | related | 0.31 |
