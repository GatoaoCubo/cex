---
quality: 8.4
id: kc_pillar_brief_p09_config_en
kind: knowledge_card
pillar: P09
title: "P09 Config — Your AI's Nervous System"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p09, config, runtime, secrets, rate-limits, llm-engineering]
tldr: "P09 Config governs runtime behavior without changing the model — environment variables, secrets, rate limits, RBAC, thinking budgets, and sandbox specs."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p09_config_pt
  - kc_pillar_brief_p08_architecture_en
  - kc_pillar_brief_p10_memory_en
  - kc_pillar_brief_p11_feedback_en
  - n00_p09_kind_index
density_score: 0.91
updated: "2026-04-22"
---

# P09 Config — Your AI's Nervous System: Settings That Control Behavior Without Touching the Brain

---

## The Universal Principle: Behavior Lives Outside the Model

Here is a counterintuitive fact that every AI practitioner eventually learns the hard way: **most of what makes an AI system behave differently in production versus development has nothing to do with the model itself.** The weights are fixed. The architecture is fixed. What changes is the operating environment — the configuration layer that surrounds the model and controls how it runs.

P09 Config is that operating environment. The nervous system metaphor is precise: your nervous system does not change the structure of your brain when you enter a cold room or a stressful meeting — it adjusts the parameters that govern how the brain operates in that context. Elevated cortisol. Restricted blood flow. Heightened threat sensitivity. The brain runs the same underlying computations; the environment modulates the outputs.

AI systems work identically. A Claude or GPT-4 model running with a `thinking_config` set to `budget_tokens: 100` produces shallow, fast responses. The same model with `budget_tokens: 10000` produces deep, deliberate chain-of-thought. The model did not change. The configuration did. A rate_limit_config set to `concurrent_requests: 20` keeps your grid stable. Without it, you get 429 cascades that can kill an overnight run. A secret_config with proper rotation policies keeps your API keys out of git history. The model is irrelevant to that concern — the config is everything.

This is not CEXAI-specific. Every major LLM framework — LangChain, LlamaIndex, CrewAI, AutoGen, OpenAI Assistants — has a configuration layer. They call it different things: runnable config, environment settings, session parameters, runtime overrides. P09 is the systematic taxonomy of that layer: **30 distinct kinds covering every dimension of runtime behavior that matters in production AI systems.**

The universal principle: **separate configuration from code, and separate runtime configuration from model identity.** An agent's identity (P02) answers "who am I." An agent's prompts (P03) answer "how do I respond." An agent's config (P09) answers "under what operating constraints do I run." These are three orthogonal concerns, and conflating them is the single most common cause of brittle AI systems.

**The practical upshot:** if your AI system behaves differently in production than it does in development, the diagnosis almost always points to a missing or mismatched P09 artifact. Wrong environment variables. Undocumented rate limits. Secrets hardcoded in prompts. Config drift between environments. P09 exists to make these problems visible, versioned, and systematic.

---

## What This Pillar Does

P09 Config governs the operational context in which agents execute — the rules of the environment rather than the rules of the agent. It answers three categories of questions:

**Operational boundaries:** How fast can this agent run? How much can it spend? What resources can it access? This covers rate_limit_config, cost_budget, usage_quota, and effort_profile.

**Security perimeter:** Who can access this agent? What credentials does it use? How are those credentials rotated? This covers secret_config, permission, rbac_policy, sso_config, oauth_app_config, and sandbox_config.

**Runtime behavior tuning:** How much does this agent think before responding? What runtime rules govern retries and timeouts? What execution environment does it target? This covers thinking_config, runtime_rule, terminal_backend, and hibernation_policy.

In the 8F pipeline, P09 artifacts predominantly serve the GOVERN (F7) and CONSTRAIN (F1) functions. They are the guardrails that the orchestration layer enforces before any F6 PRODUCE step runs. You do not write a P09 artifact during generation — you read P09 artifacts at F1 to understand what constraints the runtime imposes, and you validate against them at F7 to ensure the produced output respects those constraints.

The critical architectural insight: **P09 is the configuration-over-code layer.** Instead of hardcoding `rpm = 50` inside your agent class, you write a `rate_limit_config` artifact. Any agent can read it. Any runtime can enforce it. Any operator can update it without touching agent code. This is the difference between a fragile script and a production system.

---

## All 30 Kinds in P09 — Universal Capability Reference

| Kind | Universal Capability | Production Importance |
|------|---------------------|----------------------|
| `env_config` | Environment variables for the agent runtime | Critical — separates dev/staging/prod |
| `path_config` | File system path declarations | High — cross-platform deployments |
| `permission` | Read/write/execute access control rules | Critical — prevents privilege escalation |
| `feature_flag` | Runtime feature toggles with gradual rollout | High — enables safe incremental releases |
| `runtime_rule` | Timeouts, retry counts, circuit breakers | Critical — prevents runaway agents |
| `secret_config` | API key and credential management with rotation | Critical — security baseline |
| `rate_limit_config` | RPM, TPM, concurrent request caps per provider | Critical — prevents 429 storms in grid runs |
| `cost_budget` | Spend caps per provider/mode/session | High — prevents runaway billing |
| `usage_quota` | Per-user or per-tenant fair-use limits | High — multi-tenant safety |
| `effort_profile` | Model tier + thinking budget per task class | High — quality vs. cost optimization |
| `thinking_config` | Extended thinking token budget settings | High — controls depth of chain-of-thought |
| `sandbox_config` | Isolated code execution environment | Critical — code execution safety |
| `sandbox_spec` | Enterprise pilot sandbox specifications | Medium — procurement gate |
| `rbac_policy` | Role-based access for multi-tenant isolation | Critical — enterprise deployments |
| `sso_config` | SAML/OIDC identity provider integration | High — enterprise auth |
| `oauth_app_config` | OAuth2/PKCE scopes and redirect config | High — API integrations |
| `data_residency` | GDPR regional data location config | High — compliance |
| `experiment_config` | A/B test and prompt variant configuration | Medium — continuous improvement |
| `quantization_config` | Local model quantization settings | Medium — local deployment optimization |
| `terminal_backend` | Execution environment abstraction (local/Docker/cloud) | High — deployment flexibility |
| `hibernation_policy` | Idle serverless shutdown and wake policy | High — cost control |
| `batch_config` | Async bulk API processing configuration | High — throughput optimization |
| `transport_config` | Network layer for realtime sessions | Medium — voice/realtime agents |
| `realtime_session` | Live bidirectional session configuration | Medium — voice/streaming agents |
| `vad_config` | Voice activity detection settings | Low — voice-specific |
| `prosody_config` | Voice personality and emotion parameters | Low — voice-specific |
| `playground_config` | Interactive evaluation sandbox | Medium — developer tooling |
| `marketplace_app_manifest` | App store listing metadata | Low — distribution |
| `kubernetes_ai_requirement` | CNCF KAR GPU topology and compliance | Medium — K8s deployments |
| `white_label_config` | White-label branding configuration | Low — reseller scenarios |

---

## Key Engineering Patterns — Universal, Works With Any AI

### Pattern 1: The Configuration Hierarchy

Every serious AI deployment has at least three levels of configuration: defaults, environment overrides, and runtime overrides. The mistake most teams make is implementing this as ad-hoc code logic. The correct approach is to model it explicitly:

```
Level 1: archetype defaults  (N00_genesis/P09_config/)
Level 2: environment overlay  (nucleus-specific P09/)
Level 3: runtime override     (session-level, from orchestrator)
```

In any framework: establish defaults in a base config file, override per environment (dev/staging/prod), allow per-session overrides for dynamic parameters. This three-level hierarchy prevents the "works in dev, breaks in prod" failure mode that affects the majority of first-generation AI deployments.

**Try this now (works with any AI):**
Before your next LLM deployment, write three config files:
1. `config_base.yaml` — provider, model, default temperature, timeout
2. `config_dev.yaml` — debug logging, lower rate limits, mock secrets
3. `config_prod.yaml` — real secrets via env vars, strict rate limits, alerting on

Load the appropriate file at startup. Never hardcode either set.

### Pattern 2: Rate Limit Prophylaxis

Rate limits are not a provider constraint to work around — they are a production safety net you should configure defensively on your side. The pattern is: document the provider's limit, set your safe limit at 80% of that, configure exponential backoff starting at 1 second, and set a maximum concurrent request count.

```yaml
# Universal rate limit config pattern
provider: anthropic
model: claude-sonnet-4-6
rpm: 50
tpm: 200000
concurrent_requests: 20       # 20 out of provider's 32 ceiling = safe headroom
backoff_strategy: exponential
backoff_base_ms: 1000
safe_limit_pct: 80            # never approach the ceiling
```

The `safe_limit_pct: 80` rule is worth internalizing: at 80% utilization, the probability of hitting a 429 error drops below 2%. At 95% utilization, it spikes to 40%+ under load. The lost throughput from operating at 80% costs far less than debugging a failed overnight grid run.

### Pattern 3: Effort Profiles — Quality vs. Cost Routing

Not all tasks deserve the same model tier or thinking depth. A document classification task does not need the same effort as a complex code architecture review. The `effort_profile` pattern formalizes this:

```yaml
# Low-effort: routine tasks
effort: low
model_tier: haiku
thinking_budget_tokens: 0
max_tokens: 512

# Medium-effort: standard builds
effort: medium
model_tier: sonnet
thinking_budget_tokens: 1024
max_tokens: 2048

# High-effort: architecture decisions, complex code
effort: high
model_tier: opus
thinking_budget_tokens: 10000
max_tokens: 8192
```

The orchestrator routes each task to the appropriate effort profile. The downstream cost impact is dramatic: a grid run that naively uses Opus for all 100 artifacts costs 10-15x more than one that uses Haiku for routine tasks and Opus only for the 5 that genuinely need it.

### Pattern 4: Secret Management — The Only Correct Approach

There is exactly one correct approach to secrets in AI systems: **secrets never appear in code, prompts, or artifact files.** They live in environment variables, injected at runtime by an orchestrator that reads them from a vault.

```yaml
# secret_config pattern
id: secret_anthropic_production
kind: secret_config
provider: anthropic
key_name: ANTHROPIC_API_KEY
source: env              # read from environment variable
rotation_policy: 90d     # rotate every 90 days
never_log: true          # never appears in trace logs
never_commit: true       # blocked by pre-commit hook
```

The `secret_config` artifact documents that a secret exists and where it comes from — without containing the secret itself. This is the reference, not the credential. The actual value lives in your CI/CD vault, `.env` file (gitignored), or secrets manager.

### Pattern 5: Terminal Backend Abstraction

Production AI systems run in multiple environments: local development, Docker containers, cloud VMs, serverless platforms. Hardcoding execution assumptions creates environment-specific breakage. The `terminal_backend` pattern abstracts this:

```yaml
# terminal_backend: abstract the "where"
backend: auto            # resolves: local > docker > modal > daytona
fallback_chain: [local, docker, modal]
container_image: cexai/nucleus:latest
resource_requirements:
  gpu: optional
  ram_gb: 8
  cpu_cores: 2
```

Any agent that reads this config can execute on any backend without code changes. This is the Hermes architecture pattern: declare intent, resolve backend at runtime.

---

## Architecture Deep Dive

### The Dependency Graph of P09

P09 artifacts rarely exist in isolation. They form a dependency chain:

```
secret_config
    |
    v
env_config -----> rate_limit_config
    |                    |
    v                    v
permission          cost_budget -----> usage_quota
    |
    v
rbac_policy -----> sso_config / oauth_app_config
    |
    v
sandbox_config -----> terminal_backend -----> hibernation_policy
```

The hierarchy matters for deployment ordering. Secret config must be available before env config can reference it. Rate limits must be established before any agent call executes. RBAC must be in place before any multi-tenant request is processed.

### The Boundary Between P09 and Other Pillars

P09 is frequently confused with neighboring pillars. The canonical boundaries:

| Situation | Correct Pillar | Why |
|-----------|---------------|-----|
| Agent's identity and persona | P02 | Who the agent is (immutable) |
| Agent's system prompt | P03 | What the agent says |
| Safety restriction on outputs | P11 | Guardrail, not config |
| Quality gate on artifacts | P11 | Feedback, not config |
| Tool access permissions | P09 (permission) | Runtime access control |
| Evaluation test limits | P07 | Evaluation infrastructure |
| Which tools exist | P04 | Tool definitions |

The key distinction: P09 governs **operating conditions**. Everything else governs content, identity, or quality. When in doubt, ask: "Is this a constraint on how the system runs, or on what it produces?" Operating constraint = P09.

### The GOVERN LLM Function

Most P09 kinds map to the LLM function `GOVERN`. In the 8F pipeline, GOVERN artifacts are read at F1 (CONSTRAIN) and enforced at F7 (GOVERN). They are passive contracts — they describe constraints rather than producing content. The exceptions:

- `rate_limit_config` → CONSTRAIN (sets upstream limits before any call)
- `terminal_backend` → CALL (invoked at F5 to determine execution environment)
- `effort_profile` → CONSTRAIN (sets model selection before reasoning begins)

This means P09 artifacts are predominantly inputs to the pipeline, not outputs. You build them once, maintain them through lifecycle_rule (P11), and the rest of the system reads them on every run.

---

## Real Examples from N00_genesis

### rate_limit_config in practice

File: `N00_genesis/P09_config/kind_rate_limit_config/kind_manifest_n00.md`

The canonical pattern for documenting provider rate limits:
```yaml
provider: anthropic
model: claude-sonnet-4-6
rpm: 50
tpm: 200000
concurrent_requests: 20
backoff_strategy: exponential
backoff_base_ms: 1000
safe_limit_pct: 80
```

This exact config was derived empirically: 32 concurrent Sonnet requests was the observed ceiling, 87.5% success rate, safe limit is ~20. The config encodes operational intelligence that took hours of grid runs to discover — so no future operator has to rediscover it.

### effort_profile in practice

File: `N00_genesis/P09_config/kind_effort_profile`

Effort profiles express the quality-cost tradeoff as a first-class configuration concern. Rather than embedding model selection logic inside agent code, the orchestrator selects an effort profile based on task classification, and all downstream model selection flows from that profile.

### hibernation_policy — the cost control pattern

File: `N00_genesis/P09_config/tpl_hibernation_policy.md`

For serverless deployments, idle compute is pure waste. The hibernation_policy declares:
- `idle_timeout`: how long with no requests before hibernating
- `wake_trigger`: what event restarts the service
- `warm_pool_size`: how many pre-warmed instances to keep

This pattern prevents the common failure mode of paying for 24/7 compute when your AI system has usage peaks and valleys.

---

## Anti-Patterns — Universal Mistakes

**Anti-pattern 1: Config embedded in prompts**
Hardcoding `"You must respond in under 200 words"` inside a system prompt is a config concern embedded in a prompt. When you need to change the limit, you have to find and edit every prompt that contains it. The correct approach: declare a `runtime_rule` with `max_output_tokens: 200` and reference it from your agent's execution config.

**Anti-pattern 2: Rate limits as try/catch**
The prevalent pattern in naive LLM code: wrap every API call in a try/except, catch the 429, sleep and retry. This is reactive rate limit handling. The P09 pattern is proactive: configure your own limits below the provider's ceiling so you never hit 429 in the first place. Reactive handling is a fallback for edge cases, not a primary strategy.

**Anti-pattern 3: One config file for all environments**
A single `config.yaml` checked into git that is shared between development and production is a security incident waiting to happen. Secrets appear in git history. Dev overrides disable production safety checks. The correct pattern: base config in git (no secrets), environment-specific overrides injected at deploy time via vault or CI/CD.

**Anti-pattern 4: Undocumented quota limits**
"We hit a quota limit and our overnight run failed" is a story told at post-mortems across the industry. Document every quota — provider limits, internal usage quotas, per-user limits — as `rate_limit_config` and `usage_quota` artifacts before the first production run. Quotas are not infrastructure surprises; they are config that you simply have not written yet.

**Anti-pattern 5: Thinking budget fixed for all tasks**
Setting `thinking_budget_tokens: 10000` for every task is the equivalent of requiring every employee to write a 50-page report before answering any question. Map task complexity to effort profiles. Reserve extended thinking for high-stakes decisions. Use fast, cheap paths for routine classification and formatting tasks.

**Anti-pattern 6: Missing hibernation config on serverless**
Deploying a serverless AI endpoint without a hibernation policy is paying for idle compute. Serverless platforms charge for active time — if your agent does nothing from 2 AM to 8 AM, that is six hours of wasted spend. A `hibernation_policy` with `idle_timeout: 5m` and appropriate warm-up strategy eliminates this.

---

## Cross-Pillar Connections

P09 sits at the intersection of identity (P02), execution infrastructure (P04), and governance (P11). Understanding the data flow:

| P09 consumes | From pillar | What it uses |
|-------------|-------------|-------------|
| Agent identity | P02 | Which agent owns which config |
| Tool definitions | P04 | Which tools need which permissions |
| Quality thresholds | P11 | What effort_profile targets which quality bar |
| Architecture decisions | P08 | Which runtime environments are approved |

| P09 feeds | To pillar | What it provides |
|----------|-----------|-----------------|
| Operating constraints | P12 | Orchestrator reads rate limits before dispatching |
| Execution environment | P12 | Terminal backend determines where workflows run |
| Permission boundaries | P11 | Guardrails read permission configs for scope |
| Cost data | P07 | Usage reports pull from cost_budget configs |

**The most critical cross-pillar dependency:** P12 Orchestration reads P09 Config before every dispatch. The orchestrator cannot safely dispatch 6 parallel nuclei without first reading `rate_limit_config` to understand provider ceilings. Config is upstream of orchestration in every production AI system.

---

## Try This Now — P09 Exercises for Any AI System

**Exercise 1: Rate Limit Audit (30 minutes)**
For every LLM API you use in production, write a `rate_limit_config` document. Include: RPM, TPM, concurrent request limit, backoff strategy. Check: are any of these currently implicit (you discover them by hitting errors)? Make them explicit.

**Exercise 2: Secret Config Sweep (1 hour)**
Search your codebase for any string matching `sk-`, `AIzaSy`, `AKIA` (common API key prefixes). Find every hardcoded or committed secret. For each one: move it to environment variable, write a `secret_config` artifact documenting its name, source, and rotation policy.

**Exercise 3: Effort Profile Design (45 minutes)**
List the top 5 task types your AI system handles. For each: what is the appropriate model tier? Extended thinking or not? Max output tokens? Write an `effort_profile` for each. Estimate the cost reduction from routing cheap tasks to smaller models.

**Exercise 4: Environment Config Separation (2 hours)**
If you have a single config file covering all environments, split it into base + per-environment overlays. Move all secrets to environment variables. Test that `config_dev.yaml` cannot accidentally connect to production resources.

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p09_config_pt]] | sibling (PT-BR) | 1.00 |
| [[kc_pillar_brief_p08_architecture_en]] | upstream | 0.48 |
| [[kc_pillar_brief_p10_memory_en]] | downstream | 0.45 |
| [[kc_pillar_brief_p11_feedback_en]] | related | 0.43 |
| [[kc_pillar_brief_p12_orchestration_en]] | downstream | 0.42 |
| [[n00_p09_kind_index]] | upstream | 0.68 |
| [[n00_rate_limit_config_manifest]] | upstream | 0.55 |
| [[mentor_context]] | upstream | 0.40 |
