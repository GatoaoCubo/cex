@echo off
:: CEX N05 — Operations Nucleus
:: CLI: codex | Model: auto (GPT) | Auth: OpenAI subscription
:: Domain: code review, testing, debugging, deployment, CI/CD

title CEX-N05-OPERATIONS
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: ALWAYS interactive — task comes from handoff file, never CLI args
codex --dangerously-bypass-approvals-and-sandbox "Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, debug, deploy, CI/CD. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
