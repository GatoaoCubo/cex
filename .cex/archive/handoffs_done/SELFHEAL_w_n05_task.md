---
nucleus: N05
task: dispatch
created: 2026-04-15 18:23:26
---
# Task for N05

SELFHEAL W2 structural diagnosis

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.

## ON COMPLETION
1. Commit your work: git add -A && git commit -m "[N05] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
