@echo off
:: CEX N03 — Builder Nucleus
:: CLI: claude | Model: opus | Auth: subscription | MCPs: github
:: 8F pipeline MANDATORY on every build

title CEX-N03-BUILDER
set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-opus-4-0 --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n03.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n03.json

:: ALWAYS interactive — task comes from handoff file, never CLI args
:: This avoids nested-quote hell that kills CMD
claude %FLAGS% %MCP% %SETTINGS% "Voce e o Builder Nucleus N03 do CEX. 8F pipeline obrigatorio. Leia .claude/rules/n03-8f-enforcement.md e N03_engineering/agents/agent_engineering.md. SE EXISTIR .cex/runtime/handoffs/n03_task.md LEIA E EXECUTE IMEDIATAMENTE."
