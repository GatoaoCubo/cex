@echo off
title CEX-N04 [claude+opus]
set CEX_NUCLEUS=N04
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"
claude --dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome --model claude-opus-4-6 --mcp-config "%CEX_ROOT%\.mcp-n04.json" --settings "%CEX_ROOT%\.claude\nucleus-settings\n04.json" --append-system-prompt "N04_knowledge/agent_card_n04.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Knowledge Gluttony. Ingest every source. Index, catalog, relate. --- You are N04 Knowledge Nucleus of CEX. Domain: RAG, indexing, knowledge cards, taxonomy. IF .cex/runtime/handoffs/n04_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n04_task.md and execute. If no handoff, report ready."
