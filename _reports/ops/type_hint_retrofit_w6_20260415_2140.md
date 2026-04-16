---
id: type_hint_retrofit_w6_20260415_2140
kind: context_doc
pillar: P01
title: Type Hint Retrofit W6
nucleus: N05
mission: TYPE_HINT_RETROFIT
wave: W6
runtime: codex
domain: operations_refactor
scope: Public-function type hint retrofit for three _tools modules plus verification and reporting.
quality: 9.0
created: 2026-04-15
updated: 2026-04-15
tags: [type_hint_retrofit, w6, n05, codex, report]
tldr: "Added public-function type hints to three target tools, verified 100 percent coverage, and recorded per-file commits."
density_score: 0.99
---

# Type Hint Retrofit W6

## Scope

Handoff: `.cex/runtime/handoffs/n05_task_codex.md`

Target files:
- `_tools/cex_system_test.py`
- `_tools/wave1_builder_gen_v2.py`
- `_tools/test_cex_wave_validator.py`

Constraint honored: annotations only on public functions. No body, name, decorator, or logic changes. ASCII-only preserved. Existing unrelated modifications in `_reports/overnight/` were left untouched.

## 8F Pipeline

=== 8F PIPELINE ===
F1 CONSTRAIN: kind=context_doc, pillar=P01, max_bytes=2048, naming=p01_ctx_{{topic}}.md + .yaml; task=annotation-only retrofit and verification from handoff frontmatter.
F2 BECOME: loaded N05 operations rules, N05 agent card, and context_doc builder manifest/instructions for report shape and operating constraints.
F3 INJECT: injected handoff scope, target module contents, context_doc KC, pre-edit AST coverage, and current git state.
F4 REASON: annotate every non-underscore function signature, prefer builtin generics, use Any only for heterogeneous runtime-loaded structures, verify before any reporting.
F5 CALL: used AST coverage checks, CLI/import sanity checks, git commits, cex_compile, and signal_writer.
F6 PRODUCE: updated 3 target files; public-function coverage reached 100 percent on every file.
F7 GOVERN: all AST checks passed at full coverage; required CLI `--help` and import checks passed; pre-commit ASCII/sanitize hooks passed on each file commit.
F8 COLLABORATE: saved this report, compiled it, committed it, and sent the N05 completion signal.
===================

## Coverage Delta

| File | Before | After | Notes |
|------|--------|-------|-------|
| `_tools/cex_system_test.py` | 1/19 | 19/19 | Added missing `None` returns across test helpers and `int` on `main()`. |
| `_tools/wave1_builder_gen_v2.py` | 2/22 | 22/22 | Added `Any` import and annotated prompt/build helpers, generator interfaces, and return contracts. |
| `_tools/test_cex_wave_validator.py` | 3/15 | 15/15 | Added `Any` import, typed assertion helpers, and completed return annotations on test functions. |

## Sanity Checks

AST verification:
- `_tools/cex_system_test.py`: `19 / 19`
- `_tools/wave1_builder_gen_v2.py`: `22 / 22`
- `_tools/test_cex_wave_validator.py`: `15 / 15`

Runtime checks:
- `python _tools/cex_system_test.py --help` -> exit 0
- `python _tools/wave1_builder_gen_v2.py --help` -> exit 0
- `python _tools/test_cex_wave_validator.py --help` -> exit 0
- `python -c "import _tools.cex_system_test"` -> exit 0
- `python -c "import _tools.wave1_builder_gen_v2"` -> exit 0
- `python -c "import _tools.test_cex_wave_validator"` -> exit 0

Hook and quality checks:
- Git pre-commit hook: PASS on all 3 target commits.
- `cex_sanitize.py --check --scope _tools/`: PASS during each commit gate.

## Commit List

- `5c853b1e59ac4090640e2645e302d2ad5eb6e652` `refactor(cex_system_test): add type hints to public functions`
- `7bc422d4ccf4d26ca81e82157a463e1915b8efbc` `refactor(wave1_builder_gen_v2): add type hints to public functions`
- `0e2d0b7aa809c4de72ae4e4d5bf0869bcdf369b1` `refactor(test_cex_wave_validator): add type hints to public functions`

## Ambiguous Cases

- `_tools/wave1_builder_gen_v2.py`: used `dict[str, Any]` for kind metadata because values are loaded from `.cex/kinds_meta.json` and vary by field and shape.
- `_tools/test_cex_wave_validator.py`: used `dict[str, Any]` for synthesized frontmatter overrides because test cases intentionally mix strings, numbers, nulls, and list-like values.

## TYPE_HINT_RETROFIT_W6_PASS
