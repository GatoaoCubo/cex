---
id: p07_se_ops_n05
kind: smoke_eval
8f: F7_govern
pillar: P07
title: "Smoke: N05 Operations Critical Path"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: smoke-eval-builder
scope: "N05 operations nucleus -- tools, signals, compile, hooks, ascii gate"
critical_path:
  - "repo_intact: .cex/ and kinds_meta.json readable"
  - "tools_importable: signal_writer module loads"
  - "compile_works: 1 artifact compiles to YAML"
  - "doctor_starts: cex_doctor.py --help exits 0"
  - "signal_writable: test signal created and cleaned"
  - "git_clean: no uncommitted changes in N05_operations/"
  - "hooks_active: cex_hooks.py pre-commit --dry-run exits 0"
  - "ascii_clean: cex_sanitize.py --check scope N05_operations/ exits 0"
timeout: 25
assertions:
  - check: ".cex/ exists and .cex/kinds_meta.json is readable"
    command: "test -d .cex && python -c \"import json; json.load(open('.cex/kinds_meta.json'))\""
    expected_exit_code: 0
    timeout_seconds: 1
    severity: critical
  - check: "signal_writer module importable"
    command: "python -c \"from _tools import signal_writer\""
    expected_exit_code: 0
    timeout_seconds: 2
    severity: critical
  - check: "compile 1 artifact produces .yaml output"
    command: "python _tools/cex_compile.py N05_operations/P07_evals/p07_se_ops_n05.md && test -f _docs/compiled/p07_se_ops_n05.yaml"
    expected_exit_code: 0
    timeout_seconds: 5
    severity: critical
  - check: "cex_doctor.py --help exits 0"
    command: "python _tools/cex_doctor.py --help"
    expected_exit_code: 0
    timeout_seconds: 2
    severity: critical
  - check: "write test signal, verify file created, remove it"
    command: "python -c \"from _tools.signal_writer import write_signal; write_signal('n05','smoke_test',0)\" && ls .cex/runtime/signals/signal_n05_smoke_test_*.json && python -c \"import glob,os; [os.remove(f) for f in glob.glob('.cex/runtime/signals/signal_n05_smoke_test_*.json')]\""
    expected_exit_code: 0
    timeout_seconds: 3
    severity: critical
  - check: "no uncommitted changes in N05_operations/"
    command: "test -z \"$(git status --porcelain N05_operations/)\""
    expected_exit_code: 0
    timeout_seconds: 2
    severity: critical
  - check: "cex_hooks.py pre-commit --dry-run exits 0"
    command: "python _tools/cex_hooks.py pre-commit --dry-run"
    expected_exit_code: 0
    timeout_seconds: 3
    severity: critical
  - check: "cex_sanitize.py --check scope N05_operations/ exits 0"
    command: "python _tools/cex_sanitize.py --check --scope N05_operations/"
    expected_exit_code: 0
    timeout_seconds: 5
    severity: critical
fast_fail: true
prerequisites:
  - "python 3.x in PATH"
  - ".cex/kinds_meta.json present and valid JSON"
  - ".cex/runtime/signals/ directory writable"
  - "git repo initialized at repo root"
  - "_tools/cex_compile.py, cex_doctor.py, cex_hooks.py, cex_sanitize.py present"
environment: "local-dev"
health_check: "python -c \"from _tools import signal_writer\" && test -d .cex"
frequency: "pre-commit, pre-dispatch"
alerting: "stdout -- failing check id + exit code"
domain: "operations, smoke testing"
quality: 9.1
tags: [smoke-eval, n05-operations, fast-fail, pre-commit, P07]
tldr: "25s smoke gate for N05: repo intact, tools importable, compile works, doctor starts, signal writable, git clean, hooks active, ascii clean."
density_score: 0.91
related:
  - type_hint_retrofit_w6_20260415_2140
  - type_hint_retrofit_w5_20260415_2140
  - p11_qg_artifact
  - p11_qg_knowledge
  - p11_qg_admin_orchestration
  - bld_tools_conformity_assessment
  - validate
  - p01_kc_git_hooks_ci
  - p04_output_github_actions
  - skill
---

## Critical Path

Cheapest checks first -- abort on first failure.

| # | Check | Command Summary | Timeout | Severity |
|---|-------|----------------|---------|----------|
| 1 | repo_intact | test .cex/ + parse kinds_meta.json | 1s | critical |
| 2 | tools_importable | python -c "from _tools import signal_writer" | 2s | critical |
| 3 | compile_works | cex_compile.py on this file + verify .yaml | 5s | critical |
| 4 | doctor_starts | cex_doctor.py --help exits 0 | 2s | critical |
| 5 | signal_writable | write signal, verify file, clean up | 3s | critical |
| 6 | git_clean | git status --porcelain N05_operations/ is empty | 2s | critical |
| 7 | hooks_active | cex_hooks.py pre-commit --dry-run exits 0 | 3s | critical |
| 8 | ascii_clean | cex_sanitize.py --check --scope N05_operations/ | 5s | critical |

Total budget: 23s (hard cap: 25s, limit: 30s).

## Assertions

All assertions are binary. `fast_fail: true` -- first FAIL aborts remaining checks.

- **repo_intact**: exit 0 = `.cex/` directory exists AND `kinds_meta.json` parses as valid JSON.
- **tools_importable**: exit 0 = `signal_writer` module loads without ImportError.
- **compile_works**: exit 0 = artifact compiles AND `.yaml` output file is present on disk.
- **doctor_starts**: exit 0 = `cex_doctor.py --help` responds (binary: starts or does not).
- **signal_writable**: exit 0 = signal file created in `.cex/runtime/signals/` then removed.
- **git_clean**: exit 0 = `git status --porcelain N05_operations/` returns empty string.
- **hooks_active**: exit 0 = pre-commit hook script responds in dry-run mode.
- **ascii_clean**: exit 0 = no non-ASCII bytes detected in N05_operations/ code files.

## Prerequisites

- `python 3.x` available in shell PATH
- `.cex/kinds_meta.json` present and valid JSON
- `.cex/runtime/signals/` directory writable by current user
- `git` initialized at repo root (for git_clean check)
- `_tools/cex_compile.py`, `_tools/cex_doctor.py`, `_tools/cex_hooks.py`, `_tools/cex_sanitize.py` present

## On Failure

| Failed Check | Likely Cause | Action |
|-------------|--------------|--------|
| repo_intact | repo not initialized or corrupted | run `python _tools/cex_setup_validator.py` |
| tools_importable | missing `_tools/__init__.py` or import error | check `_tools/` integrity |
| compile_works | frontmatter parse error or compiler bug | run `cex_compile.py --debug` |
| doctor_starts | missing dependency or broken script | inspect `cex_doctor.py` directly |
| signal_writable | disk permissions or missing runtime dir | `mkdir -p .cex/runtime/signals/` |
| git_clean | uncommitted N05 changes after build | commit or stash before dispatch |
| hooks_active | hook script missing or broken | `python _tools/cex_hooks.py --install` |
| ascii_clean | non-ASCII bytes in N05 code files | `python _tools/cex_sanitize.py --fix --scope N05_operations/` |

Escalation: if smoke fails in CI, skip all unit_eval and e2e_eval suites. Page on-call via alerting channel.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[type_hint_retrofit_w6_20260415_2140]] | upstream | 0.31 |
| [[type_hint_retrofit_w5_20260415_2140]] | upstream | 0.27 |
| [[p11_qg_artifact]] | downstream | 0.27 |
| [[p11_qg_knowledge]] | downstream | 0.25 |
| [[p11_qg_admin_orchestration]] | downstream | 0.24 |
| [[bld_tools_conformity_assessment]] | upstream | 0.23 |
| [[validate]] | downstream | 0.23 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.23 |
| [[p04_output_github_actions]] | upstream | 0.23 |
| [[skill]] | downstream | 0.23 |
