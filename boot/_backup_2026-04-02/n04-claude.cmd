@echo off
:: CEX N04 — Knowledge Nucleus (CLAUDE OVERRIDE)
title CEX-N04-KNOWLEDGE
set CLAUDECODE=
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-sonnet-4-6 --no-chrome

claude %FLAGS% "Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."
