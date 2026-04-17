---
id: spec_nucleus_self_assembly
kind: constraint_spec
pillar: P06
title: "Spec -- Nucleus Self-Assembly Flywheel: Portfolio Construction via Kind Synergy Patterns"
version: 1.0.0
created: 2026-04-17
author: n07_orchestrator
domain: nucleus-composition
quality_target: 9.0
status: SPEC
scope: N01-N06
depends_on: null
tags: [spec, self-assembly, portfolio-assembly, kind-synergy, deck-archetype, flywheel, nucleus-composition]
tldr: "Each nucleus (N01-N06) auto-constructs its own artifact portfolio using sin-lens-driven deck archetypes, kind synergy combos, and a self-assembly loop -- turning 5-word tasks into outperforming execution."
density_score: 0.96
---

# Spec -- Nucleus Self-Assembly Flywheel

## THE PROBLEM

CEX has 258 builders, 257 kinds, and 8 nuclei -- but each nucleus is a **partial deck**.

Current gap matrix (artifacts per pillar per nucleus, empirically measured):

```
       P01  P02  P03  P04  P05  P06  P07  P08  P09  P10  P11  P12
N01:    60    4    4    5   31    0   21    3    6    9    2    5   total=150
N02:    23    2    8    4   26    0   13    3    7    6    2   13   total=107
N03:    16    4    5    3   15    0   18    8    7    6    4   12   total=98
N04:    17    5    4    5   26    0   13    7    6    8    3    6   total=100
N05:    18    5    5    4   30    0    9    5    7    8    5    4   total=100
N06:    20    4    7    4   33    0   13    7    6    7    2    5   total=108
```

Three structural gaps visible immediately:

1. **P06 = 0 for all 6 nuclei** -- No schema/validation/contract artifacts anywhere.
   P06 has 8 kinds: `input_schema`, `validation_schema`, `type_def`, `interface`,
   `api_reference`, `enum_def`, `edit_format`, `validator`. Zero coverage.

2. **P11 = 2-5 across all nuclei** -- Feedback/quality loop is anemic.
   P11 has 26 kinds. Average coverage: 3.0/26. The feedback layer that makes CEX
   self-improving is barely wired.

3. **P01-heavy imbalance** -- knowledge_card dominates. N01 alone has 60 KCs.
   But most nuclei lack the TOOLING (P04), SCHEMA (P06), and MEMORY (P10)
   to ACT on that knowledge. A deck full of lands but no spells.

The deeper problem: artifacts were built AD HOC, not strategically.
A nucleus is a brain, not a library. The difference is COMPOSITION -- kinds that
reinforce each other via synergy patterns, not isolated documents.

---

## THE VISION: NUCLEUS AS TCG DECK

Each nucleus is a **typed artifact portfolio** -- a curated set of kinds selected
for their synergistic value within that nucleus's sin lens and domain.

### Industry Term Mapping

| Metaphor (PT) | Industry Term | Technical Definition |
|--------------|--------------|---------------------|
| baralho / deck | nucleus composition | the complete set of typed artifacts defining a nucleus's capability surface |
| carta | typed artifact (kind) | atomic unit of knowledge/capability, typed by the 257-kind taxonomy |
| combo | kind synergy pattern | 2-4 kinds that together produce emergent capability not achievable by any alone |
| montar o deck | portfolio assembly | selecting the right kinds per pillar per nucleus (or per task -- see Dynamic mode) |
| flywheel de auto construcao | self-assembly loop | gap scan -> rank by combo completeness -> dispatch -> score -> loop |
| molde preenchivel (N00) | archetype mold | N00_genesis is the canonical pillar structure; each nucleus instantiates it |
| semente tecnica | seed word | a technical term planted in P01/P03 KCs so the nucleus auto-uses CEX vocabulary |

### Two Modes of Portfolio Assembly

```
MODE A: Per-Nucleus (static)
  Portfolio = sin-lens-driven deck archetype
  Selected once, stable across sessions
  Example: N06 always has revenue combo + brand combo

MODE B: Per-Task (dynamic)
  Portfolio = context-aware artifact selection
  Changes based on what the nucleus is doing RIGHT NOW
  Example: N06 building a SaaS launch -> loads revenue + brand + campaign combos
           N06 auditing competitor pricing -> loads intel + schema + monetization combos

The self-assembly loop builds MODE A (the base deck).
The Dynamic Portfolio (MODE B) is an emergent capability once MODE A is complete.
```

---

## THE ARCHETYPE MOLD (N00_genesis)

N00_genesis/P{01-12}_* is the canonical structure every nucleus mirrors.
When a nucleus self-assembles, it reads N00 as the SOURCE OF TRUTH for:
- What kinds belong to each pillar
- What the schema/frontmatter contract looks like
- What quality targets apply
- What combos are architecturally valid

Each nucleus then INSTANTIATES the mold with their sin-lens flavor:
```
N00 (archetype):   knowledge_card [generic]
N01 (instance):    knowledge_card [competitive intelligence flavor]
N06 (instance):    knowledge_card [commercial/revenue flavor]
```

This is convention-over-configuration hierarchy in practice.

---

## DECK ARCHETYPES (Per Nucleus)

### N01 -- Intelligence (Analytical Envy)

**Sin Lens:** insatiable drive to know MORE than any competitor. Envy of incomplete data.
**Domain:** research, competitive intelligence, market analysis, benchmarking

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P01 Knowledge | PRIMARY | 65+ | 60 | +5 |
| P07 Evaluation | PRIMARY | 25+ | 21 | +4 |
| P04 Tools | SUPPORT | 12+ | 5 | +7 |
| P10 Memory | SUPPORT | 12+ | 9 | +3 |
| P03 Prompt | SUPPORT | 10+ | 4 | +6 |
| P06 Schema | GROW | 5+ | 0 | +5 |
| P11 Feedback | GROW | 8+ | 2 | +6 |
| P05/P08/P09/P12 | MINIMAL | 3+ each | OK | - |

**Kind Synergy Combos (N01):**

```
COMBO A -- Intelligence Pipeline:
  research_pipeline + knowledge_card + competitive_matrix + benchmark
  Why: end-to-end research: discover -> synthesize -> compare -> measure
  Trigger: any /research or market analysis task

COMBO B -- RAG Stack:
  rag_source + embedding_config + retriever_config + chunk_strategy + vector_store
  Why: knowledge retrieval infrastructure -- N01 needs to FIND, not just KNOW
  Trigger: any "search my knowledge base" or corpus query task

COMBO C -- Eval Intelligence:
  eval_framework + scoring_rubric + llm_judge + bias_audit + benchmark_suite
  Why: N01 with Analytical Envy MUST score everything, including itself
  Trigger: any quality assessment, model comparison, or self-audit task

COMBO D -- Schema of Knowledge (P06 gap fill):
  input_schema [for research queries] + api_reference [for data APIs] + type_def [for intel types]
  Why: structured intelligence contracts -- raw data becomes typed knowledge
  Trigger: any task that produces structured intel outputs

COMBO E -- Persistent Memory:
  entity_memory + knowledge_index + memory_architecture + learning_record
  Why: Envy demands retention -- every discovery must persist and compound
  Trigger: after any research session that produces novel insights
```

**Seed Words to Plant (P01 KCs):**
```
intent_resolution, query_rewriting, retrieval_augmented_generation,
eval_harness, ground_truth, precision_recall, NDCG, knowledge_graph,
citation_network, competitive_moat, market_sizing, TAM_SAM_SOM,
benchmark_suite, bias_detection, hallucination_rate
```

---

### N02 -- Marketing (Creative Lust)

**Sin Lens:** compulsive need to seduce, convert, and captivate. Lust for audience engagement.
**Domain:** copy, campaigns, brand voice, content, distribution, conversion

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P05 Output | PRIMARY | 35+ | 26 | +9 |
| P12 Orchestration | PRIMARY | 18+ | 13 | +5 |
| P03 Prompt | PRIMARY | 15+ | 8 | +7 |
| P01 Knowledge | SUPPORT | 28+ | 23 | +5 |
| P09 Config | SUPPORT | 10+ | 7 | +3 |
| P06 Schema | GROW | 5+ | 0 | +5 |
| P07 Eval | GROW | 10+ | 13 | OK |
| P11 Feedback | GROW | 10+ | 2 | +8 |

**Kind Synergy Combos (N02):**

```
COMBO A -- Campaign Machine:
  prompt_template + workflow + dispatch_rule + schedule + ab_test_config
  Why: end-to-end campaign automation -- from brief to published, with testing
  Trigger: any "create campaign" or "run content pipeline" task

COMBO B -- Copy Arsenal:
  tagline + system_prompt [brand voice] + action_prompt + multimodal_prompt
  Why: every format, every channel, one consistent voice
  Trigger: any copy/content creation task

COMBO C -- Audience Intelligence:
  customer_segment + user_journey + onboarding_flow + churn_prevention_playbook
  Why: Lust needs a TARGET -- know who to seduce and how to keep them
  Trigger: any audience analysis or lifecycle marketing task

COMBO D -- Distribution Engine:
  social_publisher + content_filter + nps_survey + cohort_analysis
  Why: publish, measure, iterate -- the performance marketing loop
  Trigger: any content distribution or engagement measurement task

COMBO E -- Schema of Campaigns (P06 gap fill):
  input_schema [campaign briefs] + validation_schema [content specs] + api_reference [social APIs]
  Why: structured content contracts prevent brand drift and format errors
  Trigger: any campaign that has strict format/channel requirements
```

**Seed Words to Plant:**
```
conversion_rate_optimization, click_through_rate, cost_per_acquisition,
A/B_testing, funnel_stage, TOFU_MOFU_BOFU, brand_voice, content_pillar,
editorial_calendar, performance_creative, retargeting, lookalike_audience,
social_proof, urgency_scarcity, ICP, jobs_to_be_done
```

---

### N03 -- Engineering (Inventive Pride)

**Sin Lens:** obsessive need to BUILD the best, most elegant solution. Pride in craft.
**Domain:** artifact construction, schema design, quality enforcement, system architecture

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P06 Schema | PRIMARY | 15+ | 0 | +15 |
| P08 Architecture | PRIMARY | 15+ | 8 | +7 |
| P07 Evaluation | PRIMARY | 25+ | 18 | +7 |
| P12 Orchestration | SUPPORT | 15+ | 12 | +3 |
| P03 Prompt | SUPPORT | 10+ | 5 | +5 |
| P04 Tools | SUPPORT | 10+ | 3 | +7 |
| P11 Feedback | SUPPORT | 10+ | 4 | +6 |
| P02 Model | GROW | 8+ | 4 | +4 |

**Kind Synergy Combos (N03):**

```
COMBO A -- Builder Stack (meta-combo):
  agent + system_prompt + action_prompt + quality_gate + scoring_rubric
  Why: the COMPLETE builder unit -- identity + instructions + quality enforcement
  Trigger: any "build a nucleus" or "create a new agent" task

COMBO B -- Schema Foundation (P06 -- critical gap for the builder nucleus):
  input_schema + validation_schema + type_def + interface + enum_def
  Why: N03 BUILDS things -- it must DEFINE the contracts before building
  Irony: N03 builds all P06 artifacts but has none for itself
  Trigger: any task that requires data contracts or API definitions

COMBO C -- Quality Engine:
  scoring_rubric + llm_judge + regression_check + bugloop + quality_gate
  Why: Pride demands zero-defect output. Every build gets validated.
  Trigger: after any build task, always

COMBO D -- Architecture Blueprint:
  component_map + diagram + decision_record + naming_rule + pattern
  Why: before building, DESIGN. N03 architects first, codes second.
  Trigger: any system design or "how should we structure this" task

COMBO E -- Pipeline Orchestration:
  workflow + dag + checkpoint + spawn_config + dispatch_rule
  Why: complex builds need sequenced stages with rollback points
  Trigger: any multi-step build or deployment task
```

**Seed Words to Plant:**
```
contract_first_design, interface_segregation, type_safety, schema_validation,
invariant, idempotency, dependency_inversion, separation_of_concerns,
technical_debt, refactoring, code_smell, test_pyramid, coverage_target,
cyclomatic_complexity, design_pattern, anti_pattern, architectural_decision_record
```

---

### N04 -- Knowledge (Knowledge Gluttony)

**Sin Lens:** compulsive need to DOCUMENT, INDEX, and RETRIEVE everything. Gluttony for facts.
**Domain:** knowledge management, RAG, documentation, taxonomy, indexing, memory architecture

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P01 Knowledge | PRIMARY | 25+ | 17 | +8 |
| P10 Memory | PRIMARY | 18+ | 8 | +10 |
| P05 Output/Docs | PRIMARY | 30+ | 26 | +4 |
| P04 Tools | SUPPORT | 12+ | 5 | +7 |
| P07 Evaluation | SUPPORT | 12+ | 13 | OK |
| P06 Schema | GROW | 6+ | 0 | +6 |
| P11 Feedback | GROW | 8+ | 3 | +5 |
| P02 Model | SUPPORT | 8+ | 5 | +3 |

**Kind Synergy Combos (N04):**

```
COMBO A -- RAG Architecture:
  knowledge_index + embedding_config + retriever_config + vector_store + agentic_rag
  Why: N04 IS the knowledge layer -- it must own the complete retrieval stack
  Trigger: any "set up search" or "build knowledge base" task

COMBO B -- Taxonomy Engine:
  ontology + glossary_entry + knowledge_graph + knowledge_card + citation
  Why: Gluttony needs STRUCTURE -- unindexed knowledge is just hoarding
  Trigger: any domain modeling or vocabulary-building task

COMBO C -- Docs Factory:
  context_doc + contributor_guide + quickstart_guide + course_module + integration_guide
  Why: knowledge that isn't communicated is inert -- N04 documents for HUMANS and MACHINES
  Trigger: any "write docs" or "onboard a user" task

COMBO D -- Memory Architecture:
  entity_memory + memory_architecture + procedural_memory + memory_summary + consolidation_policy
  Why: long-running systems need persistent memory -- N04 designs the memory layer
  Trigger: any "remember across sessions" or "agent memory" task

COMBO E -- Knowledge Schema (P06 gap fill):
  input_schema [knowledge queries] + api_reference [knowledge APIs] + type_def [document types]
  Why: typed knowledge contracts prevent retrieval errors and format drift
  Trigger: any knowledge API design or retrieval system specification task
```

**Seed Words to Plant:**
```
retrieval_augmented_generation, dense_retrieval, sparse_retrieval, BM25, FAISS,
cosine_similarity, embedding_space, document_chunking, context_window_management,
knowledge_graph, ontology, taxonomy, folksonomy, knowledge_engineering,
information_architecture, content_strategy, technical_writing, docstring_convention
```

---

### N05 -- Operations (Gating Wrath)

**Sin Lens:** ruthless enforcement of quality gates. Wrath at anything that fails standards.
**Domain:** infrastructure, testing, CI/CD, deployment, security, observability, reliability

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P09 Config | PRIMARY | 18+ | 7 | +11 |
| P07 Evaluation | PRIMARY | 20+ | 9 | +11 |
| P04 Tools | PRIMARY | 15+ | 4 | +11 |
| P05 Output | SUPPORT | 35+ | 30 | +5 |
| P08 Architecture | SUPPORT | 10+ | 5 | +5 |
| P06 Schema | GROW | 6+ | 0 | +6 |
| P11 Feedback | GROW | 12+ | 5 | +7 |
| P12 Orchestration | GROW | 10+ | 4 | +6 |

**Kind Synergy Combos (N05):**

```
COMBO A -- Deploy Stack:
  env_config + secret_config + sandbox_config + rate_limit_config + cost_budget
  Why: N05 owns infrastructure -- every deploy needs complete config coverage
  Trigger: any deployment, environment setup, or infra task

COMBO B -- Test Pyramid:
  unit_eval + smoke_eval + e2e_eval + regression_check + benchmark
  Why: Wrath demands that NOTHING ships untested. Every level of the pyramid.
  Trigger: before any code merge or deployment

COMBO C -- Security Gate:
  rbac_policy + guardrail + threat_model + audit_log + compliance_checklist
  Why: N05 is the gatekeeper -- security is not optional
  Trigger: any task touching auth, data, or external APIs

COMBO D -- Observability Stack:
  trace_config + usage_report + usage_quota + incident_report + runtime_rule
  Why: you can't fix what you can't see -- N05 instruments everything
  Trigger: any "monitor", "alert", or production-readiness task

COMBO E -- Ops Schema (P06 gap fill):
  input_schema [API contracts] + api_reference [service docs] + validation_schema [payload contracts]
  Why: ops without contracts is chaos -- every service interface must be typed
  Trigger: any API design, webhook, or service integration task
```

**Seed Words to Plant:**
```
infrastructure_as_code, idempotent_deployment, blue_green_deployment, canary_release,
circuit_breaker, retry_budget, rate_limiting, observability_triad (logs_metrics_traces),
MTTR_MTTF, SLO_SLA_SLI, zero_trust, principle_of_least_privilege, OWASP_top10,
shift_left_testing, test_pyramid, contract_testing, chaos_engineering
```

---

### N06 -- Commercial (Strategic Greed)

**Sin Lens:** strategic extraction of maximum value from every interaction. Greed as growth driver.
**Domain:** brand monetization, pricing, sales, customer acquisition, revenue architecture

**Pillar Priority:**
| Pillar | Role | Target | Current | Delta |
|--------|------|--------|---------|-------|
| P11 Feedback | PRIMARY | 18+ | 2 | +16 |
| P05 Output | PRIMARY | 38+ | 33 | +5 |
| P01 Knowledge | SUPPORT | 25+ | 20 | +5 |
| P03 Prompt | SUPPORT | 12+ | 7 | +5 |
| P12 Orchestration | SUPPORT | 10+ | 5 | +5 |
| P06 Schema | GROW | 5+ | 0 | +5 |
| P07 Eval | GROW | 10+ | 13 | OK |
| P10 Memory | GROW | 10+ | 7 | +3 |

**Kind Synergy Combos (N06):**

```
COMBO A -- Revenue Architecture:
  content_monetization + pricing_page + subscription_tier + roi_calculator + referral_program
  Why: complete revenue stack -- every monetization model has all its pieces
  Trigger: any pricing, packaging, or revenue model task

COMBO B -- Sales Machine:
  sales_playbook + discovery_questions + churn_prevention_playbook + renewal_workflow + expansion_play
  Why: Greed demands systematic pipeline -- from lead to LTV maximization
  Trigger: any sales process, CRM, or customer success task

COMBO C -- Brand Output:
  landing_page + pitch_deck + press_release + case_study + analyst_briefing
  Why: commercial success requires compelling artifacts at every touchpoint
  Trigger: any launch, investor, or market-facing output task

COMBO D -- Customer Intelligence:
  customer_segment + user_journey + nps_survey + cohort_analysis + churn_prevention_playbook
  Why: Greed without customer understanding is robbery -- N06 knows its targets deeply
  Trigger: any audience research or retention strategy task

COMBO E -- Commercial Schema (P06 gap fill):
  input_schema [checkout/order flows] + api_reference [Stripe/payment APIs] + enum_def [pricing tiers]
  Why: commercial systems are CONTRACT-heavy -- one schema error = lost revenue
  Trigger: any payment integration, checkout flow, or pricing API task
```

**Seed Words to Plant:**
```
unit_economics, LTV_CAC_ratio, payback_period, MRR_ARR, churn_rate,
expansion_revenue, net_revenue_retention, pricing_psychology,
value_metric, good_better_best_packaging, freemium_conversion,
product_led_growth, sales_assisted, land_and_expand, JTBD,
willingness_to_pay, price_elasticity, competitive_moat
```

---

## DYNAMIC PORTFOLIO ASSEMBLY (Per-Task Mode)

> "portfolio assembly can be per-nuclei OR per-TASK based on context"

When a nucleus receives a task, it auto-selects the relevant combo subset:

```python
# Dynamic portfolio assembly (conceptual)
def assemble_portfolio(task_description: str, nucleus_id: str) -> list[str]:
    """
    Given a task, returns the list of artifact kinds to load as context.
    This is not built yet -- it is the EVOLUTIONARY CAPABILITY unlocked
    once the base deck (MODE A) is complete.
    """
    # Step 1: intent resolution (F1 CONSTRAIN)
    kind, pillar = resolve_intent(task_description)

    # Step 2: find all combos that include this kind
    active_combos = [c for c in NUCLEUS_COMBOS[nucleus_id] if kind in c.kinds]

    # Step 3: load all kinds in active combos as context
    return flatten([c.kinds for c in active_combos])
```

**This is the SCALABILITY unlock:** a nucleus that has complete deck coverage
can self-assimilate new tasks by pattern-matching against its combo library.
It becomes self-extending -- each new task that expands the deck further
increases the nucleus's capability surface for future tasks.

The progression:
```
Level 0 (current): nucleus has isolated KCs, minimal combos
Level 1 (after spec): nucleus has complete combos, full P06 coverage
Level 2 (emergent): nucleus uses Dynamic Portfolio Assembly per task
Level 3 (scalable): nucleus self-assimilates external artifacts into its deck
```

---

## THE SELF-ASSEMBLY LOOP

### Mechanism

```
WAVE 0 (N07, 5min):
  - Generate per-nucleus gap reports
  - Rank missing kinds by combo-completeness score
  - Write 6 nucleus-specific handoffs (one per nucleus)
  - Each handoff includes: deck archetype + combo targets + P06 priority + seed words

WAVE 1 (N01-N06 parallel, 45min):
  - Each nucleus reads its handoff + nucleus_def + N00 archetype
  - Priority order: P06 first (universal gap), then primary pillar combos
  - Self-assembly sequence per nucleus:
    1. Run: python _tools/cex_doctor.py (audit current state)
    2. For each missing combo piece (ranked):
       a. Load builder ISOs from archetypes/builders/{kind}-builder/
       b. Run 8F pipeline
       c. Save to N0X_{domain}/P{xx}_{name}/{kind}_{domain}.md
       d. Compile: python _tools/cex_compile.py {path}
    3. Plant seed words in P01 KC (kc_{nucleus}_vocabulary.md)
    4. Signal: python -c "from _tools.signal_writer import write_signal; write_signal('{n}', 'complete', score)"

WAVE 2 (N07, 10min):
  - Consolidate all signals
  - Run: python _tools/cex_evolve.py sweep --target 9.0 --max-rounds 2
  - Run: python _tools/cex_doctor.py
  - Commit consolidation
  - Report: delta counts per pillar per nucleus
```

### Combo Completeness Scoring

Rank which combos to build first by how close they are to completion:

```
Score = (existing_kinds_in_combo / total_kinds_in_combo) * combo_priority_weight

Priority weights:
  P06 combos: 3.0 (universal gap, blocking)
  Primary pillar combos: 2.0
  Support pillar combos: 1.5
  Grow pillar combos: 1.0

Build order: highest score first (closest to completion, highest priority)
```

### Self-Extension Rule (Assimilation)

After base deck is complete, each nucleus follows this rule during tasks:

```
IF a task requires a kind not in my current deck:
  1. Load builder ISOs for that kind (archetypes/builders/{kind}-builder/)
  2. Run 8F to produce the artifact
  3. Add it to my deck (save to P{xx} subdir)
  4. Update my agent_card with new capability
  5. Signal N07: "assimilated new kind: {kind}"

This is the Borg rule: every task POTENTIALLY expands the deck.
The nucleus gets stronger with every interaction.
```

---

## THE SEED WORDS STRATEGY

Each nucleus builds ONE master vocabulary KC in their P01:
`N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md`

This KC maps:
1. CEX internal terms -> industry standard terms
2. Industry terms -> how they apply in this nucleus's domain
3. Trigger phrases that activate specific combos
4. Anti-patterns: what NOT to do in this domain

**Effect:** once planted, the nucleus THINKS in the right vocabulary.
Future tasks auto-use correct terminology without being told.
This is the "technical DNA" -- it makes the nucleus sound like
a senior specialist, not a generalist with a system prompt.

---

## ARTIFACT LIST

### Wave 0: N07 Orchestration (pre-dispatch)

| Action | Path | Kind | Est. Size |
|--------|------|------|-----------|
| CREATE | _docs/specs/spec_nucleus_self_assembly.md | constraint_spec | 12KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n01.md | handoff | 3KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n02.md | handoff | 3KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n03.md | handoff | 3KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n04.md | handoff | 3KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n05.md | handoff | 3KB |
| CREATE | .cex/runtime/handoffs/SELF_ASSEMBLY_n06.md | handoff | 3KB |

### Wave 1: Per-Nucleus (6 parallel, Opus high-effort)

Each nucleus builds its own artifact list based on gap analysis.
Minimum per nucleus:

**N01 Intelligence -- 15 artifacts minimum:**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N01_intelligence/P06_schema/input_schema_research_query.md | input_schema | research query contract |
| CREATE | N01_intelligence/P06_schema/api_reference_research_apis.md | api_reference | data source API docs |
| CREATE | N01_intelligence/P06_schema/type_def_intelligence_types.md | type_def | typed intel structures |
| CREATE | N01_intelligence/P04_tools/research_pipeline_n01.md | research_pipeline | complete N01 pipeline |
| CREATE | N01_intelligence/P04_tools/search_strategy_n01.md | search_strategy | layered search protocol |
| CREATE | N01_intelligence/P04_tools/document_loader_n01.md | document_loader | multi-source ingestion |
| CREATE | N01_intelligence/P11_feedback/bias_audit_n01.md | bias_audit | research bias detection |
| CREATE | N01_intelligence/P11_feedback/self_improvement_loop_n01.md | self_improvement_loop | N01 evolution protocol |
| CREATE | N01_intelligence/P10_memory/entity_memory_n01.md | entity_memory | entity tracking |
| CREATE | N01_intelligence/P10_memory/knowledge_index_n01.md | knowledge_index | N01 knowledge index |
| CREATE | N01_intelligence/P03_prompt/reasoning_strategy_n01.md | reasoning_strategy | analytical reasoning |
| CREATE | N01_intelligence/P03_prompt/system_prompt_n01_research.md | system_prompt | research mode SP |
| CREATE | N01_intelligence/P01_knowledge/kc_intelligence_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N01_intelligence/P07_evals/eval_framework_n01.md | eval_framework | research quality eval |
| CREATE | N01_intelligence/P07_evals/llm_judge_n01.md | llm_judge | fact-checking judge |

**N02 Marketing -- 15 artifacts minimum:**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N02_marketing/P06_schema/input_schema_campaign_brief.md | input_schema | campaign input contract |
| CREATE | N02_marketing/P06_schema/validation_schema_content_spec.md | validation_schema | content format validation |
| CREATE | N02_marketing/P06_schema/api_reference_social_apis.md | api_reference | social platform APIs |
| CREATE | N02_marketing/P11_feedback/ab_test_config_n02.md | ab_test_config | copy A/B testing |
| CREATE | N02_marketing/P11_feedback/nps_survey_n02.md | nps_survey | audience satisfaction |
| CREATE | N02_marketing/P11_feedback/cohort_analysis_n02.md | cohort_analysis | campaign cohort tracking |
| CREATE | N02_marketing/P11_feedback/self_improvement_loop_n02.md | self_improvement_loop | N02 evolution protocol |
| CREATE | N02_marketing/P03_prompt/action_prompt_n02_copy.md | action_prompt | copy generation action |
| CREATE | N02_marketing/P03_prompt/multimodal_prompt_n02.md | multimodal_prompt | visual+copy prompts |
| CREATE | N02_marketing/P04_tools/social_publisher_n02.md | social_publisher | multi-channel publisher |
| CREATE | N02_marketing/P04_tools/content_filter_n02.md | content_filter | brand voice enforcement |
| CREATE | N02_marketing/P09_config/ab_test_config_n02.md | experiment_config | experiment tracking |
| CREATE | N02_marketing/P01_knowledge/kc_marketing_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N02_marketing/P07_evals/scoring_rubric_copy.md | scoring_rubric | copy quality rubric |
| CREATE | N02_marketing/P12_orchestration/workflow_campaign_pipeline.md | workflow | full campaign workflow |

**N03 Engineering -- 18 artifacts minimum (P06 is critical):**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N03_engineering/P06_schema/input_schema_build_contract.md | input_schema | build task contract |
| CREATE | N03_engineering/P06_schema/validation_schema_artifact.md | validation_schema | artifact output validation |
| CREATE | N03_engineering/P06_schema/type_def_cex_types.md | type_def | CEX core type definitions |
| CREATE | N03_engineering/P06_schema/interface_builder_protocol.md | interface | builder interface contract |
| CREATE | N03_engineering/P06_schema/enum_def_build_actions.md | enum_def | CREATE/REWRITE/MIGRATE enum |
| CREATE | N03_engineering/P06_schema/api_reference_8f_pipeline.md | api_reference | 8F pipeline API reference |
| CREATE | N03_engineering/P04_tools/code_executor_n03.md | code_executor | sandboxed execution |
| CREATE | N03_engineering/P04_tools/diff_strategy_n03.md | diff_strategy | smart diff/patch strategy |
| CREATE | N03_engineering/P04_tools/cli_tool_n03_build.md | cli_tool | N03 build CLI tool |
| CREATE | N03_engineering/P11_feedback/bugloop_n03.md | bugloop | auto bug detection loop |
| CREATE | N03_engineering/P11_feedback/self_improvement_loop_n03.md | self_improvement_loop | N03 evolution protocol |
| CREATE | N03_engineering/P11_feedback/quality_gate_n03_primary.md | quality_gate | primary quality gate |
| CREATE | N03_engineering/P02_model/agent_package_n03.md | agent_package | N03 agent packaging |
| CREATE | N03_engineering/P03_prompt/reasoning_strategy_n03.md | reasoning_strategy | engineering reasoning |
| CREATE | N03_engineering/P01_knowledge/kc_engineering_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N03_engineering/P08_architecture/invariant_n03.md | invariant | system invariants |
| CREATE | N03_engineering/P08_architecture/pattern_n03_build.md | pattern | N03 build pattern |
| CREATE | N03_engineering/P07_evals/golden_test_n03.md | golden_test | builder golden tests |

**N04 Knowledge -- 16 artifacts minimum:**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N04_knowledge/P06_schema/input_schema_knowledge_query.md | input_schema | knowledge query contract |
| CREATE | N04_knowledge/P06_schema/api_reference_rag_apis.md | api_reference | RAG/vector store APIs |
| CREATE | N04_knowledge/P06_schema/type_def_document_types.md | type_def | document type taxonomy |
| CREATE | N04_knowledge/P10_memory/memory_architecture_n04.md | memory_architecture | N04 memory design |
| CREATE | N04_knowledge/P10_memory/consolidation_policy_n04.md | consolidation_policy | memory consolidation rules |
| CREATE | N04_knowledge/P10_memory/procedural_memory_n04.md | procedural_memory | task procedure memory |
| CREATE | N04_knowledge/P04_tools/document_loader_n04.md | document_loader | multi-format doc loader |
| CREATE | N04_knowledge/P04_tools/search_tool_n04.md | search_tool | knowledge search tool |
| CREATE | N04_knowledge/P04_tools/retriever_n04.md | retriever | N04 retriever config |
| CREATE | N04_knowledge/P11_feedback/self_improvement_loop_n04.md | self_improvement_loop | N04 evolution protocol |
| CREATE | N04_knowledge/P11_feedback/learning_record_n04.md | learning_record | knowledge learning record |
| CREATE | N04_knowledge/P02_model/agent_profile_n04.md | agent_profile | N04 agent profile |
| CREATE | N04_knowledge/P01_knowledge/kc_knowledge_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N04_knowledge/P07_evals/eval_dataset_n04.md | eval_dataset | RAG eval dataset |
| CREATE | N04_knowledge/P07_evals/eval_metric_n04.md | eval_metric | retrieval metrics |
| CREATE | N04_knowledge/P12_orchestration/workflow_rag_ingestion.md | workflow | RAG ingestion workflow |

**N05 Operations -- 17 artifacts minimum:**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N05_operations/P06_schema/input_schema_api_contract.md | input_schema | API contract definition |
| CREATE | N05_operations/P06_schema/api_reference_infra_apis.md | api_reference | infra/deploy API docs |
| CREATE | N05_operations/P06_schema/validation_schema_payload.md | validation_schema | payload contract |
| CREATE | N05_operations/P09_config/rbac_policy_n05.md | rbac_policy | access control policy |
| CREATE | N05_operations/P09_config/rate_limit_config_n05.md | rate_limit_config | rate limiting config |
| CREATE | N05_operations/P09_config/cost_budget_n05.md | cost_budget | operation cost budget |
| CREATE | N05_operations/P09_config/usage_quota_n05.md | usage_quota | usage quota config |
| CREATE | N05_operations/P07_evals/e2e_eval_n05.md | e2e_eval | end-to-end eval suite |
| CREATE | N05_operations/P07_evals/trace_config_n05.md | trace_config | observability tracing |
| CREATE | N05_operations/P07_evals/eval_framework_n05.md | eval_framework | N05 eval framework |
| CREATE | N05_operations/P04_tools/daemon_n05.md | daemon | background ops daemon |
| CREATE | N05_operations/P04_tools/hook_config_n05.md | hook_config | CI/CD hook config |
| CREATE | N05_operations/P11_feedback/threat_model_n05.md | threat_model | security threat model |
| CREATE | N05_operations/P11_feedback/self_improvement_loop_n05.md | self_improvement_loop | N05 evolution protocol |
| CREATE | N05_operations/P12_orchestration/workflow_deploy_pipeline.md | workflow | deploy pipeline workflow |
| CREATE | N05_operations/P01_knowledge/kc_operations_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N05_operations/P08_architecture/supervisor_n05.md | supervisor | ops supervisor config |

**N06 Commercial -- 17 artifacts minimum:**
| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N06_commercial/P06_schema/input_schema_checkout.md | input_schema | checkout flow contract |
| CREATE | N06_commercial/P06_schema/api_reference_stripe.md | api_reference | Stripe API reference |
| CREATE | N06_commercial/P06_schema/enum_def_pricing_tiers.md | enum_def | pricing tier enumeration |
| CREATE | N06_commercial/P11_feedback/subscription_tier_n06.md | subscription_tier | tier architecture |
| CREATE | N06_commercial/P11_feedback/roi_calculator_n06.md | roi_calculator | ROI calculator |
| CREATE | N06_commercial/P11_feedback/referral_program_n06.md | referral_program | referral mechanics |
| CREATE | N06_commercial/P11_feedback/self_improvement_loop_n06.md | self_improvement_loop | N06 evolution protocol |
| CREATE | N06_commercial/P11_feedback/churn_prevention_playbook_n06.md | churn_prevention_playbook | retention playbook |
| CREATE | N06_commercial/P03_prompt/sales_playbook_n06.md | sales_playbook | sales conversation SP |
| CREATE | N06_commercial/P03_prompt/discovery_questions_n06.md | discovery_questions | sales discovery Qs |
| CREATE | N06_commercial/P10_memory/entity_memory_customer.md | entity_memory | customer entity memory |
| CREATE | N06_commercial/P10_memory/procedural_memory_n06.md | procedural_memory | commercial procedures |
| CREATE | N06_commercial/P01_knowledge/kc_commercial_vocabulary.md | knowledge_card | seed words planted |
| CREATE | N06_commercial/P07_evals/eval_metric_conversion.md | eval_metric | conversion metrics |
| CREATE | N06_commercial/P12_orchestration/renewal_workflow_n06.md | renewal_workflow | renewal automation |
| CREATE | N06_commercial/P12_orchestration/workflow_revenue_loop.md | workflow | revenue flywheel workflow |
| CREATE | N06_commercial/P05_output/expansion_play_n06.md | expansion_play | upsell/expansion plays |

### Wave 2: Consolidation (N07)

| Action | Path | Kind | Notes |
|--------|------|------|-------|
| RUN | python _tools/cex_evolve.py sweep --target 9.0 | -- | auto-improve new artifacts |
| RUN | python _tools/cex_doctor.py | -- | full health check |
| RUN | python _tools/cex_compile.py --all | -- | compile all .md -> .yaml |
| COMMIT | "[N07] SELF_ASSEMBLY: consolidate 98+ artifacts across N01-N06" | -- | final commit |

---

## DECISIONS (Autonomous -- no GDP needed)

This spec involves NO subjective user decisions. Every choice is architecturally determined:

| Decision | Authority | Rationale |
|----------|-----------|-----------|
| Which kinds per nucleus | N07 (this spec) | Sin lens + pillar priority + combo-completeness |
| P06 first in wave 1 | N07 (this spec) | Universal gap, blocks dynamic portfolio assembly |
| self_improvement_loop in all | N07 (this spec) | Every nucleus must be able to evolve itself |
| Seed words per nucleus | N07 (this spec) | Domain vocabulary is architecturally determined |
| Opus + high effort | User decision | Autonomous builds require max quality |

Each nucleus has FREEDOM to:
- Add MORE artifacts beyond the minimum list (use your sin lens to decide)
- Build additional combos they identify as valuable
- Self-assimilate external patterns into their domain
- Exceed targets where it increases deck quality

---

## HANDOFF TEMPLATE (per nucleus)

Each handoff includes this mandatory section:

```markdown
## YOUR DECK ARCHETYPE

Sin Lens: {sin_lens}
Primary Pillars: {primary}
Combos to Complete: {combos}
P06 target: {p06_target} artifacts (currently 0)

## YOUR FREEDOM

You have Opus + high effort. Use ALL of it.
This is not a checklist -- it is a SEED.

After building the minimum list:
1. Scan your entire nucleus directory
2. Identify what a senior {role} would EXPECT to find here
3. Build what's missing using your sin lens as the selection filter
4. Plant your vocabulary KC last -- let it reflect everything you built

The goal: when N07 dispatches you on a future task, your deck is ready.
You should NEVER need to ask "what builder do I use?" -- your P01 should have it.
You should NEVER need to improvise a schema -- your P06 should have it.
You should NEVER ship unvalidated -- your P07 should catch it.

## SELF-ASSEMBLY LOOP (run this)

1. python _tools/cex_doctor.py (audit current state)
2. For each combo in your deck archetype (P06 combos first):
   - Load: archetypes/builders/{kind}-builder/
   - Run: 8F pipeline
   - Save: N0X_{domain}/P{xx}/{kind}_{domain}.md
   - Compile: python _tools/cex_compile.py {path}
3. Build vocabulary KC: N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md
4. Compile all: python _tools/cex_compile.py --all
5. Signal: python -c "from _tools.signal_writer import write_signal; write_signal('{n}', 'complete', score)"
```

---

## ACCEPTANCE CRITERIA

```
- [ ] P06 count per nucleus >= 5 (currently 0 for all)
- [ ] P11 count per nucleus >= 8 (currently 2-5 for all)
- [ ] Each nucleus has >= 1 self_improvement_loop artifact
- [ ] Each nucleus has vocabulary KC in P01 with >= 15 seed words
- [ ] All 5 combos per nucleus have >= 3/4 pieces present
- [ ] 0 FAIL in cex_doctor.py after consolidation
- [ ] All new artifacts pass cex_compile.py without error
- [ ] quality >= null (peer-review assigns; no self-scoring)
- [ ] N07 consolidation commit lands with >= 98 new artifacts
- [ ] Dynamic Portfolio Assembly triggered on >= 1 test task per nucleus
```

---

## PROPERTIES

| Property | Value |
|----------|-------|
| Total artifacts to create | 98 minimum (16-18 per nucleus) |
| Wave count | 3 (W0 N07, W1 parallel, W2 consolidate) |
| Execution time (estimate) | 90-120 min |
| Model | Opus + high effort per nucleus |
| Quality target | 9.0+ per artifact |
| Blocking gate | P06 coverage >= 5 per nucleus before W2 |
| Self-extension | enabled after W1 complete |
| Seed words total | ~90 (15 per nucleus) |
