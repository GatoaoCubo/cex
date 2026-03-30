@echo off
:: CEX N02 — Marketing Nucleus
:: CLI: claude | Model: sonnet | Auth: subscription | MCPs: markitdown + fetch

title CEX-N02-MARKETING
set CLAUDECODE=
set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n02.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n02.json

:: ALWAYS interactive — task comes from handoff file, never CLI args
claude %FLAGS% %MCP% %SETTINGS% "Voce e N02 Marketing Nucleus do CEX. Dominio: copy, anuncios, branding. Siga 8F pipeline. Leia CLAUDE.md. SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE."
