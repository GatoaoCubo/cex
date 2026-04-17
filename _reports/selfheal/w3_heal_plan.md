---
id: w3_heal_plan
kind: audit_log
pillar: P11
title: SELFHEAL W3 -- Heal Plan
version: 1.0.0
created: 2026-04-15
author: n03_engineering
quality: 9.0
mission: SELFHEAL
wave: 3
nucleus: n03
picks: 10
sources:
  - _reports/selfheal/w2_n01_diagnosis.md
  - _reports/selfheal/w2_n05_diagnosis.md
density_score: 1.0
---

# SELFHEAL W3 -- Heal Plan

> **N03 Engineering | Wave 3 | 2026-04-15**
> TOP 10 defects selected from W2 N01 (semantic) + W2 N05 (structural).
> Selection: trivial first, medium to fill slots, zero hard.

## Selection Summary

| effort | count | decisions |
|--------|-------|-----------|
| trivial | 2 | patch (frontmatter + field update) |
| medium | 8 | 3 patch (content qualifiers) + 5 regenerate (FAIL builder density) |
| hard | 0 | (excluded by rule) |

## Heal Plan (ranked)

| rank | path | defect | decision | command | rationale |
|------|------|--------|----------|---------|-----------|
| 1 | `P11_feedback/examples/p11_content_monetization_faz_um_crm_pra_pet_shop.md` | missing `quality` key (has id/kind/pillar) | patch | `edit frontmatter: add 'quality: null'` | trivial; 1-line fix; unblocks P11 example scan |
| 2 | `N04_knowledge/P01_knowledge/rag_source_knowledge.md` | `last_checked: 2024-03-30` stale for live RAG source | patch | `edit frontmatter: set last_checked: 2026-04-15` | trivial; freshness field; no content change |
| 3 | `N05_operations/P01_knowledge/kc_ollama_deployment_guide.md` | hardcoded `v0.3.7` (Apr 2024); Ollama now v0.6.x | patch | `edit body: remove version pin, reference "latest stable"` | medium; version drift; avoids future re-stale |
| 4 | `N06_commercial/P01_knowledge/kc_ai_saas_monetization.md` | 2023 Gartner/Forrester/IDC stats unqualified | patch | `edit body: append "as of 2023" to all % claims + Gartner 2025 note` | medium; H semver drift (72%->84% usage-based) |
| 5 | `N06_commercial/P01_knowledge/kc_ai_compliance_gdpr.md` | EU AI Act (2025) absent from GDPR coverage | patch | `edit body: add 1-line section "EU AI Act (2025) -- high-risk AI systems"` | medium; compliance gap; legal risk if cited |
| 6 | `archetypes/builders/agent-grounding-record-builder/` | density <0.78 on 3 ISOs; 2 files >6144B | regenerate | `python _tools/cex_8f_runner.py --kind agent_grounding_record --rebuild-iso` | medium; FAIL status blocks doctor clean |
| 7 | `archetypes/builders/agent-name-service-record-builder/` | density <0.78 on 3 ISOs; 2 files >6144B | regenerate | `python _tools/cex_8f_runner.py --kind agent_name_service_record --rebuild-iso` | medium; FAIL status; sibling of #6, same pattern |
| 8 | `archetypes/builders/conformity-assessment-builder/` | density <0.78 on 3 ISOs; 2 files >6144B | regenerate | `python _tools/cex_8f_runner.py --kind conformity_assessment --rebuild-iso` | medium; FAIL status; compliance-critical kind |
| 9 | `archetypes/builders/contributor-guide-builder/` | density <0.78 on 3 ISOs; 1 file >6144B | regenerate | `python _tools/cex_8f_runner.py --kind contributor_guide --rebuild-iso` | medium; FAIL status; docs-kind verbose boilerplate |
| 10 | `archetypes/builders/webinar-script-builder/` | density <0.78 on 3 ISOs; 1 file >6144B | regenerate | `python _tools/cex_8f_runner.py --kind webinar_script --rebuild-iso` | medium; FAIL status; last of 5 FAIL cluster |

## Execution Notes

- **Ranks 1-5 (patch)** are safe for a single N04/N05 pass; no dependency chain.
- **Ranks 6-10 (regenerate)** share the same root cause (verbose scaffold boilerplate). Dispatch to N03 as a batch; density target 0.85+.
- **Out of scope (deferred)**: `kc_email_html_responsive.md` (P3 optional), 22 `quality:null` (peer-review queue, expected), 63 WARN builders (compaction pass, low priority), ~900-file coverage gap (W4 extended scan).

## Expected Post-W3 State

| metric | pre-W3 | post-W3 target |
|--------|--------|----------------|
| FAIL builders | 5 | 0 |
| W2 heal priority queue (P1-P3) | 6 open | 1 open (email qualifier) |
| doctor:zero_fail gate | FAIL | PASS |
| total defects cleared | -- | 10 |

## Next Wave

W4 should dispatch:
- **N01** -> P12_orchestration (~138 files, high stale risk)
- **N04** -> P11_feedback (~55 files, quality gate drift)
- **N03** -> 63 WARN builder compaction (size >6144B cluster)
