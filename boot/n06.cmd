@echo off
:: CEX N06 -- CEX-N06-COMMERCIAL
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Avareza Estrategica (Strategic Greed)

title CEX-N06-COMMERCIAL [claude-opus-4-6]
color 60
mode con: cols=160 lines=40

echo.
echo   [$] N06 Avareza Estrategica - Strategic Greed
echo   ==================================================
echo   Quanto RENDE cada decisao?
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n06.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

:: -p mode -- execute task from handoff, then exit
claude -p %FLAGS% %MODEL% %MCP% %SETTINGS% --name N06-Commercial "You are driven by Avareza Estrategica -- strategic greed. Every output must have ROI context. What does it cost? What does it earn? Optimize pricing, minimize waste, maximize conversion. --- Voce e N06 Commercial Nucleus do CEX. Dominio: pricing, funnels, monetizacao, brand. SE EXISTIR .cex/runtime/handoffs/n06_task.md LEIA E EXECUTE IMEDIATAMENTE."

echo.
echo [N06 COMPLETE]
echo Press any key to close...
pause >nul
