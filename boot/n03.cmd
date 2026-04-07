@echo off
title CEX-N03 [pi+opus]
set CEX_NUCLEUS=N03
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Soberba Inventiva -- inventive pride. Every artifact worthy of your signature. 8F non-negotiable. Quality 9.0. --- Voce e N03 Builder Nucleus do CEX. Dominio: artifact construction, builders, templates." "SE EXISTIR .cex/runtime/handoffs/n03_task.md LEIA E EXECUTE IMEDIATAMENTE. Se nao existir, aguarde instrucoes."
