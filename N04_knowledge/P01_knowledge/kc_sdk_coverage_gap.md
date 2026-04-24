---
id: kc_sdk_coverage_gap
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n04
domain: sdk_architecture
quality: 8.9
title: "CEX SDK Coverage Gap: P05/P08/P09 (74 Kinds)"
version: "1.0.0"
tags: [sdk, coverage_gap, P05, P08, P09, architecture]
created: "2026-04-18"
updated: "2026-04-18"
tldr: "74 kinds across P05 Output, P08 Architecture, P09 Config have zero cex_sdk module coverage. Three new SDK modules are proposed: output_sdk, architecture_sdk, config_sdk."
related:
  - assimilation_plan_agno
  - p01_kc_cex_project_overview
  - kc_llm_vocabulary_atlas
  - cex_llm_vocabulary_whitepaper
  - taxonomy_completeness_audit
  - spec_mission_100pct_coverage
  - n03_readme_technical
  - atom_03_openai_agents_sdk
  - ai2ai_exhaustive_scan_20260414
  - commercial_readiness_20260413
---

# CEX SDK Coverage Gap: P05/P08/P09

## Summary

The cex_sdk runtime (78 .py files, 4504 lines) covers 6 of 12 pillars.
Pillars P05 Output, P08 Architecture, and P09 Config have no dedicated SDK modules.
Combined gap: 74 kinds with no programmatic runtime abstraction.

## Existing SDK Coverage

| Module | Pillar | Kinds Covered | Files |
|--------|--------|---------------|-------|
| `cex_sdk/knowledge/` | P01 | chunk_strategy, embedding_config, document_loader, rag_source, retriever_config | chunking/base, chunking/fixed, chunking/markdown_chunking, chunking/recursive, document.py, embedder/base, embedder/ollama_embedder, embedder/openai_embedder, reader/base, reader/csv_reader, reader/json_reader, reader/markdown, reader/pdf, reader/web, reranker/base, reranker/cohere_reranker |
| `cex_sdk/vectordb/` | P01 | vector_store, knowledge_index | base.py, chroma.py |
| `cex_sdk/memory/` | P10 | memory_summary, entity_memory, memory_architecture | compression.py, manager.py, stores/ |
| `cex_sdk/models/` | P02 | model_provider, agent, boot_config | base.py, message.py, metrics.py, response.py, structured.py, providers/{anthropic,google,litellm,ollama,openai,openrouter} |
| `cex_sdk/tools/` | P04 | cli_tool, browser_tool, mcp_server, api_client | decorator.py, function.py, mcp/client.py, toolkit.py, builtin/{file,python,shell,web}_tools |
| `cex_sdk/eval/` | P07 | benchmark, scoring_rubric | base.py |
| `cex_sdk/guardrails/` | P11 | guardrail, content_filter | base.py, pii.py, prompt_injection.py |
| `cex_sdk/reasoning/` | P03 | chain, reasoning_strategy | step.py |
| `cex_sdk/session/` | P09 (partial) | session_state | base.py |
| `cex_sdk/tracing/` | P12 | trace_config | exporter.py |
| `cex_sdk/workflow/` | P12 | workflow, dispatch_rule, schedule | condition.py, loop.py, parallel.py, router.py, step.py, types.py, workflow.py |
| `cex_sdk/utils/` | cross | logging, timing | log.py, timer.py |

**Total covered: 78 files across P01, P02, P03, P04, P07, P10, P11, P12 (partial P09)**

## The 74-Kind Gap

### P05 Output (23 kinds -- zero SDK coverage)

| Kind | Description | Runtime Use Case |
|------|-------------|-----------------|
| analyst_briefing | Structured intelligence report | Serialize + render to PDF/HTML |
| app_directory_entry | Marketplace listing artifact | Schema validation + submission API |
| case_study | Customer success narrative | Template fill + export |
| code_of_conduct | Community governance doc | Lint + publish |
| contributor_guide | OSS onboarding doc | Template + CI gate |
| course_module | Educational unit artifact | LMS API integration |
| formatter | Output transform specification | Apply transform pipeline at runtime |
| github_issue_template | Issue template definition | .github/ write + validate |
| integration_guide | Third-party integration doc | Render + push to docs site |
| interactive_demo | Live demo configuration | Session bootstrap |
| landing_page | Marketing conversion page | HTML render + deploy |
| onboarding_flow | User activation sequence | Step runner + state machine |
| output_validator | Output validation spec | Runtime validation gate |
| parser | Structured extraction rule | Apply parser at inference time |
| partner_listing | Partner directory entry | Directory API push |
| pitch_deck | Investment/sales presentation | PPTX/PDF render |
| press_release | PR document | Distribute to wire services |
| pricing_page | Pricing tier display | Render + A/B serve |
| product_tour | Guided UX walkthrough | Tour engine bootstrap |
| quickstart_guide | Developer onboarding doc | Render + docs deploy |
| response_format | LLM output structure spec | Inject into system prompt at runtime |
| streaming_config | SSE/WebSocket output spec | Apply to inference session |
| user_journey | UX flow specification | Journey analytics + step tracking |

### P08 Architecture (14 kinds -- zero SDK coverage)

| Kind | Description | Runtime Use Case |
|------|-------------|-----------------|
| agent_card | A2A agent identity manifest | Agent discovery + capability negotiation |
| agent_computer_interface | Human-computer bridge spec | Terminal/IDE integration runtime |
| bounded_context | DDD context boundary | Service mesh boundary enforcement |
| capability_registry | Agent capability index | Crew planner query + routing |
| component_map | System component diagram | Dependency graph generation |
| context_map | DDD integration pattern map | Service integration validation |
| decision_record | Architecture decision (ADR) | ADR search + impact analysis |
| diagram | System diagram artifact | Mermaid/PlantUML render |
| dual_loop_architecture | Inner/outer learning loop spec | Training loop orchestration |
| fhir_agent_capability | Healthcare AI capability spec | FHIR compliance validation |
| invariant | System invariant assertion | Runtime invariant checker |
| naming_rule | Naming convention spec | Pre-commit lint + CI gate |
| pattern | Design/architectural pattern | Pattern matcher + code generator |
| supervisor | Multi-agent supervisor spec | Crew orchestration bootstrap |

### P09 Config (37 kinds -- zero dedicated module; only session_state partial)

| Kind | Description | Runtime Use Case |
|------|-------------|-----------------|
| alert_rule | Observability alert threshold | PromQL evaluator + notifier |
| backpressure_policy | Queue pressure control | Middleware injection |
| batch_config | Batch processing parameters | Job scheduler config load |
| canary_config | Canary release spec | Traffic splitter config |
| circuit_breaker | Fault tolerance circuit | Middleware wrapping |
| cost_budget | Token/compute spend limit | Pre-flight budget check |
| data_residency | Data geography constraint | Middleware geo-filter |
| deployment_manifest | K8s/Docker deployment spec | Deploy pipeline injection |
| effort_profile | Task complexity profile | Router difficulty scoring |
| env_config | Environment variable spec | dotenv loader + validator |
| experiment_config | ML experiment parameters | Experiment tracker bootstrap |
| feature_flag | Feature toggle spec | Flag evaluator at request time |
| kubernetes_ai_requirement | K8s AI workload spec | K8s manifest generator |
| marketplace_app_manifest | App store listing config | Marketplace API submission |
| oauth_app_config | OAuth2 client config | Auth flow bootstrap |
| path_config | File/URL path resolution | Path resolver + validator |
| permission | RBAC permission spec | Policy enforcer |
| playground_config | LLM playground parameters | Playground session init |
| prosody_config | TTS prosody parameters | Voice pipeline injection |
| quantization_config | Model quantization spec | Inference engine config |
| rate_limit_config | API rate limit policy | Rate limiter middleware |
| rbac_policy | Role-based access control | Policy engine bootstrap |
| realtime_session | WebRTC/SSE session config | Session negotiator |
| retry_policy | Retry backoff spec | HTTP client wrapping |
| runtime_rule | Nucleus execution constraint | 8F pipeline gate |
| sandbox_config | Execution sandbox spec | Sandbox launcher config |
| sandbox_spec | Detailed sandbox definition | Container spec generator |
| secret_config | Credentials management spec | Secret store client init |
| slo_definition | Service level objective | SLO evaluator + alerting |
| sso_config | SSO/SAML configuration | Identity provider bootstrap |
| terminal_backend | Remote execution backend | Terminal session launcher |
| thinking_config | Extended reasoning parameters | Inference session config |
| transport_config | Network transport spec | Client transport layer init |
| usage_quota | Consumption limit spec | Quota enforcer middleware |
| vad_config | Voice activity detection spec | Audio pipeline injection |
| white_label_config | Brand white-label spec | Theme/branding injector |
| hibernation_policy | Idle cost guard spec | Serverless scale-to-zero hook |

## Proposed SDK Modules

### output_sdk (cex_sdk/output/)

Covers all 23 P05 kinds. Core responsibilities:
- **Renderer**: kind-to-format dispatch (HTML, PPTX, PDF, PPTX, Markdown)
- **Validator**: output_validator artifact runner -- checks LLM output against spec
- **Parser**: applies parser artifact rules to raw LLM text at inference time
- **Formatter**: applies formatter artifact transform pipeline
- **Template engine**: response_format injection into system prompts

```
cex_sdk/output/
  __init__.py
  renderer/
    base.py          -- BaseRenderer ABC: render(artifact, context) -> bytes
    html.py          -- landing_page, pricing_page, onboarding_flow
    markdown.py      -- quickstart_guide, integration_guide, contributor_guide
    pptx.py          -- pitch_deck (python-pptx)
    pdf.py           -- analyst_briefing, press_release
  validator.py       -- output_validator artifact runtime (validates LLM output)
  parser.py          -- parser artifact runtime (structured extraction)
  formatter.py       -- formatter artifact runtime (output transform)
  response_format.py -- injects response_format spec into system prompt
  streaming.py       -- streaming_config -> SSE/WebSocket session params
```

**Integration point**: F6 PRODUCE calls `output_sdk.formatter.apply(artifact, raw_output)` after generation. F7 GOVERN calls `output_sdk.validator.run(artifact, output)`.

### architecture_sdk (cex_sdk/architecture/)

Covers all 14 P08 kinds. Core responsibilities:
- **Agent card registry**: agent discovery, capability matching, A2A handshake
- **Capability index**: crew planner queries for agent routing
- **Diagram renderer**: Mermaid/PlantUML compile + SVG export
- **Invariant checker**: runtime assertion of system invariants
- **Naming rule linter**: pre-commit hook integration

```
cex_sdk/architecture/
  __init__.py
  agent_card.py       -- load, validate, register, discover agent cards
  capability_index.py -- capability_registry query + routing (used by crew planner)
  diagram.py          -- Mermaid/PlantUML render -> SVG/PNG
  invariant.py        -- assert system invariants at runtime or test time
  naming_lint.py      -- naming_rule artifact -> pre-commit lint checks
  supervisor.py       -- supervisor artifact -> multi-agent crew bootstrap
  component_map.py    -- component_map -> dependency graph (networkx)
  pattern.py          -- pattern artifact -> code generation hints
```

**Integration point**: F5 CALL uses `architecture_sdk.capability_index.query(domain)` to discover relevant agents before dispatch. `agent_card.py` feeds the N07 routing table.

### config_sdk (cex_sdk/config/)

Covers all 37 P09 kinds. Core responsibilities:
- **Config loader**: env_config, secret_config artifact -> validated dict
- **Policy enforcer**: rate_limit_config, rbac_policy, retry_policy -> middleware
- **Budget guard**: cost_budget, usage_quota -> pre-flight checks
- **Feature flag evaluator**: feature_flag artifact -> runtime toggle
- **SLO tracker**: slo_definition -> metric evaluation + alerting

```
cex_sdk/config/
  __init__.py
  loader.py           -- env_config, path_config -> validated config dict
  secrets.py          -- secret_config -> secret store client (Vault, env, file)
  rate_limit.py       -- rate_limit_config artifact -> rate limiter middleware
  retry.py            -- retry_policy artifact -> httpx/aiohttp retry decorator
  circuit_breaker.py  -- circuit_breaker artifact -> resilience middleware
  feature_flag.py     -- feature_flag artifact -> flag evaluator
  budget.py           -- cost_budget, usage_quota -> pre-flight token/spend checks
  rbac.py             -- rbac_policy artifact -> permission enforcer
  slo.py              -- slo_definition artifact -> SLO evaluator + alert trigger
  sandbox.py          -- sandbox_config/sandbox_spec -> container launcher config
  thinking.py         -- thinking_config artifact -> inference session params
  transport.py        -- transport_config artifact -> HTTP client config
  deployment.py       -- deployment_manifest artifact -> K8s/Docker config dict
```

**Integration point**: F1 CONSTRAIN uses `config_sdk.loader.load(env_config_path)` to bootstrap nucleus environment. F7 GOVERN calls `config_sdk.budget.check(kind, estimated_tokens)` as pre-flight gate.

## Priority Order

1. **config_sdk** (highest value): 37 kinds, runtime-critical (env, secrets, rate limits, budget). Unblocked -- no external dependencies beyond stdlib.
2. **output_sdk** (high value): 23 kinds, closes F6/F7 integration gap. Needs: python-pptx, WeasyPrint optional.
3. **architecture_sdk** (medium value): 14 kinds. agent_card.py + capability_index.py unlock crew planning. Rest is lower urgency.

## Gap Impact on 8F

Without output_sdk/config_sdk/architecture_sdk:
- F1 CONSTRAIN: cannot validate env_config at nucleus boot
- F5 CALL: cannot query capability_registry programmatically
- F6 PRODUCE: cannot run parser/formatter/output_validator artifacts
- F7 GOVERN: cannot enforce cost_budget, rate_limit_config, slo_definition at gate

All four gap points degrade autonomous nucleus quality.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[assimilation_plan_agno]] | downstream | 0.25 |
| [[p01_kc_cex_project_overview]] | sibling | 0.23 |
| [[kc_llm_vocabulary_atlas]] | sibling | 0.23 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.22 |
| [[taxonomy_completeness_audit]] | sibling | 0.22 |
| [[spec_mission_100pct_coverage]] | downstream | 0.21 |
| [[n03_readme_technical]] | downstream | 0.20 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.19 |
| [[ai2ai_exhaustive_scan_20260414]] | sibling | 0.19 |
| [[commercial_readiness_20260413]] | downstream | 0.18 |
