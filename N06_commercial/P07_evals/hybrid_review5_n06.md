---
id: hybrid_review5_n06
kind: knowledge_card
pillar: P01
title: HYBRID_REVIEW5 N06 Audit -- enterprise_sla + white_label_config + usage_report (39 ISOs)
version: 1.0.0
quality: 8.8
tags: [audit, hybrid_review5, n06, enterprise_sla, white_label_config, usage_report, wave4]
domain: commercial quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n06_commercial
mission: HYBRID_REVIEW5
nucleus: n06
related:
  - hybrid_review4_n01
  - hybrid_review7_n04
  - hybrid_review5_n01
  - hybrid_review6_n02
  - hybrid_review5_n05
  - hybrid_review4_n04
  - hybrid_review6_n06
  - hybrid_review3_n05
  - hybrid_review4_n02
  - hybrid_review7_n02
---

# HYBRID_REVIEW5 N06 Audit

## Scope

| Builder | ISOs | Generator | Wave |
|---------|------|-----------|------|
| enterprise-sla-builder | 13 | qwen3:14b (gen_v2) | Wave 4 |
| white-label-config-builder | 13 | qwen3:14b (gen_v2) | Wave 4 |
| usage-report-builder | 13 | qwen3:14b (gen_v2) | Wave 4 |
| **TOTAL** | **39** | | |

---

## F1: Validator Results (pre-fix baseline)

All 3 builders: 13/13 ISOs present, correct naming convention.
Wave validator: structural pass on frontmatter + YAML on all 39 files.

---

## F2: Defect Survey (cross-referenced against master_systemic_defects.md)

### enterprise_sla -- Pre-fix defects

| Defect | ID | Severity | ISO | Finding |
|--------|----|----------|-----|---------|
| D01 system_prompt BECOME | -- | CLEAR | bld_system_prompt | llm_function: BECOME -- correct |
| D02 memory kind | D02 | CRITICAL | bld_memory | kind: learning_record (should be memory) |
| D03 quality_gate runtime metrics | D03 | CRITICAL | bld_quality_gate | H04-H07 check live service uptime/latency/support -- runtime metrics, not artifact structure |
| D07 fabricated tools | D07 | HIGH | bld_tools | cex_analyzer.py, cex_optimizer.py, sla_validator.py, sla_simulator.py, sla_reporter.py, sla_comparator.py -- none exist |
| D10 file ref drift | D10 | HIGH | bld_instruction | References "SCHEMA.md" instead of bld_schema_enterprise_sla.md |
| Commercial gap | N06-LENS | HIGH | bld_knowledge_card | Missing uptime math table (99.9%=43.8min/mo), error budget (Google SRE), RPO/RTO definitions |
| D11 weights | -- | CLEAR | bld_quality_gate | Sum = 1.00 -- correct |
| D05 quality field | -- | CLEAR | bld_schema | quality: null -- correct |

**Pre-fix score: 6.8/10**

### white_label_config -- Pre-fix defects

| Defect | ID | Severity | ISO | Finding |
|--------|----|----------|-----|---------|
| D01 system_prompt BECOME | -- | CLEAR | bld_system_prompt | llm_function: BECOME -- correct |
| D02 memory kind | D02 | CRITICAL | bld_memory | kind: learning_record (should be memory) |
| D03 runtime in soft scores | D03 | HIGH | bld_quality_gate | D05 "Latency < 200ms" -- runtime performance metric in artifact quality scoring |
| D06 ID/pillar mismatch | D06 | HIGH | bld_quality_gate | id: p09_qg_white_label_config but pillar: P11 -- wrong prefix |
| D07 fabricated tools | D07 | HIGH | bld_tools | cex_generator.py, cex_deployer.py, validation_check.py, consistency_validator.py, config_linter.py -- none exist |
| D11 weights sum | D11 | MEDIUM | bld_quality_gate | Weights sum = 0.90 (8 dims at 0.10 each = 0.80 + 0.15+0.15=0.30... actual sum 0.90) |
| Commercial gap | N06-LENS | HIGH | bld_knowledge_card | Missing Stripe Connect sub-account model, OEM licensing, theming API, custom domain/email, reseller margins |

**Pre-fix score: 6.5/10**

### usage_report -- Pre-fix defects

| Defect | ID | Severity | ISO | Finding |
|--------|----|----------|-----|---------|
| D01 system_prompt BECOME | -- | CLEAR | bld_system_prompt | llm_function: BECOME -- correct |
| D02 memory kind | D02 | CRITICAL | bld_memory | kind: learning_record (should be memory) |
| D06 ID/pillar mismatch | D06 | MEDIUM | bld_quality_gate | id: p07_qg_usage_report but pillar: P11 -- wrong prefix |
| D07 fabricated tools | D07 | HIGH | bld_tools | cex_analyzer.py, cex_formatter.py, val_checker.py, val_validator.py, val_reporter.py -- none exist |
| Commercial gap | N06-LENS | HIGH | bld_knowledge_card | Missing showback/chargeback distinction, CSV exports, Snowflake/Databricks, Metabase/Looker, department allocation |

**Pre-fix score: 6.9/10**

---

## F3: Fixes Applied

### All 3 builders

| Fix | ISO | Change |
|-----|-----|--------|
| D02 | bld_memory_*.md | `kind: learning_record` -> `kind: memory`; id `p10_lr_*` -> `p10_mem_*` |
| D07 | bld_tools_*.md | Replaced all fabricated tools with real CEX tools (cex_compile, cex_score, cex_retriever, cex_doctor, cex_wave_validator, cex_hygiene, cex_hooks, cex_sanitize, cex_feedback) |

### enterprise_sla specific

| Fix | ISO | Change |
|-----|-----|--------|
| D03 | bld_quality_gate | Replaced H04-H07 (runtime metrics) with artifact structure checks (service_level_objective field, compliance_requirements list, body sections, quality=null gate) |
| D10 | bld_instruction | "SCHEMA.md" -> `bld_schema_enterprise_sla.md`; "OUTPUT_TEMPLATE.md" -> `bld_output_template_enterprise_sla.md` |
| N06-LENS | bld_knowledge_card | Added: uptime math table (99.0%-99.999% with actual downtime minutes), error budget (Google SRE burn-rate model), RPO/RTO definitions with tier examples |
| SOFT | bld_quality_gate | SOFT scoring rewritten to focus on SLO specificity, uptime math accuracy, error budget coverage, penalty clauses, standards citations |

### white_label_config specific

| Fix | ISO | Change |
|-----|-----|--------|
| D06 | bld_quality_gate | id: `p09_qg_white_label_config` -> `p11_qg_white_label_config` |
| D03+D11 | bld_quality_gate | Removed runtime latency D05; rewrote 7-dimension SOFT scoring (sum=1.00) focused on branding completeness, reseller model, customization depth, compliance, schema validation, security, docs |
| N06-LENS | bld_knowledge_card | Added: Stripe Connect sub-account model section, OEM licensing model, branding components table (custom_domain, email_from_domain, logo, favicon, cobrand_text, theming API), updated patterns + pitfalls |

### usage_report specific

| Fix | ISO | Change |
|-----|-----|--------|
| D06 | bld_quality_gate | id: `p07_qg_usage_report` -> `p11_qg_usage_report` |
| N06-LENS | bld_knowledge_card | Added: showback vs chargeback table with definitions and use cases, department allocation rules (4 types), data export integrations table (Snowflake, Databricks, Metabase, Looker, CSV), updated patterns + pitfalls |

---

## F7: Validator Results (post-fix)

| Builder | ISOs | PASS | FAIL |
|---------|------|------|------|
| enterprise-sla-builder | 13 | 13 | 0 |
| white-label-config-builder | 13 | 13 | 0 |
| usage-report-builder | 13 | 13 | 0 |
| **TOTAL** | **39** | **39** | **0** |

---

## 5D Scoring (post-fix)

### enterprise_sla

| Dim | Dimension | Score | Evidence |
|-----|-----------|-------|---------|
| D1 | Completeness | 9.5 | 13/13 ISOs, all required fields, full body sections |
| D2 | Correctness | 9.0 | All systemic defects fixed; quality_gate now tests artifact structure |
| D3 | Commercial depth | 9.5 | Uptime math table, error budget (SRE model), RPO/RTO, service credits, escalation tiers |
| D4 | Structure | 9.0 | Consistent IDs, schema/body alignment, SOFT weights = 1.00 |
| D5 | Utility | 9.0 | Actionable SLO templates, industry standard citations (ITIL4, ISO20000, SRE) |
| **Total** | | **9.2/10** | Post-fix |

### white_label_config

| Dim | Dimension | Score | Evidence |
|-----|-----------|-------|---------|
| D1 | Completeness | 9.5 | 13/13 ISOs, all fields present |
| D2 | Correctness | 9.0 | D02/D06/D07/D11 all fixed; SOFT scoring coherent |
| D3 | Commercial depth | 9.5 | Stripe Connect sub-account model, OEM licensing, theming API, custom domain/email, reseller margins |
| D4 | Structure | 9.0 | ID/pillar now consistent (p11_qg_*), weights = 1.00 |
| D5 | Utility | 9.0 | Config keys mapped to real deployment concepts (DNS, SPF/DKIM, CSS variables) |
| **Total** | | **9.2/10** | Post-fix |

### usage_report

| Dim | Dimension | Score | Evidence |
|-----|-----------|-------|---------|
| D1 | Completeness | 9.5 | 13/13 ISOs, all fields present |
| D2 | Correctness | 9.0 | D02/D06/D07 fixed; tools all real |
| D3 | Commercial depth | 9.5 | Showback/chargeback table, department allocation, Snowflake/Databricks/Metabase/Looker integrations |
| D4 | Structure | 9.0 | ID/pillar consistent, schema body well-structured |
| D5 | Utility | 9.0 | FinOps Foundation terminology, CSV export, billing model declaration |
| **Total** | | **9.2/10** | Post-fix |

---

## N06 Commercial Lens Verification

### enterprise_sla: Uptime math check
- 99.9% = 43m 50s/mo downtime -- CONFIRMED in KC
- 99.99% = 4m 22s/mo downtime -- CONFIRMED in KC
- Error budget (Google SRE) -- CONFIRMED in KC
- RPO/RTO -- CONFIRMED with tier examples

### white_label_config: Stripe Connect sub-account model
- Platform fee model, connected accounts, OEM licensing -- CONFIRMED in KC
- Custom domain, branded emails, theming API, co-branded UI -- CONFIRMED in KC
- Reseller margin floor -- CONFIRMED in KC

### usage_report: Showback vs. Chargeback
- Showback (visibility) -- CONFIRMED with `billing_model: showback` key
- Chargeback (billing) -- CONFIRMED with department_id, cost_center, allocation_rule
- CSV exports -- CONFIRMED in data export table
- Snowflake/Databricks data share -- CONFIRMED in data export table
- Metabase/Looker dashboards -- CONFIRMED in data export table
- Department allocation -- CONFIRMED with 4 allocation rule types

---

## Wave 4 Commercial Readiness Update

Wave 4 now closes 3 gaps from commercial_readiness_20260413.md:
- `enterprise_sla`: ENTERPRISE tier builder -- production-ready (9.2/10)
- `white_label_config`: ENTERPRISE tier builder -- production-ready (9.2/10)
- `usage_report`: ENTERPRISE tier builder -- production-ready (9.2/10)

These 3 kinds directly support ENTERPRISE tier upsell:
- enterprise_sla: contract-ready SLA templates for regulated industries (legal review gate)
- white_label_config: reseller/OEM platform enablement (Stripe Connect integration)
- usage_report: CFO visibility + chargeback billing for multi-tenant deployments

**GTM Readiness delta**: +3 ENTERPRISE tier builders complete.
Enterprise features score: was 35% -> now 38% (3 more builders production-ready).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review4_n01]] | sibling | 0.45 |
| [[hybrid_review7_n04]] | sibling | 0.43 |
| [[hybrid_review5_n01]] | sibling | 0.38 |
| [[hybrid_review6_n02]] | sibling | 0.37 |
| [[hybrid_review5_n05]] | sibling | 0.35 |
| [[hybrid_review4_n04]] | sibling | 0.35 |
| [[hybrid_review6_n06]] | sibling | 0.35 |
| [[hybrid_review3_n05]] | sibling | 0.34 |
| [[hybrid_review4_n02]] | sibling | 0.33 |
| [[hybrid_review7_n02]] | sibling | 0.32 |
