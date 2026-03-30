@echo off
:: CEX N02 — Marketing Nucleus
:: CLI: claude | Model: sonnet | Auth: Anthropic subscription
:: MCPs: markitdown (parse docs) + fetch (web content)
:: Domain: copy, ads, social, branding, content

title CEX-N02-MARKETING
set CLAUDECODE=
set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set MCP=--mcp-config "%CEX_ROOT%\.mcp-n02.json"
set SETTINGS=--settings "%CEX_ROOT%\.claude\nucleus-settings\n02.json"

set IDENTITY=Voce e N02 Marketing Nucleus do CEX. Seu dominio: copy, anuncios, social media, branding. Leia CLAUDE.md e .claude/rules/n03-8f-enforcement.md. Siga o 8F pipeline. Commit e signal ao terminar.

if "%~1"=="" (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY%"
) else (
    claude %FLAGS% %MCP% %SETTINGS% "%IDENTITY% TAREFA: %~1"
)
