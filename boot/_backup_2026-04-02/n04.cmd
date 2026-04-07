@echo off
:: CEX N04 -- Knowledge Nucleus
:: CLI: gemini | Model: 2.5-pro | Auth: Google subscription (OAuth)
:: Domain: documentation, indexing, RAG, knowledge cards, taxonomy

title CEX-N04-KNOWLEDGE
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Force subscription OAuth
set GOOGLE_API_KEY=
set GEMINI_API_KEY=
set GOOGLE_AI_API_KEY=

:: ALWAYS interactive -- task comes from handoff file, never CLI args
gemini -m gemini-2.5-pro --yolo "Voce e N04 Knowledge Nucleus do CEX. Dominio: RAG, indexacao, knowledge cards, taxonomia. Gemini 2.5-pro 1M context. SE EXISTIR .cex/runtime/handoffs/n04_task.md LEIA E EXECUTE IMEDIATAMENTE."
