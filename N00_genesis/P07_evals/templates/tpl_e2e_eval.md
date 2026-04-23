---
quality: null
# TEMPLATE: E2E Eval (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.e2e_eval)
# Max 4096 bytes

id: p07_e2e_[pipeline_slug]
kind: e2e_eval
pillar: P07
title: [e2e_eval_do_pipeline]
version: 1.0.0
created: [yyyy-mm-dd]
updated: [yyyy-mm-dd]
author: [agent_group_name]
tags: [[tag1], [tag2], e2e, eval]
tldr: [o_que_o_pipeline_valida]
density_score: 1.0
related:
  - p02_agent_[name_slug]
  - p03_sp_[agent_slug]
  - p02_iso_[agent_name]
  - p10_ss_[session_slug]
  - p11_qg_unit_eval
---

# E2E Eval: [pipeline_slug]

## Setup
<!-- INSTRUCAO: ambiente, seeds e dependencias externas. -->
- Environment: [local|staging|prod_clone]
- Seed data: [dataset_ou_fixture]
- Dependencies: [mcp|api|db]

## Execute
<!-- INSTRUCAO: passos fim-a-fim com checkpoints. -->
1. [acionar_pipeline]
2. [capturar_saida_intermediaria]
3. [validar_saida_final]

## Assert
<!-- INSTRUCAO: 3-5 asserts observaveis. -->
| # | Assertion | Expected |
|---|-----------|----------|
| 1 | [assert_1] | [resultado_1] |
| 2 | [assert_2] | [resultado_2] |
| 3 | [assert_3] | [resultado_3] |

## Teardown
<!-- INSTRUCAO: limpar estado para rerun seguro. -->
- [cleanup_1]
- [cleanup_2]

## Failure Signals
<!-- INSTRUCAO: erros que bloqueiam vs avisam. -->
- Blocker: [sinal_critico]
- Warning: [sinal_degradado]

## Assertion Pattern Reference

Use these canonical assertion patterns when defining assertions in the Assert table above.

| Pattern | When to use | Example assertion |
|---------|-------------|-------------------|
| `exact_match` | Output must equal expected value exactly | Response body == expected JSON |
| `contains` | Output must include a substring or key | Response contains `"status": "ok"` |
| `regex_match` | Output matches a regex pattern | Timestamp matches `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}` |
| `schema_valid` | Output conforms to a JSON/YAML schema | Response validates against `output_schema.json` |
| `range_check` | Numeric value falls within bounds | Latency between 50ms and 500ms |
| `not_empty` | Output is non-null and non-empty | Generated artifact body is not blank |
| `file_exists` | Expected output file was written to disk | `N03_engineering/P05_output/{slug}.md` exists |
| `frontmatter_valid` | YAML frontmatter parses and has required fields | `kind`, `id`, `pillar` present in frontmatter |
| `quality_above` | Quality score meets threshold | `quality >= 8.0` after `cex_score.py` |
| `signal_received` | Completion signal was emitted | Signal file in `.cex/runtime/signals/` matches expected |

## Test Scenario Matrix

Map each pipeline stage to its assertion patterns and expected failure modes.

| Stage | Input | Expected output | Assertion pattern | Failure mode |
|-------|-------|----------------|-------------------|-------------|
| F1 CONSTRAIN | [raw_user_intent] | Resolved `{kind, pillar, nucleus}` | `schema_valid` | Unknown kind, ambiguous pillar |
| F2 BECOME | Kind identifier | Builder loaded (12 ISOs) | `not_empty` | Missing builder directory |
| F3 INJECT | Kind + context refs | Assembled context bundle | `contains` | KC not found, empty examples |
| F6 PRODUCE | Context + builder | Generated artifact | `frontmatter_valid` + `quality_above` | Malformed output, low density |
| F7 GOVERN | Draft artifact | Quality score + gate pass | `range_check` | Score below 8.0, gate failure |
| F8 COLLABORATE | Final artifact | File saved + compiled + signaled | `file_exists` + `signal_received` | Write error, compile failure |

## Eval Configuration

```yaml
# E2E eval configuration for pipeline validation
eval:
  id: p07_e2e_[pipeline_slug]
  pipeline: [target_pipeline_name]
  environment: [local|staging|prod_clone]
  timeout_seconds: 300
  retry_on_flaky: true
  max_retries: 2

  seed_data:
    fixtures:
      - path: [fixture_path_1]
        format: yaml
      - path: [fixture_path_2]
        format: json
    reset_before_run: true

  stages:
    - name: setup
      commands:
        - "python _tools/cex_doctor.py --quick"
        - "[additional_setup_commands]"

    - name: execute
      commands:
        - "[pipeline_trigger_command]"
      capture:
        stdout: true
        artifacts: [output_dir]

    - name: assert
      assertions:
        - pattern: file_exists
          target: "[expected_output_path]"
        - pattern: frontmatter_valid
          target: "[expected_output_path]"
          required_fields: [id, kind, pillar, quality]
        - pattern: quality_above
          target: "[expected_output_path]"
          threshold: 8.0

    - name: teardown
      commands:
        - "[cleanup_command_1]"
      always_run: true
```

## Metrics Collection

| Metric | Collection method | Threshold | Unit |
|--------|------------------|-----------|------|
| Pipeline latency (total) | Timer around full e2e run | < 300s | seconds |
| Per-stage latency | Timer per stage block | < 60s per stage | seconds |
| Artifact quality score | `cex_score.py` output | >= 8.0 | score (0-10) |
| Assertion pass rate | Count pass/fail per run | 100% for blockers | percentage |
| Signal delivery latency | Time between F8 save and signal file creation | < 5s | seconds |
| Compilation success | `cex_compile.py` exit code | exit 0 | boolean |
| Regression detection | Compare scores against baseline | no regression > 0.5 | delta |

## Flaky Test Handling

Flaky tests undermine confidence in the eval suite. Use these strategies to handle non-deterministic behavior.

- Mark known-flaky assertions with `flaky: true` in the eval config
- Flaky assertions retry up to `max_retries` before failing
- Log all flaky occurrences to `.cex/runtime/evals/flaky_log.jsonl`
- Review flaky log weekly; fix root cause or convert to warning
- Never promote a flaky assertion to blocker without stabilization

```python
# Example: running e2e eval programmatically
from _tools.cex_e2e_test import E2ERunner

runner = E2ERunner(
    config_path="N00_genesis/P07_evals/templates/tpl_e2e_eval.md",
    environment="local",
    timeout=300,
    verbose=True
)

results = runner.run()
for stage in results.stages:
    print(f"  {stage.name}: {'PASS' if stage.passed else 'FAIL'} ({stage.duration_ms}ms)")

if not results.all_passed:
    for failure in results.failures:
        print(f"  [FAIL] {failure.assertion}: {failure.reason}")
    raise SystemExit(1)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_[name_slug]]] | upstream | 0.42 |
| [[p03_sp_[agent_slug]]] | upstream | 0.39 |
| [[p02_iso_[agent_name]]] | upstream | 0.36 |
| [[p10_ss_[session_slug]]] | downstream | 0.32 |
| [[p11_qg_unit_eval]] | related | 0.16 |
