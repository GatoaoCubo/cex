---
id: n01_output_cf_dags_and_specs
kind: context_doc
pillar: P01
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
domain: "content_factory"
quality: 9.1
tags: [output, content-factory, wave2, dags, constraint-specs]
tldr: "N01 wave2 output: 6 DAGs (64 nodes) + 6 constraint specs for Content Factory autonomous pipeline"
density_score: 1.0
---

# N01 Output: Content Factory DAGs & Constraint Specs

**Mission**: MISSION_content_factory_wave2
**Nucleus**: N01 Intelligence
**Date**: 2026-04-06
**Status**: COMPLETE

---

## Summary

Produced **6 DAGs** and **6 constraint specs** for the Content Factory autonomous pipeline.
Zero new kinds created — all artifacts use existing CEX kinds (`dag`, `constraint_spec`).

## DAGs Produced (P12_orchestration/dags/content_factory/)

| # | File | Nodes | Edges | Max Parallelism | Est. Duration | Critical Path Length |
|---|------|-------|-------|-----------------|---------------|---------------------|
| 1 | dag_cf_master.md | 13 | 17 | 5 | 120min | 8 nodes |
| 2 | dag_cf_video.md | 11 | 12 | 3 | 45min | 9 nodes |
| 3 | dag_cf_course.md | 11 | 13 | 4 | 84min | 8 nodes |
| 4 | dag_cf_ebook.md | 10 | 11 | 2 | 70min | 8 nodes |
| 5 | dag_cf_presentation.md | 9 | 10 | 3 | 35min | 7 nodes |
| 6 | dag_cf_social.md | 10 | 11 | 3 | 45min | 8 nodes |

**Totals**: 64 nodes, 74 edges across 6 DAGs.

### Architecture

```
dag_cf_master (root)
├── fork_video ──→ dag_cf_video
├── fork_course ──→ dag_cf_course
├── fork_ebook ──→ dag_cf_ebook
├── fork_presentation ──→ dag_cf_presentation
└── fork_social ──→ dag_cf_social
```

Master DAG fans out to 5 sub-pipelines after authoring the master longform.
All sub-pipelines converge at `collect_outputs` → `quality_gate` → `publish`.

### Parallelism Analysis

| DAG | Parallel Group | Nodes |
|-----|---------------|-------|
| master | brand_inject + research | 2 |
| master | 5 format forks | 5 (max) |
| video | voiceover + visuals + music | 3 |
| course | TTS + slides + quizzes + supplements | 4 |
| ebook | review + illustrations / outline + cover | 2+2 |
| presentation | notes + design + charts | 3 |
| social | posts + carousels + clips | 3 |

## Constraint Specs Produced (P03_prompts/constraints/content_factory/)

| # | File | Constraint Type | Key Rules |
|---|------|----------------|-----------|
| 1 | p03_constraint_cf_video.md | format_rules | Duration tiers (15/30/60/300s), aspect ratios, audio LUFS, hook timing |
| 2 | p03_constraint_cf_course.md | format_rules | 5-12 modules, 3-8 lessons, quiz rules, SCORM compliance, certification |
| 3 | p03_constraint_cf_ebook.md | format_rules | 5-15 chapters, 2K-5K words/chapter, PDF+EPUB+MOBI, typography rules |
| 4 | p03_constraint_cf_presentation.md | format_rules | 10-30 slides, 3-5 bullets, speaker notes, PPTX+PDF+GSlides export |
| 5 | p03_constraint_cf_podcast.md | format_rules | 10-30min duration, -16 LUFS, intro/body/outro, RSS metadata |
| 6 | p03_constraint_cf_brief.md | input_schema | 6 required fields (topic, audience, formats, brand_ref, tone, goal) |

### Cross-Reference Matrix

| Constraint Spec | Consumed by DAG | At Node |
|----------------|----------------|---------|
| cs_cf_brief | dag_cf_master | ingest_brief |
| cs_cf_video | dag_cf_video | quality_check |
| cs_cf_course | dag_cf_course | quality_check |
| cs_cf_ebook | dag_cf_ebook | quality_check |
| cs_cf_presentation | dag_cf_presentation | quality_check |
| cs_cf_podcast | (future dag_cf_podcast) | quality_check |

## Schema Compliance

All DAGs follow `bld_schema_dag`:
- [x] id matches `^p12_dag_[a-z][a-z0-9_]+$`
- [x] kind: dag, lp: P12
- [x] nodes with id, label, agent_group
- [x] edges with from, to
- [x] quality: null
- [x] Acyclic graphs verified
- [x] execution_order, parallel_groups, critical_path computed

All constraint specs follow `bld_schema_constraint_spec`:
- [x] id matches `^p03_constraint_[a-z][a-z0-9_]+$`
- [x] kind: constraint_spec, pillar: P03
- [x] All 4 body sections: Overview, Constraint Definition, Provider Compatibility, Integration
- [x] quality: null
- [x] MUST/MUST_NOT rules with concrete values
- [x] Quality metrics with min/target/max

## Notes for N07

- `dag_cf_master` references all 5 sub-DAGs via `linked_artifacts.related`
- Each sub-DAG references its constraint spec in `linked_artifacts.related`
- The brief constraint spec (`cs_cf_brief`) is the entry gate — no brief, no pipeline
- Podcast has a constraint spec but no DAG yet (not in wave2 scope, flagged for wave3)
- All DAGs use nucleus routing consistent with N07 orchestrator rules
