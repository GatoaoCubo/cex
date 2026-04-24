---
id: p01_kc_intent_resolution_benchmark
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Intent Resolution Benchmark: Confidence Scoring, Clarification Patterns, Query Decomposition + 50-Case Test Dataset"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: N01_intelligence
domain: intent-resolution
origin: src_standards_global
quality: 8.9
tags: [intent, confidence, clarification, decomposition, benchmark, scoring, fallback, slot-filling, NLU, multi-turn]
tldr: "Cross-industry research on confidence scoring (5 frameworks), multi-turn clarification (4 patterns), query decomposition (3 approaches), plus a 50-case benchmark dataset (25 EN + 25 PT) spanning easy/medium/hard difficulty."
when_to_use: "When implementing confidence scoring in CEX intent resolution. When designing clarification UX. When building query decomposition for compound intents. When testing intent resolution accuracy."
keywords: [confidence-scoring, fallback-threshold, clarification-dialog, slot-filling, query-decomposition, sub-question, intent-splitting, benchmark-dataset]
long_tails:
  - "how do Rasa Dialogflow and Amazon Lex handle confidence scoring for intent classification"
  - "what clarification patterns should an agent framework use when confidence is low"
  - "how to decompose compound user intents into atomic sub-queries for multi-agent dispatch"
  - "benchmark dataset for testing intent resolution accuracy in bilingual agent systems"
axioms:
  - "Every framework uses confidence scoring -- the difference is WHERE they set the threshold and WHAT happens below it"
  - "Clarification is cheaper than misrouting -- a 2-turn clarification costs less than re-dispatching a wrong nucleus"
  - "Query decomposition at resolution time is the single highest-leverage improvement for CEX's motor"
feeds_kinds: [router, guardrail, quality_gate, eval_dataset, instruction, knowledge_card]
linked_artifacts:
  related:
    - N01_intelligence/P05_output/report_input_intent_resolution.md
    - _tools/cex_8f_motor.py
    - _tools/cex_query.py
    - _tools/cex_retriever.py
    - .claude/rules/n07-input-transmutation.md
    - N03_engineering/P01_knowledge/kc_intent_resolution_map.md
density_score: 0.91
related:
  - kc_tool_first_patterns
  - p01_report_intent_resolution
  - p01_kc_input_intent_resolution
  - p01_kc_prompt_compiler
  - bld_collaboration_router
  - n04_rc_knowledge
  - p02_rt_SCOPE_SLUG
  - llm-judge-builder
  - ex_dispatch_rule_research
  - bld_collaboration_llm_judge
---

# Intent Resolution Benchmark

## Part 1: Confidence Scoring Research

### 1.1 Framework Comparison: Confidence Methods

Every surveyed framework implements confidence scoring -- but with fundamentally different architectures. The table below compares 7 systems across 4 dimensions.

| Framework | Confidence Method | Score Range | Default Threshold | Fallback Strategy |
|-----------|------------------|-------------|-------------------|-------------------|
| **Rasa** | DIET classifier softmax + FallbackClassifier | 0.0-1.0 | 0.3 (nlu_threshold) | Two-stage: (1) affirm intent, (2) rephrase. `ambiguity_threshold` = 0.1 for top-2 delta |
| **Dialogflow CX** | ML classification with per-flow thresholds | 0.0-1.0 | 0.3 (configurable to 0.7+ recommended) | `no-match` event triggers fallback page. Generative fallback via LLM (2025+) |
| **Amazon Lex V2** | `nluIntentConfidenceScore` per interpretation | 0.0-1.0 | `nluIntentConfidenceThreshold` (configurable) | Returns up to 4 alternatives + `AMAZON.FallbackIntent`. Comparative scores, not absolute |
| **LlamaIndex** | Selector implicit (LLM-based or Pydantic matching) | No explicit 0-1 score | No threshold parameter | Falls through to default QueryEngine. No structured fallback |
| **DSPy** | Assertions as soft constraints; confidence via output field | Declarative (pass/fail) | `dspy.Suggest` (soft) vs `dspy.Assert` (hard) | Backtrack + retry (up to `max_backtrack` iterations). Self-refining loop |
| **OpenAI Agents SDK** | Triage agent uses LLM reasoning (no numeric score) | Implicit (LLM judgment) | None (LLM decides) | `handoff()` to specialist or ask user. Guardrails validate I/O |
| **Semantic Router** | Cosine similarity between query embedding and route utterance embeddings | 0.0-1.0 | ~0.5-0.82 (route-specific) | Below threshold -> default route or larger LLM fallback. Sub-ms latency |

### 1.2 Three Architectures for Confidence Scoring

The industry has converged on three distinct approaches. CEX must choose one (or compose them).

| Architecture | How It Works | Strengths | Weaknesses | Who Uses It |
|-------------|-------------|-----------|------------|-------------|
| **A. Classifier softmax** | Train an intent classifier; softmax gives probability distribution over intents | Numerically precise, trainable, fast | Requires training data, brittle on OOD inputs, overconfident on seen patterns | Rasa (DIET), Dialogflow CX, Amazon Lex |
| **B. Embedding similarity** | Embed query + intent exemplars; cosine similarity = confidence | Zero-shot capable, no training needed, handles novel inputs | Threshold tuning is empirical, no probability interpretation, sensitive to embedding model | Semantic Router, LangChain SemanticRouter |
| **C. LLM-as-judge** | Ask the LLM itself how confident it is (explicit field or chain-of-thought) | Most flexible, handles complex/ambiguous inputs, can explain reasoning | Slow (full LLM call), expensive, hallucination risk on confidence values | OpenAI Agents SDK (implicit), DSPy (via assertions) |

**Recommendation for CEX**: **Hybrid B+C** (embedding similarity as fast gate, LLM-as-judge for ambiguous cases).

Rationale vs alternatives:
- **vs A (classifier softmax)**: CEX has no training data and 123 kinds that change. A trained classifier would need retraining on every kind addition. Embedding similarity handles new kinds zero-shot.
- **vs B alone**: Embedding similarity can't handle compound intents ("build agent AND test it") or contextual disambiguation ("agent" in P02 vs "agent" in A2A). LLM-as-judge resolves these.
- **vs C alone**: LLM-as-judge is too slow/expensive for every input. Embedding similarity handles 80%+ of inputs in <10ms. LLM only needed for the ambiguous 20%.

### 1.3 Threshold Design: What the Industry Learned

| Lesson | Source | Implication for CEX |
|--------|--------|-------------------|
| **Dual threshold**: confidence + ambiguity gap | Rasa (`nlu_threshold` + `ambiguity_threshold`) | CEX should reject when (a) top score < 0.5 OR (b) top-2 delta < 0.15 |
| **Per-flow thresholds** beat global thresholds | Dialogflow CX (per-flow ML settings) | CEX should allow per-pillar or per-nucleus threshold tuning |
| **Comparative scores, not absolute** | Amazon Lex (explicit warning in docs) | Don't treat 0.7 as "good" universally -- compare relative rankings |
| **Route-specific thresholds** outperform global | Semantic Router (per-route score_threshold) | Some kinds are naturally harder to match -- "agent" is ambiguous, "mcp_server" is precise |
| **Self-refining is better than hard failure** | DSPy (assertion backtracking) | When confidence is low, try reformulating before falling back to user |
| **Sub-ms is achievable** for embedding-based routing | Semantic Router benchmarks (<1ms for 100 routes) | CEX with 123 kinds can still achieve <10ms routing with embeddings |

### 1.4 Proposed CEX Confidence Scoring Design

```
User Input
    |
    v
[1] TF-IDF keyword match (current cex_query.py)
    |-- exact match in OBJECT_TO_KINDS? --> confidence = 1.0 --> PROCEED
    |-- TF-IDF top hit score > 0.8?     --> confidence = TF-IDF score --> PROCEED
    |
    v (no match or low score)
[2] Embedding similarity (NEW -- cosine against kind exemplars)
    |-- top cosine > 0.65?              --> confidence = cosine score --> PROCEED
    |-- top cosine 0.40-0.65?           --> AMBIGUOUS (go to step 3)
    |-- top cosine < 0.40?              --> UNKNOWN (go to step 4)
    |
    v (ambiguous)
[3] LLM-as-judge (NEW -- ask model to classify with reasoning)
    |-- model returns kind + confidence  --> weighted average with step 2
    |-- model says "unclear"             --> CLARIFY (go to step 4)
    |
    v (unknown or unclear)
[4] Clarification dialog (Part 2 of this research)
    |-- ask user for more context
    |-- re-run pipeline with enriched input
```

**Cost analysis vs alternatives**:
- Current CEX (keyword-only): 0ms, 0 cost, ~60% accuracy on novel inputs
- Proposed hybrid: <10ms for 80% (embedding), ~500ms for 15% (LLM), ~3s for 5% (clarification). 95%+ accuracy target.
- Full LLM-as-judge (every input): ~500ms per input, ~$0.002/input. Overkill for "cria agente" which is a trivial match.

---

## Part 2: Multi-Turn Clarification Patterns

### 2.1 Framework Comparison: How Systems Ask for Clarification

| Framework | Clarification Mechanism | Trigger | Turns Needed | User Experience |
|-----------|------------------------|---------|-------------|-----------------|
| **Rasa** | `TwoStageFallbackPolicy`: (1) affirm top intent, (2) if denied, rephrase. Forms for slot filling with `required_slots` and `slot_was_set` conditions | Confidence below `nlu_threshold` OR ambiguity below `ambiguity_threshold` | 2 (affirm/deny + rephrase) or N (for N missing slots) | "Did you mean X?" -> "No" -> "Please rephrase" |
| **Dialogflow CX** | `no-match` event handlers per page. Generative fallback (2025+) uses LLM to ask targeted questions. Slot filling with `is_required` and custom reprompts | Confidence below per-flow threshold. Missing required parameters | 1-3 per missing slot | "I didn't catch that. Which city?" |
| **Amazon Lex** | `AMAZON.FallbackIntent` + `elicitSlot` directive. Returns up to 4 alternative intents for disambiguation | All intents below `nluIntentConfidenceThreshold`. Missing slots for confirmed intent | 1 (disambiguation) + N (slots) | "Did you mean A, B, or C?" + slot prompts |
| **MAC Framework** (2026) | Multi-agent: Supervisor detects ambiguity, Expert asks domain-specific questions. Hierarchical clarification reduces turns by 25% | Model uncertainty detection (entropy-based) | 4.86 avg (vs 6.53 without), +7.8% task success | Agent-to-agent clarification before user |
| **Microsoft CLU** | Entity slot filling in multi-turn. Users correct/clarify throughout conversation. System accommodates various communication styles | Missing entities in recognized intent | Flexible (user-driven) | Natural conversation flow |

### 2.2 Four Clarification Patterns (Industry Taxonomy)

| Pattern | When to Use | Example | Strength | Weakness |
|---------|------------|---------|----------|----------|
| **P1: Binary Confirmation** | Top intent has moderate confidence (0.5-0.7) | "Did you mean 'create an agent'? (yes/no)" | Fast, low friction, works for clear near-misses | Useless when top intent is wrong |
| **P2: Disambiguation Menu** | Top 2-3 intents are close in confidence | "I see a few options: (a) agent, (b) agent_card, (c) agent_package. Which?" | Surfaces alternatives user might not know about | Overwhelming with >4 options |
| **P3: Slot Filling** | Intent is clear but parameters are missing | "Got it -- create an agent. What domain? (e.g., sales, support, research)" | Progressive refinement, natural flow | Can feel interrogative with many slots |
| **P4: Open Rephrase** | Confidence is very low (<0.3), no good candidates | "I'm not sure what you need. Can you describe it differently?" | Catches completely novel intents | Frustrating if system should have understood |

### 2.3 Proposed CEX Clarification Flow

CEX currently has GDP (Guided Decision Protocol) for subjective decisions, but NO structured clarification for ambiguous intents. GDP is all-or-nothing (6 questions upfront). The industry pattern is progressive slot filling.

**Proposed design** (compared against 2 alternatives):

| Approach | How | Pros | Cons | Verdict |
|----------|-----|------|------|---------|
| **A: GDP extension** | Add intent-clarification questions to existing GDP flow | Reuses existing code. User already knows GDP | GDP is for WHAT (subjective). Clarification is for WHICH (objective). Mixing them confuses both | REJECT |
| **B: Standalone clarification agent** | New N00-level module that intercepts low-confidence intents | Clean separation. Testable independently. Can use MAC-style multi-agent | Another component to maintain. Overhead for simple clarifications | PARTIALLY ACCEPT (for complex cases) |
| **C: Inline progressive clarification** | Embed clarification into `cex_8f_motor.py` at F1 CONSTRAIN | Zero overhead for high-confidence. Progressive for ambiguous. Fastest path to production | Mixes resolution + interaction in one module | **ACCEPT as default** |

**Proposed CEX clarification protocol**:

```
confidence >= 0.7  --> PROCEED (no clarification)
confidence 0.5-0.7 --> P1 Binary: "I'll interpret 'X' as {kind}. Correct? (y/n)"
confidence 0.3-0.5 --> P2 Disambiguate: "Did you mean: (a) {kind1}, (b) {kind2}, (c) {kind3}?"
confidence < 0.3   --> P4 Open: "I'm not sure which artifact type fits. Can you describe what you want to achieve?"

After kind is resolved:
  missing required slots --> P3 Slot Fill: ask for each missing parameter progressively
```

**Multi-turn state tracking** (new for CEX):

```yaml
# .cex/runtime/clarification_state.yaml (ephemeral, per-session)
session_id: "abc123"
original_input: "build something for onboarding"
clarification_turns:
  - turn: 1
    question: "Did you mean: (a) workflow, (b) landing_page, (c) prompt_template?"
    answer: "a"
    resolved: { kind: workflow, confidence: 0.85 }
  - turn: 2
    question: "What triggers this workflow? (e.g., new user signup, course enrollment)"
    answer: "new user signup"
    resolved: { domain: "onboarding", trigger: "signup" }
resolution:
  kind: workflow
  pillar: P12
  nucleus: N03
  confidence: 0.85
  turns_needed: 2
```

---

## Part 3: Query Decomposition Research

### 3.1 The Problem

CEX's `cex_8f_motor.py` already detects multi-object intents ("cria agente e workflow") by splitting on ` e `, `+`, `,`. But this is **syntactic splitting only** -- it doesn't handle:
- Semantic compounds: "build a CRM with auth and payments" (1 project, 3 concerns)
- Implicit compounds: "research and implement competitor pricing" (2 actions, 1 domain)
- Cross-nucleus compounds: "analyze the market then write ad copy" (N01 then N02)

### 3.2 Framework Comparison: Decomposition Approaches

| Framework | Decomposition Method | Granularity | Handles Implicit Compounds? | Output Format |
|-----------|---------------------|-------------|---------------------------|---------------|
| **LlamaIndex SubQuestionQE** | LLM generates sub-questions from compound query. Each sub-question routed to a specific QueryEngineTool by metadata match | Per-retrieval-source | Yes (LLM understands semantic structure) | List of `SubQuestion(sub_question, tool_name)` |
| **LangChain QueryDecomposition** | LLM decomposes query into atomic queries. Multi-Query Retriever generates N reformulations for diversity | Per-query (retrieval) | Partially (reformulation, not intent splitting) | List of reformulated query strings |
| **Google Research (EMNLP 2025)** | Two-stage decomposition: (1) summarize context per screen, (2) extract intent from summaries. Small models outperform monolithic LLMs | Per-intent (action level) | Yes (designed for multi-action inputs) | Structured intent + entities per action |
| **CrewAI** | Developer pre-decomposes via Task definitions. No automatic decomposition | Per-task (developer-defined) | No (manual) | Task objects with descriptions |
| **CEX (current)** | Regex split on ` e ` / `+` / `,` in `parse_intent()` | Per-object (syntactic) | No | List of object strings |

### 3.3 Three Decomposition Architectures

| Architecture | How | Strengths | Weaknesses | Fit for CEX |
|-------------|-----|-----------|------------|-------------|
| **D1: Regex/syntactic** (current CEX) | Split on conjunctions and delimiters | Zero latency, zero cost, deterministic | Misses implicit compounds. "Build CRM" stays as 1 intent even though it implies agent + workflow + API client | KEEP as Layer 1 (fast path) |
| **D2: LLM decomposition** (LlamaIndex/LangChain) | Ask LLM to decompose the query into sub-queries with tool assignments | Handles any complexity. Can infer implicit sub-tasks | Slow (~500ms), expensive, may over-decompose simple inputs | ADD as Layer 2 (for compounds) |
| **D3: Template-based decomposition** | Pre-define decomposition rules for known compound patterns | Fast, predictable, no LLM cost | Limited to known patterns. Doesn't generalize | ADD as Layer 1.5 (known patterns) |

**Proposed CEX decomposition pipeline**:

```
User Input: "research competitor pricing and build a pricing page"
    |
    v
[Layer 1] Syntactic split (current regex)
    --> ["research competitor pricing", "build a pricing page"]
    --> If split produces 2+ segments: resolve each independently
    |
    v (if Layer 1 produces only 1 segment and it's complex)
[Layer 1.5] Template matching (NEW)
    --> Pattern: "{verb1} X and {verb2} Y" --> split into 2 intents
    --> Pattern: "{verb} X with Y and Z" --> 1 intent, 3 slot values
    --> If matched: split or annotate accordingly
    |
    v (if still ambiguous)
[Layer 2] LLM decomposition (NEW -- only for genuine compounds)
    --> Prompt: "Decompose this user request into atomic sub-tasks.
                For each: intent_verb, target_kind, target_nucleus, dependencies."
    --> Output: structured JSON of sub-tasks
    |
    v
[Merge] Dependency analysis
    --> Which sub-tasks can run in parallel? (different nuclei)
    --> Which are sequential? (output of A feeds input of B)
    --> Generate wave plan for N07 dispatch
```

### 3.4 Template Library for Known Compound Patterns

| User Pattern | Decomposition | Dependency | Example |
|-------------|--------------|------------|---------|
| "{verb} X and Y" (same verb, different objects) | 2 parallel intents, same verb | None (parallel) | "create agent and workflow" -> N03: agent, N03: workflow |
| "{verb1} X then {verb2} Y" (sequential actions) | 2 sequential intents | B depends on A | "research competitors then write copy" -> N01: KC, then N02: copy |
| "{verb} X with Y and Z" (1 intent, compound params) | 1 intent, multi-slot | None (single artifact) | "build CRM with auth" -> N03: workflow (slots: auth=true) |
| "{verb1} X and {verb2} it" (action + meta-action) | 2 sequential intents, shared object | B operates on A's output | "create agent and test it" -> N03: agent, N05: unit_eval |
| "X for Y" (intent + domain) | 1 intent, domain slot filled | None | "pricing page for SaaS" -> N03: landing_page (domain: SaaS) |

### 3.5 Industry Terminology

| CEX Term | Industry Term | Used By | Standard? |
|----------|-------------|---------|-----------|
| "Multi-object detection" | **Query Decomposition** | LlamaIndex, LangChain, IR literature | Yes (standard in IR) |
| "Syntactic split" | **Conjunct Splitting** | NLU literature, Rasa | Niche (NLU-specific) |
| "LLM decomposition" | **Sub-Question Generation** | LlamaIndex (SubQuestionQueryEngine) | Emerging standard |
| "Template matching" | **Pattern-Based Intent Splitting** | Dialogflow CX (composite entities) | Domain-specific |
| "Wave plan" | **Task Graph / DAG** | CrewAI, AutoGen, Temporal | Yes (standard in orchestration) |

---

## Part 4: Benchmark Dataset (50 Cases)

### 4.1 Dataset Design

| Dimension | Value |
|-----------|-------|
| Total cases | 50 |
| Languages | 25 English + 25 Portuguese |
| Difficulty levels | Easy (20), Medium (15), Hard (15) |
| Coverage | 12 pillars, 8 nuclei, 35+ unique kinds |
| Purpose | Measure intent resolution accuracy at F1 CONSTRAIN |

**Difficulty definitions**:
- **Easy**: exact keyword match or canonical kind name (e.g., "create agent")
- **Medium**: synonym, abbreviation, or slight ambiguity (e.g., "deploy my app" = env_config + workflow)
- **Hard**: vague, compound, metaphorical, or requires world knowledge (e.g., "make onboarding smooth")

### 4.2 English Test Cases (25)

| # | Phrase | Expected Kind | Pillar | Nucleus | Difficulty | Notes |
|---|--------|--------------|--------|---------|------------|-------|
| EN-01 | "create an agent for sales" | agent | P02 | N03 | Easy | Exact match: "agent" in OBJECT_TO_KINDS |
| EN-02 | "build a webhook for Stripe" | webhook | P04 | N05 | Easy | Exact match: "webhook" |
| EN-03 | "write a knowledge card about RAG" | knowledge_card | P01 | N04 | Easy | Exact match: "knowledge card" |
| EN-04 | "set up MCP server" | mcp_server | P04 | N05 | Easy | Exact match: "mcp" |
| EN-05 | "add a quality gate" | quality_gate | P11 | N03 | Easy | Exact match: "quality gate" |
| EN-06 | "design the architecture" | diagram | P08 | N03 | Medium | "architecture" -> diagram? component_map? decision_record? |
| EN-07 | "deploy my app" | env_config | P09 | N05 | Medium | "deploy" not a kind -- maps to env_config or workflow |
| EN-08 | "fix the tests" | unit_eval | P07 | N05 | Medium | "fix" + "tests" -> N05 operations, kind ambiguous |
| EN-09 | "make content for Instagram" | prompt_template | P03 | N02 | Medium | "content for Instagram" -> marketing copy, kind unclear |
| EN-10 | "connect to the database" | db_connector | P04 | N05 | Easy | Exact match: "database" |
| EN-11 | "document the API" | context_doc | P01 | N04 | Medium | "document" verb + "API" -> context_doc or api_client? |
| EN-12 | "research competitor pricing" | knowledge_card | P01 | N01 | Easy | "research" -> N01, "competitor pricing" -> KC |
| EN-13 | "build a CRM with auth and payments" | workflow | P12 | N03 | Hard | Compound: 1 project, 3 subsystems. Needs decomposition |
| EN-14 | "make onboarding smooth" | workflow | P12 | N03 | Hard | Vague: "smooth" is subjective. "onboarding" -> workflow? landing_page? |
| EN-15 | "I need a bot that answers questions" | agent | P02 | N03 | Medium | "bot" synonym for agent. "answers questions" -> RAG? |
| EN-16 | "set up the pricing tiers" | content_monetization | P11 | N06 | Medium | "pricing tiers" -> content_monetization or landing_page? |
| EN-17 | "analyze market trends" | knowledge_card | P01 | N01 | Easy | "analyze" -> N01, "market trends" -> KC |
| EN-18 | "write ad copy for Black Friday" | prompt_template | P03 | N02 | Easy | "ad copy" -> N02, P03 prompt_template |
| EN-19 | "research competitors AND build a pricing page" | COMPOUND: knowledge_card + landing_page | P01 + P05 | N01 + N03 | Hard | Explicit compound. Must decompose into 2 tasks |
| EN-20 | "automate the deployment pipeline" | workflow | P12 | N05 | Medium | "automate" + "deployment pipeline" -> workflow + N05 |
| EN-21 | "improve all low-quality artifacts" | optimizer | P11 | N05 | Hard | Meta-intent: operates on system, not a single artifact |
| EN-22 | "add monitoring and alerts" | trace_config | P09 | N05 | Medium | "monitoring" -> trace_config? notifier? Both? |
| EN-23 | "create a course about AI agents" | content_monetization | P11 | N06 | Medium | "course" -> N06 commercial, content_monetization |
| EN-24 | "the system is broken, fix it" | bugloop | P11 | N05 | Hard | Vague: "system" = which system? "broken" = how? Needs clarification |
| EN-25 | "translate everything to Portuguese" | formatter | P05 | N03 | Hard | Vague scope: "everything" is undefined. "translate" not a standard action |

### 4.3 Portuguese Test Cases (25)

| # | Phrase | Expected Kind | Pillar | Nucleus | Difficulty | Notes |
|---|--------|--------------|--------|---------|------------|-------|
| PT-01 | "cria um agente de vendas" | agent | P02 | N03 | Easy | Exact match: "agente" -> agent |
| PT-02 | "fazer um webhook pro Hotmart" | webhook | P04 | N05 | Easy | "webhook" exact + domain "Hotmart" |
| PT-03 | "documentar os padroes de RAG" | knowledge_card | P01 | N04 | Easy | "documentar" + "RAG" -> KC |
| PT-04 | "configurar servidor MCP" | mcp_server | P04 | N05 | Easy | "mcp" exact match |
| PT-05 | "adicionar gate de qualidade" | quality_gate | P11 | N03 | Easy | "gate de qualidade" -> quality_gate |
| PT-06 | "quero um bot que responde duvidas" | agent | P02 | N03 | Medium | "bot" synonym for agent. "responde duvidas" -> RAG context |
| PT-07 | "melhorar a landing page" | landing_page | P05 | N03 | Easy | "landing page" exact match, "melhorar" = improve verb |
| PT-08 | "pesquisar concorrentes do mercado EdTech" | knowledge_card | P01 | N01 | Easy | "pesquisar" -> N01, "concorrentes" -> competitive KC |
| PT-09 | "montar funil de vendas" | workflow | P12 | N06 | Medium | "funil de vendas" -> sales funnel. Kind: workflow or content_monetization? |
| PT-10 | "conectar com API do Stripe" | api_client | P04 | N05 | Easy | "API" exact match + domain "Stripe" |
| PT-11 | "preciso de uma forma de agendar postagens" | schedule | P12 | N07 | Medium | "agendar postagens" -> schedule. No direct keyword match |
| PT-12 | "criar prompt de sistema para atendimento" | system_prompt | P03 | N03 | Easy | "prompt de sistema" -> system_prompt |
| PT-13 | "quero que o sistema aprenda com os erros" | learning_record | P10 | N04 | Hard | Abstract: "aprenda com erros" = learning_record? bugloop? feedback loop? |
| PT-14 | "analise o mercado e depois crie copy de venda" | COMPOUND: knowledge_card + prompt_template | P01 + P03 | N01 + N02 | Hard | Sequential compound. "analise" -> N01, "crie copy" -> N02 |
| PT-15 | "fazer um diagrama da arquitetura" | diagram | P08 | N03 | Easy | "diagrama" exact match |
| PT-16 | "to perdido, me ajuda a comecar" | CLARIFICATION_NEEDED | - | - | Hard | Vague: zero actionable content. Must trigger P4 (open rephrase) |
| PT-17 | "configurar limites de taxa para API" | rate_limit_config | P09 | N05 | Medium | "limites de taxa" -> rate_limit_config (not exact keyword) |
| PT-18 | "validar todos os artefatos" | SYSTEM_COMMAND | - | N05 | Medium | Meta-intent: maps to cex_doctor.py, not a kind |
| PT-19 | "criar template de email e landing page" | COMPOUND: prompt_template + landing_page | P03 + P05 | N03 + N03 | Hard | Explicit compound. Same nucleus, 2 kinds |
| PT-20 | "preciso de guardrails pro agente" | guardrail | P11 | N03 | Easy | "guardrails" exact match |
| PT-21 | "otimizar o consumo de tokens" | context_window_config | P03 | N03 | Medium | "consumo de tokens" -> context_window_config? optimizer? |
| PT-22 | "o deploy ta quebrado" | bugloop | P11 | N05 | Hard | Vague: "deploy quebrado" needs diagnosis. Could be env_config, workflow, or bugloop |
| PT-23 | "quero vender curso online de Python" | content_monetization | P11 | N06 | Medium | "vender curso" -> N06 commercial. content_monetization kind |
| PT-24 | "faz um benchmark dos modelos" | benchmark | P07 | N05 | Easy | "benchmark" exact match |
| PT-25 | "resolver conflitos de merge no git" | NOT_CEX_DOMAIN | - | - | Hard | Out-of-domain: git merge conflicts are not a CEX artifact kind. Should recognize and redirect |

### 4.4 Difficulty Distribution and Expected Resolution

| Difficulty | Count | Expected Confidence Range | Expected Clarification Turns | Current CEX Accuracy (estimated) |
|-----------|-------|--------------------------|-----------------------------|---------------------------------|
| Easy | 20 | 0.85-1.0 | 0 | ~95% (keyword match works) |
| Medium | 15 | 0.50-0.84 | 0-1 | ~55% (synonym/ambiguity gaps) |
| Hard | 15 | 0.00-0.49 | 1-3 | ~20% (compound/vague/OOD) |
| **Overall** | **50** | - | - | **~60% (weighted)** |

### 4.5 Special Case Categories

| Category | Cases | Why It Matters |
|----------|-------|---------------|
| **Exact keyword match** | EN-01 to EN-05, PT-01 to PT-05, PT-07, PT-08, PT-10, PT-12, PT-15, PT-20, PT-24 | Baseline: current system should get 100% of these |
| **Synonym resolution** | EN-06, EN-07, EN-09, EN-15, PT-06, PT-09, PT-11, PT-17, PT-21 | Requires semantic understanding beyond keyword table |
| **Compound intent** | EN-13, EN-19, PT-14, PT-19 | Requires decomposition (Part 3 of this research) |
| **Vague/ambiguous** | EN-14, EN-21, EN-24, EN-25, PT-13, PT-16, PT-22 | Requires clarification (Part 2 of this research) |
| **Meta-intent** (system command) | EN-21, PT-18 | Maps to a tool, not a kind. Different resolution path |
| **Out-of-domain** | PT-25 | System should recognize and redirect gracefully |

### 4.6 Scoring Rubric for Benchmark Evaluation

| Metric | Definition | Weight |
|--------|-----------|--------|
| **Kind accuracy** | Correct kind identified (exact match) | 40% |
| **Pillar accuracy** | Correct pillar identified | 20% |
| **Nucleus accuracy** | Correct nucleus routed to | 20% |
| **Compound detection** | Correctly identified as compound (true/false) | 10% |
| **Clarification appropriateness** | Triggered clarification when needed, didn't when not | 10% |

**Pass threshold**: 80% overall accuracy (weighted). Per-difficulty targets:
- Easy: >= 95%
- Medium: >= 75%
- Hard: >= 50%

---

## Part 5: CEX Implementation Roadmap

Based on this research, the recommended implementation order (compared against 2 alternatives):

| Priority | Feature | Effort | Impact | Dependencies |
|----------|---------|--------|--------|-------------|
| **P0** | Run this benchmark against current `cex_8f_motor.py` to establish baseline | 2h | Measures current gap objectively | None |
| **P1** | Add confidence score output to `classify_objects()` | 4h | Enables all downstream improvements | None |
| **P2** | Implement embedding similarity (Layer 2 in proposed design) | 8h | Handles synonym resolution (+15% accuracy) | Embedding model choice |
| **P3** | Template-based decomposition (Layer 1.5) | 4h | Handles known compound patterns | P1 |
| **P4** | Inline progressive clarification (Part 2 design) | 8h | Handles ambiguous inputs | P1 |
| **P5** | LLM-as-judge fallback (Layer 3) | 4h | Handles novel/complex inputs | P1 + P2 |
| **P6** | LLM decomposition for genuine compounds | 4h | Handles implicit compounds | P1 + P3 |

**Alternative roadmap A** (embedding-first): P0 -> P2 -> P1 -> P4 -> P3 -> P5 -> P6. Higher upfront investment but better long-term accuracy. Rejected because P1 (confidence scoring) is a prerequisite for knowing WHEN to use embeddings.

**Alternative roadmap B** (LLM-first): P0 -> P5 -> P1 -> P4 -> P6 -> P2 -> P3. Fastest to implement but highest runtime cost. Rejected because LLM-for-everything is expensive at scale and unnecessary for 80% of inputs.

---

## Appendix A: Sources

| Source | Type | Year |
|--------|------|------|
| [Rasa FallbackClassifier](https://legacy-docs-oss.rasa.com/docs/rasa/fallback-handoff/) | Official docs | 2025 |
| [Rasa TwoStageFallbackPolicy](https://rasa.com/docs/rasa/2.x/reference/rasa/core/policies/two_stage_fallback/) | Official docs | 2025 |
| [Dialogflow CX Intent Matching](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) | Official docs | 2025 |
| [Dialogflow CX Agent Settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings) | Official docs | 2025 |
| [Amazon Lex V2 Confidence Scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-confidence-scores.html) | Official docs | 2025 |
| [Amazon Lex Intent Confidence Selection](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html) | Official docs | 2025 |
| [LlamaIndex RouterQueryEngine](https://developers.llamaindex.ai/python/framework/module_guides/querying/router/) | Official docs | 2026 |
| [LlamaIndex SubQuestionQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/sub_question_query_engine/) | Official docs | 2026 |
| [DSPy Assertions Paper](https://arxiv.org/pdf/2312.13382) | Research paper | 2023 |
| [DSPy Optimizers](https://dspy.ai/learn/optimization/optimizers/) | Official docs | 2026 |
| [Semantic Router](https://github.com/aurelio-labs/semantic-router) | Open source | 2025 |
| [OpenAI Agents SDK Handoffs](https://openai.github.io/openai-agents-python/handoffs/) | Official docs | 2025 |
| [MAC: Multi-Agent Clarification Framework](https://aclanthology.org/2026.iwsds-1.1/) | Research paper (ACL) | 2026 |
| [Google: Small Models, Big Results (EMNLP 2025)](https://arxiv.org/abs/2509.12423) | Research paper | 2025 |
| [Microsoft CLU Multi-Turn Slot Filling](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/concepts/multi-turn-conversations) | Official docs | 2025 |
| [Dropbox DSPy Optimization](https://dropbox.tech/machine-learning/optimizing-dropbox-dash-relevance-judge-with-dspy) | Engineering blog | 2025 |
| [Building Production-Grade Semantic Router 2026](https://atul4u.medium.com/building-a-production-grade-semantic-router-the-smart-way-to-route-ai-prompts-f303e6d2ae7e) | Industry article | 2026 |
| [Embedding Intent Classification <1ms](https://medium.com/@durgeshrathod.777/intent-classification-in-1ms-how-we-built-a-lightning-fast-classifier-with-embeddings-db76bfb6d964) | Engineering blog | 2025 |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_tool_first_patterns]] | sibling | 0.32 |
| [[p01_report_intent_resolution]] | sibling | 0.28 |
| [[p01_kc_input_intent_resolution]] | sibling | 0.27 |
| [[p01_kc_prompt_compiler]] | sibling | 0.25 |
| [[bld_collaboration_router]] | downstream | 0.24 |
| [[n04_rc_knowledge]] | related | 0.22 |
| [[p02_rt_SCOPE_SLUG]] | downstream | 0.22 |
| [[llm-judge-builder]] | downstream | 0.22 |
| [[ex_dispatch_rule_research]] | downstream | 0.21 |
| [[bld_collaboration_llm_judge]] | downstream | 0.21 |
