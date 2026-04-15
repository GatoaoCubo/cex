---
nucleus: N04
task: dispatch
created: 2026-04-15 18:40:36
---
# Task for N04

SELFHEAL W4 content heals

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.

## ON COMPLETION
1. Commit your work: git add -A && git commit -m "[N04] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
