# CEX Coverage Matrix - 69 Artifact Types across 12 LPs
> Generated: 2026-03-23 | Source: all 12 _schema.yaml files + templates/ + examples/ dirs
> Status: template coverage complete (69/69)

| # | LP | Type | Schema | Template | Example | density_min | max_bytes | Gap |
|---|----|------|--------|----------|---------|-------------|-----------|-----|
| 1 | P01 | knowledge_card | YES | YES | YES | - | - | - |
| 2 | P01 | rag_source | YES | YES | NO | - | - | example |
| 3 | P01 | glossary_entry | YES | YES | NO | - | - | example |
| 4 | P01 | context_doc | YES | YES | NO | - | - | example |
| 5 | P01 | embedding_config | YES | YES | NO | - | - | example |
| 6 | P01 | few_shot_example | YES | YES | NO | - | - | example |
| 7 | P02 | agent | YES | YES | YES | - | - | - |
| 8 | P02 | lens | YES | YES | NO | - | - | example |
| 9 | P02 | boot_config | YES | YES | NO | - | - | example |
| 10 | P02 | mental_model | YES | YES | NO | - | - | example |
| 11 | P02 | model_card | YES | YES | NO | - | - | example |
| 12 | P02 | router | YES | YES | NO | - | - | example |
| 13 | P02 | fallback_chain | YES | YES | NO | - | - | example |
| 14 | P02 | iso_package | YES | YES | NO | - | - | example |
| 15 | P03 | system_prompt | YES | YES | YES | - | - | - |
| 16 | P03 | action_prompt | YES | YES | YES | - | - | - |
| 17 | P03 | prompt_template | YES | YES | NO | - | - | example |
| 18 | P03 | instruction | YES | YES | NO | - | - | example |
| 19 | P03 | chain | YES | YES | NO | - | - | example |
| 20 | P04 | skill | YES | YES | YES | - | - | - |
| 21 | P04 | mcp_server | YES | YES | NO | - | - | example |
| 22 | P04 | hook | YES | YES | NO | - | - | example |
| 23 | P04 | plugin | YES | YES | NO | - | - | example |
| 24 | P04 | client | YES | YES | NO | - | - | example |
| 25 | P04 | cli_tool | YES | YES | NO | - | - | example |
| 26 | P04 | scraper | YES | YES | NO | - | - | example |
| 27 | P04 | connector | YES | YES | NO | - | - | example |
| 28 | P04 | daemon | YES | YES | NO | - | - | example |
| 29 | P05 | output_schema | YES | YES | NO | - | - | example |
| 30 | P05 | parser | YES | YES | NO | - | - | example |
| 31 | P05 | formatter | YES | YES | NO | - | - | example |
| 32 | P05 | naming_rule | YES | YES | NO | - | - | example |
| 33 | P06 | input_schema | YES | YES | NO | - | - | example |
| 34 | P06 | type_def | YES | YES | NO | - | - | example |
| 35 | P06 | validator | YES | YES | NO | - | - | example |
| 36 | P06 | interface | YES | YES | NO | - | - | example |
| 37 | P06 | output_schema | YES | YES | NO | - | - | example |
| 38 | P07 | unit_eval | YES | YES | NO | - | - | example |
| 39 | P07 | smoke_eval | YES | YES | NO | - | - | example |
| 40 | P07 | e2e_eval | YES | YES | NO | - | - | example |
| 41 | P07 | benchmark | YES | YES | NO | - | - | example |
| 42 | P07 | golden_test | YES | YES | NO | - | - | example |
| 43 | P07 | scoring_rubric | YES | YES | NO | - | - | example |
| 44 | P08 | satellite_spec | YES | YES | NO | - | - | example |
| 45 | P08 | pattern | YES | YES | NO | - | - | example |
| 46 | P08 | law | YES | YES | YES | - | - | - |
| 47 | P08 | diagram | YES | YES | NO | - | - | example |
| 48 | P08 | component_map | YES | YES | NO | - | - | example |
| 49 | P09 | env_config | YES | YES | NO | - | - | example |
| 50 | P09 | path_config | YES | YES | NO | - | - | example |
| 51 | P09 | permission | YES | YES | NO | - | - | example |
| 52 | P09 | feature_flag | YES | YES | NO | - | - | example |
| 53 | P09 | runtime_rule | YES | YES | NO | - | - | example |
| 54 | P10 | mental_model | YES | YES | NO | - | - | example |
| 55 | P10 | brain_index | YES | YES | NO | - | - | example |
| 56 | P10 | learning_record | YES | YES | NO | - | - | example |
| 57 | P10 | session_state | YES | YES | NO | - | - | example |
| 58 | P10 | axiom | YES | YES | NO | - | - | example |
| 59 | P11 | quality_gate | YES | YES | NO | - | - | example |
| 60 | P11 | bugloop | YES | YES | NO | - | - | example |
| 61 | P11 | lifecycle_rule | YES | YES | NO | - | - | example |
| 62 | P11 | guardrail | YES | YES | NO | - | - | example |
| 63 | P11 | optimizer | YES | YES | NO | - | - | example |
| 64 | P12 | workflow | YES | YES | NO | - | - | example |
| 65 | P12 | dag | YES | YES | YES | - | - | - |
| 66 | P12 | spawn_config | YES | YES | NO | - | - | example |
| 67 | P12 | signal | YES | YES | NO | - | - | example |
| 68 | P12 | handoff | YES | YES | NO | - | - | example |
| 69 | P12 | dispatch_rule | YES | YES | NO | - | - | example |

---

## Statistics

| Metric | Count | % |
|--------|-------|---|
| Total types | 69 | 100% |
| Types with schema | 69 | 100% |
| Types with template | 69 | 100.0% |
| Types with example | 7 | 10.1% |
| Fully covered (schema+template+example) | 7 | 10.1% |
| Missing template only | 0 | 0.0% |
| Missing example only | 62 | 89.9% |
| Missing template+example | 0 | 0.0% |

### Coverage by LP

| LP | Types | Templates | Examples | Fully Covered |
|----|-------|-----------|----------|---------------|
| P01 Knowledge | 6 | 6 | 1 | 1 |
| P02 Model | 8 | 8 | 1 | 1 |
| P03 Prompt | 5 | 5 | 2 | 2 |
| P04 Tools | 9 | 9 | 1 | 1 |
| P05 Output | 4 | 4 | 0 | 0 |
| P06 Schema | 5 | 5 | 0 | 0 |
| P07 Evals | 6 | 6 | 0 | 0 |
| P08 Architecture | 5 | 5 | 1 | 1 |
| P09 Config | 5 | 5 | 0 | 0 |
| P10 Memory | 5 | 5 | 0 | 0 |
| P11 Feedback | 5 | 5 | 0 | 0 |
| P12 Orchestration | 6 | 6 | 1 | 1 |

---

## Top 10 Priority Gaps

Types still missing examples after template closure:

| Priority | Type | LP | Rationale |
|----------|------|----|-----------|
| 1 | rag_source | P01 | Example gap after template closure |
| 2 | glossary_entry | P01 | Example gap after template closure |
| 3 | context_doc | P01 | Example gap after template closure |
| 4 | embedding_config | P01 | Example gap after template closure |
| 5 | few_shot_example | P01 | Example gap after template closure |
| 6 | lens | P02 | Example gap after template closure |
| 7 | boot_config | P02 | Example gap after template closure |
| 8 | mental_model | P02 | Example gap after template closure |
| 9 | model_card | P02 | Example gap after template closure |
| 10 | router | P02 | Example gap after template closure |

---

*Audit source: `C:\Users\PC\Documents\GitHub\cex` | 12 _schema.yaml files | 69 templates | 7 examples*
*ATLAS-CODEX | 2026-03-23*
