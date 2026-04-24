---
id: team_charter_synthesis_default.md
kind: team_charter
8f: F8_collaborate
pillar: P12
llm_function: GOVERN
charter_id: synthesis_default_20260422
crew_template_ref: p12_ct_knowledge_synthesis.md
mission_statement: "Synthesize a target knowledge domain into structured, indexed KCs that fill identified library gaps and pass the P01 quality gate."
quality_gate: 9.0
deadline: "2026-12-31T23:59:59Z"
deliverables:
  - "raw_source_log (knowledge_card P01) -- source trail for all scanned material"
  - "gap_map (>=5 knowledge gaps identified and prioritized)"
  - ">=3 knowledge_cards (P01) curated, deduplicated, vocabulary-compliant"
  - "coverage_report (gap_resolution_rate >= 0.90, index entry count, broken-link count)"
budget:
  tokens: 90000
  wall_clock_seconds: 1800
  usd: 3.00
stakeholders: ["n07_orchestrator", "n04_knowledge", "n01_intelligence"]
escalation_protocol: "If any role crosses its token ceiling or fails 3 consecutive quality checks, emit signal_{role}_escalate.json to .cex/runtime/signals/. n07 reads and either extends budget or kills the crew."
termination_criteria: "ANY of: (1) indexer signals coverage_complete with gap_resolution_rate >= 0.90; (2) budget exhausted; (3) deadline passed; (4) 3 consecutive QA rejects on the same KC."
quality: null
density_score: null
title: "Team Charter -- Knowledge Synthesis Default"
version: "1.0.0"
tags: [team_charter, knowledge_synthesis, knowledge, n04]
tldr: "Default mission contract for knowledge_synthesis crew; fills library gaps in a target domain."
domain: "knowledge synthesis governance"
created: "2026-04-22"
related:
  - p12_ct_knowledge_synthesis.md
  - p02_ra_researcher.md
  - p02_ra_curator.md
  - p02_ra_indexer.md
  - bld_examples_team_charter
  - team-charter-builder
  - p01_kc_token_budgeting
  - p03_pt_orchestration_task_dispatch
  - cost-budget-builder
  - bld_collaboration_cost_budget
---

## Mission Statement
Synthesize a target knowledge domain into structured, indexed knowledge_cards
that fill identified library gaps and pass the P01 quality gate (>= 9.0).
The output makes the domain queryable via TF-IDF and wikilink traversal from
any nucleus.

## Deliverables
1. raw_source_log (knowledge_card under P01) -- source trail for all scanned material
2. gap_map -- list of >=5 knowledge concepts missing or weak in the P01 library
3. >=3 knowledge_cards (P01) curated, deduplicated, vocabulary-compliant
4. coverage_report -- gap_resolution_rate, total_kcs_added, index_entry_count, broken_link_count

## Success Metrics
- Each knowledge_card quality >= 9.0 (gate p11_qg_knowledge_card)
- gap_resolution_rate >= 0.90 (indexer-verified)
- Wall-clock under 1800s for the full crew
- Token budget under 90000 total
- All 3 a2a-task handoff signals present and parseable

## Budget
- Tokens: 90000 (hard ceiling; per-role ceilings: researcher 25k, curator 40k, indexer 25k)
- Wall-clock: 1800s
- USD: 3.00 at Sonnet-4-6 pricing (roughly 30k input + 60k output tokens)

## Stakeholders
- n07_orchestrator (dispatches + monitors + consolidates)
- n04_knowledge (nucleus that owns the crew instance)
- n01_intelligence (consumer of synthesized KCs for research tasks)

## Escalation Protocol
If any role crosses its token ceiling or fails 3 consecutive quality checks,
emit `signal_{role}_escalate.json` to `.cex/runtime/signals/`. n07 reads and
either extends budget (with justification) or halts the crew cleanly.

## Termination Criteria
ANY of:
1. indexer signals `coverage_complete` with gap_resolution_rate >= 0.90
2. Token or wall-clock budget exhausted (crew halts; partial KCs committed)
3. Deadline passed
4. 3 consecutive QA rejects on the same KC (stuck curation loop)

## Domain Scope (override per instance)
Set `domain_scope` in the run command to target a specific knowledge area:
```bash
python _tools/cex_crew.py run knowledge_synthesis \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_synthesis_default.md \
    --var domain_scope="8F pipeline patterns" \
    --execute
```
Default scope when not overridden: `general knowledge library enrichment`.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_knowledge_synthesis.md]] | related | 0.50 |
| [[p02_ra_researcher.md]] | upstream | 0.42 |
| [[p02_ra_curator.md]] | upstream | 0.41 |
| [[p02_ra_indexer.md]] | upstream | 0.38 |
| [[bld_examples_team_charter]] | upstream | 0.28 |
| [[team-charter-builder]] | related | 0.25 |
| [[p01_kc_token_budgeting]] | upstream | 0.22 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.20 |
| [[cost-budget-builder]] | upstream | 0.19 |
| [[bld_collaboration_cost_budget]] | related | 0.18 |
