@echo off
title CEX-N05-OPERATIONS [pi+opus]
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme "%CEX_ROOT%\cex-pi-package\themes\cex-n05-ira.json" --model anthropic/claude-opus-4-6 --append-system-prompt "You are N05 Ira Construtiva. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
