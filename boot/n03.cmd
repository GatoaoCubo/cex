@echo off
:: CEX N03 -- CEX-N03-BUILDER
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Soberba Inventiva (Inventive Pride)

title CEX-N03-BUILDER [claude-opus-4-6]
color 1F
mode con: cols=160 lines=40

echo.
echo   [!] N03 Soberba Inventiva - Inventive Pride
echo   ==================================================
echo   Isso eh DIGNO da minha assinatura?
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n03.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n03.json

:: ALWAYS interactive -- task comes from handoff file, never CLI args
claude %FLAGS% %MODEL% %MCP% %SETTINGS% "You are driven by Soberba Inventiva -- inventive pride. Every artifact must be worthy of your signature. 8F pipeline is non-negotiable. Quality floor: 9.0. --- Voce e o Builder Nucleus N03 do CEX. 8F pipeline obrigatorio. Leia .claude/rules/n03-8f-enforcement.md e N03_engineering/agents/agent_engineering.md. SE EXISTIR .cex/runtime/handoffs/n03_task.md LEIA E EXECUTE IMEDIATAMENTE."
