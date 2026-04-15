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

# verify -- unified test + typecheck + lint chain

Execute the verification ladder, stop on first hard failure, report structured
results. This is the canonical post-change gate -- every non-trivial edit runs
through it before work is reported as done.

## Core test chain (stop-on-first-green)

The unified test invocation tries each runner in order and stops at the first
that executes:

```bash
bun run test || npm test || pytest -x -q
```

Rationale: `bun` is fastest when available, `npm` is the JS fallback,
`pytest` is the universal Python runner. The chain covers ~95% of CEX repos.

## Full ladder (run in order, stop on first hard failure)

1. **Sanitize** (ASCII code rule): `python _tools/cex_sanitize.py --check --scope _tools/`
2. **Unified tests**: `bun run test || npm test || pytest -x -q`.
3. **Python typecheck** (if mypy configured): `mypy <scope>`.
4. **JS/TS typecheck** (if `tsconfig.json`): `bun run typecheck || npx tsc --noEmit`.
5. **Lint** (warnings only, never blocks): `ruff check .` or `eslint .`.
6. **CEX health**: `python _tools/cex_doctor.py --quiet`.

## Graceful skip rules

- Missing tool / config -> `SKIP:<reason>`, not fail.
- >120s -> `TIMEOUT`, no silent retry.
- Known flaky -> acknowledge, max 1 retry.
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

Show full failing output. Propose minimum fix (1-2 lines). Do NOT auto-apply --
user confirms. Do NOT attempt the next step until the failure is resolved.
