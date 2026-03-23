# CEX Coverage Matrix — 69 Artifact Types across 12 LPs
> Note: Actual count is 69 types (handoff referenced 68 — 1 type added in P02: iso_package)
> Generated: 2026-03-23 | Source: all 12 _schema.yaml files + templates/ + examples/ dirs

| # | LP | Type | Schema | Template | Example | density_min | max_bytes | Gap |
|---|----|------|--------|----------|---------|-------------|-----------|-----|
| 1 | P01 | knowledge_card | YES | YES | YES | 0.8 | 5120 | - |
| 2 | P01 | rag_source | YES | NO | NO | - | 1024 | template+example |
| 3 | P01 | glossary_entry | YES | NO | NO | - | 512 | template+example |
| 4 | P01 | context_doc | YES | NO | NO | - | 2048 | template+example |
| 5 | P01 | embedding_config | YES | NO | NO | - | 512 | template+example |
| 6 | P01 | few_shot_example | YES | NO | NO | - | 1024 | template+example |
| 7 | P02 | agent | YES | YES | YES | - | 5120 | - |
| 8 | P02 | lens | YES | NO | NO | - | 2048 | template+example |
| 9 | P02 | boot_config | YES | NO | NO | - | 2048 | template+example |
| 10 | P02 | mental_model | YES | NO | NO | - | 2048 | template+example |
| 11 | P02 | model_card | YES | NO | NO | - | 2048 | template+example |
| 12 | P02 | router | YES | NO | NO | - | 1024 | template+example |
| 13 | P02 | fallback_chain | YES | NO | NO | - | 512 | template+example |
| 14 | P02 | iso_package | YES | NO | NO | 0.8 | 4096 | template+example |
| 15 | P03 | system_prompt | YES | NO | NO | - | 4096 | template+example |
| 16 | P03 | action_prompt | YES | NO | NO | - | 2048 | template+example |
| 17 | P03 | prompt_template | YES | YES | YES | - | 8192 | - |
| 18 | P03 | instruction | YES | NO | NO | - | 1024 | template+example |
| 19 | P03 | chain | YES | NO | NO | - | 2048 | template+example |
| 20 | P04 | skill | YES | YES | YES | - | 5120 | - |
| 21 | P04 | mcp_server | YES | NO | NO | - | 2048 | template+example |
| 22 | P04 | hook | YES | NO | NO | - | 1024 | template+example |
| 23 | P04 | plugin | YES | NO | NO | - | 2048 | template+example |
| 24 | P04 | client | YES | NO | NO | - | 1024 | template+example |
| 25 | P04 | cli_tool | YES | NO | NO | - | 1024 | template+example |
| 26 | P04 | scraper | YES | NO | NO | - | 1024 | template+example |
| 27 | P04 | connector | YES | NO | NO | - | 1024 | template+example |
| 28 | P04 | daemon | YES | NO | NO | - | 1024 | template+example |
| 29 | P05 | output_schema | YES | YES | YES | - | 4096 | - |
| 30 | P05 | parser | YES | NO | NO | - | 4096 | template+example |
| 31 | P05 | formatter | YES | NO | YES | - | 4096 | template |
| 32 | P05 | naming_rule | YES | NO | YES | - | 4096 | template |
| 33 | P06 | input_schema | YES | YES | YES | - | 3072 | - |
| 34 | P06 | type_def | YES | NO | NO | - | 3072 | template+example |
| 35 | P06 | validator | YES | YES | YES | - | 3072 | - |
| 36 | P06 | interface | YES | NO | YES | - | 3072 | template |
| 37 | P06 | output_schema | YES | NO | NO | - | 3072 | template+example |
| 38 | P07 | unit_eval | YES | YES | NO | - | 4096 | example |
| 39 | P07 | smoke_eval | YES | NO | YES | - | 3072 | template |
| 40 | P07 | e2e_eval | YES | NO | NO | - | 4096 | template+example |
| 41 | P07 | benchmark | YES | NO | NO | - | 4096 | template+example |
| 42 | P07 | golden_test | YES | YES | YES | - | 4096 | - |
| 43 | P07 | scoring_rubric | YES | NO | YES | - | 3072 | template |
| 44 | P08 | satellite_spec | YES | YES | YES | - | 4096 | - |
| 45 | P08 | pattern | YES | YES | YES | - | 4096 | - |
| 46 | P08 | law | YES | NO | YES | - | 3072 | template |
| 47 | P08 | diagram | YES | NO | NO | - | 4096 | template+example |
| 48 | P08 | component_map | YES | NO | NO | - | 3072 | template+example |
| 49 | P09 | env_config | YES | YES | YES | - | 4096 | - |
| 50 | P09 | path_config | YES | NO | YES | - | 3072 | template |
| 51 | P09 | permission | YES | NO | NO | - | 3072 | template+example |
| 52 | P09 | feature_flag | YES | YES | YES | - | 1536 | - |
| 53 | P09 | runtime_rule | YES | NO | YES | - | 3072 | template |
| 54 | P10 | mental_model | YES | YES | YES | - | 3072 | - |
| 55 | P10 | brain_index | YES | NO | YES | - | 3072 | template |
| 56 | P10 | learning_record | YES | YES | YES | - | 3072 | - |
| 57 | P10 | session_state | YES | NO | NO | - | 3072 | template+example |
| 58 | P10 | axiom | YES | NO | YES | - | 3072 | template |
| 59 | P11 | quality_gate | YES | YES | YES | - | 4096 | - |
| 60 | P11 | bugloop | YES | YES | YES | - | 4096 | - |
| 61 | P11 | lifecycle_rule | YES | NO | YES | - | 4096 | template |
| 62 | P11 | guardrail | YES | NO | YES | - | 4096 | template |
| 63 | P11 | optimizer | YES | NO | YES | - | 4096 | template |
| 64 | P12 | workflow | YES | YES | YES | - | 3072 | - |
| 65 | P12 | dag | YES | NO | YES | - | 3072 | template |
| 66 | P12 | spawn_config | YES | NO | YES | - | 3072 | template |
| 67 | P12 | signal | YES | NO | NO | - | 4096 | template+example |
| 68 | P12 | handoff | YES | YES | YES | - | 4096 | - |
| 69 | P12 | dispatch_rule | YES | NO | NO | - | 3072 | template+example |

---

## Statistics

| Metric | Count | % |
|--------|-------|---|
| Total types | 69 | 100% |
| Types with schema | 69 | 100% |
| Types with template | 19 | 27.5% |
| Types with example | 33 | 47.8% |
| Fully covered (schema+template+example) | 18 | 26.1% |
| Missing template only | 9 | 13.0% |
| Missing example only | 1 | 1.4% |
| Missing template+example | 41 | 59.4% |

### Coverage by LP

| LP | Types | Templates | Examples | Fully Covered |
|----|-------|-----------|----------|---------------|
| P01 Knowledge | 6 | 1 | 1 | 1 |
| P02 Model | 8 | 1 | 1 | 1 |
| P03 Prompt | 5 | 1 | 1 | 1 |
| P04 Tools | 9 | 1 | 1 | 1 |
| P05 Output | 4 | 1 | 3 | 1 |
| P06 Schema | 5 | 2 | 3 | 2 |
| P07 Evals | 6 | 2 | 3 | 1 |
| P08 Architecture | 5 | 2 | 3 | 2 |
| P09 Config | 5 | 2 | 4 | 2 |
| P10 Memory | 5 | 2 | 4 | 2 |
| P11 Feedback | 5 | 2 | 5 | 2 |
| P12 Orchestration | 6 | 2 | 4 | 2 |

---

## Top 10 Priority Gaps

Types with zero coverage (template=NO, example=NO), ordered by usage criticality:

| Priority | Type | LP | Rationale |
|----------|------|----|-----------|
| 1 | system_prompt | P03 | Every agent needs one — most universal type in CEX |
| 2 | mcp_server | P04 | CODEXA depends on 5+ MCPs; no reference pattern |
| 3 | model_card | P02 | LLM spec tracking (pricing, context) — ops critical |
| 4 | e2e_eval | P07 | Full pipeline testing has no template, blocks QA |
| 5 | iso_package | P02 | Portable agent format — high reuse potential |
| 6 | context_doc | P01 | Domain context for RAG — foundational for P01 |
| 7 | action_prompt | P03 | Task-focused prompts — 2nd most common P03 type |
| 8 | signal | P12 | Inter-agent communication — orchestration backbone |
| 9 | dispatch_rule | P12 | Routing rules — no template blocks new satellite onboarding |
| 10 | diagram | P08 | Architecture diagrams — visualization gap across all LPs |

---

*Audit source: `C:\Users\PC\Documents\GitHub\cex` | 12 _schema.yaml files | 19 templates | 33 examples*
*PYTHA[KNOWLEDGE] | 2026-03-23*
