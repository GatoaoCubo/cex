---
nucleus: n02
mission: SHOWOFF_W5
runtime: gemini
model: gemini-2.5-flash
---
# N02 -- SHOWOFF Wave 5 (gemini)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w5/` if missing.
2. Create file `_showoff/w5/n02_gemini.md` with EXACTLY this content:

```
---
id: showoff_w5_n02_gemini
kind: smoke_eval
title: "SHOWOFF Wave 5 -- n02 via gemini"
version: 1
quality: null
pillar: P07
nucleus: n02
runtime: gemini
model: gemini-2.5-flash
wave: 5
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 5

Nucleus: n02
Runtime: gemini
Model: gemini-2.5-flash
Signed: alive
```

3. Run: `git add _showoff/w5/n02_gemini.md && git commit -m "[n02] SHOWOFF W5 via gemini"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n02', 'complete', 9.0, mission='SHOWOFF_W5')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
