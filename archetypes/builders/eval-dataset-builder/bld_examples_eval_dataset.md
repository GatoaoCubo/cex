---
kind: examples
id: bld_examples_eval_dataset
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of eval_dataset artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: eval-dataset-builder
## Golden Example
INPUT: "Create eval dataset for testing CEX artifact quality gate validation — 200 cases covering all 10 HARD gate checks"
OUTPUT:
```yaml
id: p07_ds_artifact_quality_gate_eval
kind: eval_dataset
pillar: P07
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "CEX Artifact Quality Gate Evaluation Dataset"
size: 200
splits:
  test: 1.0
schema_fields:
  - input
  - expected_output
  - metadata
quality: null
tags: [eval_dataset, quality-gate, artifact-validation, P07]
tldr: "200 test cases covering all 10 HARD gates for CEX artifact validation, eval-only split"
description: "Evaluation dataset for CEX artifact quality gate validation covering all hard gate failure modes"
source: "synthetic"
framework: "braintrust"
task_type: "classification"
language: "en"
license: "MIT"
refresh_cadence: "on-demand"
```
## Overview
Tests the CEX artifact quality gate validator across all 10 HARD gate conditions.
Used by EDISON to verify artifact validation logic and by CI to catch regression in gate checks.
## Schema
### input
Type: dict
The artifact under evaluation — contains `frontmatter` (dict) and `body` (string).
Example: `{"frontmatter": {"id": "p04_cli_foo", "kind": "cli_tool", "quality": null}, "body": "## Commands\n..."}`
### expected_output
Type: dict
The expected gate result — contains `passed` (bool), `failures` (list[string]), `score` (float or null).
Example: `{"passed": false, "failures": ["H05: quality is not null"], "score": null}`
### metadata
Type: dict
Case-level annotations for filtering and analysis.
Values: `{gate_id: "H05", failure_mode: "quality_not_null", difficulty: "easy", artifact_kind: "cli_tool"}`
## Splits
| Split | Percentage | Cases | Rationale |
|-------|-----------|-------|-----------|
| test | 100% | 200 | Pure evaluation — no training use for a rule-based validator |
Total: 100% (200 cases)
Split rationale: Quality gate validation is deterministic rule-checking, not learned behavior. All cases are test-only to maximize coverage signal per case.
## Integration
Framework: braintrust
Loading:
```python
import braintrust
project = braintrust.init("cex-quality-gates")
dataset = project.datasets.create(name="p07_ds_artifact_quality_gate_eval")
for case in dataset:
    result = validate_artifact(case["input"]["frontmatter"], case["input"]["body"])
    # compare to case["expected"]
```
Version migration: v1 -> v2 adds `gate_weights` to metadata dict. Load both versions with `dataset.pull(version="1.0.0")` for reproducibility.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_ds_ pattern (H02 pass)
- kind: eval_dataset (H04 pass)
- schema_fields has input + expected_output (H07 pass)
- splits: test: 1.0 sums to 1.0 (H08 pass)
- size: 200 positive integer (H09 pass)
- body has all 4 sections: Overview, Schema, Splits, Integration (H10 pass)
- schema_fields list matches ## Schema section names exactly
- source declared as synthetic (SOFT pass)
- framework specified as braintrust with loading snippet (SOFT pass)
- split rationale explains why train is absent (SOFT pass)
- task_type: classification matches schema design (SOFT pass)

## Anti-Example
INPUT: "Create eval dataset for testing my chatbot"
BAD OUTPUT:
```yaml
id: chatbot-eval
kind: dataset
pillar: evals
name: My Chatbot Eval
size: "a lot"
quality: 8.5
tags: [eval]
```
Some test cases for my chatbot.
## Cases
- Ask it about weather
- Ask it about sports
FAILURES:
1. id: "chatbot-eval" has hyphens and no `p07_ds_` prefix -> H02 FAIL
2. kind: "dataset" not "eval_dataset" -> H04 FAIL
3. pillar: "evals" not "P07" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. size: "a lot" not a positive integer -> H09 FAIL
6. Missing fields: splits, schema_fields, version, created, updated, author, tldr -> H06 FAIL
7. splits absent — cannot verify they sum to 1.0 -> H08 FAIL
8. schema_fields absent — input and expected_output not declared -> H07 FAIL
9. tags: only 1 item, missing "eval_dataset" -> SOFT FAIL
10. Body missing ## Schema, ## Splits, ## Integration sections -> H10 FAIL
11. "Cases" section contains prose descriptions, not schema — actual data in spec body -> SOFT FAIL
12. No source, framework, or task_type declared -> multiple SOFT FAIL
