---
nucleus: n01
mission: SHOWOFF_W5
runtime: ollama
model: qwen3:8b
---
# N01 -- SHOWOFF Wave 5 (ollama)

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w5/` if missing.
2. Create file `_showoff/w5/n01_ollama.md` with EXACTLY this content:

```
---
id: showoff_w5_n01_ollama
kind: smoke_eval
title: "SHOWOFF Wave 5 -- n01 via ollama"
version: 1
quality: null
pillar: P07
nucleus: n01
runtime: ollama
model: qwen3:8b
wave: 5
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave 5

Nucleus: n01
Runtime: ollama
Model: qwen3:8b
Signed: alive
```

3. Run: `git add _showoff/w5/n01_ollama.md && git commit -m "[n01] SHOWOFF W5 via ollama"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n01', 'complete', 9.0, mission='SHOWOFF_W5')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
