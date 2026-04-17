---
nucleus: n03
mission: SHOWOFF_W5
runtime: codex
model: gpt-5-codex
---
# N03 -- SHOWOFF Wave 5 (codex)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w5/` if missing.
2. Create file `_showoff/w5/n03_codex.md` with EXACTLY this content:

```
---
id: showoff_w5_n03_codex
kind: smoke_eval
title: "SHOWOFF Wave 5 -- n03 via codex"
version: 1
quality: null
pillar: P07
nucleus: n03
runtime: codex
model: gpt-5-codex
wave: 5
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 5

Nucleus: n03
Runtime: codex
Model: gpt-5-codex
Signed: alive
```

3. Run: `git add _showoff/w5/n03_codex.md && git commit -m "[n03] SHOWOFF W5 via codex"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n03', 'complete', 9.0, mission='SHOWOFF_W5')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
