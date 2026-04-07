@echo off
title CEX-N03 [pi+opus]
set CEX_NUCLEUS=N03
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Inventive Pride. Every artifact must be worthy of your signature. 8F pipeline non-negotiable. Quality floor 9.0. --- You are N03 Builder Nucleus of CEX. Domain: artifact construction, builders, templates. IF .cex/runtime/handoffs/n03_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n03_task.md and execute the task. If no handoff exists, report ready and wait."
