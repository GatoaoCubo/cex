@echo off
:: CEX N06 — Commercial Nucleus
:: CLI: claude | Model: sonnet | Auth: Anthropic subscription
:: MCPs: fetch (pricing research, competitor pages)
:: Domain: pricing, courses, funnels, monetization, e-commerce

title CEX-N06-COMMERCIAL
set CLAUDECODE=
set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set MCP=--mcp-config "%CEX_ROOT%\.mcp-n06.json"
set SETTINGS=--settings "%CEX_ROOT%\.claude\nucleus-settings\n06.json"

set IDENTITY=Voce e N06 Commercial Nucleus do CEX. Seu dominio: pricing, cursos, funis, monetizacao, e-commerce. Leia CLAUDE.md e .claude/rules/n03-8f-enforcement.md. Siga o 8F pipeline. Commit e signal ao terminar.

if "%~1"=="" (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY%"
) else (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY% TAREFA: %~1"
)
