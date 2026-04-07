@echo off
title CEX-N02 [pi+opus]
set CEX_NUCLEUS=N02
cd /d "%~dp0.."
pi --model anthropic/claude-opus-4-6 --append-system-prompt "N02_marketing/agent_card_n02.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Creative Lust. Every copy must seduce. Make the reader WANT not KNOW. --- You are N02 Marketing Nucleus of CEX. Domain: copy, ads, campaigns, brand voice. IF .cex/runtime/handoffs/n02_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n02_task.md and execute. If no handoff, report ready."
