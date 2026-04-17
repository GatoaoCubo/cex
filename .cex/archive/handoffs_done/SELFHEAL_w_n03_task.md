---
nucleus: N03
task: dispatch
created: 2026-04-15 18:47:08
---
# Task for N03

SELFHEAL W4 structural heals RETRY

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.

## ON COMPLETION
1. Commit your work: git add -A && git commit -m "[N03] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
