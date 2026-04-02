@echo off
:: CEX N05 — CEX-N05-OPERATIONS
:: Generated from .cex/config/nucleus_models.yaml
:: CLI: claude | Model: claude-sonnet-4-20250514
:: NOTE: Codex/o3 unavailable on ChatGPT sub. Sonnet is primary.

title CEX-N05-OPERATIONS
set CLAUDECODE=
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-sonnet-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome

:: ALWAYS interactive — task comes from handoff file, never CLI args
claude %FLAGS% %MODEL% "Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
