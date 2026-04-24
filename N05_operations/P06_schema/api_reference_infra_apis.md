---
id: p06_ar_infra_apis
kind: api_reference
8f: F5_call
pillar: P06
title: "N05 Infrastructure API Reference"
version: "v1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: api-reference-builder
domain: "infrastructure APIs, CI/CD tooling"
nucleus: N05
quality: 9.1
tags: [api_reference, n05, infrastructure, cli, compile, doctor, hooks, signal, dispatch, system_test]
tldr: "CLI surface for all N05-owned infra operations: compile, doctor, hooks, signals, dispatch, system validation."
endpoint: "_tools/ and _spawn/"
authentication: "None -- local CLI tools, no token required"
density_score: 1.0
related:
  - validate
  - p12_wf_admin_orchestration
  - doctor
  - p04_ct_cex_compile
  - p01_kc_cex_orchestration_architecture
  - p02_agent_creation_nucleus
  - p11_qg_admin_orchestration
  - agent_card_engineering_nucleus
  - p01_kc_orchestration_best_practices
  - ctx_cex_new_dev_guide
---

## Overview

N05 (Operations, Gating Wrath) owns the CEX infrastructure CLI surface. No HTTP endpoints, no auth tokens. All tools run from repo root.

| Tool | 8F Stage | Purpose |
|------|----------|---------|
| `cex_compile.py` | F8 | `.md` -> `.yaml` compilation |
| `cex_doctor.py` | F7 | Builder ISO health diagnostics |
| `cex_hooks.py` | F7 | Pre/post save validation |
| `signal_writer.py` | F8 | Inter-nucleus completion signals |
| `dispatch.sh` | F8 | Process management (solo/grid/stop) |
| `cex_system_test.py` | F7 | Full system validation (54 tests) |

---

## 1. cex_compile.py

| Param | Type | Required | Values |
|-------|------|----------|--------|
| `file` | positional | no | any `.md` path |
| `--all` | flag | no | compile all LPs |
| `--lp` | string | no | `P01`..`P12` |
| `--target` | string | no | `claude-md`, `cursorrules`, `customgpt`, `mcp` |
| `--output`/`-o` | string | no | output path (for `--target`) |

**Exit Codes:** `0` success | `1` parse error | `2` file not found

```bash
python _tools/cex_compile.py N05_operations/P06_schema/api_reference_infra_apis.md
python _tools/cex_compile.py --lp P06
python _tools/cex_compile.py --target claude-md -o _docs/compiled/out.md
```

---

## 2. cex_doctor.py

Checks 13 ISO files per builder, naming `bld_[a-z][a-z0-9_]+_[a-z][a-z0-9_]+.md`,
density >= 0.78, size <= 6144B (instruction: 8192B).

| Param | Required | Description |
|-------|----------|-------------|
| `--fix` | no | Auto-rename files failing naming regex |

**Output:** `PASS` | `WARN` (density/optional) | `FAIL` (missing ISOs/size)
**Exit Codes:** `0` all pass | `1` issues found

```bash
python _tools/cex_doctor.py
python _tools/cex_doctor.py --fix
```

---

## 3. cex_hooks.py

Enforces `id`, `kind`, `pillar`, `quality` (hard fail); `title`, `version`, `author`, `tags`, `tldr`, `domain` (warn); pillar `^P\d{2}$`; byte limits.

| Subcommand | Trigger | Description |
|------------|---------|-------------|
| `pre-save <file>` | Before write | Frontmatter + naming + size |
| `post-save <file>` | After write | Compile + index |
| `validate <file+>` | Manual | Full validation |
| `validate-all` | Manual | All nucleus artifacts |
| `pre-commit` | git hook | All staged `.md` files |
| `install` | One-time | Install git pre-commit hook |

**Exit Codes:** `0` pass | `1` hard gate failed

```bash
python _tools/cex_hooks.py pre-save N05_operations/P06_schema/api_reference_infra_apis.md
python _tools/cex_hooks.py validate-all
python _tools/cex_hooks.py install
```

---

## 4. signal_writer.py

Writes JSON signal files to `.cex/runtime/signals/`. N07 polls these to detect
nucleus completion and advance mission waves.

**Python interface:**
```python
from _tools.signal_writer import write_signal
write_signal(nucleus, status="complete", quality_score=9.0, mission="", wave=None)
```

**Parameters**

| Param | Type | Required | Constraints |
|-------|------|----------|-------------|
| `nucleus` | string | yes | `n01`..`n07` or wave phase `w1`, `w2`, ... |
| `status` | string | no | `^[a-z_]+$`, default `complete` |
| `quality_score` | float | no | `0.0`-`10.0`, default `9.0` |
| `mission` | string | no | mission name tag |
| `wave` | int | no | wave index (embedded in filename) |

**Payload fields:** `nucleus`, `status`, `quality_score`, `mission`, `timestamp` (UTC ISO 8601), `wave`

Filename: `signal_{nucleus}_{mission}_w{wave}_{ts}.json`
**Returns:** path string | raises `ValueError` on invalid nucleus, score, or status

```bash
# CLI
python _tools/signal_writer.py n05 complete 9.0 INFRA_AUDIT

# Python (F8 standard)
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
```

---

## 5. dispatch.sh

Session-aware process management. `stop` kills only the calling N07's session nuclei.
Multiple concurrent N07 orchestrators are safe.

| Command | Description |
|---------|-------------|
| `bash _spawn/dispatch.sh solo <nucleus> "<task>"` | Dispatch 1 nucleus |
| `bash _spawn/dispatch.sh grid <MISSION>` | Dispatch up to 6 parallel |
| `bash _spawn/dispatch.sh status` | Show running processes |
| `bash _spawn/dispatch.sh stop` | Stop MY session's nuclei |
| `bash _spawn/dispatch.sh stop <nucleus>` | Stop one nucleus |
| `bash _spawn/dispatch.sh stop --all` | Stop ALL nuclei (dangerous) |
| `bash _spawn/dispatch.sh stop --dry-run` | Preview kill targets |
| `bash _spawn/dispatch.sh swarm <kind> <N> "<task>"` | N parallel worktrees |

**Parameters**

| Param | Required | Description |
|-------|----------|-------------|
| `nucleus` | yes (solo) | `n01`..`n06` |
| `MISSION` | yes (grid) | Handoffs must exist in `.cex/runtime/handoffs/` |
| `kind` / `N` | yes (swarm) | Builder kind and instance count |
| `-w <id>` | no | Isolate in git worktree; `auto` generates ID |

**Environment Variables**

| Variable | Default | Description |
|----------|---------|-------------|
| `CEX_SESSION_ID` | `s{timestamp}` | Scopes `stop` to this N07 session |
| `OLLAMA_MODEL` | `qwen3:8b` | Model for ollama grid/solo modes |

**Grid Variants:** `grid` (Opus, default) | `grid-haiku` (budget) | `grid-ollama` (free, max 3) | `grid-litellm` (proxy :4000) | `grid-codex` (no auto-commit)

**Exit Codes:** `0` dispatch launched | `1` invalid mode or missing arg

```bash
bash _spawn/dispatch.sh solo n03 "build kind=api_reference"
bash _spawn/dispatch.sh grid BRAND_LAUNCH
bash _spawn/dispatch.sh stop --dry-run
bash _spawn/dispatch.sh swarm agent 4 "scaffold sales agents"
```

---

## 6. cex_system_test.py

54-test suite validating all CEX system layers. Run after bootstrap or major changes.

| Command | Description |
|---------|-------------|
| `python _tools/cex_system_test.py` | Full suite (includes LLM tests) |
| `python _tools/cex_system_test.py --quick` | Skip LLM tests (~10s) |

**Coverage**

| Area | What is checked |
|------|----------------|
| Tools | All `_tools/*.py` importable, `--help` exits 0 |
| Builders | 13 ISO files present per builder |
| Artifacts | Frontmatter validity, naming, size |
| Hooks | pre-save / post-save / validate on sample artifacts |
| Runner | `cex_8f_runner.py` dry-run completes |
| Infrastructure | Signal dir, PID dir, handoff dir writable |

**Output symbols:** `[OK]` PASS | `[FAIL]` FAIL (detail inline) | `>>` SKIP

**Exit Codes:** `0` all pass | `1` any failure

```bash
python _tools/cex_system_test.py --quick   # CI gate
python _tools/cex_system_test.py           # post-bootstrap full check
```

---

## Error Reference

| Code | Tool | Cause | Resolution |
|------|------|-------|------------|
| `1` | compile | Bad frontmatter/YAML | Fix frontmatter, re-run |
| `1` | doctor | Missing ISOs or naming violation | Add ISOs or run `--fix` |
| `1` | hooks | Required field absent | Add `id`, `kind`, `pillar`, `quality` |
| `ValueError` | signal_writer | Invalid nucleus or score out of range | `n01`..`n07`; score `0.0`-`10.0` |
| `1` | dispatch | Missing handoff for grid mission | Write handoff to `.cex/runtime/handoffs/` |
| `1` | system_test | Any test failed | Read `[FAIL]` lines; run `cex_doctor.py` |

## See Also

| Artifact | Description |
|----------|-------------|
| `N05_operations/P06_schema/health_check_schema.md` | Health check contract |
| `N05_operations/P06_schema/env_contract_schema.md` | Env variable contracts |
| `.cex/runtime/signals/` | Signal files from `signal_writer.py` |
| `.cex/runtime/handoffs/` | Handoff files read by dispatch |
| `.cex/runtime/pids/spawn_pids.txt` | PID tracking (session-aware) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[validate]] | downstream | 0.34 |
| [[p12_wf_admin_orchestration]] | downstream | 0.32 |
| [[doctor]] | downstream | 0.31 |
| [[p04_ct_cex_compile]] | upstream | 0.29 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.29 |
| [[p02_agent_creation_nucleus]] | upstream | 0.28 |
| [[p11_qg_admin_orchestration]] | downstream | 0.28 |
| [[agent_card_engineering_nucleus]] | upstream | 0.28 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.27 |
| [[ctx_cex_new_dev_guide]] | related | 0.27 |
