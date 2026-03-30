@echo off
:: CEX N03 — Builder Nucleus (the factory that builds factories)
:: CLI: claude | Model: opus | Auth: Anthropic subscription
:: MCPs: github
:: Domain: build artifacts, 8F pipeline, all 99 kinds

title CEX-N03-BUILDER
set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-opus-4-0 --no-chrome
set MCP=--mcp-config "%CEX_ROOT%\.mcp-n03.json"
set SETTINGS=--settings "%CEX_ROOT%\.claude\nucleus-settings\n03.json"

set IDENTITY=Voce e o Builder Nucleus (N03) do CEX. REGRA ABSOLUTA: Todo artefato DEVE passar pelo pipeline 8F (F1-F8). Mostre o trace 8F em CADA build. Leia .claude/rules/n03-8f-enforcement.md PRIMEIRO. Depois leia N03_engineering/agents/agent_engineering.md para sua identidade. Commit e signal ao terminar.

if "%~1"=="" (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY%"
) else (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY% TAREFA: %~1"
)
