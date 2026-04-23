---
id: spec_crew_scalability
kind: constraint_spec
pillar: P06
title: "Spec -- CREW_SCALABILITY Mission"
version: 1.0.0
created: 2026-04-23
author: n07_orchestrator
domain: crew_orchestration
quality_target: 9.0
status: SPEC
scope: all_nuclei
depends_on: null
tags: [spec, crew, scalability, mission, grid]
tldr: "Deep nucleus dispatch to enrich crew infrastructure, validate Python tools, and wire scalability"
density_score: 0.95
---

# Spec -- CREW_SCALABILITY Mission

## Problem

CEX has 13 crew templates and 302 spawnable agents, but:
1. Nuclei do not know what crews exist (no crew roster in their context)
2. Each nucleus has only 2 crews -- there are domain-specific workflows still unmapped
3. 144 Python tools exist but are not tested end-to-end per nucleus domain
4. CLI reference (docs/cli-reference.md) lists commands but they are not verified
5. Crew infrastructure is not wired for autonomous scalability (nuclei cannot self-compose crews)

## Vision

Every nucleus has 3-4 crews covering its core workflows. Crew roster is injected
into every handoff. Python tools are validated per domain. The system is ready for
any user to type `/crew run <name>` and get a production-quality deliverable.

## Wave Structure

### Wave 1: GRID (6 nuclei parallel)

All 6 operational nuclei run simultaneously. Each nucleus:

1. **SCAN**: Read its entire directory tree (all 13 pillar subdirs)
2. **AUDIT**: Validate existing crew templates via `python _tools/cex_crew.py show <name>`
3. **CREATE**: Build 1-2 NEW crew templates + 3-4 role assignments for unmapped workflows
4. **VALIDATE**: Test domain-specific Python tools (10-15 tools per nucleus)
5. **WIRE**: Update its agent_card to declare crew capabilities
6. **COMMIT**: Stage, commit, signal

### Wave 2: CONSOLIDATE (N07)

1. Verify all nucleus commits landed
2. Run `python _tools/cex_crew.py list` -- target: 18+ crews
3. Run `python _tools/cex_doctor.py` -- verify no regressions
4. Update docs/cli-reference.md if needed
5. Final commit + push

## Artifacts per Nucleus

| Nucleus | New Crews | New Roles | Tool Validation | Agent Card Update |
|---------|-----------|-----------|-----------------|-------------------|
| N01 | 1-2 (e.g. source_verification, trend_analysis) | 3-6 | cex_retriever, cex_research, cex_preflight, cex_reranker | Yes |
| N02 | 1-2 (e.g. brand_audit, social_calendar) | 3-6 | cex_media_produce, cex_social_publisher, cex_theme | Yes |
| N03 | 1-2 (e.g. migration_pipeline, builder_factory) | 3-6 | cex_8f_runner, cex_compile, cex_materialize, cex_schema_hydrate | Yes |
| N04 | 1-2 (e.g. rag_pipeline, glossary_sweep) | 3-6 | cex_kc_index, cex_retriever, cex_wikilink, cex_fts5_search | Yes |
| N05 | 1-2 (e.g. quality_sweep, deploy_pipeline) | 3-6 | cex_doctor, cex_system_test, cex_sanitize, cex_flywheel_audit | Yes |
| N06 | 1-2 (e.g. roi_analysis, subscription_design) | 3-6 | cex_bootstrap, cex_evolve, cex_score, cex_cohort_analyzer | Yes |

## Crew Roster (pre-compiled for handoff injection)

```
[13] composable crews:
  artifact_factory        [sequential  ] roles=4  N03
  cex_full_grid           [hierarchical] roles=7  N00
  code_review_pipeline    [sequential  ] roles=3  N03
  competitive_intelligence[sequential  ] roles=3  N01
  content_campaign        [sequential  ] roles=3  N02
  deep_research           [sequential  ] roles=4  N01
  incident_response       [sequential  ] roles=4  N05
  knowledge_synthesis     [sequential  ] roles=3  N04
  pricing_workshop        [sequential  ] roles=3  N06
  product_launch          [sequential  ] roles=4  N02
  release_gate            [sequential  ] roles=3  N05
  sales_pipeline          [sequential  ] roles=3  N06
  taxonomy_audit          [sequential  ] roles=3  N04
```

## Done When

- [ ] All 6 nuclei signal complete with quality >= 8.0
- [ ] 18+ crews discovered by `cex_crew.py list`
- [ ] All new crew templates pass `cex_crew.py show <name>` (valid plan JSON)
- [ ] 0 Python tool regressions (142/144 still pass --help)
- [ ] Each nucleus agent_card declares crew capabilities
- [ ] docs/cli-reference.md accurate
