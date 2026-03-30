@echo off
:: CEX Boot - N04 Knowledge Builder via Gemini CLI
:: Gemini 2.5 Pro: 1M token context — ideal for large knowledge bases, RAG, docs
:: Auth: Google One subscription (OAuth, $0 cost) | Model: gemini-2.5-pro

title CEX-N04-KNOWLEDGE
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Force subscription OAuth (no API keys = uses Google One OAuth)
set GOOGLE_API_KEY=
set GEMINI_API_KEY=
set GOOGLE_AI_API_KEY=

if "%~1"=="" (
    gemini -m gemini-2.5-pro --yolo
) else (
    gemini -m gemini-2.5-pro --yolo "%~1"
)
