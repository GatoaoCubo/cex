@echo off
:: CEX N05 -- CEX-N05-OPERATIONS (FALLBACK: claude/sonnet)
:: When codex/o3 is unavailable
:: Generated 2026-04-02

title CEX-N05-OPERATIONS [claude fallback]
set CLAUDECODE=
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-sonnet-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome

claude %FLAGS% %MODEL% "Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
