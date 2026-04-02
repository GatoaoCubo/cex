@echo off
:: CEX Boot - N07 Orchestrator (nucleus mode)
:: Runtime: pi (subscription/OAuth) | Model: claude-opus-4-6 | Thinking: xhigh
:: The orchestrator. NEVER builds. Dispatches to N01-N06.

title CEX-N07-ORCHESTRATOR
set CLAUDECODE=
set CEX_NUCLEUS=N07
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: ALWAYS interactive — N07 orchestrates, never receives task args
:: Reads handoff from .cex/runtime/handoffs/n07_task.md if present
pi --model anthropic/claude-opus-4-6 --thinking xhigh
