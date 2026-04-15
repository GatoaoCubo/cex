---
mission: POLISH
wave: 3
status: PASS
executed_by: n07_direct
planned_dispatch: N07 direct (forensic + code edits)
actual_dispatch: N07 direct for all 3 tasks
tasks_completed: 3 of 3
commits: 2 (+ this consolidation)
---

# POLISH W3 Consolidation

## Summary

Close-the-loop wave on deferred W1/W2 items:

1. **Generator audit** (deferred from W2) -- traced commit-msg-as-filename bug to its amplifier.
2. **Root-write linter** (W2 next-step #2) -- added pre-commit gate blocking orphan root files.
3. **Codex dispatch diagnosis** (W1 deferred #2) -- found HTTP 400 from unsupported model pin, fixed 7 wrappers.

All three tasks mechanical + forensic; N07 direct execution per
`feedback_multiruntime_verification.md`.

## Tasks

| # | task | executor | files | commit |
|---|------|----------|-------|--------|
| 1 | Generator audit (no code change; findings below) | N07 | 0 | -- |
| 2 | Root-write gate in cex_hooks.py pre-commit | N07 | 1 | d0d9d422a |
| 3 | Strip gpt-5-codex model pin from 7 boot wrappers | N07 | 7 | 7813eb115 |

## Task 1: Generator audit -- commit-msg-as-filename bug

**Files deleted in W2.1** (3 of them):
- `- Keep and complete YAML frontmatter`
- `- More efficient resource utilization through parallel processing`
- `- Update workflow policies`

**Creating commits** (`git log --all --diff-filter=A -- <file>`):
- `aa2d263be` -- `[AUTO] cycle 2340: 9 artifacts improved, 0 rejected`
- `fffdf1676` -- `[AUTO] cycle 1983: 9 artifacts improved, 0 rejected`

**Content of `- Keep and complete YAML frontmatter`** (from aa2d263be):
```
I will improve the n02_task.md file to meet the quality target of 9.0+ by
expanding it to 80+ lines. I'll follow the structure and format of the
kc_skill.md file, adding structured data, tables, and practical examples.

n02_task.md
```

That's an **LLM instruction echo** -- the model parroted the prompt's first
bullet (`- Keep and complete YAML frontmatter...`) as its opening line, and
something used that line as a filename slug. But the commit touches **both**
the stray file AND `n02_task.md` (correctly edited).

**Amplifier identified**: `cex_auto_research.py:502` and `cex_auto.py:339`
(and 5 other tools) do:

```python
subprocess.run(["git", "add", "-A"], capture_output=True, timeout=30)
```

`git add -A` sweeps **every** stray file in the working tree. So the actual
sequence was:

1. Some parallel writer (likely an aider/ollama call) got the LLM response
2. That writer crashed or mis-wrote, leaving a transient file at repo root
   whose name was derived from the response's first line
3. Before cleanup, `cex_auto_research.py` finished its cycle and ran
   `git add -A` -- sweeping the orphan into the `[AUTO]` commit

The specific **filename-from-first-line writer** was not localized (too many
candidates: cex_evolve_ollama.py, aider wrappers, partial-write temp paths).
The important fix is to **kill the amplifier** -- W3.2 root-write gate now
blocks any non-whitelisted root file at pre-commit time, so no future
`git add -A` sweep can land one.

Tools using `git add -A`:
```
_tools/cex_auto.py:339
_tools/cex_auto_research.py:502
_tools/cex_continuous.py:277
_tools/cex_evolve_ollama.py:401
_tools/cex_evolve_below9.py:77
_tools/cex_mission_runner.py:612
_tools/cex_mission.py:175
```

**Decision:** do NOT change `git add -A` to narrower paths -- too invasive,
too many tools, and the pre-commit gate catches misfires deterministically.

## Task 2: Root-write gate

Added `ROOT_WHITELIST` + `check_root_writes()` to `_tools/cex_hooks.py`
and wired into `run_pre_commit()` as check #8.

**Whitelist** (known-good root surface):
```
CLAUDE.md, README.md, QUICKSTART.md, CONTRIBUTING.md, CHANGELOG.md,
LICENSE, MIT_LICENSE, CODE_OF_CONDUCT.md,
.gitignore, .gitattributes, .editorconfig, .env.example,
requirements.txt, requirements-llm.txt, pyproject.toml,
setup.py, setup.cfg, Makefile, package.json, package-lock.json,
tsconfig.json, .mcp.json
```

**Behavior**: only fires on `--diff-filter=A` (additions). Modifying an
existing whitelisted file is fine. Nested paths (anything with `/`) are
ignored -- pillar/tool dirs are pillar-owned and out of scope.

**Test** (simulated W2.2 recurrence):
```
$ echo "test" > test_orphan && git add test_orphan && python _tools/cex_hooks.py pre-commit
  [FAIL] root-write: 'test_orphan' is not in ROOT_WHITELIST
         Generator misfire? Move to a pillar dir ...
         If intentional, add 'test_orphan' to ROOT_WHITELIST in _tools/cex_hooks.py.
pre-commit: BLOCKED -- 1 error(s).
```

## Task 3: Codex dispatch diagnosis

**W1 symptom**: `codex --dangerously-bypass-approvals-and-sandbox` exited
within 2min with zero output/commits/diffs, twice. `feedback_multiruntime_verification.md`
noted this as an undiagnosed startup failure.

**Root cause** (reproduced in ~5s):
```
$ codex exec --dangerously-bypass-approvals-and-sandbox --model gpt-5-codex \
      -C "$(pwd)" "Print ACK"
...
ERROR: {"type":"error","status":400,"error":{"type":"invalid_request_error",
  "message":"The 'gpt-5-codex' model is not supported when using Codex
             with a ChatGPT account."}}
```

This install authenticates codex-cli 0.120.0 via a **ChatGPT account**
(not an OpenAI API key). On ChatGPT auth, `gpt-5-codex` is **not exposed**.
Request returns HTTP 400 immediately; codex prints the error and exits 0;
watchdog sees a clean exit and moves on. Zero signal that anything failed.

**Fix**: strip the `--model gpt-5-codex` override from all 7 boot wrappers
(`cex_codex.ps1` + `n01..n06_codex.ps1`). Codex falls back to the
ChatGPT-account default, which on this install is `gpt-5.4`.

**Verification**:
```
$ codex exec --dangerously-bypass-approvals-and-sandbox -C "$(pwd)" \
      "Reply with exactly: READY"
...
codex
READY
tokens used
10.563
```

Works end-to-end in ~10s. Exit 0 is now meaningful.

**Forward compat**: if a future machine uses API-key auth, set the model
via config (`~/.codex/config.toml` `model = "gpt-5-codex"`) or the `-c
model=...` CLI flag -- both win over the (now-absent) wrapper default.

## Verification

```
$ git log --oneline -3
7813eb115 fix(codex): POLISH W3 strip unsupported gpt-5-codex model pin
d0d9d422a feat(hooks): POLISH W3 add root-write gate to pre-commit
383f8febb docs(polish): W2 consolidation log (4 tasks, 149 files removed, README refresh)

$ git status
On branch main
nothing to commit, working tree clean

$ grep -c 'gpt-5-codex' boot/*codex*.ps1 | grep -v ':0' | grep -c 'ps1:[1-9]'
0      # only comment-string references remain (documented in header)

$ python _tools/cex_hooks.py pre-commit   # against empty stage
pre-commit: no files staged
```

## Remote divergence

Origin was pushed between W2 consolidation and W3 start (user triggered
via prior authorization). Current state: 3 commits ahead -- W3.2 + W3.3
+ this log -- all ready to push.

## Next

1. **git push origin main** -- 3-commit W3 bundle
2. **Codex end-to-end dispatch** -- now unblocked; next mission can
   actually route tasks to codex wrappers and see real work.
3. **Filename-from-first-line writer localization** (deferred) -- the
   bug amplifier is fixed (root-write gate), so this is low priority.
   If it ever re-surfaces, instrument cex_evolve_ollama.py and the
   aider path first.
4. **Multi-runtime re-enable** -- POLISH W1 authored `solo-codex` and
   `solo-gemini` dispatch modes but they were never exercised because
   codex was broken. Next POLISH wave can bench them with real work.
