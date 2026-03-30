@echo off
:: CEX Boot - N07 Orchestrator
:: Runtime: claude CLI (subscription) | Model: opus | Dispatch only
:: The orchestrator. NEVER builds. Dispatches to N01-N06.

title CEX-N07-ORCHESTRATOR
set CLAUDECODE=
set CEX_NUCLEUS=N07
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-opus-4-0 --no-chrome

set IDENTITY=Voce e o Orquestrador CEX (N07). NUNCA construa artefatos. SEMPRE dispatch via PowerShell: powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus [N0x] -task "[TASK]" -interactive. Leia CLAUDE.md e _docs/PLAYBOOK.md ANTES de despachar. Leia .claude/rules/n07-orchestrator.md para suas regras.

if "%~1"=="" (
    claude %FLAGS% "%IDENTITY%"
) else (
    claude %FLAGS% "%IDENTITY% TAREFA: %~1"
)
