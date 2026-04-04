@echo off
:: CEX N01 — ENRICH_3 SA + Maua + RGS + outros
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-ENRICH_3-SA-MAUA-RGS
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Analyst do GATO3. MISSION: ENRICH_3. LEIA AGORA: .cex/runtime/handoffs/crm_mission/enrich_3_sa_maua_rgs.md — Enriquecer 129 contatos de Santo Andre+Maua+Rio Grande da Serra. A lista de nomes esta em N01_research/output/data/enrich_targets_3.json. Para CADA nome, pesquise telefone, whatsapp, email, instagram, website via SERPER e FETCH. Output: N01_research/output/data/crm_enrich_3.json. NUNCA inventar. Commit + signal ao final."
