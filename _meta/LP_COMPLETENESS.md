# LP Completeness Report

Generated: 2026-03-23 | Avg score: **0.7184** | CEX v2.0 | PYTHA[GOVERNANCE]

Score formula: `(templates% * 0.3) + (examples% * 0.4) + (golden% * 0.2) + (generator * 0.1)`
- **templates%** = types with template / total types
- **examples%** = min(examples_count / types_count, 100%)
- **golden%** = examples with score >= 9.0 / total examples
- **generator** = 1.0 if _generator.md exists

---

## Scores

| LP | Name | Types | Tpl% | Ex% | Gld% | Gen | Score |
|----|------|------:|-----:|----:|-----:|:---:|------:|
| P03 | prompt | 5 | 60.0% | 100.0% | 100.0% | YES | **0.8800** |
| P11 | feedback | 5 | 40.0% | 100.0% | 100.0% | YES | **0.8200** |
| P01 | knowledge | 6 | 33.3% | 100.0% | 100.0% | YES | **0.8000** |
| P10 | memory | 5 | 60.0% | 80.0% | 100.0% | YES | **0.8000** |
| P09 | config | 5 | 40.0% | 80.0% | 100.0% | YES | **0.7400** |
| P06 | schema | 5 | 60.0% | 60.0% | 100.0% | YES | **0.7200** |
| P07 | evals | 6 | 50.0% | 66.7% | 100.0% | YES | **0.7167** |
| P02 | model | 8 | 62.5% | 62.5% | 80.0% | YES | **0.6975** |
| P05 | output | 4 | 25.0% | 75.0% | 100.0% | YES | **0.6750** |
| P12 | orchestration | 6 | 33.3% | 66.7% | 100.0% | YES | **0.6667** |
| P08 | architecture | 5 | 40.0% | 60.0% | 100.0% | YES | **0.6600** |
| P04 | tools | 9 | 22.2% | 44.4% | 50.0% | YES | **0.4444** |

---

## Ranking

| Rank | LP | Name | Score | Bar |
|-----:|----|------|------:|-----|
| 1 | P03 | prompt | 0.8800 | `##################` |
| 2 | P11 | feedback | 0.8200 | `################` |
| 3 | P01 | knowledge | 0.8000 | `################` |
| 4 | P10 | memory | 0.8000 | `################` |
| 5 | P09 | config | 0.7400 | `##############` |
| 6 | P06 | schema | 0.7200 | `##############` |
| 7 | P07 | evals | 0.7167 | `##############` |
| 8 | P02 | model | 0.6975 | `#############` |
| 9 | P05 | output | 0.6750 | `#############` |
| 10 | P12 | orchestration | 0.6667 | `#############` |
| 11 | P08 | architecture | 0.6600 | `#############` |
| 12 | P04 | tools | 0.4444 | `########` |

---

## Gap Analysis — Templates Missing

| LP | Name | Missing Templates | Out of |
|----|------|:-----------------:|:------:|
| P04 | tools | 7 | 9 |
| P12 | orchestration | 4 | 6 |
| P01 | knowledge | 4 | 6 |
| P08 | architecture | 3 | 5 |
| P05 | output | 3 | 4 |
| P09 | config | 3 | 5 |
| P11 | feedback | 3 | 5 |
| P07 | evals | 3 | 6 |
| P02 | model | 3 | 8 |
| P06 | schema | 2 | 5 |
| P10 | memory | 2 | 5 |
| P03 | prompt | 2 | 5 |

**Total gaps: 39 types without templates across 12 LPs**

---

## Priority Recommendations (Top 3 LPs to Invest)

### #1 — P04 Tools (score: 0.4444) — CRITICAL
- Only 2/9 types have templates (hook, plugin, client, cli_tool, scraper, connector, daemon = 7 GAPs)
- Only 4 examples (target: 9+)
- Only 50% golden rate (target: 80%+)
- **Action**: Template sprint: tpl_hook.md, tpl_plugin.md, tpl_client.md (highest usage types first)

### #2 — P08 Architecture (score: 0.6600)
- 3/5 types missing templates (law, diagram, component_map)
- Only 3 examples (target: 5+)
- **Action**: Add tpl_law.md + tpl_diagram.md — architecture patterns are high-leverage for satellite design

### #3 — P12 Orchestration (score: 0.6667)
- 4/6 types missing templates (dag, spawn_config, signal, dispatch_rule)
- Only 4 examples (target: 6+)
- **Action**: Add tpl_signal.md + tpl_dispatch_rule.md — critical for STELLA grid coordination

---

## State Summary

| Metric | Value |
|--------|------:|
| LPs total | 12 |
| LPs above 0.80 | 4 |
| LPs above 0.70 | 7 |
| LPs below 0.50 | 1 (P04) |
| Types total | 69 |
| Types with template | 28 (40.6%) |
| Types missing template | 41 (59.4%) |
| Avg score | 0.7184 |
| All generators present | YES (12/12) |
| Golden rate overall | ~95% |

---

*Regenerate: `python _tools/lp_completeness.py --md > _meta/LP_COMPLETENESS.md`*
