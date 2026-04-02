@echo off
:: CEX N01 — Research Nucleus (CLAUDE OVERRIDE)
title CEX-N01-RESEARCH
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-sonnet-4-20250514 --no-chrome

claude %FLAGS% "Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
