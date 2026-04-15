---
name: verify
description: Run the project's test + typecheck + lint chain and report pass-fail per layer.
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]
activation:
  triggers: ["/verify", "verify", "run tests", "check everything"]
  nuclei: [N03, N05, N07]
  depth: full
mirror_of: .claude/skills/verify.md
---

# verify — test + typecheck + lint chain

Execute the verification ladder, stop on first hard failure, report structured results.

## Chain (stop-on-fail)

1. **Sanitize** (ASCII code rule): `python _tools/cex_sanitize.py --check --scope _tools/`
2. **Python tests**: `pytest -x -q` (or `python -m pytest`).
3. **Python typecheck** (if mypy configured): `mypy <scope>`.
4. **JS/TS tests** (if `package.json`): `bun test || npm test`.
5. **JS/TS typecheck** (if `tsconfig.json`): `bun run typecheck || npx tsc --noEmit`.
6. **Lint** (last, warnings only): `ruff check .` or `eslint .`.
7. **CEX health**: `python _tools/cex_doctor.py --quiet`.

## Graceful skip rules

- Missing tool / config -> `SKIP:<reason>`, not fail.
- >120s -> `TIMEOUT`, no silent retry.
- Known flaky -> acknowledge, max 1 retry.

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

Show full failing output. Propose minimum fix (1-2 lines). Do NOT auto-apply -- user confirms.
