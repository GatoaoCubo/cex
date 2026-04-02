@echo off
:: CEX N04 — CEX-N04-KNOWLEDGE (FALLBACK 1: codex/o3)
:: When gemini crashes (Node v24 bug, etc.)
:: Generated 2026-04-02

title CEX-N04-KNOWLEDGE [codex fallback]
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

codex -m o3 --full-auto "Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia, schemas. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."
