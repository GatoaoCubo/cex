---
name: verify
description: Run the project's test / type-check / lint chain and report pass-fail per layer. Use when user says "verify", "/verify", "run tests", or after any non-trivial code change before handing control back.
---

# verify — test + typecheck + lint chain

Execute the verification ladder, stop on first hard failure, report structured results.

## Chain (stop-on-fail)

1. **Sanitize** (ASCII code rule): `python _tools/cex_sanitize.py --check --scope _tools/` (exit 1 = dirty).
2. **Python tests** (if any target is .py): `pytest -x -q` (or `python -m pytest`).
3. **Python typecheck** (if `mypy.ini` or `pyproject.toml` has mypy): `mypy <scope>`.
4. **JS/TS tests** (if `package.json` exists): `bun test || npm test`.
5. **JS/TS typecheck** (if `tsconfig.json`): `bun run typecheck || npx tsc --noEmit`.
6. **Lint** (last, warnings only): `ruff check .` or `eslint .`.
7. **CEX health**: `python _tools/cex_doctor.py --quiet`.

## Graceful skip rules

- Step unavailable (no tool, no config) → skip with `SKIP:<reason>`, not fail.
- Step times out > 120s → mark `TIMEOUT`, do not retry silently.
- Flaky-known test: acknowledge, do not rerun more than once.

## Output format

```
VERIFY: {PASS|FAIL|PARTIAL}
 sanitize:  PASS
 pytest:    PASS (47 passed, 2 skipped)
 mypy:      SKIP (no config)
 doctor:    PASS (118/118 builders)
 lint:      PARTIAL (3 warnings, 0 errors)
```

## After-fail protocol

If any hard-fail step fails:
1. Show the full failing output (not summarized).
2. Propose the minimum fix (1-2 lines).
3. Do NOT auto-apply — user confirms.
