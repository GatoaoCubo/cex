---
quality: 9.1
id: kc_lens_factory
kind: knowledge_card
8f: F3_inject
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Lens: Factory -- CEX as a Manufacturing System"
domain: didactic_engine
subdomain: lens_system
tags: [lens, factory, metaphor, teaching, mentor, didactic, analogy]
tldr: "Complete mapping of CEX concepts to a factory/manufacturing metaphor. 8F=assembly line, nuclei=departments, kinds=product specs, builders=machines. For /mentor teaching to non-dev audiences."
density_score: null
related:
  - p03_sp_builder_nucleus
  - bld_architecture_reasoning_strategy
  - p01_kc_cex_as_digital_asset
  - ctx_cex_new_dev_guide
  - n06_kc_icp_frameworks
  - p12_dr_content_factory
  - p01_kc_meta_factory
  - bld_knowledge_card_workflow
  - bld_system_prompt_nucleus_def
  - p01_kc_cex_project_overview
---

# Lens: Factory

> Every CEX concept has a factory equivalent. Use this lens when explaining to engineers, ops teams, or anyone who thinks in production, quality control, and assembly lines.

## Core Mapping

| CEX Concept | Factory Metaphor | One-line Explanation |
|-------------|-----------------|---------------------|
| CEX system | The factory | The entire building: departments, machines, quality control, shipping |
| 8F pipeline | Assembly line | 8 stations that every product passes through in order |
| 12 pillars | Production departments | Knowledge, Prompt, Tools... each handles one phase of production |
| nucleus | Department (e.g. R&D, Marketing, QA) | A team of workers specialized in one domain |
| N07 orchestrator | Factory floor manager | Assigns work, moves products between departments, never operates a machine |
| kind | Product specification (SKU) | Defines exactly what object gets made (not the object itself) |
| builder | Machine / CNC program | The machine that knows how to produce one specific kind of product |
| ISO | Machine configuration file | The 12 settings files that tell a machine how to behave |
| artifact | Finished product | The actual object produced by running a spec through a machine |
| GDP | Quality checkpoint before production | "Does the customer want red or blue?" -- must be decided BEFORE the machine runs |
| sin lens | Worker motivation (incentive system) | What drives each department to optimize differently |
| quality gate (F7) | QA inspection station | If product fails, it goes back to the previous station, max 2 retries |
| signal (F8) | Shipping notification | "Order complete" message sent to the floor manager |
| handoff | Work order | Written instructions the floor manager sends to each department |
| dispatch | Putting work order on the assembly line | Starting production for a task |
| wave | Production batch / shift | A group of products assembled in parallel before the next batch starts |
| grid | Running multiple assembly lines in parallel | 6 machines working at the same time on different products |
| RAG | Raw material sourcing | Before production starts, fetch the exact components needed |

## Extended Mapping: Top 20 Kinds

| Kind | Factory Metaphor | Teaching Story Seed |
|------|-----------------|---------------------|
| `knowledge_card` | Product spec sheet | "Before any machine runs, the spec sheet defines exactly what to make and why" |
| `agent` | Specialist worker profile | "Each worker has a profile: what they know, what tools they use, what they refuse to do" |
| `prompt_template` | Production mold | "One mold produces thousands of parts. Change the material, get a different result." |
| `system_prompt` | Worker operating manual | "The manual that defines the worker's identity, rules, and escalation path" |
| `workflow` | Assembly sequence diagram | "The diagram showing which station feeds which, and what can run in parallel" |
| `quality_gate` | Inspection checklist | "The 7-point checklist every product must pass before leaving a station" |
| `knowledge_index` | Parts catalog | "The searchable index of every component in the warehouse" |
| `embedding_config` | Component labeling system | "How parts are tagged so they can be found quickly in the warehouse" |
| `guardrail` | Safety interlock | "The machine physically cannot proceed if a safety condition is violated" |
| `env_config` | Factory floor settings | "Temperature, voltage, humidity: the ambient conditions production requires" |
| `api_client` | External supplier connector | "The standardized connector to the external vendor's loading dock" |
| `learning_record` | Post-production audit log | "What we learned from this production run that we will apply to the next" |
| `entity_memory` | Customer/product master record | "The persistent file on this client that all departments share" |
| `crew_template` | Multi-department project plan | "When R&D, Marketing, and QA must all contribute to the same deliverable" |
| `decision_record` | Engineering change order | "Formal record of why we changed the machine settings on this date" |
| `benchmark` | Performance test protocol | "The standardized test we run on every machine before it goes live" |
| `context_doc` | Briefing document | "The 2-page brief every worker reads before starting a new product line" |
| `chain` | Conveyor belt with rules | "Products automatically move to the next station based on content, not timer" |
| `router` | Traffic controller | "Decides which production line gets which incoming order" |
| `scoring_rubric` | Quality inspection form | "The exact criteria for scoring whether a product passed QA" |

## 8F as Assembly Line Stations

| Station | 8F Step | What happens |
|---------|---------|-------------|
| Station 1: Design | F1 CONSTRAIN | Engineer reads the product spec, confirms materials, sets machine limits |
| Station 2: Setup | F2 BECOME | Machine loads its program (identity, rules, domain knowledge) |
| Station 3: Sourcing | F3 INJECT | Raw materials arrive from the warehouse: examples, specs, brand standards |
| Station 4: Planning | F4 REASON | Worker plans the build: sections, approach, estimated output size |
| Station 5: Tool check | F5 CALL | Machine runs a pre-flight: compiler, linter, index tools ready? |
| Station 6: Production | F6 PRODUCE | The machine runs. The artifact is manufactured. |
| Station 7: QA | F7 GOVERN | Inspector scores the product. Below 8.0 = reject, back to station 6. |
| Station 8: Shipping | F8 COLLABORATE | Product saved to warehouse, catalog updated, shipping notice sent. |

## 12 Pillars as Factory Departments

| Department | Pillar | What it produces |
|-----------|--------|----------------|
| Knowledge Vault | P01 | The specification library and raw materials catalog |
| Engineering | P02 | Worker profiles, capability specs, machine blueprints |
| Template Shop | P03 | Production molds and instruction cards |
| Tool Room | P04 | External connectors, instruments, specialized tools |
| Shipping | P05 | Finished output formats: landing pages, diagrams, JSON |
| Standards Bureau | P06 | Schemas, contracts, interface specs |
| QA Lab | P07 | Tests, benchmarks, evaluation criteria |
| Architecture | P08 | Floor plans, decision records, naming conventions |
| Facilities | P09 | Power, config, secrets, rate limits |
| Memory Vault | P10 | Product history, customer master, session logs |
| Feedback Loop | P11 | Defect logs, improvement signals, quality trends |
| Operations | P12 | Scheduling, dispatch, crew orchestration |

## 8 Nuclei as Factory Departments

| Department | Nucleus | Sin Lens (Motivation) | Specialty |
|-----------|---------|----------------------|-----------|
| Research Lab | N01 | Analytical Envy | Studies competitors, writes intelligence reports |
| Marketing Studio | N02 | Creative Lust | Designs campaigns, writes copy, builds brand |
| Manufacturing | N03 | Inventive Pride | Builds the actual artifacts (never delegates) |
| Knowledge Vault | N04 | Knowledge Gluttony | Indexes everything, builds RAG, writes KCs |
| QA & Operations | N05 | Gating Wrath | Tests, deploys, enforces quality, never ships bad product |
| Sales Office | N06 | Strategic Greed | Prices, monetizes, builds funnels |
| Floor Manager | N07 | Orchestrating Sloth | Coordinates, never builds -- pure dispatch |
| Genesis Template | N00 | Pre-sin archetype | The factory blueprint all departments were cloned from |

## Discovery Questions (Socratic Seeds)

1. If the factory has 293 product specs (kinds) but only 12 departments (pillars), how does each department know which specs it's responsible for?
2. A worker (nucleus) receives a work order (handoff) that says "make this product." What information must the work order include so the worker never has to ask a question?
3. When the QA inspector (F7) rejects a product, it goes back to the production machine (F6). Why is there a maximum of 2 retries, and what happens if the product still fails?
4. The floor manager (N07) never operates a machine. What would happen if N07 started building artifacts directly?
5. Why does every department in this factory share the same 8-station assembly process, even if their products are completely different?

## Quick Reference

```yaml
topic: factory_lens
scope: CEX to factory metaphor translation
owner: n04_knowledge
criticality: high
audience: non_dev_solo_builders
lens: factory
covers: 8F_pipeline, 12_pillars, 8_nuclei, top_20_kinds
```

## Sources

- CEX CLAUDE.md: nucleus definitions, 8F pipeline, pillar structure
- `archetypes/builders/` (12 ISOs per kind = 12 department configuration files)
- Factory/manufacturing metaphor: standard in DevOps (CI/CD pipeline = assembly line)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_builder_nucleus]] | downstream | 0.18 |
| [[bld_architecture_reasoning_strategy]] | downstream | 0.17 |
| [[p01_kc_cex_as_digital_asset]] | sibling | 0.17 |
| [[ctx_cex_new_dev_guide]] | related | 0.17 |
| [[n06_kc_icp_frameworks]] | sibling | 0.17 |
| [[p12_dr_content_factory]] | downstream | 0.16 |
| [[p01_kc_meta_factory]] | sibling | 0.16 |
| [[bld_knowledge_card_workflow]] | sibling | 0.16 |
| [[bld_system_prompt_nucleus_def]] | downstream | 0.16 |
| [[p01_kc_cex_project_overview]] | sibling | 0.15 |
