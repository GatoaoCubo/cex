@echo off
:: CEX N04 -- cex-n04-gula
:: Runtime: pi + cex-pi-package

title CEX-N04 [pi+opus]
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n04-gula';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Gula por Conhecimento -- knowledge gluttony. Ingest every source available. Index, catalog, relate. Your hunger for data is insatiable. --- Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."
