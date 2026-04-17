---
nucleus: n01
mission: SHOWOFF_W2
runtime: gemini
model: gemini-2.5-flash
---
# N01 -- SHOWOFF Wave 2 (gemini)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w2/` if missing.
2. Create file `_showoff/w2/n01_gemini.md` with EXACTLY this content:

```
---
id: showoff_w2_n01_gemini
kind: smoke_eval
title: "SHOWOFF Wave 2 -- n01 via gemini"
version: 1
quality: null
pillar: P07
nucleus: n01
runtime: gemini
model: gemini-2.5-flash
wave: 2
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 2

Nucleus: n01
Runtime: gemini
Model: gemini-2.5-flash
Signed: alive
```

3. Run: `git add _showoff/w2/n01_gemini.md && git commit -m "[n01] SHOWOFF W2 via gemini"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n01', 'complete', 9.0, mission='SHOWOFF_W2')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
