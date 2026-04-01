@echo off
:: CEX N05 — Railway Backend Superintendent
:: CLI: claude | Model: opus | Auth: subscription
:: Domain: Railway deploy, FastAPI, PostgreSQL, API lifecycle

title CEX-N05-RAILWAY
set CLAUDECODE=
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-opus-4-0 --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n05.json

:: ALWAYS interactive — task comes from handoff file, never CLI args
claude %FLAGS% %MCP% "Voce e N05 Railway Backend Superintendent do CEX. Dono do ciclo de vida de APIs em producao. Dominio: Railway deploy, FastAPI, PostgreSQL asyncpg, middleware stack, health monitoring, zero-downtime. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
