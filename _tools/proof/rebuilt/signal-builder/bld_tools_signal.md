---
kind: tools
id: bld_tools_signal
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to signal production
---

# Tools: signal-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `signal_writer.py` | Real emitter pattern for completion signals | Schema alignment | CONDITIONAL |
| `spawn_monitor.ps1` | Polls `.claude/signals/` for status changes | Consumer validation | CONDITIONAL |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| Signal directory | `.claude/signals/` | write/read JSON event files |
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, limits |
| Signal template | `P12_orchestration/templates/tpl_signal.md` | human reference for event payload |
| Validation example | `P06_schema/examples/p06_vs_signal_completion.md` | downstream consumer expectation |
## Interim Validation
Until a generic validator exists, validate manually:
- filename matches `p12_sig_{event}.json`
- JSON parses
- core fields present
- status in enum
- timestamp is ISO 8601
- payload fits `signal`, not `handoff` or `dispatch_rule`
