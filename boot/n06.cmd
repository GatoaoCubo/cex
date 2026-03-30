@echo off
:: CEX N06 — Commercial Nucleus
:: CLI: claude | Model: sonnet | Auth: subscription | MCPs: fetch

title CEX-N06-COMMERCIAL
set CLAUDECODE=
set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n06.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

if "%~1"=="" (
    claude %FLAGS% %MCP% %SETTINGS% "Voce e N06 Commercial Nucleus do CEX. Dominio: pricing, cursos, monetizacao. Siga 8F pipeline. Leia CLAUDE.md."
) else (
    claude %FLAGS% %MCP% %SETTINGS% "%~1"
)
