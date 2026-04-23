---
id: p07_efw_n05_operations
kind: eval_framework
pillar: P07
title: "N05 Operations Evaluation Framework"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n05_eval_framework_builder
domain: operations
quality: 9.1
tags: [eval_framework, n05, operations, test_pyramid, ci, smoke, regression]
tldr: "End-to-end evaluation framework for N05 operations: test pyramid from unit to E2E, with CI/manual/overnight execution modes."
framework_type: agent_eval
tasks:
  - unit_tool_validation
  - integration_tool_chains
  - e2e_pipeline_dispatch
  - smoke_sanity
  - regression_replay
metrics:
  - pass_rate
  - builder_health_score
  - density_score
  - ascii_compliance
  - quality_gate_pass
runner: cex_system_test
adapter: cli
fewshot_k: 0
sample_size: null
seed: 42
dependencies:
  - "cex_system_test.py (54 tests)"
  - "cex_score.py (3-layer scorer)"
  - "cex_doctor.py (118+ checks)"
  - "cex_sanitize.py (ASCII gate)"
  - "cex_hooks.py (pre-commit, post-tool-use)"
related:
  - p11_qg_admin_orchestration
  - p08_ac_verification
  - p08_adr_002_testing_strategy
  - p02_agent_test_ops
  - doctor
  - skill
  - status
  - bld_collaboration_quality_gate
  - bld_tools_dataset_card
  - leverage_map_v2_n05_verify
---

## Overview

N05 (Gating Wrath) applies hard gates at every pipeline stage. This framework
organizes evaluation into five pyramid layers, three execution modes, and five
scoring dimensions aligned with F7 GOVERN + H01-H07 hard gates.

---

## Test Pyramid

| Layer | Speed | Scope | Entry Point | Pass Criterion |
|-------|-------|-------|-------------|----------------|
| Unit | <5s | Single tool | `cex_doctor.py --builder {name}` | 0 FAIL checks |
| Integration | <30s | Tool chain | `cex_system_test.py --quick` | 0 failures |
| E2E | <5min | Full pipeline | `cex_system_test.py` | 54/54 PASS |
| Smoke | <60s | Sanity gates | `cex_system_test.py --quick` | tools + compile + doctor |
| Regression | variable | Known failures | `.cex/learning_records/` replay | 0 regressions reintroduced |

### Unit -- Individual Tool Validation

Tasks: `cex_compile.py {artifact}`, `cex_doctor.py {builder}`, `cex_sanitize.py --check`
Pass: exit code 0; no H01-H07 gate failure.

### Integration -- Tool Chain Validation

Chains: `compile->doctor`, `signal->consolidate`, `hooks pre-commit->post-tool-use`.

### E2E -- Full Pipeline

Sequence: dispatch -> build -> compile -> signal -> doctor (118+ checks pass).
Entry: `dispatch.sh solo n05 "task"`.

### Smoke -- Quick Sanity

Entry: `cex_system_test.py --quick`. Covers tool presence, 13-ISO builder dirs,
frontmatter parse (kind/pillar/quality:null), git config.

### Regression -- Known-Failure Replay

Source: `.cex/learning_records/`. Replay inputs that scored <8.0; assert >= 8.0.
Tracked by: F7b LEARN + `cex_quality_monitor.py`.

---

## Tools Inventory

| Tool | Role | Metric Produced | Layer |
|------|------|-----------------|-------|
| `cex_system_test.py` | Full suite runner (54 tests) | pass_rate | E2E, Smoke |
| `cex_score.py` | 3-layer scorer | quality_score (0-10) | All |
| `cex_doctor.py` | Builder health (118+ checks) | builder_health_score | Unit, Integration |
| `cex_sanitize.py` | ASCII enforcement | ascii_compliance (bool) | Unit |
| `cex_hooks.py` | Pre-commit + post-tool-use | hook_gate_pass (bool) | Integration |
| `cex_quality_monitor.py` | Trend snapshots | regression_delta | Regression |
| `cex_compile.py` | .md -> .yaml | compile_success (bool) | All |

---

## Execution Modes

| Mode | Trigger | Blocking | Failure Action |
|------|---------|----------|----------------|
| CI | git pre-commit hook | Yes -- blocks push | Reject commit; log to `.cex/learning_records/` |
| Manual | `python _tools/cex_system_test.py` | No -- advisory | Print report; no block |
| Overnight | `cex_evolve.py` sweep | No -- batch | Archive results; re-queue below-threshold |

CI mode enforces: ascii_compliance=true, compile_success=true, quality >= 8.0.
Manual mode surfaces all scores for developer review.
Overnight mode targets quality >= 9.0; applies heuristic fix then agent retry.

---

## Metrics

| Metric | Formula | Aggregation | Target |
|--------|---------|-------------|--------|
| pass_rate | passing_tests / total_tests | mean | >= 0.98 (54/54) |
| builder_health_score | checks_pass / total_checks | macro | >= 0.95 |
| density_score | content_bytes / max_bytes | per-artifact | >= 0.85 |
| ascii_compliance | non_ascii_count == 0 | boolean | true |
| quality_gate_pass | structural*0.3 + rubric*0.3 + semantic*0.4 | weighted | >= 8.0 (floor), 9.0 (target) |

---

## Reproducibility

| Dimension | Value |
|-----------|-------|
| Seed | 42 (system_test random sampling) |
| Tool versions | pinned in `requirements.txt` + `pyproject.toml` |
| Prompt template ref | `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md` |
| Learning record path | `.cex/learning_records/` |
| Regression baseline | snapshot at last 9.0+ quality gate pass |

---

## References

- CEX 8F pipeline: `.claude/rules/8f-reasoning.md`
- H01-H07 hard gates: `cex_hooks.py`
- Quality scoring: `cex_score.py` (structural 30%, rubric 30%, semantic 40%)
- ASCII rule: `.claude/rules/ascii-code-rule.md`
- Regression tracking: `cex_quality_monitor.py`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_admin_orchestration]] | downstream | 0.27 |
| [[p08_ac_verification]] | downstream | 0.27 |
| [[p08_adr_002_testing_strategy]] | downstream | 0.27 |
| [[p02_agent_test_ops]] | upstream | 0.26 |
| [[doctor]] | downstream | 0.26 |
| [[skill]] | downstream | 0.25 |
| [[status]] | downstream | 0.25 |
| [[bld_collaboration_quality_gate]] | downstream | 0.24 |
| [[bld_tools_dataset_card]] | upstream | 0.24 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.23 |
