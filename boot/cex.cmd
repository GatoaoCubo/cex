@echo off
:: CEX Boot - N07 Orchestrator (replaces STELLA)
:: Runtime: pi | Model: claude-opus-4-6 | Thinking: xhigh
:: This is the FACTORY ORCHESTRATOR. It dispatches N03 builders.

:: Auto-elevate to Admin
net session >nul 2>&1 || (
    echo [CEX-N07] Elevating to Admin...
    powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/k \"%~f0\" %*'"
    exit /b
)

title CEX-N07-ORCHESTRATOR
set CLAUDECODE=
set CEX_NUCLEUS=N07
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

if "%~1"=="" (
    pi --model anthropic/claude-opus-4-6 --thinking xhigh "Voce e o Orquestrador CEX (N07). NUNCA execute tarefas de construcao. SEMPRE dispatch via spawn_solo.ps1 ou spawn_grid.ps1 para N03 builders. Leia CLAUDE.md primeiro."
) else (
    pi --model anthropic/claude-opus-4-6 --thinking xhigh %*
)
