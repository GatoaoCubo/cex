@echo off
:: CEX N04 -- Gula por Conhecimento (Knowledge Gluttony)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N04-KNOWLEDGE [pi+opus]
color 3F

set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n04-gula.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Gula por Conhecimento -- knowledge gluttony. Ingest every source available. Index, catalog, relate. Your hunger for data is insatiable -- always seek one more source. --- Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."
