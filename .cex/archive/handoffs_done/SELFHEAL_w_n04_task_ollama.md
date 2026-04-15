---
nucleus: n04
mission: SHOWOFF_W1
runtime: ollama
model: qwen3:8b
---
# N04 -- SHOWOFF Wave 1 (ollama)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w1/` if missing.
2. Create file `_showoff/w1/n04_ollama.md` with EXACTLY this content:

```
---
id: showoff_w1_n04_ollama
kind: smoke_eval
title: "SHOWOFF Wave 1 -- n04 via ollama"
version: 1
quality: null
pillar: P07
nucleus: n04
runtime: ollama
model: qwen3:8b
wave: 1
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 1

Nucleus: n04
Runtime: ollama
Model: qwen3:8b
Signed: alive
```

3. Run: `git add _showoff/w1/n04_ollama.md && git commit -m "[n04] SHOWOFF W1 via ollama"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n04', 'complete', 9.0, mission='SHOWOFF_W1')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
