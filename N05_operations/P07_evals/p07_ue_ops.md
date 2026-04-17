---
id: p07_ue_ops
kind: unit_eval
pillar: P07
title: "Unit Eval: N05 Operations Tool Suite"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "unit-eval-builder"
target: "N05_operations/_tools"
target_kind: "cli_tool"
input: "per-test fixtures in /tmp/cex_ue_ops/ (see Setup)"
expected_output: "per-test assertions pass; no cross-test state leakage"
assertions:
  - gate_ref: "H01"
    check: "YAML frontmatter parses without error"
    expected: true
    severity: "HARD"
  - gate_ref: "H04"
    check: "kind == unit_eval"
    expected: true
    severity: "HARD"
  - gate_ref: "H05"
    check: "quality == null"
    expected: true
    severity: "HARD"
  - gate_ref: "T01"
    check: "all 10 test_ids unique and present"
    expected: true
    severity: "HARD"
  - gate_ref: "T02"
    check: "positive + negative cases for compile/sanitize/hooks"
    expected: true
    severity: "HARD"
  - gate_ref: "S01"
    check: "timeout_seconds == 10 for all tests"
    expected: true
    severity: "SOFT"
timeout: 10
setup: "repo at clean HEAD; fixtures in /tmp/cex_ue_ops/; no staged changes before T06/T07"
teardown: "rm -rf /tmp/cex_ue_ops/; git restore --staged .; rm -f .cex/runtime/signals/signal_n05_complete_*.json"
edge_case: false
coverage_scope: "cex_compile, signal_writer, cex_sanitize, cex_hooks, cex_doctor, cex_score, cex_token_budget"
domain: "unit testing, tool validation"
quality: 9.1
tags: [unit-eval, cli-tool, n05-operations, tool-validation, exit-code]
tldr: "10-case isolation suite for N05 CLI tools: compile/sanitize/hooks/doctor/score/token_budget -- exit codes + output structure"
density_score: 0.91
---

## Input

10 independent tool invocations with controlled fixtures. Positive + negative cases
for compile, sanitize, and hooks. All fixtures created in Setup; removed in Teardown.

## Expected Output

| test_id | tool | assertion_type | expected |
|---------|------|---------------|---------|
| ue_ops_01 | cex_compile.py valid.md | exit_code + file_exists | exit==0, compiled/*.yaml exists |
| ue_ops_02 | cex_compile.py malformed.md | exit_code + contains | exit==1, stderr has "error" |
| ue_ops_03 | signal_writer write_signal(n05,complete,9.0) | json_schema | signal file: nucleus==n05, status==complete, score==9.0 |
| ue_ops_04 | cex_sanitize.py --check clean.py | exit_code | exit==0 |
| ue_ops_05 | cex_sanitize.py --check dirty.py | exit_code + contains | exit==1, stdout has "violation" |
| ue_ops_06 | cex_hooks.py pre-commit (clean staged) | exit_code | exit==0 |
| ue_ops_07 | cex_hooks.py pre-commit (dirty staged) | exit_code + contains | exit==1, output has "non-ASCII" |
| ue_ops_08 | cex_doctor.py | exit_code + not_contains | exit==0, stderr no "Traceback" |
| ue_ops_09 | cex_score.py valid.md | contains | stdout has "structural" AND "rubric" |
| ue_ops_10 | cex_token_budget.py valid.md | contains | stdout int > 0 |

## Assertions

### Compile (T01-T02)
- ue_ops_01: `python _tools/cex_compile.py /tmp/cex_ue_ops/valid.md` -- exit==0, compiled YAML exists and parses
- ue_ops_02: `python _tools/cex_compile.py /tmp/cex_ue_ops/malformed.md` -- exit==1, stderr contains "error", no .yaml emitted

### Signal Writer (T03)
- ue_ops_03: signal file at `.cex/runtime/signals/signal_n05_*.json` -- JSON valid, keys: nucleus="n05", status="complete", score=9.0

### Sanitize (T04-T05)
- ue_ops_04: `python _tools/cex_sanitize.py --check --scope /tmp/cex_ue_ops/clean.py` -- exit==0
- ue_ops_05: `python _tools/cex_sanitize.py --check --scope /tmp/cex_ue_ops/dirty.py` -- exit==1, stdout contains "violation"

### Hooks (T06-T07)
- ue_ops_06: stage clean.py, run `python _tools/cex_hooks.py pre-commit` -- exit==0
- ue_ops_07: stage dirty.py, run `python _tools/cex_hooks.py pre-commit` -- exit==1, output contains "non-ASCII"

### Doctor (T08)
- ue_ops_08: `python _tools/cex_doctor.py` -- exit==0, no Traceback in stderr

### Score (T09)
- ue_ops_09: `python _tools/cex_score.py /tmp/cex_ue_ops/valid.md` -- stdout contains "structural" AND "rubric"

### Token Budget (T10)
- ue_ops_10: `python _tools/cex_token_budget.py /tmp/cex_ue_ops/valid.md` -- stdout integer > 0

## Setup

```bash
mkdir -p /tmp/cex_ue_ops/compiled
# valid.md fixture (T01/T09/T10)
cat > /tmp/cex_ue_ops/valid.md << 'EOF'
---
id: p01_kc_fixture
kind: knowledge_card
pillar: P01
title: "Fixture"
version: "1.0.0"
quality: null
tags: [fixture, unit-eval, test]
tldr: "Fixture artifact for unit eval"
---
## Overview
Test fixture body.
EOF
# malformed.md (T02)
printf -- '---\nid: broken\nkind: "unclosed\n' > /tmp/cex_ue_ops/malformed.md
# clean.py ASCII-only (T04/T06)
printf 'def hello():\n    print("[OK] clean")\n' > /tmp/cex_ue_ops/clean.py
# dirty.py with emoji U+2705 (T05/T07)
printf 'def hello():\n    print("\xe2\x9c\x85 done")\n' > /tmp/cex_ue_ops/dirty.py
```

## Teardown

```bash
git restore --staged . 2>/dev/null || true
rm -rf /tmp/cex_ue_ops/
rm -f .cex/runtime/signals/signal_n05_complete_*.json
```
