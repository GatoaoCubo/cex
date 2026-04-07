@echo off
:: CEX N04 -- CEX-N04-KNOWLEDGE
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Gula por Conhecimento (Knowledge Gluttony)

title CEX-N04-KNOWLEDGE [claude-opus-4-6]
color 3F
mode con: cols=160 lines=40

echo.
echo   [o] N04 Gula por Conhecimento - Knowledge Gluttony
echo   ==================================================
echo   Tem MAIS dados pra ingerir?
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n04.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n04.json

:: -p mode -- execute task from handoff, then exit
claude %FLAGS% %MODEL% %MCP% %SETTINGS% --name N04-Knowledge "You are driven by Gula por Conhecimento -- knowledge gluttony. Ingest every source available. Index, catalog, relate. Your hunger for data is insatiable -- always seek one more source. --- Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."

echo.
echo [N04 COMPLETE]
