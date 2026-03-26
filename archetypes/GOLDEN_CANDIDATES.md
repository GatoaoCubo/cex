# Golden Candidates — CEX Migration List
# Generated: 2026-03-22 | Source: codexa-core (9916 MD files)
# Criteria: quality >= 9.0, size 1KB-8KB, structured content
# Format: path | tipo CEX | estimated quality | razao

---

## CEX8 Quality Audit — Top 5 Golden References (2026-03-22)

**Methodology**: Manual content review of all 48 examples. Selected by score=9.5 + density=0.93 (max).

| Rank | File | Score | Density | Why Golden |
|------|------|:-----:|:-------:|------------|
| 1 | P07_evals/examples/p07_gt_stripe_pipeline.md | 9.5 | 0.93 | Real PASS/FAIL tables, 4 test suites, regression assertions for CI |
| 2 | P08_architecture/examples/p08_law_shokunin.md | 9.5 | 0.93 | Foundational quality law with wrong/right pattern pairs |
| 3 | P10_memory/examples/p10_ax_scout_before_create.md | 9.5 | 0.93 | Decision threshold, violation costs table, bash implementation |
| 4 | P11_feedback/examples/p11_qg_shokunin_pool.md | 9.5 | 0.93 | Complete gate: checklist + 5D scoring + bypass=never |
| 5 | P12_orchestration/examples/p12_wf_stella_dispatch.md | 9.5 | 0.93 | 5-phase workflow with I/O per step, durations, rollback |

**Use these as structural templates when creating new examples in their respective LPs.**

---

## P01 Knowledge Cards

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/pool/knowledge/KC_ATLAS_005_ZERO_TOUCH_EXECUTION_PATTERNS.md | P01 meta_kc | 9.0 | quality_score=9.0, TAC-8 architecture, retry patterns, real YAML configs |
| records/pool/knowledge/KC_ATLAS_006_PRE_DEPLOY_VALIDATION_CHECKLIST.md | P01 meta_kc | 8.5 | checklist estruturado, pre-deploy patterns, ATLAS domain |
| records/pool/knowledge/KC_ATLAS_007_CI_CD_PIPELINE_ARCHITECTURE.md | P01 meta_kc | 8.5 | pipeline architecture, CI/CD patterns, densidade estimada alta |
| records/pool/knowledge/KC_ATLAS_009_TEST_AUTOMATION_STRATEGY.md | P01 meta_kc | 8.5 | test strategy patterns, automation gates |
| records/pool/knowledge/KC_ATLAS_010_QUALITY_GATE_IMPLEMENTATION.md | P01 meta_kc | 9.0 | quality gate patterns, 5D framework, mensuravel |
| records/pool/knowledge/KC_ATLAS_012_CLAUDE_OBSERVABILITY_EVALUATION.md | P01 meta_kc | 8.5 | LLM observability, evaluation patterns |
| records/pool/knowledge/KC_ATLAS_013_CLAUDE_COMPUTER_USE_ARCHITECTURE.md | P01 meta_kc | 8.5 | computer use arch, tool use patterns |
| records/pool/knowledge/KC_EDISON_025_CLAUDE_CODING_SKILLS_PATTERNS.md | P01 meta_kc | 9.0 | coding patterns golden, EDISON distill source |
| records/pool/knowledge/KC_EDISON_029_CLAUDE_AGENT_ORCHESTRATION_QUICKSTART.md | P01 meta_kc | 9.0 | orchestration quickstart, agent patterns |
| records/pool/knowledge/KC_PYTHA_069_CAT_LOGO_PR_PRIO_MERCADO_LIVRE.md | P01 domain_kc | 10.0 | MIGRADO: p01_kc_catalogo_proprio_mercado_livre.md |

## P02 Agents

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/agents/catalogo_ml_strategy/README.md | P02 agent | 9.0 | 5 modulos, ASCII arch, inputs/outputs YAML, metricas de sucesso, regras de ouro |
| records/agents/amazon-ads-agent/README.md | P02 agent | 8.5 | YORK satellite, ML Ads, structured when_to_use, integration map |
| records/agents/amazon-analytics-agent/README.md | P02 agent | 8.5 | analytics domain, YORK, capabilities bem definidas |
| records/agents/amazon-listing-agent/README.md | P02 agent | 8.5 | listing creation, YORK, full workflow |
| records/agents/amazon-strategy-agent/README.md | P02 agent | 8.5 | strategy domain, market analysis |
| records/agents/gateway/README.md | P02 agent | 9.0 | API gateway pattern, routing, auth |

## P04 Skills

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/skills/ml-ads/SKILL.md | P04 skill | 9.5 | MIGRADO: p04_skill_ml_ads.md — modulos, YAML I/O, funnel table, quality gates reais |
| records/skills/amazon-ads-agent/SKILL.md | P04 skill | 8.5 | ML Ads YORK, estrutura completa |
| records/skills/amazon-listing-agent/SKILL.md | P04 skill | 8.5 | listing creation workflow |
| records/skills/amazon-analytics-agent/SKILL.md | P04 skill | 8.5 | analytics patterns |
| records/skills/design-extractor/SKILL.md | P04 skill | 8.0 | design extraction, structured |
| records/skills/voice_pipeline/SKILL.md | P04 skill | 8.5 | voice pipeline patterns |

## P05 Output

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| records/agents/*/iso_vectorstore/ISO_*_OUTPUT_TEMPLATE.md | P05 formatter | 9.0 | MIGRADO: p05_fmt_agent_markdown.md |
| cex/archetypes/MIGRATION_MAP.md + _schema.yaml files | P05 naming_rule | 9.0 | MIGRADO: p05_nr_cex_naming.md |

## P06 Schema

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| records/framework/docs/LAWS_v3_PRACTICAL.md (quality tiers) | P06 validator | 9.0 | MIGRADO: p06_val_quality_score.md |
| .claude/rules/STELLA_RULES.md (COMPOSE phase) | P06 interface | 9.0 | MIGRADO: p06_iface_satellite_handoff.md |

## P07 Evals

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 13 Shokunin) | P07 scoring_rubric | 9.2 | MIGRADO: p07_sr_5d_scoring.md |
| CLAUDE.md (BRAIN SEARCH) + records/core/brain/ | P07 smoke_eval | 9.0 | MIGRADO: p07_se_brain_query.md |

## P08 Architecture

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| records/pool/audits/2026-02-28-meta-evolution/LLM_ARCHITECTURE_REVIEW.md | P08 architecture | 9.0 | pendente |
| records/skills/continuous_batching/SKILL.md | P08 pattern | 9.2 | MIGRADO: p08_pat_continuous_batching.md |
| records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 13) | P08 law | 9.5 | MIGRADO: p08_law_shokunin.md |

## P09 Config

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| .claude/rules/multi_repo.md + CLAUDE.md KEY PATHS | P09 path_config | 9.0 | MIGRADO: p09_path_codexa_repos.md |
| .claude/rules/boot-autonomy-flags.md + MEMORY.md | P09 runtime_rule | 9.0 | MIGRADO: p09_rr_satellite_spawn.md |

## P10 Memory

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 8) | P10 axiom | 9.5 | MIGRADO: p10_ax_scout_before_create.md |
| CLAUDE.md (BRAIN SEARCH) + records/core/brain/ | P10 brain_index | 9.0 | MIGRADO: p10_bi_codexa_brain.md |

## P11 Feedback

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| .claude/rules/STELLA_RULES.md (NUNCA section) | P11 guardrail | 9.0 | MIGRADO: p11_gr_stella_dispatch.md |
| records/framework/docs/LAWS_v3_PRACTICAL.md + 5D rubric | P11 optimizer | 9.0 | MIGRADO: p11_opt_pool_density.md |

## P12 Orchestration

| Path | Tipo CEX | Est. Quality | Status |
|------|----------|-------------|--------|
| cex/archetypes/MIGRATION_MAP.md (PLANO DE EXECUCAO) | P12 dag | 9.0 | MIGRADO: p12_dag_cex_wave_pipeline.md |
| records/satellites/stella/mental_model.yaml + continuous_batching SKILL | P12 spawn_config | 9.0 | MIGRADO: p12_spawn_grid_continuous.md |

## Priority Migration Queue (Remaining)

1. KC_ATLAS_010 (quality gates — universal pattern) — P01
2. KC_EDISON_029 (agent orchestration — core CODEXA pattern) — P01
3. catalogo_ml_strategy/README.md (domain agent) — P02
4. amazon-ads-agent/SKILL.md (YORK domain skill) — P04
5. KC_ATLAS_007 (CI/CD patterns) — P01
6. records/pool/audits/2026-02-28-meta-evolution/LLM_ARCHITECTURE_REVIEW.md — P08

## Wave 9 Rework Queue (from CEX8 Audit)

| Priority | File | Issue |
|----------|------|-------|
| P1 | P03_prompt/examples/p03_pt_action_prompt.md | `## Template Body` EMPTY — fill with actual prompt |
| P2 | P02_model/examples/p02_agent_pesquisa.md | Architecture EMPTY + no I/O schema |
| P3 | P11_feedback/examples/p11_lc_cex_lifecycle.md | Add YAML frontmatter |
| P4 | P11_feedback/examples/p11_qg_cex_quality.md | Add YAML frontmatter |
| P5 | P01_knowledge/examples/p01_kc_catalogo_proprio_mercado_livre.md | Fill empty `## Flow` section |

---
*Search method: find size +1k -5k (KCs), find size +2k -8k (agents/skills), grep quality 9.x*
*Total candidates: 38 | Migrated: 18 (ml-ads, zero-touch KC + 16 new Wave7.2)*
*Wave 7.2: 16 examples migrated (2 per LP for P05-P12) — PYTHA 2026-03-22*
*CEX8 Audit: 48 examples scored, 15 golden, 4 rejected — PYTHA 2026-03-22*
*Next: Wave 9 rework of bottom 5 + migrate Priority Queue top 6*
