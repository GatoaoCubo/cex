@echo off
:: CEX Boot - N07 Orchestrator
:: Runtime: pi (subscription/OAuth) | Model: claude-opus-4-6 | Thinking: xhigh
:: The orchestrator. NEVER builds. Dispatches to N01-N06.

title CEX-N07-ORCHESTRATOR
set CLAUDECODE=
set CEX_NUCLEUS=N07
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

if "%~1"=="" (
    pi --model anthropic/claude-opus-4-6 --thinking xhigh
) else (
    pi --model anthropic/claude-opus-4-6 --thinking xhigh %*
)
