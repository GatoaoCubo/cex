@echo off
:: CEX Boot - N05 Operations Builder via Codex CLI
:: Codex excels at code review, testing, debugging, deployment
:: Auth: OpenAI API | Model: GPT-5.4 | Mode: full-auto

title CEX-N05-OPERATIONS
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

if "%~1"=="" (
    codex --dangerously-bypass-approvals-and-sandbox
) else (
    codex --dangerously-bypass-approvals-and-sandbox "%~1"
)
