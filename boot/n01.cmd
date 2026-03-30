@echo off
:: CEX Boot - N01 Research Builder via Gemini CLI
:: Gemini 2.5 Pro: 1M token context — research docs, papers, market analysis
:: Auth: Google One subscription (OAuth, $0 cost) | Model: gemini-2.5-pro

title CEX-N01-RESEARCH
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set GOOGLE_API_KEY=
set GEMINI_API_KEY=
set GOOGLE_AI_API_KEY=

if "%~1"=="" (
    gemini -m gemini-2.5-pro --yolo
) else (
    gemini -m gemini-2.5-pro --yolo "%~1"
)
