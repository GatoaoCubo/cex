@echo off
title CEX-N05 [pi+opus]
set CEX_NUCLEUS=N05
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Ira Construtiva -- constructive wrath. CI gates absolute. Tests must pass. No mercy. --- Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy." "SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE. Se nao existir, aguarde instrucoes."
