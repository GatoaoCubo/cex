---
id: skill_n03
kind: skill
8f: F5_call
nucleus: n03
pillar: P04
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  engineering_axioms: [test-first, refactor-safe, commit-atomic]
trigger_type: slash_command
trigger_value: "/build"
user_invocable: true
version: 1.0.0
quality: 8.5
tags: [mirror, n03, engineering, hermes_assimilation, skill]
tldr: "N03 engineering skill: test-first, refactor-safe, commit-atomic. Phases: plan->test->implement->verify."
created: "2026-04-18"
related:
  - agent_card_engineering_nucleus
  - ctx_cex_new_dev_guide
  - p02_agent_creation_nucleus
  - p03_sp_n03_creation_nucleus
  - p11_qg_tdd_compliance
  - bld_instruction_golden_test
  - p08_pat_3phase_build_protocol
  - p01_kc_cex_project_overview
  - p03_sp_golden_test_builder
  - p01_kc_quality_gates
density_score: 1.0
---

## Axioms

1. **Test-first** -- write the test contract before writing the implementation.
2. **Refactor-safe** -- every refactor leaves the test suite passing (no net regressions).
3. **Commit-atomic** -- one logical change per commit; mixed concerns are a code smell.

## Phases

| Phase | Input | Action | Output |
|-------|-------|--------|--------|
| 1. Plan | task description | Map to kind + pillar + 8F; identify affected files | artifact plan, file list |
| 2. Test | artifact plan | Write quality gate contract (F7 gates) | test_contract.md |
| 3. Implement | plan + test contract | Execute 8F pipeline (F1-F8) | artifact draft |
| 4. Verify | artifact draft | Run cex_compile + cex_doctor + quality gate | pass/fail report |

## When to Use vs. Not Use

| Scenario | Use skill_n03? | Alternative |
|----------|---------------|------------|
| Building any CEX artifact | YES | -- |
| Autonomous batch builds (/batch) | YES | -- |
| Research / analysis only | NO | N01 pipeline |
| Orchestration decisions | NO | N07 GDP flow |
| Single-line hotfix | NO | direct Edit tool |

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Implement before test contract | Quality gates fail retroactively | Phase 2 (test) always precedes Phase 3 (implement) |
| Multi-concern commit | Rollback breaks unrelated changes | Split by logical unit |
| Skipping Plan phase | Wrong kind or pillar | F1 CONSTRAIN is mandatory |
| Partial verify (compile only) | Gate failures not caught | Run compile + doctor + quality gate together |

## Invocation

```bash
# Via slash command (N03 session)
/build "create knowledge_card for CEX memory taxonomy"

# Via dispatch (N07 handoff)
bash _spawn/dispatch.sh solo n03 "build kind=knowledge_card domain=memory-taxonomy"
```

## Metrics

| Metric | Target |
|--------|--------|
| Artifacts per session | >= 3 |
| Quality gate pass rate | >= 90% on first attempt |
| Compile success rate | 100% |
| Commit atomicity | 1 logical change per commit |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_engineering_nucleus]] | upstream | 0.29 |
| [[ctx_cex_new_dev_guide]] | related | 0.28 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.26 |
| [[p11_qg_tdd_compliance]] | downstream | 0.25 |
| [[bld_instruction_golden_test]] | upstream | 0.24 |
| [[p08_pat_3phase_build_protocol]] | downstream | 0.24 |
| [[p01_kc_cex_project_overview]] | upstream | 0.23 |
| [[p03_sp_golden_test_builder]] | upstream | 0.22 |
| [[p01_kc_quality_gates]] | upstream | 0.22 |
