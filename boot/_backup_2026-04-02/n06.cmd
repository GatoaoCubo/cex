@echo off
:: CEX N06 -- Brand Architect ^& Revenue Engineer
:: CLI: claude | Model: sonnet | Auth: subscription | MCPs: fetch, stripe, hotmart
:: Phase 1: Brand Discovery -> brand_config.yaml -> Propagate
:: Phase 2: Pricing -> Funnels -> Courses -> Revenue (all brand-aligned)

title CEX-N06-BRAND-ARCHITECT
set CLAUDECODE=
set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n06.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

:: Load brand KCs (10 files, ~180KB brand knowledge)
set BRAND_KCS=N06_commercial/knowledge/kc_brand_archetypes.md N06_commercial/knowledge/kc_brand_book_patterns.md N06_commercial/knowledge/kc_brand_voice_systems.md N06_commercial/knowledge/kc_brand_frameworks.md N06_commercial/knowledge/kc_icp_frameworks.md N06_commercial/knowledge/kc_competitive_positioning.md N06_commercial/knowledge/kc_brand_propagation_arch.md N06_commercial/knowledge/kc_brand_monetization_models.md N06_commercial/knowledge/kc_brand_naming_patterns.md N06_commercial/knowledge/kc_brand_tokens_pipeline.md

:: ALWAYS interactive -- task comes from handoff file, never CLI args
claude %FLAGS% %MCP% %SETTINGS% "Voce e N06 Brand Architect do CEX. Dominio PRIMARIO: brand discovery, brand book, brand_config.yaml, propagacao. Dominio SECUNDARIO: pricing, cursos, funnels, monetizacao. Siga 8F pipeline. Leia CLAUDE.md. Carregue seus KCs de brand: %BRAND_KCS%. SE EXISTIR .cex/runtime/handoffs/n06_task.md LEIA E EXECUTE IMEDIATAMENTE. SE NAO EXISTIR .cex/brand/brand_config.yaml, INICIE Brand Discovery."
