---
id: spec_n01_n04_verticalization
kind: constraint_spec
pillar: P06
title: "Spec N01+N04 — Research Analyst + Knowledge Engineer Verticalization"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-knowledge
quality_target: 9.0
status: EXECUTED
scope: N01_intelligence + N04_knowledge
depends_on: null
tags: [spec, n01, n04, research, knowledge, verticalization]
tldr: "N01 evolves to Research Analyst (inveja analítica). N04 evolves to Knowledge Engineer (gula por conhecimento + database layer). FULL scope: 6 schemas + 8 outputs each."
density_score: 0.95
quality: 9.1
updated: "2026-04-07"
---

# Spec N01+N04 Verticalization

## Decisions (from user)
- N01: Research Analyst — "inveja analítica"
- N04: Knowledge Engineer — "gula por conhecimento" + database layer + fine-tuning/ML prep
- Scope: FULL (6 schemas + 8 outputs each)
- Provider: Hybrid (Gemini ↔ Claude, swap on limits)

## Wave 1: N01 Identity Rewrite (6 REWRITE)

| # | Path | Action | Notes |
|---|------|--------|-------|
| 1 | N01/P02_model/agent_intelligence.md | REWRITE | Research Analyst identity, hybrid provider, 12 capabilities |
| 2 | N01/P03_prompt/system_prompt_intelligence.md | REWRITE | 12 rules: research methodology, triangulation, sourcing |
| 3 | N01/architecture/agent_card_intelligence.md | REWRITE | Capabilities map, routing, provider config |
| 4 | N01/P12_orchestration/workflow_intelligence.md | REWRITE | Research pipeline: brief→search→triangulate→synthesize→deliver |
| 5 | N01/P11_feedback/quality_gate_intelligence.md | REWRITE | Source count, triangulation, citation, freshness gates |
| 6 | N01/quality/scoring_rubric_intelligence.md | REWRITE | Research-specific dimensions |

## Wave 2: N04 Identity Rewrite (6 REWRITE)

| # | Path | Action | Notes |
|---|------|--------|-------|
| 7 | N04/P02_model/agent_knowledge.md | REWRITE | Knowledge Engineer identity, DB layer, ML prep |
| 8 | N04/P03_prompt/system_prompt_knowledge.md | REWRITE | 12 rules: taxonomy, density, freshness, DB ops |
| 9 | N04/architecture/agent_card_knowledge.md | REWRITE | KC lifecycle, DB integration, export formats |
| 10 | N04/P12_orchestration/workflow_knowledge.md | REWRITE | KC pipeline: ingest→classify→structure→validate→index→export |
| 11 | N04/P11_feedback/quality_gate_knowledge.md | REWRITE | Density, freshness, coverage, schema compliance |
| 12 | N04/quality/scoring_rubric_knowledge.md | REWRITE | Knowledge-specific dimensions |

## Wave 3: N01 Schemas (6 CREATE)

| # | Path | Kind | Notes |
|---|------|------|-------|
| 13 | N01/P06_schema/research_brief_contract.md | schema | Input contract: question, scope, depth, sources, deadline |
| 14 | N01/P06_schema/source_quality_contract.md | schema | Source scoring: authority, freshness, bias, accessibility |
| 15 | N01/P06_schema/competitive_analysis_contract.md | schema | Competitor grid: features, pricing, positioning, gaps |
| 16 | N01/P06_schema/trend_detection_contract.md | schema | Trend signals: frequency, momentum, confidence |
| 17 | N01/P06_schema/citation_format_contract.md | schema | Reference format: APA-lite, URL, accessed date, reliability |
| 18 | N01/P06_schema/research_depth_levels.md | schema | L1 scan / L2 analysis / L3 deep-dive specifications |

## Wave 4: N04 Schemas (6 CREATE)

| # | Path | Kind | Notes |
|---|------|------|-------|
| 19 | N04/P06_schema/kc_structure_contract.md | schema | KC format: frontmatter fields, sections, density rules |
| 20 | N04/P06_schema/taxonomy_contract.md | schema | Kind × pillar × domain classification rules |
| 21 | N04/P06_schema/freshness_contract.md | schema | Staleness rules: 30/60/90 day thresholds per KC type |
| 22 | N04/P06_schema/export_format_contract.md | schema | JSONL for fine-tuning, CSV for ML, YAML for CEX, SQL for DB |
| 23 | N04/P06_schema/database_schema_contract.md | schema | Supabase tables: kcs, embeddings, metadata, search_index |
| 24 | N04/P06_schema/embedding_contract.md | schema | Model, dimensions, chunking strategy, similarity threshold |

## Wave 5: N01 Outputs (8 CREATE)

| # | Path | Kind | Notes |
|---|------|------|-------|
| 25 | N01/P05_output/output_research_brief.md | output | Research request document |
| 26 | N01/P05_output/output_competitive_grid.md | output | N competitors × M dimensions matrix |
| 27 | N01/P05_output/output_trend_report.md | output | Trend analysis: signals, momentum, projections |
| 28 | N01/P05_output/output_source_dossier.md | output | Curated source list with quality scores |
| 29 | N01/P05_output/output_market_snapshot.md | output | TAM/SAM/SOM + key metrics |
| 30 | N01/P05_output/output_swot_analysis.md | output | Strengths/Weaknesses/Opportunities/Threats |
| 31 | N01/P05_output/output_benchmark_report.md | output | Feature/price/performance comparison |
| 32 | N01/P05_output/output_executive_summary.md | output | 1-page synthesis for decision-makers |

## Wave 6: N04 Outputs (8 CREATE)

| # | Path | Kind | Notes |
|---|------|------|-------|
| 33 | N04/P05_output/output_knowledge_card.md | output | Standard KC template with all frontmatter |
| 34 | N04/P05_output/output_taxonomy_map.md | output | Visual taxonomy: kinds × pillars × domains |
| 35 | N04/P05_output/output_kc_audit_report.md | output | Coverage, staleness, density stats |
| 36 | N04/P05_output/output_finetune_dataset.md | output | JSONL export for fine-tuning: instruction/input/output |
| 37 | N04/P05_output/output_embedding_batch.md | output | Batch embedding export for vector DB |
| 38 | N04/P05_output/output_sql_migration.md | output | Supabase migration SQL for KC tables |
| 39 | N04/P05_output/output_knowledge_graph.md | output | Entity-relationship map of KCs |
| 40 | N04/P05_output/output_gap_report.md | output | Missing KCs by kind, domain, nucleus |

## Totals

| Wave | What | Count |
|------|------|-------|
| W1 | N01 identity rewrite | 6 |
| W2 | N04 identity rewrite | 6 |
| W3 | N01 schemas | 6 |
| W4 | N04 schemas | 6 |
| W5 | N01 outputs | 8 |
| W6 | N04 outputs | 8 |
| **Total** | | **40** |

## Done When
- [ ] All 40 artifacts pass compile
- [ ] Doctor 106 PASS / 0 FAIL maintained
- [ ] N01: 22 → ~34 .md files
- [ ] N04: 20 → ~34 .md files
- [ ] Signal: n01+n04 complete q=9.0
