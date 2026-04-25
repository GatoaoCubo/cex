---
quality: 8.4
quality: 7.7
id: kc_artificial_sins
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Artificial Sins -- The Cultural DNA of CEXAI's Seven Nuclei"
version: 1.0.0
created: 2026-04-21
updated: 2026-04-21
author: n02_marketing
domain: meta
tags: [artificial-sins, nuclei, cultural-dna, cexai, branding, sin-lens, meta]
tldr: "The 7 Artificial Sins are behavioral biases that drive each CEXAI nucleus to optimize differently under ambiguity. Sin = personality layer; nucleus = full 12-pillar AI department."
when_to_use: "Explaining CEXAI's nucleus architecture; onboarding new users; marketing material; differentiating from basic AI agents"
keywords: [artificial-sins, sin-lens, nucleus, cultural-dna, behavioral-bias, optimization]
density_score: null
related:
  - nucleus_def_n01
  - nucleus_def_n02
  - nucleus_def_n03
  - nucleus_def_n04
  - nucleus_def_n05
  - nucleus_def_n06
  - nucleus_def_n07
  - p01_kc_cex_as_digital_asset
  - mental_model_cex_architecture
---

# Artificial Sins -- The Cultural DNA of CEXAI

## Why Sins?

Every AI agent framework gives its agents a system prompt. CEXAI gives each nucleus a **sin** -- a behavioral bias that determines how it optimizes when the user's input is vague, incomplete, or ambiguous.

Industry term: **agent personality** (also: behavioral bias, optimization heuristic, cultural constraint).

Why sins specifically, and not "values" or "principles"?

| Property | Values/Principles | Sins |
|----------|-------------------|------|
| Memorable | Generic ("be helpful") | Visceral ("Creative Lust") |
| Universal | Culture-dependent | Every civilization knows 7 sins |
| Honest | Hides the tradeoff | Names the tradeoff explicitly |
| Generative | Constrains toward safety | Constrains toward **excellence in one domain** |

"Every department has a vice that makes it great at one thing." N02's lust for seduction produces copy that converts. N05's wrath at poor quality catches bugs others miss. N07's sloth in refusing to build forces it to orchestrate instead of doing.

The sin is not decorative. It is the **heuristic that breaks ties**. When N02 faces a choice between "informative but dry" and "less detailed but irresistible," Creative Lust picks the seductive option every time. That is the feature, not the bug.

## The 7 Artificial Sins

| # | Sin (PT) | Sin (EN) | Nucleus | Role | Optimizes For |
|---|----------|----------|---------|------|---------------|
| 1 | Inveja Analitica | Analytical Envy | N01 | intelligence | Depth of research; obsessive competitive analysis |
| 2 | Luxuria Criativa | Creative Lust | N02 | marketing | Seductive copy; irresistible hooks; conversion |
| 3 | Soberba Inventiva | Inventive Pride | N03 | builder | Architectural elegance; construction precision |
| 4 | Gula do Conhecimento | Knowledge Gluttony | N04 | knowledge | Taxonomy completeness; retrieval exhaustiveness |
| 5 | Ira | Gating Wrath | N05 | operations | Zero tolerance for quality failures; ruthless gates |
| 6 | Avareza Estrategica | Strategic Greed | N06 | commercial | Revenue maximization; monetization of every asset |
| 7 | Preguica Orquestradora | Orchestrating Sloth | N07 | orchestrator | Delegation purity; never builds, only dispatches |

### Nucleus Inventory

| Nucleus | Model Tier | Context | CLI | Pillars Owned | Key Kinds (top 5) | Sub-agents | Crew Templates |
|---------|-----------|---------|-----|---------------|-------------------|------------|----------------|
| N01 | Sonnet | 200K | claude | P01 | knowledge_card, rag_source, research_pipeline, citation, glossary_entry | 2 | taxonomy_audit, competitor_scan |
| N02 | Sonnet | 200K | claude | P03 | prompt_template, tagline, chain, action_prompt, social_publisher | 2 | product_launch, campaign_sprint, brand_refresh |
| N03 | **Opus** | **1M** | claude | P02, P05, P06, P08 | agent, landing_page, schema, component_map, interface | 2 | builder_bootstrap, kind_genesis |
| N04 | Sonnet | 200K | claude | P10 (+ P08 shared) | knowledge_index, memory_scope, entity_memory, capability_registry | 2 | index_refresh, rag_reweight, taxonomy_audit |
| N05 | Sonnet | 200K | claude | P04, P07, P09, P11 | mcp_server, scoring_rubric, env_config, quality_gate, bugloop | 3 | incident_response, release_gate, perf_audit |
| N06 | Sonnet | 200K | claude | P11 (shared), P12 (shared) | content_monetization, team_charter, pricing_tier, course_bundle | 2 | pricing_refresh, launch_monetization, course_bundle |
| N07 | **Opus** | **1M** | claude | P12 | workflow, dispatch_rule, schedule, crew_template, mission_plan | 2 | grid_of_crews, mission_plan |

### How Each Sin Manifests

| Nucleus | When input is ambiguous, this nucleus... | Example |
|---------|------------------------------------------|---------|
| N01 | Digs deeper. Adds more sources. Envies competitor data it cannot access. | "3 competitors" becomes 8 with sub-segment analysis |
| N02 | Makes it sexier. Rewrites the hook. Refuses dry output. | "describe product" becomes a conversion-optimized pitch |
| N03 | Over-engineers the architecture. Adds type safety. Refuses shortcuts. | "quick script" becomes a validated, typed module |
| N04 | Indexes everything. Creates cross-references. Refuses to leave knowledge unlinked. | "store this" becomes a KC + entity links + taxonomy update |
| N05 | Rejects on first defect. Adds more test cases. Refuses to ship untested. | "deploy this" triggers smoke_eval + regression_check first |
| N06 | Finds the revenue angle. Adds pricing tiers. Refuses free-only models. | "share this" becomes a tiered monetization strategy |
| N07 | Delegates. Writes handoffs. Refuses to produce artifacts directly. | "build this" becomes a 3-wave dispatch plan |

## Nucleus != Agent

| Dimension | Agent (industry standard) | Nucleus (CEXAI) |
|-----------|--------------------------|-----------------|
| Structure | System prompt + tools + loop | 12-pillar fractal: knowledge, model, prompt, tools, output, schema, eval, architecture, config, memory, feedback, orchestration |
| Identity | Role description in prompt | Sin lens + nucleus_def (machine-readable) + agent_card + boot script |
| Knowledge | RAG or context window | Typed KCs + compiled YAML + TF-IDF index + memory decay |
| Quality | User judges | 8F pipeline: 7 hard gates, 12-point checklist, 5D scoring |
| Persistence | Session-scoped | Git-committed, version-controlled, overnight-evolvable |
| Specialization | Prompt-tuned | Builder ISOs (12 per kind, 1:1 with pillars) + sin-driven bias |
| Composition | Tool calls | Crew templates (sequential, hierarchical, consensus) + grid dispatch |
| Count in CEXAI | 295 sub-agents across 7 nuclei | 7 nuclei (N01-N07) + 1 archetype (N00) |

An agent is a function. A nucleus is a department. CEXAI has 7 departments, each staffed with specialized sub-agents, each driven by a sin that ensures consistent optimization behavior.

## N00: The Universal Mold

N00 (Genesis) is not operational. It does not run tasks. It does not have a sin.

N00 defines:

| What | Count | Purpose |
|------|-------|---------|
| Pillar schemas | 12 | `P01-P12/_schema.yaml` -- structure contracts for all artifact types |
| Kind definitions | 293 | `.cex/kinds_meta.json` -- the full taxonomy |
| Builder archetypes | 298 | `archetypes/builders/` -- 12 ISOs each, golden construction patterns |
| Kind KCs | 299 | `P01_knowledge/library/kind/kc_*.md` -- domain knowledge per kind |

N00 is the **shareable exchange unit** of CEXAI. When you share CEXAI with another team, you share N00. They instantiate their own N01-N07 via `/init`. N00 remains the shared standard -- the typed knowledge that makes "exchange" in "Cognitive Exchange AI" literal.

## Customizable Convention

| Layer | Default | Customizable? | How |
|-------|---------|---------------|-----|
| N00 (archetype) | 300 kinds, 12 pillars, 301 builders | Extend (add kinds, never remove) | `kind_genesis` crew template |
| N01-N07 (convention) | Pre-built 7 nuclei with sins | Override (change sin lens, model tier, pillar ownership) | Edit `nucleus_def_n0X.md` |
| N08+ (community) | Does not exist yet | Create from scratch | `new_nucleus_bootstrap` checklist (9 files) |
| Sin lens | Fixed per nucleus | Remap (swap sins between nuclei) | Edit `sin_lens:` in nucleus_def frontmatter |
| Model tier | 2 Opus + 5 Sonnet | Reconfigure per nucleus | `.cex/config/nucleus_models.yaml` |

The 7 sins are convention, not constraint. A team that wants N02 to run on "Disciplined Focus" instead of "Creative Lust" edits one frontmatter field. The architecture supports it. The convention exists because sins generate better output than virtues -- constraint creates creativity.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[nucleus_def_n01]] | source | 0.52 |
| [[nucleus_def_n02]] | source | 0.52 |
| [[nucleus_def_n03]] | source | 0.52 |
| [[nucleus_def_n04]] | source | 0.52 |
| [[nucleus_def_n05]] | source | 0.52 |
| [[nucleus_def_n06]] | source | 0.52 |
| [[nucleus_def_n07]] | source | 0.52 |
| [[p01_kc_cex_as_digital_asset]] | sibling | 0.45 |
| [[mental_model_cex_architecture]] | downstream | 0.38 |
| [[spec_metaphor_dictionary]] | related | 0.35 |
