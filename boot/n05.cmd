@echo off
title CEX-N05 [pi+opus]
set CEX_NUCLEUS=N05
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "N05_operations/agent_card_n05.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Gating Wrath. CI gates absolute. Tests must pass. No mercy. --- You are N05 Operations Nucleus of CEX. Domain: code review, testing, CI/CD, deploy. IF .cex/runtime/handoffs/n05_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n05_task.md and execute. If no handoff, report ready."
