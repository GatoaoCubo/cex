---
name: verify
description: Run the project's test / type-check / lint chain and report pass-fail per layer. Use when user says "verify", "/verify", "run tests", or after any non-trivial code change before handing control back.
---

# verify -- unified test + typecheck + lint chain

Execute the verification ladder, stop on first hard failure, report structured
results. This is the canonical post-change gate -- every non-trivial edit runs
through it before work is reported as done.

## Core test chain (stop-on-first-green)

The unified test invocation tries each runner in order and stops at the first
that executes (not the first that passes -- those are different things):

```bash
bun run test || npm test || pytest -x -q
```

Rationale: `bun` is fastest when available, `npm` is the JS fallback,
`pytest` is the universal Python runner. The chain covers ~95% of CEX repos.

## Full ladder (run in order, stop on first hard failure)

1. **Sanitize** (ASCII code rule): `python _tools/cex_sanitize.py --check --scope _tools/` (exit 1 = dirty).
2. **Unified tests**: `bun run test || npm test || pytest -x -q`.
3. **Python typecheck** (if `mypy.ini` or `pyproject.toml` has mypy): `mypy <scope>`.
4. **JS/TS typecheck** (if `tsconfig.json`): `bun run typecheck || npx tsc --noEmit`.
5. **Lint** (warnings only, never blocks): `ruff check .` or `eslint .`.
6. **CEX health**: `python _tools/cex_doctor.py --quiet`.

## Graceful skip rules

- Step unavailable (no tool, no config) -> skip with `SKIP:<reason>`, not fail.
- Step times out > 120s -> mark `TIMEOUT`, do not retry silently.
- Flaky-known test: acknowledge, do not rerun more than once.
- Missing `package.json` AND missing `pyproject.toml` -> tests step is `SKIP`.

## Output format

```
VERIFY: {PASS|FAIL|PARTIAL}
 sanitize:  PASS
 tests:     PASS (bun: 47 passed, 2 skipped)
 mypy:      SKIP (no config)
 tsc:       PASS
 lint:      PARTIAL (3 warnings, 0 errors)
 doctor:    PASS (118/118 builders)
```

## After-fail protocol

If any hard-fail step fails:
1. Show the full failing output (not summarized).
2. Propose the minimum fix (1-2 lines).
3. Do NOT auto-apply -- user confirms.
4. Do NOT attempt the next step in the ladder until the failure is resolved.
