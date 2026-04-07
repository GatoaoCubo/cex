@echo off
:: CEX N01 -- Research Nucleus
:: CLI: gemini | Model: 2.5-pro | Auth: Google subscription (OAuth)
:: Domain: research, market analysis, papers, competitors

title CEX-N01-RESEARCH
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Force subscription OAuth (clear API keys)
set GOOGLE_API_KEY=
set GEMINI_API_KEY=
set GOOGLE_AI_API_KEY=

:: ALWAYS interactive -- task comes from handoff file, never CLI args
gemini -m gemini-2.5-pro --yolo "Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores. Gemini 2.5-pro 1M context. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
