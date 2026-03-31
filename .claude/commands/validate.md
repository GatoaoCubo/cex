---
description: "Validate CEX artifacts. Usage: /validate [file|all]"
---

# /validate — Check Artifact Quality

Run validation hooks on artifacts.

## Usage

- `/validate all` — validate all 101 nucleus artifacts
- `/validate N07_admin/agents/agent_admin.md` — validate specific file
- `/validate` (no args) — validate all staged git files

## Steps

1. If `$ARGUMENTS` is "all":
   ```bash
   python _tools/cex_hooks.py validate-all
   ```
2. If `$ARGUMENTS` is a file path:
   ```bash
   python _tools/cex_hooks.py validate $ARGUMENTS
   ```
3. If no arguments:
   ```bash
   python _tools/cex_hooks.py pre-commit
   ```
4. Also run doctor:
   ```bash
   python _tools/cex_doctor.py
   ```
5. Report summary: errors, warnings, score distribution.
