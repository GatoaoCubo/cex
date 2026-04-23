---
id: pipeline_template_n03
kind: pipeline_template
nucleus: n03
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_pipeline_template.md
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  scenarios: [new_feature, bug_fix_unknown, bug_fix_known, refactoring, perf_opt]
scenario: refactoring
stages:
  - role: finder
    model_tier: medium
    optional: false
  - role: analyst
    model_tier: medium
    optional: false
  - role: architect
    model_tier: high
    optional: false
  - role: coder
    model_tier: high
    optional: false
  - role: reviewer
    model_tier: medium
    optional: false
  - role: tester
    model_tier: low
    optional: false
revision_loop:
  max_iterations: 3
  escalation_target: user
quality_gates:
  mandatory: [reviewer, tester]
  priority_order: [quality, tests, implementation]
version: 1.0.0
quality: 8.4
tags: [mirror, n03, engineering, hermes_assimilation, pipeline_template]
tldr: "N03 dev pipeline templates: refactor, feature, bug-fix. Quality-first gate sequence with 8F alignment."
created: "2026-04-18"
related:
  - bld_instruction_hitl_config
  - p10_lr_golden_test_builder
  - bld_knowledge_card_golden_test
  - bld_config_hitl_config
  - quality-gate-builder
---

## Axioms

1. **Finder before coder** -- never write code before locating all affected surfaces.
2. **Reviewer is mandatory** -- no pipeline ships without a code quality gate.
3. **Tester closes the loop** -- regression gate is the last gate, not an afterthought.

## Canonical Stage Sequences

| Scenario | Stages | Notes |
|----------|--------|-------|
| new_feature | finder -> architect -> coder -> reviewer -> tester | architect required; design before implement |
| bug_fix_known | finder -> debugger -> fixer -> reviewer -> tester | known root cause; skip analyst |
| bug_fix_unknown | finder -> analyst -> debugger -> fixer -> reviewer -> tester | analyst required to locate root cause |
| refactoring | finder -> analyst -> architect -> refactorer -> reviewer -> tester | architect validates structure changes |
| perf_opt | finder -> analyst -> optimizer -> reviewer -> tester | optimizer role required; no architecture change |

## Quality Gates (N03)

| Gate | Role | Pass Criteria |
|------|------|--------------|
| Code quality | reviewer | No anti-patterns, density >= 0.85, 8F trace present |
| Regression | tester | All tests pass, no new failures |
| Schema integrity | reviewer | Breaking changes flagged + documented |

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Skipping finder | Missed callsites | finder is always stage 1, non-optional |
| Coder before architect (new_feature) | Design debt compounds | architect precedes coder in new_feature |
| Tester as optional | Silent regressions | tester is mandatory in all scenarios |
| Reviewer only at end | Late detection | reviewer can run mid-pipeline on large features |

## Instantiation

```python
from cex_sdk.pipeline import Pipeline
pl = Pipeline.from_template('pipeline_template_n03.yaml')
result = pl.run(task='refactor auth module', codebase='src/')
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_hitl_config]] | upstream | 0.19 |
| [[p10_lr_golden_test_builder]] | upstream | 0.18 |
| [[bld_knowledge_card_golden_test]] | upstream | 0.18 |
| [[bld_config_hitl_config]] | upstream | 0.18 |
| [[quality-gate-builder]] | upstream | 0.15 |
