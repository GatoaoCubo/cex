@echo off
:: CEX Boot - N03 Builder Nucleus (replaces EDISON)
:: Runtime: claude CLI | Model: opus | MCP: optional

title CEX-N03-BUILDER
set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model opus --no-chrome

set IDENTITY=Voce e o Builder Nucleus (N03). Leia N03_engineering/agents/agent_engineering.md e N03_engineering/prompts/system_prompt_engineering.md. Depois execute as tarefas do handoff em .cex/handoffs/.

if "%~1"=="" (
    claude %FLAGS% "%IDENTITY%"
) else (
    claude %FLAGS% %*
)
