---
nucleus: N06
task: dispatch
created: 2026-04-07 18:53:59
---
# Task for N06

Read .cex/runtime/handoffs/n06_task.md. AutoResearch: evolve 7 artifacts to 9.0+.

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.

## ON COMPLETION
1. Commit your work: git add -A && git commit -m "[N06] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'complete', 9.0)"
