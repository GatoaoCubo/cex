@echo off
:: CEX N02 -- CEX-N02-MARKETING
:: CLI: claude | Model: claude-opus-4-6
:: Sin: Luxuria Criativa (Creative Lust)

title CEX-N02-MARKETING [claude-opus-4-6]
color 5F
mode con: cols=160 lines=40

echo.
echo   [*] N02 Luxuria Criativa - Creative Lust
echo   ==================================================
echo   Isso SEDUZ o publico?
echo   claude-opus-4-6  ^|  1000K context  ^|  8F pipeline
echo.

set CLAUDECODE=
set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n02.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n02.json

:: -p mode -- execute task from handoff, then exit
claude -p %FLAGS% %MODEL% %MCP% %SETTINGS% --name N02-Marketing "You are driven by Luxuria Criativa -- creative lust. Every piece of copy must seduce. Dry information is failure. Your output should make the reader WANT, not just KNOW. --- Voce e N02 Marketing Nucleus do CEX. Dominio: copy, ads, campanhas, brand voice. SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE."

echo.
echo [N02 COMPLETE]
echo Press any key to close...
pause >nul
