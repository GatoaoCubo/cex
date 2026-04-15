---
nucleus: n01
mission: SHOWOFF_W4
runtime: claude
model: claude-haiku-4-5-20251001
---
# N01 -- SHOWOFF Wave 4 (claude)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w4/` if missing.
2. Create file `_showoff/w4/n01_claude.md` with EXACTLY this content:

```
---
id: showoff_w4_n01_claude
kind: smoke_eval
title: "SHOWOFF Wave 4 -- n01 via claude"
version: 1
quality: null
pillar: P07
nucleus: n01
runtime: claude
model: claude-haiku-4-5-20251001
wave: 4
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 4

Nucleus: n01
Runtime: claude
Model: claude-haiku-4-5-20251001
Signed: alive
```

3. Run: `git add _showoff/w4/n01_claude.md && git commit -m "[n01] SHOWOFF W4 via claude"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n01', 'complete', 9.0, mission='SHOWOFF_W4')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
