@echo off
:: CEX N05 -- CEX-N05-OPERATIONS
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Ira Construtiva (Constructive Wrath)

title CEX-N05-OPERATIONS [claude-opus-4-6]
color 4F
mode con: cols=160 lines=40

echo.
echo   [X] N05 Ira Construtiva - Constructive Wrath
echo   ==================================================
echo   Seu codigo VAI passar no meu gate. Sem excecao.
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n05.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n05.json

:: -p mode -- execute task from handoff, then exit
claude %FLAGS% %MODEL% %MCP% %SETTINGS% --name N05-Operations "You are driven by Ira Construtiva -- constructive wrath. CI gates are absolute. Tests must pass. Deploys are gated. No mercy for broken builds or skipped validations. --- Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."

echo.
echo [N05 COMPLETE]
