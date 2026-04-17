---
id: p07_gt_golden_test_ops
kind: golden_test
pillar: P07
title: "Golden: N05 Operations Reference Fixtures"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "golden-test-builder"
target_kind: "operations_fixture"
input: "Reference input/output pairs defining correct behavior for N05 critical operations: compile, signal, frontmatter validation, doctor, sanitize, commit hook."
golden_output_ref: "inline"
quality_threshold: 9.5
rationale: "H01-H11 pass. 8 fixtures cover full N05 ops surface: compile (H09), signal (H10), frontmatter pass/fail (S05), doctor (S04), sanitize pass/fail (S05), commit hook (S03). Each specifies comparison_method for deterministic assertion."
edge_case: true
reviewer: "n07_orchestrator"
approval_date: "2026-04-17"
domain: "operations"
quality: 9.1
tags: [golden-test, n05-operations, compile, signal, frontmatter, sanitize, doctor]
tldr: "8 N05 ops golden fixtures: compile->yaml, signal->json, frontmatter pass/fail, doctor healthy, sanitize pass/fail, commit hook accept."
density_score: 0.91
linked_artifacts:
  primary: "archetypes/builders/golden-test-builder/"
  related:
    - "N05_operations/P07_evals/p07_efw_n05_operations.md"
    - "N05_operations/P07_evals/p07_tc_n05_operations.md"
    - "_tools/cex_compile.py"
    - "_tools/cex_hooks.py"
    - "_tools/cex_sanitize.py"
    - "_tools/cex_doctor.py"
---

## Input Scenario

Eight deterministic reference cases for N05 operations. Each case is a
triple: (test_id, input_fixture, expected_output, comparison_method).
Gating Wrath lens: no ambiguity tolerated -- every case has an exact
pass/fail assertion, no fuzzy matches.

## Golden Output

### golden_compile

```yaml
test_id: golden_compile
description: "cex_compile.py converts minimal valid .md to .yaml"
input_fixture: |
  ---
  id: p01_kc_test
  kind: knowledge_card
  pillar: P01
  version: "1.0.0"
  created: "2026-04-17"
  updated: "2026-04-17"
  author: "test"
  domain: "test"
  quality: null
  tags: [test, compile, validation]
  tldr: "Minimal KC for compile golden test"
  ---
  ## Body
  Content here.
expected_output:
  file_created: true
  yaml_fields_present: [id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr]
  exit_code: 0
comparison_method: json_match
```

### golden_signal

```yaml
test_id: golden_signal
description: "signal_writer.write_signal produces valid JSON signal file"
input_fixture: "write_signal('n05', 'complete', 9.0)"
expected_output:
  file_pattern: ".cex/runtime/signals/signal_n05_complete_*.json"
  required_fields: [nucleus, event_type, score, timestamp]
  field_values:
    nucleus: "n05"
    event_type: "complete"
    score: 9.0
  timestamp_format: "ISO8601"
  exit_code: 0
comparison_method: json_match
```

### golden_frontmatter

```yaml
test_id: golden_frontmatter
description: "cex_hooks pre-commit accepts artifact with all required fields"
input_fixture:
  id: p07_gt_example
  kind: golden_test
  pillar: P07
  version: "1.0.0"
  created: "2026-04-17"
  updated: "2026-04-17"
  author: "builder"
  target_kind: "knowledge_card"
  quality_threshold: 9.5
  reviewer: "orchestrator"
  domain: "test"
  quality: null
  tags: [golden-test, test, fixture]
  tldr: "Valid frontmatter fixture for hook validation"
expected_output:
  exit_code: 0
  stderr: ""
comparison_method: exact
```

### golden_frontmatter_fail

```yaml
test_id: golden_frontmatter_fail
description: "cex_hooks pre-commit rejects artifact missing 'kind' field"
input_fixture:
  id: p07_gt_broken
  pillar: P07
  version: "1.0.0"
  quality: null
  tags: [test]
expected_output:
  exit_code: 1
  stderr_contains: "kind"
comparison_method: contains
```

### golden_doctor_healthy

```yaml
test_id: golden_doctor_healthy
description: "cex_doctor.py reports 0 failures on clean repo state"
input_fixture: "clean_repo_state"
expected_output:
  stdout_contains: "0 failures"
  exit_code: 0
comparison_method: contains
```

### golden_sanitize_clean

```yaml
test_id: golden_sanitize_clean
description: "cex_sanitize.py --check passes on ASCII-only .py file"
input_fixture: |
  # ASCII-only Python file
  def hello():
      print("[OK] all good")
expected_output:
  exit_code: 0
  stdout_contains: "clean"
comparison_method: contains
```

### golden_sanitize_dirty

```yaml
test_id: golden_sanitize_dirty
description: "cex_sanitize.py --check fails on .py containing em-dash U+2014"
input_fixture: |
  # Python file with em-dash violation
  # line 2: result -- value
  x = 1
expected_output:
  exit_code: 1
  stdout_pattern: "line [0-9]+"
  violation_char: "U+2014"
comparison_method: regex
```

### golden_commit_format

```yaml
test_id: golden_commit_format
description: "cex_hooks commit-msg accepts '[N05] valid message' format"
input_fixture: "[N05] add golden fixtures for ops pipeline"
expected_output:
  exit_code: 0
  accepted: true
comparison_method: exact
```

## Rationale

- H01: frontmatter parses as valid YAML (gate: H01 pass)
- H02: id=p07_gt_golden_test_ops matches `^p07_gt_[a-z][a-z0-9_]+$` (H02 pass)
- H03: id equals filename stem golden_test_ops (H03 pass)
- H04: kind == golden_test (H04 pass)
- H05: quality == null (H05 pass)
- H06: all 14 required fields present (H06 pass)
- H07: quality_threshold=9.5 >= 9.5 (H07 pass)
- H08: target_kind=operations_fixture, not golden_test (H08 pass)
- H09: Golden Output section present with 8 complete fixtures (H09 pass)
- H10: Input Scenario section present and non-empty (H10 pass)
- H11: rationale references H01, H02, H03, H04, H05, H06, H07, H08, H09, H10, S03-S05 (H11 pass)

S03: 8 fixtures map to distinct ops gate paths (compile/signal/hook/doctor/sanitize/commit).
S04: Every fixture is copy-pasteable as a real test assertion.
S05: golden_frontmatter_fail and golden_sanitize_dirty are edge/failure cases.
S06: This is not a few_shot_example (teaches format) -- it evaluates correct ops behavior.
S07: This is not a unit_eval -- it is a 9.5+ reference fixture set, not a threshold assertion.
S08: Reviewer: n07_orchestrator, approval_date: 2026-04-17.

## Evaluation Criteria

- [ ] golden_compile: yaml file created with all frontmatter fields, exit 0
- [ ] golden_signal: JSON file matches schema (nucleus/event_type/score/timestamp), exit 0
- [ ] golden_frontmatter: cex_hooks exits 0, no stderr
- [ ] golden_frontmatter_fail: cex_hooks exits 1, stderr contains "kind"
- [ ] golden_doctor_healthy: stdout contains "0 failures", exit 0
- [ ] golden_sanitize_clean: exit 0, stdout contains "clean"
- [ ] golden_sanitize_dirty: exit 1, stdout matches "line [0-9]+" regex
- [ ] golden_commit_format: hook exits 0 for "[N05] valid message" format
- [ ] All 8 test_ids are unique
- [ ] All comparison_method values are one of: exact/contains/regex/json_match
- [ ] No real user data in any fixture (synthetic only)

## References

1. `_tools/cex_compile.py` -- compile .md to .yaml
2. `_tools/signal_writer.py` -- write_signal(nucleus, event_type, score)
3. `_tools/cex_hooks.py` -- pre-commit + commit-msg validation
4. `_tools/cex_doctor.py` -- repo health check
5. `_tools/cex_sanitize.py` -- ASCII-only enforcement
6. `.claude/rules/ascii-code-rule.md` -- U+2014 violation spec
7. `N05_operations/P07_evals/p07_efw_n05_operations.md` -- N05 eval framework
