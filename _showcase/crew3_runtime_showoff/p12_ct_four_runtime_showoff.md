---
id: p12_ct_four_runtime_showoff.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: four_runtime_showoff
purpose: Same task across 5 runtime+context configs -- prove CEXAI context beats raw model size
process: consensus
crewai_equivalent: "Process.consensus"
autogen_equivalent: "GroupChat.broadcast_vote"
swarm_equivalent: "baseline||sonnet||ollama||gemini||codex"
handoff_protocol_id: a2a-task-consensus
quality: 8.8
density_score: high
title: "Four Runtime Showoff Crew Template"
version: "1.0.0"
author: crew-template-builder
tags: [crew_template, benchmark, consensus, multi_runtime, showcase]
tldr: "5-way consensus: CEXAI Sonnet vs naked Opus + Ollama/Gemini/Codex -- proof by delta"
domain: "cross-runtime benchmark orchestration"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_baseline_runner.md
  - p02_ra_cexai_sonnet_runner.md
  - p02_ra_cexai_ollama_runner.md
  - p02_ra_cexai_gemini_runner.md
  - p02_ra_cexai_codex_runner.md
  - p12_ct_product_launch.md
  - bld_collaboration_crew_template
  - bld_schema_crew_template
  - p11_qg_crew_template
  - bld_instruction_crew_template
---

## Overview
Prove CEXAI framework leverage: 12 ISOs + KCs + memory elevates mid-tier
models above raw flagships. Five roles run the SAME task in parallel with
zero inter-role reads (isolation validates the benchmark). Aggregator
scores all 5 and produces the delta table. Consumers: N02 (proof asset),
N01 (benchmark intelligence).

**Task:** "Build an agent for customer support triage with RAG-based
knowledge retrieval, escalation rules, and multi-language support."

## Roles

| Role | Assignment ID | Config | Proves |
|------|---------------|--------|--------|
| baseline | p02_ra_baseline_runner.md | Opus + zero ctx | Best model, no framework |
| cexai_sonnet | p02_ra_cexai_sonnet_runner.md | Sonnet + full CEXAI | Framework on mid-tier |
| cexai_ollama | p02_ra_cexai_ollama_runner.md | llama3.1:8b + full | Leverage on free local |
| cexai_gemini | p02_ra_cexai_gemini_runner.md | Gemini flash + full | Leverage on Gemini |
| cexai_codex | p02_ra_cexai_codex_runner.md | GPT-5 + full CEXAI | Leverage on GPT |

## Process
Topology: `consensus`. All 5 roles run in parallel, zero dependencies.
Aggregator fires after all 5 completion signals arrive.

## Comparison Metrics

| Metric | Tool | Measures |
|--------|------|---------|
| L1 structural | cex_score.py --l1 | Required fields + sections |
| L2 rubric | cex_score.py --l2 | D01-D05 weighted |
| Hydration density | density_score field | Schema fields populated |
| Cross-ref count | role_assignment refs | Atom reuse |
| Consistency | cex_doctor.py --check | Schema violations |
| Reusability | capability_registry | Crews reusing artifact |

## Expected Results

| Role | L1 | L2 | Delta (L1/L2) |
|------|----|----|---------------|
| baseline (Opus, 0 ctx) | ~6.5 | ~7.0 | reference |
| cexai_sonnet | ~9.0 | ~9.2 | +2.5/+2.2 |
| cexai_ollama (8b) | ~7.5 | ~7.8 | +1.0/+0.8 |
| cexai_gemini (flash) | ~8.0 | ~8.3 | +1.5/+1.3 |
| cexai_codex (GPT-5) | ~8.5 | ~8.8 | +2.0/+1.8 |

## Memory Scope

| Role | Scope | Retention |
|------|-------|-----------|
| baseline | private | per-run only |
| cexai_sonnet | private | per-run + .cex/experiments/ |
| cexai_ollama | private | per-run + .cex/experiments/ |
| cexai_gemini | private | per-run + .cex/experiments/ |
| cexai_codex | private | per-run + .cex/experiments/ |

All private -- cross-contamination invalidates the comparison.

## Handoff Protocol
`a2a-task-consensus` -- each role emits `artifact_path` + `l1_score` +
`l2_score` + `runtime_id`. Aggregator fires on all 5 (15min timeout per
role; DNF if exceeded). Writes delta table to
`.cex/runtime/crews/{instance_id}/comparison_report.md`.

## Success Criteria
- [ ] All 5 artifacts under `.cex/runtime/crews/{instance_id}/`
- [ ] Each passes H01 (valid YAML) and H03 (kind=agent)
- [ ] cexai_sonnet L2 >= baseline L2 (framework leverage confirmed)
- [ ] comparison_report.md written with full delta table
- [ ] All 5 a2a-task-consensus signals in `.cex/runtime/signals/`
- [ ] Row appended to `.cex/experiments/results.tsv`

## Instantiation
```bash
python _tools/cex_crew.py run four_runtime_showoff \
    --charter _showcase/crew3_runtime_showoff/team_charter_showoff.md
# Add --execute for real LLM calls
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_baseline_runner.md]] | upstream | 0.42 |
| [[p02_ra_cexai_sonnet_runner.md]] | upstream | 0.41 |
| [[p02_ra_cexai_ollama_runner.md]] | upstream | 0.39 |
| [[p02_ra_cexai_gemini_runner.md]] | upstream | 0.38 |
| [[p02_ra_cexai_codex_runner.md]] | upstream | 0.37 |
| [[p12_ct_product_launch.md]] | sibling | 0.33 |
| [[bld_collaboration_crew_template]] | related | 0.30 |
| [[bld_schema_crew_template]] | upstream | 0.28 |
| [[p11_qg_crew_template]] | upstream | 0.27 |
| [[bld_instruction_crew_template]] | upstream | 0.25 |
