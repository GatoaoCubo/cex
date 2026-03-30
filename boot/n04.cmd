@echo off
:: CEX N04 — Knowledge Nucleus
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

if "%~1"=="" (
    gemini -m gemini-2.5-pro --yolo
) else (
    gemini -m gemini-2.5-pro --yolo "%~1"
)
