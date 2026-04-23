---
id: p11_qg_tdd_compliance
kind: quality_gate
pillar: P11
title: "Gate: TDD Compliance"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
domain: build
quality: 9.1
tags: [tdd, testing, quality-gate, red-green-refactor, build-discipline]
tldr: "Enforces test-first development: RED verified before code, YAGNI compliance, no RED commits merged"
when_to_use: "Before merging any code commit in builder_agent or operations_agent build pipelines"
keywords: [tdd-compliance, test-first, red-green-refactor, commit-hygiene]
long_tails:
  - como validar se codigo segue TDD corretamente
  - quality gate para garantir test-first development
axioms:
  - No code exists without a test that drove its creation
  - Every commit on the branch must have all tests passing
density_score: 0.91
related:
  - p01_kc_tdd_as_llm_skill
  - p02_agent_test_ops
  - p12_dr_test
  - p07_gt_stripe_pipeline
  - p12_wf_auto_ship
  - bld_sp_quality_gate_software_project
  - kc_git_workflow_for_agents
  - p01_kc_engineering_best_practices
  - n05_self_review_2026-04-02
  - bld_output_template_contributor_guide
---

# Gate: TDD Compliance

## Definition

| Property | Value |
|----------|-------|
| Metric | tdd_compliance_score |
| Threshold | 1.0 (all 7 checks pass) |
| Operator | == |
| Scope | builder_agent and operations_agent build agent_groups |
| Trigger | Pre-merge on any branch with code changes |

## Actions

| Result | Action | Escalation |
|--------|--------|------------|
| Pass (7/7) | Approve merge, proceed to deploy pipeline | None |
| Partial (5-6/7) | Block merge, return specific failing checks | Author fixes within same PR |
| Fail (<5/7) | Block merge, flag for process review | Notify agent_group owner + orchestrator |

## Checklist

- [ ] C1: Test written BEFORE implementation (git diff timeline: test file timestamp < impl file)
- [ ] C2: RED phase verified — test runs and FAILS before implementation exists (captured output)
- [ ] C3: GREEN phase — minimal code to pass test (no speculative features added)
- [ ] C4: REFACTOR phase — cleanup without behavior change (test suite still green)
- [ ] C5: Commit state GREEN only — every commit has all tests passing (no broken windows)
- [ ] C6: YAGNI — no code exists without a corresponding test driving it
- [ ] C7: Tests assert behavior (WHAT), not implementation (HOW) — no private method testing

## Scoring

| Dimension | Weight | Evidence Required |
|-----------|--------|-------------------|
| Test-first order | 30% | `git log --diff-filter=A` shows test file added before impl file |
| RED phase evidence | 25% | CI log or local output showing test failure before fix |
| YAGNI compliance | 20% | No untested code paths (coverage delta = 0 for new code) |
| Behavior focus | 15% | Tests assert return values/side effects, not mock call counts |
| Commit hygiene | 10% | `git log --oneline` + `pytest` on each commit = all green |

**Formula**: `score = (test_first * 0.3) + (red_phase * 0.25) + (yagni * 0.2) + (behavior * 0.15) + (commit_hygiene * 0.1)`

Each dimension: 0 (fail) or 10 (pass). Score >= 7.0 to merge.

## Anti-Patterns (Instant Fail)

- Writing code first, backfilling tests afterward ("test-after" is not TDD)
- Skipping RED phase entirely (test never seen failing = may be vacuously true)
- Testing implementation details (mocking internals, asserting private state)
- Committing with failing tests ("I'll fix it next commit" = broken window)
- Gold-plating in GREEN phase (adding features no test currently requires)

## Bypass Protocol

- Conditions: Hotfix patches with P0 production incident (max 24h bypass window)
- Approver: orchestrator orchestrator or project owner
- Audit: Bypass logged with incident ID + follow-up TDD ticket auto-created
- Limit: Max 2 bypasses per sprint; 3rd triggers mandatory process review

## Verification Commands

```bash
# Check test-first order via git
git log --diff-filter=A --name-only --pretty=format:"%H %ai" -- "tests/" "src/"

# Run full suite to verify GREEN state
pytest --tb=short -q

# Coverage delta for new code only
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

---
*Quality Gate v1.0 | builder_agent Build Domain | 2026-03-24*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_tdd_as_llm_skill]] | upstream | 0.43 |
| [[p02_agent_test_ops]] | upstream | 0.35 |
| [[p12_dr_test]] | downstream | 0.26 |
| [[p07_gt_stripe_pipeline]] | upstream | 0.26 |
| [[p12_wf_auto_ship]] | downstream | 0.26 |
| [[bld_sp_quality_gate_software_project]] | sibling | 0.25 |
| [[kc_git_workflow_for_agents]] | upstream | 0.24 |
| [[p01_kc_engineering_best_practices]] | upstream | 0.22 |
| [[n05_self_review_2026-04-02]] | upstream | 0.22 |
| [[bld_output_template_contributor_guide]] | upstream | 0.21 |
