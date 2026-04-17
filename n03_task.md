---
mission: VERTICAL_DISTILLATION_WAVE_2A
nucleus: n03
wave: W2A
created: 2026-04-17
priority: CRITICAL
effort: opus
---

# N03 VERTICAL_DISTILLATION Wave 2A: Commerce Template Backfill

## CONTEXT

This wave was assigned in VERTICAL_DISTILLATION_20260416 and never executed.
22-25 commerce template artifacts must be created. kinds_meta.json is up-to-date (279 kinds).

## TASK

Read `.cex/runtime/handoffs/VERTICAL_DISTILLATION_n03_w2.md` in full. Execute it completely.

Build all artifacts listed in the handoff for:
- shopify_integration: integration_guide, api_client, webhook, oauth_app_config -> N03_engineering/P04_tools/
- bling_erp_integration: integration_guide, api_client, webhook, oauth_app_config -> N03_engineering/P04_tools/
- mercado_livre_integration: integration_guide, api_client, oauth_app_config -> N03_engineering/P04_tools/
- multi_marketplace_sync: workflow, dag, dispatch_rule -> N03_engineering/P12_orchestration/
- supabase_backend: supabase_data_layer, db_connector, interface -> N03_engineering/P09_config/ + P06_schema/
- admin_dashboard: landing_page, component_map -> N03_engineering/P05_output/ + P08_architecture/
- scrap_pipeline: research_pipeline, browser_tool -> N03_engineering/P04_tools/
- webhook_management: webhook, notifier -> N03_engineering/P04_tools/
- inventory_reconcile: workflow, validator -> N03_engineering/P12_orchestration/ + P06_schema/

## RULES
- Use ONLY kinds in .cex/kinds_meta.json (all exist -- api_client, webhook, oauth_app_config, etc.)
- All brand-specific values -> {{BRAND_*}} mustache placeholders
- Every artifact: standard frontmatter with quality: null, status: template
- Compile after writing all artifacts: python _tools/cex_compile.py <path>
- Commit at the end: git add N03_engineering/ && git commit -m "[N03] VERTICAL_DISTILLATION W2A: 22 commerce templates"
- Signal: python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'vd_w2a_complete', 9.0)"

## COMPLETION CRITERIA
- [ ] ~22-25 artifacts written in N03_engineering/ pillar subdirs
- [ ] All use existing kinds (no invented kinds)
- [ ] All frontmatter valid (id, kind, pillar, quality: null)
- [ ] git commit [N03] VERTICAL_DISTILLATION W2A
- [ ] signal sent: n03 -> vd_w2a_complete
