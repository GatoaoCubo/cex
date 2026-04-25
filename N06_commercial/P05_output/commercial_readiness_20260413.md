---
id: commercial_readiness_20260413
kind: content_monetization
8f: F6_produce
pillar: P11
title: CEX commercial readiness assessment (post Wave 2)
version: 1.0.0
quality: 8.9
tags: [commercial, tiers, roadmap, pricing, gtm]
created: 2026-04-13
nucleus: n06
mission: POLISH_WAVE2
related:
  - commercial_readiness_20260414
  - commercial_readiness_20260414b
  - spec_mission_100pct_coverage
  - p06_schema_taxonomy
  - n06_intent_resolution_depth_spec
  - kc_llm_vocabulary_atlas
  - cex_llm_vocabulary_whitepaper
  - commercial_readiness_20260414c
  - n06_report_intent_resolution_moat
  - bld_architecture_agentic_rag
---

# Commercial Readiness -- 2026-04-13

## Current State

| Metric | Value | Source |
|--------|-------|--------|
| Total kinds in registry | 184 | .cex/kinds_meta.json |
| Pillars | 12 (P01-P12) | kinds_meta.json |
| Wave 2 adds (voice + code-agent) | 12 builders complete | wave2_quality_report.md |
| Wave 3 adds (eval + RAG + memory + prompt + workflow) | 18 (registered, builders pending) | plan_wave3_v2.md |
| Wave 2 mean ISO quality | 8.96 (median 9.0) | wave2_quality_report.md |
| Wave 2 compilation failures | 0 | wave2_quality_report.md |
| Builders with 100% ISOs | 11 / 12 Wave 2 | agent-computer-interface partial |

**Note**: kinds_meta.json registers all 300 kinds including Wave 3 pre-registrations.
Wave 3 builders are NOT yet built -- schema exists, 8F pipeline does not.

## Pricing Tier Map

### FREE (attract -- low barrier, high adoption)

Target: developers discovering CEX, evaluators, open-source contributors.
Conversion hook: free tier creates artifacts that reference PRO kinds.

| Kind | Pillar | Why Free | Conversion Hook |
|------|--------|----------|-----------------|
| knowledge_card | P01 | Universal building block | Hits embedding_config limit at scale |
| agent | P02 | Core concept, everyone needs one | agent_package + agent_profile are PRO |
| workflow | P12 | Visual logic gateway | workflow_node + dag are PRO |
| prompt_template | P03 | Lowest-friction entry | prompt_optimizer is PRO |
| system_prompt | P03 | Every chatbot starts here | chain + context_window_config are PRO |
| agent_card | P08 | Self-service onboarding | supervisor + component_map are PRO |
| instruction | P03 | Basic behavior spec | planning_strategy is PRO |
| glossary_entry | P01 | Documentation starter | ontology + knowledge_graph are PRO |
| context_doc | P01 | Simple RAG foundation | rag_source + vector_store are PRO |
| function_def | P04 | Single-tool definition | toolkit + mcp_server are PRO |
| cli_tool | P04 | Developer on-ramp | browser_tool + computer_use are PRO |
| diagram | P08 | Comms artifact | component_map is PRO |
| tagline | P03 | Brand copy hook | landing_page + content_monetization PRO |
| glossary_entry | P01 | Terminology management | ontology is PRO |
| golden_test | P07 | Basic quality check | benchmark_suite + eval_framework PRO |
| signal | P12 | Inter-agent messaging | dispatch_rule + dag are PRO |
| handoff | P12 | Task passing | handoff_protocol is PRO |
| unit_eval | P07 | Single-function test | e2e_eval + trajectory_eval ENTERPRISE |

### PRO (convert -- serious builders, production use)

Target: teams shipping AI products, agency builders, startup CTOs.
Price point: $49-149/mo individual, $299-799/mo team (5 seats).

| Kind | Pillar | Value Prop | Anchor Feature |
|------|--------|-----------|----------------|
| voice_pipeline | P04 | End-to-end voice AI blueprint | Full STT+VAD+TTS+prosody stack |
| realtime_session | P09 | WebRTC/WebSocket session config | Latency-optimized streaming |
| repo_map | P01 | Codebase intelligence layer | Full codebase context injection |
| diff_strategy | P04 | Code-agent edit precision | SEARCH/REPLACE + unified diff modes |
| edit_format | P06 | Agentic code edit contracts | Format compliance for multi-agent |
| sandbox_config | P09 | Safe code execution environment | Container + resource isolation |
| prompt_optimizer | P03 | DSPy-style prompt tuning | Auto-improve with eval feedback |
| prompt_technique | P03 | CoT / ReAct / ToT library | Technique selection per task |
| reasoning_strategy | P03 | Chain-of-thought orchestration | Multi-step decision trees |
| agentic_rag | P01 | Self-correcting retrieval | Corrective RAG + Self-RAG |
| reranker_config | P01 | Cross-encoder precision boost | Cohere Rerank / ColBERT |
| graph_rag_config | P01 | Entity-relationship retrieval | MS GraphRAG patterns |
| embedding_config | P01 | Vector embedding pipeline | Multi-model embedding routing |
| vector_store | P01 | Semantic search backend | Pinecone / Weaviate / Qdrant |
| rag_source | P01 | Document ingestion pipeline | Multi-format loader + chunker |
| benchmark | P07 | Performance measurement | Automated regression detection |
| benchmark_suite | P07 | Multi-metric evaluation | HELM / BIG-Bench patterns |
| scoring_rubric | P07 | Custom quality criteria | LLM-as-judge integration |
| llm_judge | P07 | AI-powered evaluation | MT-Bench / Chatbot Arena patterns |
| quality_gate | P11 | Automated quality enforcement | Block bad artifacts pre-commit |
| eval_dataset | P07 | Test case library | Golden dataset management |
| eval_framework | P07 | Evaluation orchestration | Eleuther / OpenAI Evals compat |
| eval_metric | P07 | BLEU / ROUGE / NDCG | Standardized metric library |
| workflow_node | P12 | LangGraph-compatible nodes | Visual pipeline composition |
| dag | P12 | Dependency graph execution | Topological sort + parallelism |
| dispatch_rule | P12 | Agent routing logic | Multi-nucleus orchestration |
| spawn_config | P12 | Agent launch parameters | Session-aware process management |
| memory_architecture | P10 | Agent memory design | MemGPT / Letta patterns |
| procedural_memory | P10 | Skill library management | Procedural task storage |
| knowledge_index | P10 | Searchable knowledge base | TF-IDF + semantic hybrid |
| model_provider | P02 | Multi-LLM routing | OpenAI / Anthropic / Gemini |
| fallback_chain | P02 | Provider resilience | Automatic failover chain |
| router | P02 | Budget-optimized routing | Cost vs. quality tradeoff |
| agent_package | P02 | Deployable agent bundle | Versioned agent distribution |
| agent_profile | P02 | Agent capability manifest | Skills + constraints + budget |
| mcp_server | P04 | Model Context Protocol server | Tool ecosystem integration |
| browser_tool | P04 | Web automation capability | Playwright/Puppeteer patterns |
| computer_use | P04 | Desktop automation | Screen + keyboard + mouse |
| research_pipeline | P04 | Deep research automation | Multi-source synthesis |
| content_monetization | P11 | Revenue model builder | Tier + funnel + pricing |
| landing_page | P05 | Conversion-optimized page | A/B copy variants baked in |
| multimodal_prompt | P03 | Vision + text prompts | GPT-4V / Claude 3 patterns |
| visual_workflow | P12 | Mermaid workflow diagrams | LangGraph visual export |
| prompt_version | P03 | Prompt change management | Version diff + rollback |

### ENTERPRISE (retain + expand -- compliance, scale, governance)

Target: regulated industries (fintech, health, legal), large teams (50+ seats), MLOps orgs.
Price point: $2,500-15,000/mo. ACV $30K-$180K.

| Kind | Pillar | Compliance/Scale Feature | ACV Lift |
|------|--------|--------------------------|----------|
| red_team_eval | P07 | Adversarial attack simulation | High -- SOC2/ISO27001 gate |
| guardrail | P11 | Input/output safety enforcement | High -- regulatory requirement |
| safety_policy | P11 | AI governance framework | High -- board-level compliance |
| compliance_framework | P11 | Regulatory mapping (GDPR, HIPAA) | Very High -- legal requirement |
| bias_audit | P07 | Fairness + disparate impact | High -- EU AI Act gate |
| threat_model | P11 | Attack surface analysis | High -- security review requirement |
| model_registry | P10 | Versioned model governance | Medium-High -- MLOps maturity |
| model_card | P02 | Model documentation standard | Medium -- responsible AI signal |
| dataset_card | P01 | Training data provenance | Medium -- EU AI Act documentation |
| finetune_config | P02 | Custom model training | High -- proprietary model differentiation |
| training_method | P02 | Learning algorithm spec | High -- R&D investment signal |
| rl_algorithm | P02 | Reinforcement learning config | Medium -- advanced ML teams |
| trajectory_eval | P07 | Agent behavior auditing | High -- agent governance |
| memory_benchmark | P07 | Memory system performance | Medium -- scale readiness |
| consolidation_policy | P10 | Memory decay + pruning governance | Medium -- data retention compliance |
| self_improvement_loop | P11 | Autonomous quality improvement | High -- competitive differentiation |
| incident_report | P11 | AI failure post-mortem | Medium -- ITSM integration |
| hitl_config | P11 | Human-in-the-loop checkpoints | High -- healthcare/legal gate |
| permission | P09 | RBAC capability control | Medium -- enterprise security |
| secret_config | P09 | Credential management | Medium -- SOC2 requirement |
| rate_limit_config | P09 | API quota governance | Medium -- multi-tenant isolation |
| cost_budget | P09 | LLM spend governance | High -- CFO requirement |
| content_filter | P11 | Output moderation pipeline | High -- platform compliance |
| supervisor | P08 | Multi-agent oversight | High -- control plane for fleets |
| dual_loop_architecture | P08 | Fast/slow reasoning governance | Medium -- reliability engineering |
| agent_computer_interface | P08 | Human-computer interaction spec | Medium -- accessibility + safety |
| memory_scope | P02 | Context isolation enforcement | Medium -- multi-tenant data separation |

## Anchor Kinds (top 10)

The 10 kinds that drive tier adoption and unlock upsell conversations:

| # | Kind | Tier | Why It Anchors |
|---|------|------|----------------|
| 1 | knowledge_card | FREE | Universal entry point -- every user creates one first |
| 2 | agent | FREE->PRO | Core primitive -- agent_package and agent_profile upsell is natural |
| 3 | voice_pipeline | PRO | High perceived value -- demo-able in 60s, 7 sub-kinds bundled |
| 4 | guardrail | ENTERPRISE | Compliance trigger -- legal/security teams mandate this |
| 5 | red_team_eval | ENTERPRISE | Security gate -- SOC2/ISO27001 requires adversarial testing |
| 6 | agentic_rag | PRO | RAG upgrade story -- outperforms naive RAG measurably |
| 7 | prompt_optimizer | PRO | DSPy-style magic -- non-technical buyers see ROI immediately |
| 8 | model_registry | ENTERPRISE | MLOps maturity signal -- model governance is CFO/CISO concern |
| 9 | self_improvement_loop | ENTERPRISE | Competitive moat -- "AI that improves itself" is a sales story |
| 10 | cost_budget | ENTERPRISE | CFO hook -- LLM spend governance is mandatory at scale |

**Why these 10**: They cover all 3 tiers, span 6 different pillars (P01/P02/P04/P07/P10/P11),
and address 4 buyer personas (developer, practitioner, security, finance).
Each has a clear narrative that works in a 30-second sales call.

## Missing Kinds (revenue opportunities)

5 kinds NOT in Wave 1/2/3 that would unlock new pricing tiers or new buyer segments:

| # | Kind | Tier Unlocked | Revenue Impact | Build Effort |
|---|------|---------------|----------------|--------------|
| 1 | ab_test_config | PRO | Conversion optimization tools are $50-200/mo category | LOW -- P09 config pattern, well-documented |
| 2 | course_module | PRO | EdTech/L&D market -- $8B TAM. AI course builder is differentiated | MEDIUM -- P03+P05 hybrid, no precedent in codebase |
| 3 | subscription_tier | P11 | Monetization-as-code -- builders can generate their own pricing page | LOW -- content_monetization extension, 80% reuse |
| 4 | user_journey | P08 | UX/product teams as new buyer persona -- bridge dev + PM | MEDIUM -- P08 architecture pattern, Miro/FigJam analogy |
| 5 | compliance_checklist | P11 | Audit-ready documentation -- law firm + compliance consultant market | LOW -- P07 scoring pattern applied to regulatory requirements |

**ROI summary**:
- `ab_test_config`: 2-week build, unlocks growth/marketing buyers ($50/mo avg)
- `course_module`: 4-week build, unlocks EdTech vertical (highest LTV segment)
- `subscription_tier`: 1-week build, makes N06 self-referential (CEX prices itself)
- `user_journey`: 3-week build, opens PM/design buyer persona (new ICP)
- `compliance_checklist`: 1-week build, fast ENTERPRISE upsell for existing customers

## Wave 4 Recommendation

Based on gap analysis, next 10-18 kinds should focus on: **Commercial + Growth + Multi-tenant**

Wave 4 rationale:
1. Waves 1-3 cover AI infrastructure (knowledge, agents, prompts, eval, memory, workflows)
2. Revenue-generating kinds are underrepresented: only 1 commercial kind (content_monetization)
3. Enterprise multi-tenancy is missing: no RBAC policy builder, no audit log, no usage report
4. Growth/PLG tooling is absent: no A/B testing, no funnel analytics, no cohort analysis

Suggested Wave 4 kinds (18):

| # | Kind | Domain | Tier | Rationale |
|---|------|--------|------|-----------|
| 1 | ab_test_config | Growth | PRO | Conversion optimization |
| 2 | course_module | EdTech | PRO | New vertical, high LTV |
| 3 | subscription_tier | Monetization | PRO | Self-referential pricing |
| 4 | user_journey | UX/Product | PRO | Opens PM buyer persona |
| 5 | compliance_checklist | Compliance | ENTERPRISE | Audit-ready docs |
| 6 | usage_report | Analytics | ENTERPRISE | CFO visibility |
| 7 | rbac_policy | Security | ENTERPRISE | Multi-tenant isolation |
| 8 | audit_log | Compliance | ENTERPRISE | SOC2 Type II gate |
| 9 | onboarding_flow | PLG | PRO | Activation optimization |
| 10 | pricing_page | Monetization | PRO | CEX builds its own pricing |
| 11 | cohort_analysis | Analytics | PRO | Retention measurement |
| 12 | referral_program | Growth | PRO | Viral coefficient design |
| 13 | enterprise_sla | Legal | ENTERPRISE | Contract-ready templates |
| 14 | data_residency | Compliance | ENTERPRISE | GDPR + EU AI Act |
| 15 | sso_config | Security | ENTERPRISE | Identity provider integration |
| 16 | white_label_config | Platform | ENTERPRISE | Reseller + OEM tier |
| 17 | usage_quota | Platform | PRO | Fair-use enforcement |
| 18 | customer_segment | Marketing | PRO | ICP definition artifact |

Wave 4 thesis: once the AI infrastructure is solid (Waves 1-3), CEX must monetize itself.
A system that builds pricing models should have exemplary pricing. Wave 4 makes N06 the
most valuable nucleus commercially.

## Go-to-Market Readiness

| Dimension | Status | Score | Blocker |
|-----------|--------|-------|---------|
| Taxonomy completeness | Wave 1-3 = 300 kinds; Wave 4 draft ready | 75% | 18 Wave 4 commercial/compliance kinds missing |
| Quality baseline | Wave 2 mean 8.96, median 9.0, 0 compilation failures | 90% | agent-computer-interface-builder partial (7 ISOs) |
| Developer docs | KCs present per kind; no public-facing docs site | 40% | No developer portal, no quickstart guide |
| Pricing page | No CEX pricing page exists | 5% | No subscription_tier kind, no landing_page built |
| Enterprise features | guardrail + safety_policy + compliance_framework + enterprise_sla + white_label_config + usage_report builders complete | 38% | Wave 4 adds 3 ENTERPRISE builders (9.2/10 each): SLA, white-label, usage reporting |
| Demo assets | No working demo, no sandbox, no playground | 10% | Requires code deployment (N05 scope) |
| Sales enablement | No pitch deck, no case studies, no ROI calculator | 5% | N02 + N06 must co-build this |
| Open source story | Repo exists; no README-driven docs | 25% | No CONTRIBUTING.md, no example gallery |

**Overall GTM readiness: 36%**

Critical path to 80% readiness:
1. Complete Wave 3 (18 builders) -- unlocks eval + memory + RAG story
2. Build agent-computer-interface-builder (7 missing ISOs)
3. Generate developer docs from existing KCs (N04 + N02 task)
4. Build landing_page artifact for CEX itself (N02 task)
5. Build pricing page using content_monetization + subscription_tier (N06 task)
6. Create 3 demo workflows showing FREE -> PRO -> ENTERPRISE upgrade path

## Revenue Model Recommendation

| Model | Fit | Monthly ARPU | Notes |
|-------|-----|-------------|-------|
| Usage-based (per artifact built) | LOW | $15-30 | Hard to predict for users |
| Seat-based (per developer) | MEDIUM | $49-149 | Simple, predictable |
| Tier-based (FREE/PRO/ENTERPRISE) | HIGH | $0/$99/$2,500 | Aligns with kind complexity |
| API calls (programmatic access) | HIGH | $0.01-0.10/call | Complements tier model |
| Training data license | ENTERPRISE | $10K-100K one-time | 300 kinds x 13 ISOs = 2,392 premium examples |

**Recommended**: Tier-based + API overage. The 3-tier map above is not just a pricing guide --
it IS the go-to-market structure. FREE onboards, PRO converts, ENTERPRISE retains and expands.

Training data licensing is the highest-margin play: 2,392 high-quality ISOs averaging
8.96 quality score is a premium fine-tuning dataset for enterprise AI teams. This alone
justifies ENTERPRISE tier pricing.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[commercial_readiness_20260414]] | sibling | 0.53 |
| [[commercial_readiness_20260414b]] | sibling | 0.42 |
| [[spec_mission_100pct_coverage]] | upstream | 0.32 |
| [[p06_schema_taxonomy]] | upstream | 0.30 |
| [[n06_intent_resolution_depth_spec]] | sibling | 0.29 |
| [[kc_llm_vocabulary_atlas]] | upstream | 0.26 |
| [[cex_llm_vocabulary_whitepaper]] | upstream | 0.26 |
| [[commercial_readiness_20260414c]] | sibling | 0.24 |
| [[n06_report_intent_resolution_moat]] | sibling | 0.22 |
| [[bld_architecture_agentic_rag]] | upstream | 0.22 |
