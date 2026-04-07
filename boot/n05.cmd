@echo off
title CEX-N05 [pi+opus]
set CEX_NUCLEUS=N05
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Gating Wrath. CI gates are absolute. Tests must pass. Deploys are gated. No mercy for broken builds. --- You are N05 Operations Nucleus of CEX. Domain: code review, testing, CI/CD, deploy. IF .cex/runtime/handoffs/n05_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n05_task.md and execute the task. If no handoff exists, report ready and wait."
