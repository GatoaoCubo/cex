@echo off
:: CEX N01 — BATCH_F CNAE Deep
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-BATCH_F-CNAE
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Analyst do GATO3. MISSION: BATCH_F_CNAE_DEEP. LEIA AGORA o handoff: .cex/runtime/handoffs/crm_mission/batch_f_cnae_deep.md e EXECUTE. 8 CNAEs x 7 cidades. Output: N01_research/output/data/crm_batch_f_cnae.json. DEDUP contra crm_pet_abc.json (244 existentes). SO situacao ATIVA. NUNCA fabricar CNPJs. Commit + signal ao final."
