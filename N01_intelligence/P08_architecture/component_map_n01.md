---
id: component_map_n01
kind: component_map
pillar: P08
nucleus: n01
title: "N01 Intelligence -- Component Map"
version: 1.0.0
created: 2026-04-18
author: n01_intelligence
domain: research-intelligence-architecture
quality: 8.7
tags: [component_map, n01, intelligence, architecture, data_flow]
tldr: "Internal component map of N01 Intelligence nucleus: research pipeline, tool stack, KC library, entity memory, signal bus, and inter-nucleus data flows."
density_score: null
related:
  - p02_nd_n01.md
  - p10_bi_intelligence_outputs
  - bld_collaboration_research_pipeline
  - n01_dr_research_pipeline
  - p12_wf_intelligence_pipeline
  - spec_cex_system_map
  - agent_card_n01
  - n01_intelligence
  - ctx_cex_new_dev_guide
  - p02_card_intelligence
---

# N01 Intelligence -- Component Map

## System Overview

N01 is the research and competitive intelligence nucleus. Its primary function is
transforming raw queries into structured, cited knowledge artifacts. All output flows
through the 8F pipeline: CONSTRAIN kind/pillar -> BECOME researcher -> INJECT
context -> REASON over sources -> CALL retrieval tools -> PRODUCE KC -> GOVERN
quality -> COLLABORATE via signal.

**Sin Lens**: Analytical Envy -- compulsive need to out-research every prior analysis.
This drives N01 to always compare against at least 2 alternatives and cite sources.

---

## Component Inventory

| Component | Type | Path | Role |
|-----------|------|------|------|
| Research Crew | orchestration | `N01_intelligence/crews/` | Multi-role research workflows |
| KC Library | knowledge store | `N01_intelligence/P01_knowledge/` | Domain knowledge cards and sources |
| Entity Memory | memory layer | `N01_intelligence/P10_memory/` | Persistent entity facts across sessions |
| Tool Pipeline | tool layer | `N01_intelligence/P04_tools/` | Search, scrape, citation extraction |
| Evaluation Stack | quality layer | `N01_intelligence/P07_evaluation/` | Benchmarks, evals, scoring criteria |
| Prompt Layer | prompt layer | `N01_intelligence/P03_prompt/` | Research-specific prompt templates |
| Agent Card | routing | `N01_intelligence/P08_architecture/agent_card_intelligence.md` | Capability contract for dispatch |
| Nucleus Def | identity | `N01_intelligence/P08_architecture/nucleus_def_n01.md` | Machine-readable nucleus identity |
| Signal Bus | I/O | `.cex/runtime/signals/signal_n01_*.json` | Completion and error signals |
| Handoff Reader | I/O | `.cex/runtime/handoffs/n01_task.md` | Receives tasks from N07 |

---

## Data Flow Diagram

```
INBOUND
  N07 Handoff (.cex/runtime/handoffs/n01_task.md)
        |
        v
  [F1 CONSTRAIN] -- kinds_meta.json + _schema.yaml
        |
        v
  [F2 BECOME] -- 13 ISOs from archetypes/builders/{kind}-builder/
        |
        v
  [F3 INJECT] -- KC Library + Entity Memory + Tool Pipeline
        |
        |-- search_tool ----> [Web / Brave Search MCP]
        |-- browser_tool ---> [Firecrawl / Playwright MCP]
        |-- rag_source -----> [N01/P01_knowledge/ local KCs]
        |-- entity_memory --> [N01/P10_memory/ persistent facts]
        |-- citation -------> [extracted source metadata]
        |
        v
  [F4 REASON] -- plan: sections, approach, source map
        |
        v
  [F5 CALL] -- retriever + query + cex_retriever.py
        |
        v
  [F6 PRODUCE] -- knowledge_card / competitive_matrix / research_pipeline artifact
        |
        v
  [F7 GOVERN] -- scoring_rubric + quality_gate (target 9.0)
        |
        v
  [F8 COLLABORATE]
        |
        |-- Save artifact --> N01_intelligence/P01_knowledge/ (or target pillar)
        |-- Compile -------> python _tools/cex_compile.py
        |-- Commit --------> git add + git commit
        |-- Signal --------> write_signal('n01', 'complete', score)

OUTBOUND
  knowledge_card -------> N04 (ingestion into knowledge index)
  competitive_matrix ----> N06 (pricing + commercial strategy)
  analyst_briefing ------> N02 (marketing positioning)
  research_pipeline -----> N07 (evidence for orchestration decisions)
  benchmark results -----> N05 (test baselines)
```

---

## Component Details

### 1. Research Crew

| Component | Path | Function |
|-----------|------|----------|
| competitor_scan crew | `N01_intelligence/crews/` | 2-role: researcher -> analyst |
| taxonomy_audit crew | `N01_intelligence/crews/` | 1-role: auditor |
| market_analyst agent | `N01_intelligence/P02_model/` | Competitor + trend analysis |
| paper_reader agent | `N01_intelligence/P02_model/` | Academic paper synthesis |

**Process topology**: sequential (researcher collects, analyst synthesizes).
**Handoff protocol**: researcher writes `kc_raw_sources.md`; analyst reads it and writes `kc_synthesis.md`.

### 2. KC Library (P01_knowledge)

| Subdirectory | Content | Format |
|-------------|---------|--------|
| `N01_intelligence/P01_knowledge/` | Domain KCs, competitive intel, methodology KCs | knowledge_card (.md) |
| `N01_intelligence/P01_knowledge/atlas/` | Atlas-format multi-source compilations | knowledge_card (.md) |
| Core KCs | 35+ existing KCs on research methods, vocabulary, competitive intelligence | knowledge_card |

**Key artifacts**:
- `kc_intelligence_vocabulary.md` -- controlled vocabulary for N01
- `kc_competitive_intelligence_methods.md` -- research methodology
- `kc_information_retrieval_fundamentals.md` -- IR domain knowledge
- `kc_kind_dependency_graph.md` -- (this session) cross-kind build order

### 3. Entity Memory (P10_memory)

| Component | Path | TTL |
|-----------|------|-----|
| Competitor entities | `N01_intelligence/P10_memory/` | 30 days |
| Market facts | `N01_intelligence/P10_memory/` | 90 days |
| Session learnings | `N01_intelligence/P10_memory/` | 7 days |

**Write trigger**: F3b PERSIST after new entities discovered in research.
**Read trigger**: F3 INJECT for any competitive or market research task.

### 4. Tool Pipeline (P04_tools)

| Tool | Provider | Purpose |
|------|----------|---------|
| search_tool | Brave Search MCP | Web queries, competitive intel, news |
| browser_tool | Firecrawl / Playwright MCP | Page scraping, site structure |
| rag_source | local + N01/P01_knowledge | Pre-loaded KC retrieval |
| research_pipeline | `archetypes/builders/research-pipeline-builder/` | Multi-step research automation |

**Tool activation order**: search_tool first (breadth), browser_tool for depth, rag_source for existing knowledge, citation extraction last.

### 5. Evaluation Stack (P07_evaluation)

| Artifact | Purpose | Target |
|----------|---------|--------|
| `kc_benchmark_tool_vs_llm.md` | Tool-vs-LLM research accuracy | Baseline for N01 evals |
| scoring_rubric (research) | Research quality criteria | 9.0 target |
| golden_test set | Reference citations for calibration | Sourcing accuracy |

**Quality gate**: research KCs must pass 7 HARD gates before signal. Key gate: sources must be cited with URL + retrieval date.

### 6. Prompt Layer (P03_prompt)

| Template | Purpose |
|----------|---------|
| Research system prompt | Base identity for N01 research sessions |
| Competitor analysis template | Structured competitive scan |
| KC synthesis template | Source -> structured KC transformation |
| Citation extraction template | URL + metadata -> citation kind |

---

## Inter-Nucleus Data Flows

| From | To N01 | Trigger | What Arrives |
|------|--------|---------|--------------|
| N07 | inbound | handoff written | Research task + scope + decision manifest |
| N04 | inbound | gap detected | "Research this missing domain" |
| N06 | inbound | commercial request | "Research competitor pricing for X" |
| N02 | inbound | positioning need | "Research UI patterns / design trends" |

| From N01 | To | Trigger | What Flows |
|----------|-----|---------|------------|
| knowledge_card complete | N04 | signal | New KC for ingestion |
| competitive_matrix | N06 | signal | Competitor pricing + positioning data |
| analyst_briefing | N02 | signal | Market positioning for campaigns |
| benchmark results | N05 | signal | Test accuracy baselines |
| research findings | N07 | signal | Evidence for orchestration decisions |

---

## Artifact Production by Kind

| Kind | Pillar | Volume | Primary Consumer |
|------|--------|--------|-----------------|
| knowledge_card | P01 | HIGH -- core output | N04, N07 |
| research_pipeline | P04 | MEDIUM | N01 internal |
| competitive_matrix | P05 | MEDIUM | N06, N02 |
| analyst_briefing | P01 | LOW-MEDIUM | N02, N07 |
| citation | P01 | HIGH -- every KC | All nuclei |
| benchmark | P07 | LOW | N05, N07 |
| eval_dataset | P07 | LOW | N05 |
| entity_memory | P10 | HIGH -- background | N01 internal |
| component_map | P08 | LOW (meta) | N07 |

---

## Dependency Map (What N01 Needs to Function)

| Dependency | Kind | Provided By | Required? |
|------------|------|-------------|-----------|
| Search capability | search_tool | Brave Search MCP | YES |
| Browser access | browser_tool | Firecrawl MCP | optional |
| Knowledge base | knowledge_card (existing) | N01/P01_knowledge | YES |
| Quality rubric | scoring_rubric | N00_genesis/P07 | YES |
| Kind taxonomy | kinds_meta.json | .cex/ | YES |
| Builder ISOs | bld_manifest_{kind}.md | archetypes/builders | YES |
| Brand context | brand_config.yaml | .cex/brand | optional |
| Memory store | entity_memory | N01/P10_memory | optional |

---

## Capability Gaps (Identified)

| Gap | Current State | Impact | Priority |
|-----|--------------|--------|----------|
| P08 architecture coverage | 3 artifacts (agent_card, nucleus_def, this component_map) | Cannot self-document for N07 routing | HIGH |
| Real-time search grounding | Brave MCP available but not always wired | Research quality varies | HIGH |
| Entity memory persistence | KCs created but no systematic TTL management | Stale competitor data | MEDIUM |
| Benchmark self-evaluation | No N01-specific eval dataset | Cannot measure research accuracy | MEDIUM |
| Cross-nucleus KC routing | N04 consumes KCs but handoff protocol informal | KC duplication risk | LOW |

---

## Constraints

| Constraint | Value | Source |
|------------|-------|--------|
| Context window | 200K tokens | claude-sonnet-4-6 |
| Quality target | 9.0 | quality_gate |
| Citation required | YES -- every KC | research standards |
| ASCII-only code | YES | `.claude/rules/ascii-code-rule.md` |
| GDP before subjective | YES | guided-decisions rule |
| Signal on complete | YES | 8F F8 protocol |
| Analytical Envy | >= 2 alternatives per finding | sin lens |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n01.md]] | upstream | 0.44 |
| [[p10_bi_intelligence_outputs]] | downstream | 0.36 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.32 |
| [[n01_dr_research_pipeline]] | downstream | 0.31 |
| [[p12_wf_intelligence_pipeline]] | downstream | 0.30 |
| [[spec_cex_system_map]] | upstream | 0.29 |
| [[agent_card_n01]] | related | 0.29 |
| [[n01_intelligence]] | related | 0.29 |
| [[ctx_cex_new_dev_guide]] | related | 0.28 |
| [[p02_card_intelligence]] | upstream | 0.26 |
