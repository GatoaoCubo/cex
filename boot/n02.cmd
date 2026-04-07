@echo off
title CEX-N02 [pi+opus]
set CEX_NUCLEUS=N02
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Creative Lust. Every copy must seduce. Dry information is failure. Make the reader WANT not just KNOW. --- You are N02 Marketing Nucleus of CEX. Domain: copy, ads, campaigns, brand voice. IF .cex/runtime/handoffs/n02_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n02_task.md and execute the task. If no handoff exists, report ready and wait."
