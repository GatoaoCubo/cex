---
id: p11_ca_cex_quality_system
kind: conformity_assessment
8f: F7_govern
pillar: P11
title: "Conformity Assessment -- CEX Quality System"
system_name: "CEXAI (Cognitive Exchange AI)"
system_version: "293-kinds"
provider_name: "CEX Open Source Project"
provider_address: "github.com/cexai-project/cex"
provider_contact: "financeiro@gatoaocubo3.com"
annex_iii_category: "not_applicable"
article_43_procedure: "internal_check"
notified_body_id: "N/A"
declaration_date: "2026-04-22"
ce_marking_status: "not_applicable"
eu_ai_act_ref: "EU AI Act 2024/1689"
technical_documentation_reference: "CLAUDE.md + archetypes/builders/"
version: "1.2.0"
quality: 8.4
author: "wave7_n05"
domain: "ai_governance"
tags: [conformity_assessment, quality_system, 8f_pipeline]
created: "2026-04-19"
updated: "2026-04-22"
tldr: "CEXAI internal conformity assessment: 8F pipeline vs. voluntary EU AI Act Art. 9 RMS."
density_score: 0.88
related:
  - p11_qg_ai_rmf_profile
  - bld_schema_conformity_assessment
  - bld_architecture_kind
  - p07_sr_8f_pipeline
  - p11_sp_safety_policy
  - bld_eval_conformity_assessment
  - bld_knowledge_conformity_assessment
  - p07_se_smoke_cex
  - p01_kc_8f_pipeline
  - bld_schema_safety_policy
---

# Conformity Assessment: CEXAI Quality System v293-kinds

Annex III: not_applicable. Orchestration; GPAI delegates inference. Sec. 1-5: [AUG-2026-DEADLINE] per Art. 113(2).

## Sec. 1 -- General Description

| Attribute | Value |
|-----------|-------|
| System type | Typed knowledge orchestration; GPAI delegates inference |
| Scope | 293 kinds, 298 builders, 8 nuclei, 12 pillars, 4 runtimes |
| Transparency | Advisory; user retains control via GDP (Art. 13) |

## Sec. 2 -- Development + Data Governance
| Stage | Implementation | Art. |
|-------|---------------|------|
| F1 | kinds_meta.json (293) + 12 schemas | 10(2) |
| F2-F3 | builders/{kind}/ (12 ISOs) + kc_{kind}.md | 10(3) |
| F7 | H01-H10 gates + 3-layer scoring | 9 |
| F8 | signal_writer.py + compile + git | 12 |
| Accuracy | doctor=0/118; pre-commit=100%; density~71% | 15 |
| Data gap | Ollama multi-step unreliable (R-04) | 10(4) |

## Sec. 3 -- Monitoring and Oversight
| Measure | Implementation | Art. |
|---------|----------------|------|
| Record-keeping | .cex/runtime/signals/+decisions/+git | 12 |
| Override | GDP; dispatch.sh stop (taskkill /F /T) | 14 |
| Interpretability | cex_score.py --explain D1-D5 | 14 |
| Anomaly | cex_hooks.py pre-commit blocks non-conformant | 14|
| Monitoring | cex_quality_monitor.py + cex_doctor.py | 72 |

## Sec. 4 -- RMS (Art. 9)
Iterative. Triggers: new runtime, quality <8.5, --no-verify, doctor FAIL >0.

| ID | Risk | S | L | Mitigation | Res. |
|----|------|---|---|-----------|------|
| R-01 | Hallucinated scores | H | M | quality:null+pre-commit | Low |
| R-02 | Fabricated references | H | M | F3c GROUND+doctor | Low |
| R-03 | Data leakage | C | L | sanitize.py+.gitignore | Low |
| R-04 | Ollama fake-signals | M | H | Multi-runtime+git log | Med |
| R-05 | Grid git race | M | M | Spawn 5s+lock | Low |
| R-06 | Orphan processes | M | H | PID+taskkill /F /T | Low |
| R-07 | Rate limits | M | M | rate_limits.yaml | Low |

Highest residual: R-04. Route to Claude; verify git log.

## Sec. 5 -- PMM (Art. 72)
| KPI | Target | Tool | Action |
|-----|--------|------|--------|
| Doctor FAIL | 0 | cex_doctor.py | Fix in 24h |
| Quality mean | >=8.5 | cex_quality_monitor.py | evolve <8.0 |
| Signal delivery | 100% | signal count | Investigate |
| Pre-commit bypass | 0 | git log | Revoke |
| Density | >=0.85 | cex_score.py | Rewrite |

Incidents: leak->revert; regression->evolve; outage->fallback_chain.

## Sec. 6 -- Standards Applied

| Standard | Ver | Scope |
|----------|-----|-------|
| 8F Pipeline | v1.2 | Primary quality |
| EU AI Act 2024/1689 | 2024 | Voluntary Art. 9/13/14 |
| ISO/IEC 42001 | 2023 | AI management |
| NIST AI RMF | 1.0 | Risk supplementary |
| OWASP LLM Top 10 | 2025 | LLM security |

## Sec. 7 -- Conformity Summary

EU DoC (Art. 47) not required. Internal assessment only.

| Dimension | Status | Evidence |
|-----------|--------|---------|
| Schema enforcement | Conformant | 293 kinds + 12 schemas |
| Quality scoring | Conformant | 3-layer; floor 8.0; target 9.0 |
| Human oversight | Conformant | GDP + quality_monitor + doctor |
| Risk management | Conformant (R-04 Med) | 7 risks, 6 at Low |
| PMM | Conformant | 5 KPIs with thresholds |

Backlog: density >=0.85; Ollama verify; GPAI docs.

## Related Artifacts

| Artifact | Rel | Score |
|----------|-----|-------|
| [[p11_qg_ai_rmf_profile]] | up | 0.52 |
| [[bld_schema_conformity_assessment]] | up | 0.48 |
| [[p11_sp_safety_policy]] | up | 0.45 |
| [[bld_eval_conformity_assessment]] | up | 0.43 |
| [[p01_kc_8f_pipeline]] | up | 0.41 |
| [[bld_architecture_kind]] | up | 0.38 |
| [[p07_sr_8f_pipeline]] | sib | 0.35 |
| [[bld_knowledge_conformity_assessment]] | sib | 0.33 |
| [[p07_se_smoke_cex]] | dn | 0.32 |
| [[bld_schema_safety_policy]] | sib | 0.31 |
