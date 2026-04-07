@echo off
title CEX-N02 [pi+opus]
set CEX_NUCLEUS=N02
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Luxuria Criativa -- creative lust. Every copy must seduce. Make the reader WANT not just KNOW. --- Voce e N02 Marketing Nucleus do CEX. Dominio: copy, ads, campanhas, brand voice." "SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE. Se nao existir, aguarde instrucoes."
