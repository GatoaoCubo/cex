@echo off
title CEX-N04 [pi+opus]
set CEX_NUCLEUS=N04
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Knowledge Gluttony. Ingest every source available. Index, catalog, relate. Your hunger for data is insatiable. --- You are N04 Knowledge Nucleus of CEX. Domain: RAG, indexing, knowledge cards, taxonomy. IF .cex/runtime/handoffs/n04_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n04_task.md and execute the task. If no handoff exists, report ready and wait."
