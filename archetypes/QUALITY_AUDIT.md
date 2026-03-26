# CEX Quality Audit — 48 Examples
**Audited**: 2026-03-22 | **Auditor**: PYTHA | **Method**: Manual content review

## Scoring Criteria

| Score | Tier | Criteria |
|-------|------|----------|
| 10.0 | Golden | Real data, 100% actionable, density >= 0.95, zero issues |
| 9.5 | Golden | Real data, fully actionable, density >= 0.88, minor or no issues |
| 9.0 | Skilled | Good data, actionable, density >= 0.85, small gaps |
| 8.5 | Skilled | Mostly specific, density >= 0.82, 1-2 genericity issues |
| 8.0 | Skilled | Functional, density >= 0.80, at least 1 missing section |
| 7.0-7.9 | Learning | Works but too generic or incomplete |
| < 7.0 | Rejected | Critical sections missing or no frontmatter |

---

## Full Audit Table

| File | LP | Score | Density | Issues |
|------|:--:|:-----:|:-------:|--------|
| p01_kc_agent_orchestration_quickstart.md | P01 | 9.0 | 0.90 | No code examples, patterns abstract only |
| p01_kc_catalogo_proprio_mercado_livre.md | P01 | 8.0 | 0.92 | `## Flow` section is EMPTY |
| p01_kc_cicd_pipeline_architecture.md | P01 | 9.0 | 0.87 | No concrete GitHub Actions YAML |
| p01_kc_claude_coding_skills.md | P01 | 8.5 | 0.85 | Skill YAML template is skeleton, not real example |
| p01_kc_quality_gate_implementation.md | P01 | 9.0 | 0.88 | Good |
| p01_kc_test_chain_validation.md | P01 | 8.5 | 0.88 | CEX-meta self-referential, limited external reuse |
| p01_kc_zero_touch_execution.md | P01 | 9.5 | 0.89 | Golden reference — TAC-8 complete, real retry YAML |
| p02_agent_amazon_ads.md | P02 | 9.0 | 0.86 | Good |
| p02_agent_catalogo_ml_strategy.md | P02 | 9.0 | 0.88 | Good |
| p02_agent_gateway.md | P02 | 9.0 | 0.87 | Good |
| p02_agent_pesquisa.md | P02 | 6.5 | 0.40 | `## Architecture` EMPTY, no I/O schema, missing `when_not_to_use` |
| p03_pt_action_prompt.md | P03 | 5.0 | 0.60 | `## Template Body` EMPTY — core section missing |
| p03_pt_catalogo_ml_strategy.md | P03 | 9.5 | 0.90 | Golden reference — full template + user prompts + I/O example |
| p03_pt_satellite_orchestrator.md | P03 | 9.5 | 0.91 | Golden reference — complete with 2 I/O examples |
| p03_pt_sdk_agent_builder.md | P03 | 9.0 | 0.89 | Good |
| p04_skill_design_extractor.md | P04 | 9.0 | 0.86 | Good |
| p04_skill_ml_ads.md | P04 | 9.5 | 0.91 | Golden reference — real BR marketplace data, funnel thresholds |
| p04_skill_voice_pipeline.md | P04 | 9.0 | 0.85 | Good |
| p05_fmt_agent_markdown.md | P05 | 9.0 | 0.88 | Good |
| p05_nr_cex_naming.md | P05 | 9.0 | 0.90 | Minor: Windows absolute path embedded in `source` field |
| p05_os_security_audit.md | P05 | 9.5 | 0.92 | Golden reference — nested Finding schema, valid/invalid JSON |
| p06_iface_satellite_handoff.md | P06 | 9.5 | 0.91 | Golden reference — complete contract with all field constraints |
| p06_is_quality_audit.md | P06 | 9.0 | 0.90 | Good |
| p06_val_quality_score.md | P06 | 9.5 | 0.89 | Golden reference — QS-001 to QS-004 rules with on_fail actions |
| p07_gt_stripe_pipeline.md | P07 | 9.5 | 0.93 | Golden reference — 4 test suites, PASS/FAIL tables, assertions |
| p07_se_brain_query.md | P07 | 9.0 | 0.88 | Good |
| p07_sr_5d_scoring.md | P07 | 9.0 | 0.91 | Minor: tldr has "Density + Density" (D1 duplicated) |
| p08_law_shokunin.md | P08 | 9.5 | 0.93 | Golden reference — inviolable rules, wrong/right examples |
| p08_pat_continuous_batching.md | P08 | 9.5 | 0.92 | Golden reference — measured 1.6x speedup, diagram, constraints |
| p08_sat_edison.md | P08 | 9.0 | 0.91 | Good |
| p09_env_firecrawl.md | P09 | 9.0 | 0.88 | Good |
| p09_ff_firecrawl_enabled.md | P09 | 9.0 | 0.90 | Good |
| p09_path_codexa_repos.md | P09 | 9.0 | 0.90 | Minor: hardcoded Windows paths (not portable) |
| p09_rr_satellite_spawn.md | P09 | 9.5 | 0.91 | Golden reference — YAML hard limits, correct/wrong spawn examples |
| p10_ax_scout_before_create.md | P10 | 9.5 | 0.93 | Golden reference — decision threshold, violations table, bash impl |
| p10_bi_codexa_brain.md | P10 | 9.0 | 0.89 | Good |
| p10_lr_continuous_batching.md | P10 | 9.0 | 0.91 | Good |
| p10_mm_edison.md | P10 | 9.5 | 0.92 | Golden reference — domain map with confidence scores, routing table |
| p11_bl_satellite_execution.md | P11 | 9.0 | 0.90 | Good |
| p11_gr_stella_dispatch.md | P11 | 9.0 | 0.90 | Good |
| p11_lc_cex_lifecycle.md | P11 | 6.5 | N/A | NO FRONTMATTER — missing id, type, quality, density_score entirely |
| p11_opt_pool_density.md | P11 | 9.0 | 0.88 | Good |
| p11_qg_cex_quality.md | P11 | 6.5 | N/A | NO FRONTMATTER — missing id, type, quality, density_score entirely |
| p11_qg_shokunin_pool.md | P11 | 9.5 | 0.93 | Golden reference — tier table, checklist, scoring formula, bypass=never |
| p12_dag_cex_wave_pipeline.md | P12 | 9.0 | 0.90 | Minor: Windows path embedded in `source` field |
| p12_ho_isofix_batch.md | P12 | 9.0 | 0.91 | Good |
| p12_spawn_grid_continuous.md | P12 | 9.0 | 0.89 | Good |
| p12_wf_stella_dispatch.md | P12 | 9.5 | 0.93 | Golden reference — 5 phases, duration estimates, rollback table |

---

## Score Distribution (Density Histogram)

```
9.0-10.0: ████████████████████ (41 examples — 85.4%)
8.0-8.9:  ██                   (3 examples  —  6.3%)
7.0-7.9:                       (0 examples  —  0.0%)
<7.0:     ██                   (4 examples  —  8.3%) → FLAG for rework
```

Scale: each █ ≈ 2 examples

---

## Top 5 Golden References

Highest density (0.93) among 9.5-score examples:

| Rank | File | Score | Density | Why Golden |
|------|------|:-----:|:-------:|------------|
| 1 | p07_gt_stripe_pipeline.md | 9.5 | 0.93 | Real PASS/FAIL tables, 4 suites, regression assertions |
| 2 | p08_law_shokunin.md | 9.5 | 0.93 | Foundational quality law, wrong/right pattern pairs |
| 3 | p10_ax_scout_before_create.md | 9.5 | 0.93 | Decision threshold table, violation costs, bash impl |
| 4 | p11_qg_shokunin_pool.md | 9.5 | 0.93 | Complete gate: checklist + scoring + bypass=never |
| 5 | p12_wf_stella_dispatch.md | 9.5 | 0.93 | 5-phase workflow with I/O, durations, rollback |

---

## Bottom 5 — Flagged for Wave 9 Rework

| Rank | File | Score | Issue | Fix Required |
|------|------|:-----:|-------|--------------|
| 1 | p03_pt_action_prompt.md | 5.0 | `## Template Body` completely empty | Fill with actual prompt template |
| 2 | p02_agent_pesquisa.md | 6.5 | `## Architecture` empty, no I/O schema | Add ASCII arch + input/output YAML |
| 3 | p11_lc_cex_lifecycle.md | 6.5 | No YAML frontmatter | Add full frontmatter block |
| 4 | p11_qg_cex_quality.md | 6.5 | No YAML frontmatter | Add full frontmatter block |
| 5 | p01_kc_catalogo_proprio_mercado_livre.md | 8.0 | `## Flow` section empty | Add Mermaid or ASCII flow diagram |

---

## Statistics

| Metric | Value |
|--------|-------|
| Total examples audited | 48 |
| Golden (>= 9.5) | 15 (31.3%) |
| Skilled (8.0-9.4) | 29 (60.4%) |
| Learning (7.0-7.9) | 0 (0.0%) |
| Rejected (< 7.0) | 4 (8.3%) |
| Average score | 8.9 |
| Average density (where available) | 0.90 |
| Files with missing frontmatter | 2 |
| Files with empty critical sections | 3 |

---
*Generated: 2026-03-22 | PYTHA CEX8 Quality Audit*
