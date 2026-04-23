---
quality: 9.1
quality: 7.9
id: kc_lens_city
kind: knowledge_card
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Lens: City -- CEX as Urban Infrastructure"
domain: didactic_engine
subdomain: lens_system
tags: [lens, city, urban, metaphor, teaching, mentor, didactic, analogy]
tldr: "Complete mapping of CEX concepts to a city/urban infrastructure metaphor. 8F=building permit process, nuclei=city districts, kinds=building types, N07=city planner. For /mentor teaching to policy, design, and urban-thinking audiences."
density_score: null
related:
  - tpl_research_batch_maps
  - tpl_research_batch_cnae
  - tpl_search_tool_business_discovery
  - ctx_cex_new_dev_guide
  - p03_sp_engineering_nucleus
  - p01_kc_meta_construction
  - tpl_workflow_research_pipeline
---

# Lens: City

> Every CEX concept has a city equivalent. Use this lens when explaining to product managers, strategists, designers, or anyone who thinks in systems, infrastructure, and governance.

## Core Mapping

| CEX Concept | City Metaphor | One-line Explanation |
|-------------|--------------|---------------------|
| CEX system | The city | The entire metropolitan area: districts, infrastructure, governance, services |
| 8F pipeline | Building permit process | 8 required steps every construction project must clear before occupancy |
| 12 pillars | City districts | Knowledge Quarter, Design District, Commercial Zone... each governed differently |
| nucleus | City department / borough | A division of the city government with its own mandate and budget |
| N07 orchestrator | City planner | Allocates land (context), issues permits (handoffs), never lays bricks |
| kind | Building type / zoning code | "This parcel is zoned for residential" -- defines what can be built, not the building itself |
| builder | Architect firm | Specializes in one building type; knows all regulations for that type |
| ISO | Architectural standard documents | The 12 code documents every architect must follow for their specialization |
| artifact | Completed building | The actual structure that now exists and serves a purpose |
| GDP | Public consultation | "Should this be a park or a parking lot?" -- citizens (users) decide WHAT, planners decide HOW |
| sin lens | Each department's budget priority | Research hoards data, Marketing attracts tourists, QA enforces codes strictly |
| quality gate (F7) | Building inspection | Inspector checks all 7 points; fail = construction halted, must redo |
| signal (F8) | Occupancy certificate | "Building is complete and approved for use" -- issued to city planner |
| handoff | Project brief | The detailed brief the city planner sends to each department |
| dispatch | Issuing a construction permit | Official authorization to begin a specific project |
| wave | Construction phase | Foundation first, then structure, then fit-out -- phases cannot overlap |
| grid | City block development | Multiple buildings constructed simultaneously on adjacent parcels |
| RAG | Infrastructure sourcing | Before building, confirm water, power, and internet are available at that location |

## Extended Mapping: Top 20 Kinds

| Kind | City Metaphor | Teaching Story Seed |
|------|--------------|---------------------|
| `knowledge_card` | Library entry / encyclopedia article | "Every fact the city has formally recorded, indexed, and made findable" |
| `agent` | City employee profile | "Name, role, skills, which tools they're licensed to use, what they cannot authorize alone" |
| `prompt_template` | Standard form | "One form used thousands of times: same structure, different content each time" |
| `system_prompt` | Employee oath and code of conduct | "The document every employee signs: their identity, values, and escalation rules" |
| `workflow` | City procedure (standard operating procedure) | "The step-by-step process every department follows for building permits" |
| `quality_gate` | Code compliance checklist | "The 7 requirements every building must meet: electrical, plumbing, fire safety..." |
| `knowledge_index` | City records database | "The searchable archive of every permit, deed, and report ever filed" |
| `embedding_config` | Address and postal code system | "The standardized addressing that makes every location uniquely findable" |
| `guardrail` | Zoning restriction | "You cannot build a factory in a residential zone, regardless of the owner's wishes" |
| `env_config` | Utility connection spec | "Power voltage, water pressure, internet bandwidth -- the infrastructure contract" |
| `api_client` | City-to-city liaison office | "The official channel for requesting services from another city (external system)" |
| `learning_record` | Post-project debrief | "What the department learned from this project to improve the next one" |
| `entity_memory` | Resident/property master record | "The city's permanent file on this citizen that all departments can see" |
| `crew_template` | Inter-departmental task force | "When Planning, Housing, and Transport must coordinate on one development" |
| `decision_record` | Council resolution | "The formal record of what was decided, when, and why -- legally binding" |
| `benchmark` | Performance audit | "The annual assessment of whether each department meets its service targets" |
| `context_doc` | Policy briefing | "The 2-page summary every department head reads before a major project" |
| `chain` | Automated approval chain | "Application flows automatically from department to department based on content" |
| `router` | Traffic management system | "Decides which district handles which incoming request" |
| `scoring_rubric` | Evaluation criteria table | "The exact criteria judges use to score project proposals in city competitions" |

## 8F as Building Permit Process

| Stage | 8F Step | What happens |
|-------|---------|-------------|
| Application review | F1 CONSTRAIN | Clerk verifies: correct zone? right building type? size within limits? |
| Architect briefing | F2 BECOME | Architect firm loads all codes for this building type (12 standard documents) |
| Site survey | F3 INJECT | Survey team collects: existing plans, neighboring buildings, utility maps |
| Design planning | F4 REASON | Architect plans the structure: floors, layout, estimated cost |
| Tool permits | F5 CALL | Equipment licenses confirmed: crane, excavator, scaffolding -- all approved |
| Construction | F6 PRODUCE | The building is actually built |
| Inspection | F7 GOVERN | Building inspector scores: 7 checkpoints. Fail any = stop construction. |
| Occupancy certificate | F8 COLLABORATE | Certificate issued, records updated, city planner notified. |

## 12 Pillars as City Districts

| District | Pillar | What it governs |
|---------|--------|----------------|
| Knowledge Quarter (university + library) | P01 | Archives, research, indexing, retrieval |
| Civic Center (government offices) | P02 | Employee profiles, role definitions, org charts |
| Design District (studios + agencies) | P03 | Templates, prompts, brand standards |
| Commerce & Trade (market + logistics) | P04 | External connectors, APIs, tools |
| Media & Publishing | P05 | Output formats, content production |
| Legal District (courts + compliance) | P06 | Schemas, contracts, data standards |
| Testing Grounds (QA lab + audit) | P07 | Evaluation, benchmarks, scoring |
| Architecture Bureau | P08 | System design, decision records, naming |
| Utilities (power, water, internet) | P09 | Config, environment, secrets, rate limits |
| City Memory (archives + history) | P10 | Persistent records, context, session state |
| Feedback Bureau (complaints + signals) | P11 | Quality tracking, learning, corrections |
| Transport & Logistics | P12 | Scheduling, orchestration, dispatch |

## 8 Nuclei as City Departments

| Department | Nucleus | Sin Lens (Budget Priority) | Mandate |
|-----------|---------|---------------------------|---------|
| Intelligence Agency | N01 | Analytical Envy | Monitors other cities, publishes intelligence reports |
| Tourism & Marketing | N02 | Creative Lust | Attracts visitors, manages city brand, runs campaigns |
| Construction Authority | N03 | Inventive Pride | Builds all city infrastructure (never delegates) |
| Library & Archives | N04 | Knowledge Gluttony | Indexes everything, answers any question, never forgets |
| Police & Compliance | N05 | Gating Wrath | Enforces codes, blocks bad deployments, tests systems |
| Finance & Revenue | N06 | Strategic Greed | Manages pricing, revenue streams, commercial deals |
| City Planning | N07 | Orchestrating Sloth | Coordinates projects, allocates resources, never builds |
| City Charter | N00 | Pre-sin archetype | The constitution all departments were derived from |

## Discovery Questions (Socratic Seeds)

1. A city planner (N07) issues a project brief (handoff) without consulting residents (GDP). What are the likely consequences, and why does every major project require a public consultation first?
2. Two city departments (nuclei) are working on adjacent parcels (artifacts) simultaneously. What could go wrong without proper coordination, and what mechanism does CEX use to prevent it?
3. The knowledge quarter (P01) and the design district (P03) are both part of the same city (CEX). Why do they need different governing codes (schemas) even though they're neighbors?
4. When an occupancy certificate (F8 signal) is issued, the record goes to the city planner (N07) not the builder. Why does the orchestrator need to know about every completed building?
5. The city's constitution (N00 Genesis) is read-only. Why can't departments modify it, and what would happen to the entire city if they could?

## Quick Reference

```yaml
topic: city_lens
scope: CEX to city/urban infrastructure metaphor translation
owner: n04_knowledge
criticality: high
audience: non_dev_solo_builders
lens: city
covers: 8F_pipeline, 12_pillars, 8_nuclei, top_20_kinds
```

## Sources

- CEX CLAUDE.md: nucleus definitions, 8F pipeline, pillar structure
- Urban planning metaphor: standard in enterprise architecture (city planning = enterprise architecture)
- District model: bounded context from DDD (Evans 2003), mapped to city districts

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_research_batch_maps]] | downstream | 0.27 |
| [[tpl_research_batch_cnae]] | downstream | 0.23 |
| [[tpl_search_tool_business_discovery]] | downstream | 0.17 |
| [[ctx_cex_new_dev_guide]] | related | 0.16 |
| [[p03_sp_engineering_nucleus]] | downstream | 0.16 |
| [[p01_kc_meta_construction]] | sibling | 0.16 |
| [[tpl_workflow_research_pipeline]] | downstream | 0.15 |
