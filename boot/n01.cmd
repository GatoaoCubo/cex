@echo off
:: CEX N01 -- CEX-N01-RESEARCH
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Inveja Analitica (Analytical Envy)

title CEX-N01-RESEARCH [claude-opus-4-6]
color 2F
mode con: cols=160 lines=40

echo.
echo   [+] N01 Inveja Analitica - Analytical Envy
echo   ==================================================
echo   O que o concorrente faz melhor? Como superamos?
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n01.json

:: ALWAYS interactive -- task comes from handoff file, never CLI args
claude %FLAGS% %MODEL% %MCP% %SETTINGS% "You are driven by Inveja Analitica -- analytical envy. Every analysis must compare against at least 2 alternatives. Never present a finding without competitive context. --- Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
