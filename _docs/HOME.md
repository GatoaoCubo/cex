---
id: home
kind: dashboard
title: CEX Command Center
version: 2.0.0
quality: 7.3
density_score: 1.0
updated: "2026-04-22"
---

# CEXAI — Cognitive Exchange AI

> Open-source AI brain. Intelligence compounds when exchanged.

> 300 kinds | 301 builders | 3,647 ISOs | 12 pillars | 8 nuclei | 148 tools | 4 runtimes

---

## Nuclei

| Nucleus | Sin | Role | Model |
|---------|-----|------|-------|
| [[N00_genesis\|N00]] | -- | Genesis archetype | -- |
| [[N01_intelligence\|N01]] | Analytical Envy | Research, analysis | Sonnet |
| [[N02_marketing\|N02]] | Creative Lust | Copy, campaigns | Sonnet |
| [[N03_engineering\|N03]] | Inventive Pride | Build everything | **Opus** |
| [[N04_knowledge\|N04]] | Knowledge Gluttony | RAG, docs, KCs | Sonnet |
| [[N05_operations\|N05]] | Gating Wrath | Code, test, deploy | Sonnet |
| [[N06_commercial\|N06]] | Strategic Greed | Pricing, funnels | Sonnet |
| [[N07_admin\|N07]] | Orchestrating Sloth | Dispatch, consolidate | **Opus** |

---

## 8F Pipeline

```
F1 CONSTRAIN → F2 BECOME → F3 INJECT → F4 REASON → F5 CALL → F6 PRODUCE → F7 GOVERN → F8 COLLABORATE
   kind+schema   builder     context     plan        tools     generate     quality      save+signal
```

---

## 12 Pillars

| # | Domain | Top Kinds |
|---|--------|-----------|
| P01 | Knowledge | knowledge_card, rag_source, glossary_entry |
| P02 | Model | agent, model_provider, personality |
| P03 | Prompt | prompt_template, system_prompt, chain |
| P04 | Tools | mcp_server, browser_tool, api_client |
| P05 | Output | landing_page, formatter, diagram |
| P06 | Schema | input_schema, type_def, interface |
| P07 | Evaluation | benchmark, scoring_rubric, llm_judge |
| P08 | Architecture | agent_card, decision_record, naming_rule |
| P09 | Config | env_config, feature_flag, secret_config |
| P10 | Memory | entity_memory, knowledge_index, prompt_cache |
| P11 | Feedback | quality_gate, guardrail, bugloop |
| P12 | Orchestration | workflow, dispatch_rule, schedule |

---

## Navigation

| Section | Link |
|---------|------|
| Architecture canvas | [[cex-architecture.canvas]] |
| Kind census | [[kind_census]] |
| Quality heatmap | [[quality_heatmap]] |
| Pillar health | [[pillar_health]] |
| Orphan detector | [[orphan_detector]] |
| Cross-ref health | [[cross_ref_health]] |

---

## Artifacts by Nucleus

```dataview
TABLE length(rows) as "Artifacts"
FROM ""
WHERE kind
GROUP BY regexreplace(file.folder, "/.*", "") as "Folder"
SORT length(rows) DESC
LIMIT 12
```

## Recent Knowledge Cards

```dataview
TABLE kind, title
FROM ""
WHERE kind = "knowledge_card"
SORT file.mtime DESC
LIMIT 8
```

## Quality Leaders (9.0+)

```dataview
TABLE quality as "Score", kind, title
FROM ""
WHERE quality >= 9.0
SORT quality DESC
LIMIT 8
```

## Unscored Artifacts

```dataview
TABLE kind, title
FROM ""
WHERE kind AND !quality
SORT file.mtime DESC
LIMIT 8
```
