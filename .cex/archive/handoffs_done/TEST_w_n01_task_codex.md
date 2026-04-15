---
nucleus: n01
mission: SHOWOFF_W3
runtime: codex
model: gpt-5-codex
---
# N01 -- SHOWOFF Wave 3 (codex)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w3/` if missing.
2. Create file `_showoff/w3/n01_codex.md` with EXACTLY this content:

```
---
id: showoff_w3_n01_codex
kind: smoke_eval
title: "SHOWOFF Wave 3 -- n01 via codex"
version: 1
quality: null
pillar: P07
nucleus: n01
runtime: codex
model: gpt-5-codex
wave: 3
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 3

Nucleus: n01
Runtime: codex
Model: gpt-5-codex
Signed: alive
```

3. Run: `git add _showoff/w3/n01_codex.md && git commit -m "[n01] SHOWOFF W3 via codex"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n01', 'complete', 9.0, mission='SHOWOFF_W3')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
