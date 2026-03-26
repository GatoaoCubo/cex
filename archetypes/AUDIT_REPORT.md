# AUDIT REPORT

Generated: 2026-03-23T18:41:12.950Z

## Summary

- LPs audited: 12
- Types defined: 69
- Expected types per CODEX.md: 68
- Examples audited: 48
- Expected examples from task brief: 46
- Templates found: 21

## LP Coverage

| LP | tipos_definidos | templates | examples | gaps |
|----|-----------------|-----------|----------|------|
| P01_knowledge | 6 | 3 | 7 | tmpl:5, ex:5 |
| P02_model | 8 | 1 | 4 | tmpl:7, ex:7 |
| P03_prompt | 5 | 1 | 4 | tmpl:4, ex:4 |
| P04_tools | 9 | 1 | 3 | tmpl:8, ex:8 |
| P05_output | 4 | 1 | 3 | tmpl:3, ex:1 |
| P06_schema | 5 | 2 | 3 | tmpl:3, ex:2 |
| P07_evals | 6 | 2 | 3 | tmpl:4, ex:3 |
| P08_architecture | 5 | 2 | 3 | tmpl:3, ex:2 |
| P09_config | 5 | 2 | 4 | tmpl:3, ex:1 |
| P10_memory | 5 | 2 | 4 | tmpl:3, ex:1 |
| P11_feedback | 5 | 2 | 6 | tmpl:3 |
| P12_orchestration | 6 | 2 | 4 | tmpl:4, ex:2 |

## Schema Findings

- Total de tipos definidos nos 12 schemas: 69
- Desvio vs CODEX.md (68 tipos): 1

### P01_knowledge
- Types in schema: 6
- Types without template: rag_source, glossary_entry, context_doc, embedding_config, few_shot_example
- Types without example: rag_source, glossary_entry, context_doc, embedding_config, few_shot_example

### P02_model
- Types in schema: 8
- Types without template: lens, boot_config, mental_model, model_card, router, fallback_chain, iso_package
- Types without example: lens, boot_config, mental_model, model_card, router, fallback_chain, iso_package

### P03_prompt
- Types in schema: 5
- Types without template: system_prompt, action_prompt, instruction, chain
- Types without example: system_prompt, action_prompt, instruction, chain

### P04_tools
- Types in schema: 9
- Types without template: mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon
- Types without example: mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon

### P05_output
- Types in schema: 4
- Types without template: parser, formatter, naming_rule
- Types without example: parser

### P06_schema
- Types in schema: 5
- Types without template: type_def, interface, output_schema
- Types without example: type_def, output_schema

### P07_evals
- Types in schema: 6
- Types without template: smoke_eval, e2e_eval, benchmark, scoring_rubric
- Types without example: unit_eval, e2e_eval, benchmark

### P08_architecture
- Types in schema: 5
- Types without template: law, diagram, component_map
- Types without example: diagram, component_map

### P09_config
- Types in schema: 5
- Types without template: path_config, permission, runtime_rule
- Types without example: permission

### P10_memory
- Types in schema: 5
- Types without template: brain_index, session_state, axiom
- Types without example: session_state

### P11_feedback
- Types in schema: 5
- Types without template: lifecycle_rule, guardrail, optimizer
- Types without example: none

### P12_orchestration
- Types in schema: 6
- Types without template: dag, spawn_config, signal, dispatch_rule
- Types without example: signal, dispatch_rule

## Example Findings

- Examples below score 8.0: 33
- Examples missing required frontmatter fields: 3
- Examples over size limit: 0

| example | lp | type | score | issues |
|---------|----|------|-------|--------|
| p04_skill_design_extractor.md | P04 | skill | 6.6 | missing:title, no-axioms |
| p04_skill_ml_ads.md | P04 | skill | 6.8 | missing:title, no-axioms |
| p04_skill_voice_pipeline.md | P04 | skill | 6.8 | missing:title, no-axioms |
| p05_fmt_agent_markdown.md | P05 | formatter | 6.8 | no-axioms |
| p05_nr_cex_naming.md | P05 | naming_rule | 6.6 | no-axioms, no-links |
| p05_os_security_audit.md | P05 | output_schema | 7.0 | no-axioms |
| p06_iface_satellite_handoff.md | P06 | interface | 7.0 | no-axioms |
| p06_is_quality_audit.md | P06 | input_schema | 7.0 | no-axioms |
| p06_val_quality_score.md | P06 | validator | 7.0 | no-axioms |
| p07_gt_stripe_pipeline.md | P07 | golden_test | 7.0 | no-axioms |
| p07_se_brain_query.md | P07 | smoke_eval | 6.6 | no-axioms, no-links |
| p07_sr_5d_scoring.md | P07 | scoring_rubric | 7.0 | no-axioms |
| p08_law_shokunin.md | P08 | law | 7.0 | no-axioms |
| p08_pat_continuous_batching.md | P08 | pattern | 7.0 | no-axioms |
| p08_sat_edison.md | P08 | satellite_spec | 7.0 | no-axioms |
| p09_env_firecrawl.md | P09 | env_config | 6.6 | no-axioms, no-links |
| p09_ff_firecrawl_enabled.md | P09 | feature_flag | 6.6 | no-axioms, no-links |
| p09_path_codexa_repos.md | P09 | path_config | 6.8 | no-axioms |
| p09_rr_satellite_spawn.md | P09 | runtime_rule | 6.8 | no-axioms |
| p10_ax_scout_before_create.md | P10 | axiom | 6.8 | no-axioms |
| p10_bi_codexa_brain.md | P10 | brain_index | 6.8 | no-axioms |
| p10_lr_continuous_batching.md | P10 | learning_record | 6.6 | no-axioms, no-links |
| p10_mm_edison.md | P10 | mental_model | 6.6 | no-axioms, no-links |
| p11_bl_satellite_execution.md | P11 | bugloop | 6.6 | no-axioms, no-links |
| p11_gr_stella_dispatch.md | P11 | guardrail | 7.0 | no-axioms |
| p11_lc_cex_lifecycle.md | P11 | lifecycle_rule | 7.1 | no-links |
| p11_opt_pool_density.md | P11 | optimizer | 7.0 | no-axioms |
| p11_qg_cex_quality.md | P11 | quality_gate | 7.1 | no-links |
| p11_qg_shokunin_pool.md | P11 | quality_gate | 6.6 | no-axioms, no-links |
| p12_dag_cex_wave_pipeline.md | P12 | dag | 6.8 | no-axioms |
| p12_ho_isofix_batch.md | P12 | handoff | 6.6 | no-axioms, no-links |
| p12_spawn_grid_continuous.md | P12 | spawn_config | 7.0 | no-axioms |
| p12_wf_stella_dispatch.md | P12 | workflow | 6.6 | no-axioms, no-links |

## Priority Actions

- Fechar cobertura de templates: 50 tipos sem template.
- Fechar cobertura de examples: 36 tipos sem example.
- Elevar examples abaixo de 8.0: 33 arquivos precisam densidade/completude maior.
- Corrigir disciplina de frontmatter: 3 examples com campos obrigatorios faltando.
- Reduzir tamanho ou quebrar arquivos oversize: 0 examples acima do limite.
