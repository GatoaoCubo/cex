---
id: team_charter_factory_default.md
kind: team_charter
pillar: P12
llm_function: GOVERN
charter_id: factory_default_20260422
crew_template_ref: p12_ct_artifact_factory.md
mission_statement: "Convert a spec or mission plan into a complete, peer-reviewed, doctor-clean artifact set under N03_engineering using the 4-role artifact_factory crew."
quality_gate: 9.0
deadline: null
deliverables:
  - "Decomposition KC (knowledge_card P01) -- typed artifact list with dependencies"
  - "Produced artifact set (kind + pillar per item, compiled, quality >= 9.0)"
  - "Review report (scores table, per-gate evidence, pass/fail per artifact)"
  - "Consistency report KC (P01) -- cross-reference map, doctor status, crew-complete"
budget:
  tokens: 160000
  wall_clock_seconds: 2700
  usd: 6.00
spec_ref: null   # override at instantiation: path to spec or mission plan file
stakeholders: ["n07_orchestrator", "n03_engineering"]
escalation_protocol: "If any role crosses its token ceiling or fails 2 consecutive quality retries, emit signal_{role}_escalate.json to .cex/runtime/signals/. n07 reads and decides: extend budget, skip artifact, or abort crew."
termination_criteria: "ANY of: (1) integrator emits crew-complete signal; (2) token budget exhausted; (3) wall-clock exceeded; (4) 3 consecutive doctor failures on same artifact."
quality: null
title: "Team Charter -- Artifact Factory Default"
version: "1.0.0"
tags: [team_charter, artifact_factory, engineering, default]
tldr: "Default mission contract for artifact_factory crew; override spec_ref at instantiation."
domain: "engineering artifact factory governance"
created: "2026-04-22"
related:
  - p12_ct_artifact_factory.md
  - p02_ra_architect.md
  - p02_ra_builder.md
  - p02_ra_reviewer.md
  - p02_ra_integrator.md
  - team-charter-builder
  - p01_kc_token_budgeting
  - bld_examples_team_charter
  - bld_collaboration_cost_budget
  - p03_pt_orchestration_task_dispatch
---

## Mission Statement
Convert a spec or mission plan (`spec_ref`) into a peer-reviewed, doctor-clean
artifact set using the 4-role `artifact_factory` crew.
Override `spec_ref` at instantiation; all other fields are production-ready defaults.

## Deliverables
1. Decomposition KC (P01) -- typed artifact list with dependency graph
2. Produced artifact set -- compiled, quality >= 9.0 per item
3. Review report -- per-gate scores, pass/fail per artifact
4. Consistency report KC (P01) -- cross-reference map + doctor status

## Success Metrics
- Decomposition KC has >= 1 artifact entry with kind + pillar + path + depends_on
- Every produced artifact quality >= 9.0 (reviewer-attested via cex_score.py)
- cex_doctor.py exits 0 on full produced set (integrator-verified)
- All 4 a2a-task handoff signals present in `.cex/runtime/signals/`
- Consistency report written before crew-complete signal

## Budget
- Tokens: 160000 (hard ceiling; allocated ~40k per role)
- Wall-clock: 2700s (45 minutes)
- USD: 6.00 at Sonnet pricing

## Stakeholders
- n07_orchestrator (dispatches + monitors + consolidates)
- n03_engineering (nucleus owning the crew instance + produced artifacts)

## Escalation Protocol
If any role crosses its token ceiling (40k) or fails 2 consecutive quality
retries on the same artifact, emit `signal_{role}_escalate.json` to
`.cex/runtime/signals/`. N07 reads and chooses: extend budget, skip the
problem artifact (mark it TODO), or abort the crew with partial results.

## Termination Criteria
ANY of:
1. integrator emits crew-complete signal with `doctor_status: pass`
2. Token budget exhausted (160k total)
3. Wall-clock exceeded (2700s)
4. 3 consecutive cex_doctor failures on the same artifact (stuck loop)

## Instantiation
```bash
# Override spec_ref then execute:
python _tools/cex_crew.py run artifact_factory \
    --charter N03_engineering/P12_orchestration/crews/team_charter_factory_default.md \
    --var spec_ref=N03_engineering/P01_knowledge/my_spec.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ct_artifact_factory.md]] | related | 0.56 |
| [[p02_ra_architect.md]] | upstream | 0.44 |
| [[p02_ra_builder.md]] | upstream | 0.42 |
| [[p02_ra_reviewer.md]] | upstream | 0.40 |
| [[p02_ra_integrator.md]] | upstream | 0.38 |
| [[team-charter-builder]] | related | 0.34 |
| [[p01_kc_token_budgeting]] | upstream | 0.28 |
| [[bld_examples_team_charter]] | upstream | 0.26 |
| [[bld_collaboration_cost_budget]] | related | 0.24 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.22 |
