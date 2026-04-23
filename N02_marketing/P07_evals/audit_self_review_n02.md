---
quality: 8.3
quality: 7.9
id: audit_self_review_n02
kind: audit_report
pillar: P07
nucleus: n02
mission: SELF_AUDIT
title: "N02 Marketing Self-Audit: Output Kinds, 8F, Brand, Collaboration"
version: 1.0.0
tags: [self-audit, marketing, output, brand, 8f, collaboration]
created: 2026-04-18
density_score: 0.91
related:
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - p06_schema_a11y_checklist
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_context_window_config
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_knowledge_card_vision_tool
updated: "2026-04-22"
---

# N02 Marketing Self-Audit: Output Kinds, 8F, Brand, Collaboration

## P03 + P05 Coverage Matrix

### P03 Prompt (21 kinds)

| Kind | Builder Exists | KC Exists | N02 Artifact Exists | Gap |
|------|:-:|:-:|:-:|-----|
| action_prompt | NO | YES | YES (2) | Builder missing -- low priority (N02 has working instances) |
| chain | YES | YES | NO | No chain artifact in N02 -- medium gap (campaign multi-step) |
| churn_prevention_playbook | NO | YES | NO | CRITICAL -- N02 is primary owner, no builder and no instance |
| constraint_spec | NO | YES | NO | Low gap -- N03 domain; N02 rarely authors constraints |
| context_file | NO | YES | NO | Low gap -- N03 domain |
| context_window_config | NO | YES | NO | Low gap -- N05 domain |
| expansion_play | NO | YES | NO | HIGH -- N02 owns expansion copy (upsell plays); no builder, no artifact |
| instruction | YES | YES | NO | Medium -- N02 has brand voice instructions but no typed instruction artifact |
| multimodal_prompt | NO | YES | YES (1) | Builder missing but N02 already has instance; upgrade needed |
| planning_strategy | NO | YES | NO | Medium -- campaign planning strategy not formalized |
| prompt_compiler | NO | YES | NO | Low gap -- N07/N03 domain |
| prompt_optimizer | NO | YES | NO | Medium -- N02 should own copy-optimization prompts |
| prompt_technique | NO | YES | NO | Low gap -- cross-nucleus utility |
| prompt_template | NO | YES | YES (4) | Builder missing -- HIGH impact; N02 is heaviest prompt_template user |
| prompt_version | NO | YES | NO | Medium -- no versioned copy variants tracked |
| reasoning_strategy | NO | YES | NO | Low gap -- N01 domain |
| reasoning_trace | NO | YES | NO | Low gap -- N01 domain |
| sales_playbook | NO | YES | NO | HIGH -- N02+N06 joint domain; zero coverage |
| system_prompt | NO | YES | YES (2) | Builder missing; N02 has instances but uses ad-hoc frontmatter |
| tagline | YES | YES | NO | Builder exists but N02 has no canonical tagline artifact |
| webinar_script | NO | YES | NO | HIGH -- content marketing staple; zero coverage in N02 |

**P03 Summary**: 21 kinds -- 3 builders (chain, instruction, tagline), 18 missing builders. N02 has active instances in: action_prompt, multimodal_prompt, prompt_template, system_prompt. Builders needed urgently: prompt_template, churn_prevention_playbook, sales_playbook, webinar_script.

### P05 Output (23 kinds)

| Kind | Builder Exists | KC Exists | N02 Artifact Exists | Gap |
|------|:-:|:-:|:-:|-----|
| analyst_briefing | NO | YES | NO | Medium -- N01/N02 joint; campaign performance briefs missing |
| app_directory_entry | NO | YES | NO | Low gap -- N05/N06 domain |
| case_study | NO | YES | YES (1) | Builder missing; N02 has one case study draft |
| code_of_conduct | NO | YES | NO | Low gap -- N04 domain |
| contributor_guide | NO | YES | NO | Low gap -- N04 domain |
| course_module | NO | YES | NO | HIGH -- edtech/content marketing; N02+N04 joint; zero coverage |
| formatter | YES | YES | NO | Builder exists; N02 has no output formatter for copy delivery |
| github_issue_template | NO | YES | NO | Low gap -- N05 domain |
| integration_guide | NO | YES | NO | Low gap -- N05 domain |
| interactive_demo | NO | YES | NO | HIGH -- landing page interactive demos are N02 domain; zero coverage |
| landing_page | NO | YES | YES (3) | Builder missing -- CRITICAL; landing_page is N02 primary output |
| onboarding_flow | NO | YES | NO | HIGH -- onboarding copy is pure N02; no builder, no artifact |
| output_validator | NO | YES | NO | Medium -- output quality check for copy missing |
| parser | YES | YES | NO | Builder exists; N02 has no copy-parsing artifact |
| partner_listing | NO | YES | NO | Medium -- partnership copy (N02+N06 joint) |
| pitch_deck | NO | YES | NO | HIGH -- sales pitch decks are core N02 output; zero coverage |
| press_release | NO | YES | NO | HIGH -- PR copy is N02 domain; zero coverage |
| pricing_page | NO | YES | NO | HIGH -- pricing copy is N02+N06 joint primary output |
| product_tour | NO | YES | NO | HIGH -- product tour scripts; N02 primary; zero coverage |
| quickstart_guide | NO | YES | NO | Medium -- N02+N04 joint; zero coverage |
| response_format | NO | YES | NO | Low gap -- N03 domain |
| streaming_config | NO | YES | NO | Low gap -- N05 domain |
| user_journey | NO | YES | YES (1) | Builder missing; N02 has one instance |

**P05 Summary**: 23 kinds -- 3 builders (formatter, parser, and landing_page builder is absent despite being N02's primary output kind). N02 has instances in: landing_page, user_journey, case_study. Critical missing builders: landing_page, pitch_deck, press_release, pricing_page, product_tour, onboarding_flow, interactive_demo.

## 8F Wiring Status

| Function | Wired? | Where | Gap |
|----------|:------:|-------|-----|
| F1 CONSTRAIN | PARTIAL | `rules/n02-marketing.md` references 8F but no explicit kind resolution map for P03+P05 | N02 lacks a local intent-resolution table; relies fully on N07 transmutation |
| F2 BECOME | YES | `P08_architecture/nucleus_def_n02.md` defines sin lens (Creative Lust), role, domain | Missing: explicit builder ISO loading step in rules |
| F2b SPEAK | YES | `P01_knowledge/kc_marketing_vocabulary.md` exists | Not referenced in boot/rules as mandatory F2b; optional in practice |
| F3 INJECT | PARTIAL | `P01_knowledge/` has 13 KCs (campaign, color theory, typography, etc.) | No explicit F3 injection protocol for brand_config.yaml |
| F3b PERSIST | NO | No entity_memory or learning_record artifacts in N02 | Session learnings not persisted; knowledge stays ephemeral |
| F4 REASON | PARTIAL | `P12_orchestration/workflow_campaign_pipeline.md` exists | GDP/manifest flow not documented for N02 specifically |
| F5 CALL | YES | `P04_tools/` has: copy_analyzer.md, headline_scorer.md, social_publisher_n02.md | content_filter wired; cex_retriever not explicitly referenced |
| F6 PRODUCE | YES | `P05_output/` has 20+ output artifacts including templates | Missing: canonical output schema for ad copy variants (A/B format) |
| F7 GOVERN | PARTIAL | rules/n02-marketing.md mentions quality: null | No N02-specific scoring rubric or quality gate artifact |
| F7b LEARN | NO | No reward_signal or regression_check artifacts in N02 | Copy performance feedback loop not formalized |
| F8 COLLABORATE | PARTIAL | `P12_orchestration/cross_nucleus_handoffs.md` covers N01->N02, N02->N05, N02->N06 | No signal_writer call in rules; relies on N07 consolidation |

**8F Summary**: F2, F5, F6 are solid. F1, F3, F4, F7, F8 are partial. F3b and F7b are entirely absent -- N02 accumulates no learning across sessions.

## Collaboration Map

| Nucleus | Direction | Trigger | Artifact Type | Formalized? |
|---------|-----------|---------|---------------|:-----------:|
| N01 Intelligence | N01 -> N02 | N01 completes market research / competitive analysis | research brief -> copy brief | YES -- cross_nucleus_handoffs.md |
| N01 Intelligence | N02 -> N01 | N02 needs audience data, trend analysis | campaign research request | PARTIAL -- dispatch rule exists, no typed handoff |
| N03 Engineering | N02 -> N03 | Landing page HTML/CSS needed from N02 copy spec | landing_page (static) -> N03 build | NO -- implicit only |
| N04 Knowledge | N02 -> N04 | Campaign KCs need indexing; RAG for copy recall | knowledge_card -> N04 index | NO -- not documented |
| N04 Knowledge | N04 -> N02 | Product knowledge brief for copy grounding | KC -> N02 context injection | PARTIAL -- templates exist |
| N05 Operations | N02 -> N05 | Deploy landing page, schedule social posts | output artifact -> N05 deploy | YES -- cross_nucleus_handoffs.md |
| N06 Commercial | N02 -> N06 | Copy feeds into pricing pages, sales playbooks | ad_copy -> N06 monetization | YES -- cross_nucleus_handoffs.md |
| N06 Commercial | N06 -> N02 | Pricing signals inform copy angles (value prop) | monetization_plan -> N02 brief | PARTIAL -- dispatch_rule exists |
| N07 Orchestrator | N07 -> N02 | Mission dispatch via handoff | n02_task.md | YES -- this session |

**Collaboration Summary**: N01->N02 and N02->N06 are the best-documented flows. N02->N03 (copy-to-build) and N02->N04 (copy-to-knowledge) are undocumented gaps. Four of nine collaboration directions have no formal artifact.

## Top 5 Creative Gaps

1. **No landing_page builder** (Severity: CRITICAL)
   Landing page is N02's single highest-impact output kind. N02 has 3 template instances but no builder with 13 ISOs. Every landing page produced by N02 is unstructured relative to 8F expectations. Without a builder, copy quality cannot be governed by F7. File needed: `archetypes/builders/landing-page-builder/`.

2. **No pitch_deck or press_release builder** (Severity: HIGH)
   Pitch decks (investor / sales) and press releases are canonical marketing outputs. Zero coverage in N02 -- no builder, no artifact, no KC instantiation. These are P05 kinds owned by N02 that have been entirely skipped. Files needed: `archetypes/builders/pitch-deck-builder/`, `archetypes/builders/press-release-builder/`.

3. **No F3b/F7b learning loop** (Severity: HIGH)
   N02 produces copy but never learns from it. No reward_signal, no regression_check, no learning_record exists in N02. Each campaign starts from scratch. A `learning_record` for copy performance (CTR, conversion, A/B winners) would compound creative quality over time. Files needed: `N02_marketing/P11_feedback/learning_record_n02_copy.md`, `N02_marketing/P11_feedback/reward_signal_n02.md`.

4. **No churn_prevention_playbook or sales_playbook** (Severity: HIGH)
   N02 owns P03 and is the natural author of sales playbooks and churn-prevention copy. These are high-business-value kinds that map directly to N06 commercial outcomes. Both kinds have KCs but zero N02 instances. Files needed: `N02_marketing/P03_prompt/churn_prevention_playbook_n02.md`, `N02_marketing/P03_prompt/sales_playbook_n02.md`.

5. **No onboarding_flow, product_tour, or interactive_demo** (Severity: HIGH)
   Three P05 output kinds that belong squarely in N02 (product marketing copy) have zero coverage: onboarding flows, product tours, and interactive demo scripts. These are the top-of-funnel activation layer -- the most conversion-critical copy after landing pages. Files needed: `N02_marketing/P05_output/onboarding_flow_n02.md`, `N02_marketing/P05_output/product_tour_n02.md`, `N02_marketing/P05_output/interactive_demo_n02.md`.

## Recommendations

1. **Build `landing-page-builder` ISOs** -- 13-ISO builder for `landing_page` kind (P05). N02 already has 3 template instances that can serve as `bld_examples`. Priority: P0. Path: `archetypes/builders/landing-page-builder/`. Dispatch to N03.

2. **Create F7b learning artifacts** -- Add `learning_record_n02_copy.md` (P11) and `reward_signal_n02.md` (P11) to `N02_marketing/P11_feedback/`. Wire F7b LEARN into `rules/n02-marketing.md` as a mandatory post-produce step. This closes the feedback loop that makes copy compound over sessions.

3. **Author missing P05 artifacts in one sprint** -- Produce: `pitch_deck_n02.md`, `press_release_n02.md`, `onboarding_flow_n02.md`, `product_tour_n02.md`, `pricing_page_n02.md` under `N02_marketing/P05_output/`. Each is a typed artifact with frontmatter; N02 can author all five in a single grid wave via the existing prompt_template and system_prompt as scaffolding.

4. **Formalize N02 -> N03 collaboration** -- Add a `dispatch_rule_n02_to_n03.md` in `N02_marketing/P12_orchestration/` that defines the handoff protocol when N02 produces copy specs that require N03 to render into HTML/CSS/React components. This is the most common undocumented cross-nucleus flow.

5. **Add prompt_template-builder and sales_playbook-builder** to archetypes -- `prompt_template` is the single most-used P03 kind in N02 (4 instances, no builder). A builder would enforce frontmatter, A/B variant structure, and quality gates. `sales_playbook` is the second priority (N02+N06 joint domain). Dispatch both to N03.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_bugloop]] | downstream | 0.48 |
| [[bld_schema_quickstart_guide]] | upstream | 0.45 |
| [[bld_schema_usage_report]] | upstream | 0.45 |
| [[p06_schema_a11y_checklist]] | upstream | 0.45 |
| [[bld_schema_pitch_deck]] | upstream | 0.44 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_context_window_config]] | upstream | 0.44 |
| [[bld_schema_search_strategy]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_knowledge_card_vision_tool]] | upstream | 0.42 |
