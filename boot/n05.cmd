@echo off
:: CEX N05 — Operations Nucleus
:: CLI: codex | Model: auto (GPT) | Auth: OpenAI subscription
:: Domain: code review, testing, debugging, deployment, CI/CD

title CEX-N05-OPERATIONS
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

if "%~1"=="" (
    codex --dangerously-bypass-approvals-and-sandbox
) else (
    codex --dangerously-bypass-approvals-and-sandbox "%~1"
)
