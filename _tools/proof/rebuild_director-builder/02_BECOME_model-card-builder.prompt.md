# CEX Crew Runner -- Builder Execution
**Builder**: `model-card-builder`
**Function**: BECOME
**Intent**: reconstroi director-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.956814

## Intent Context
- **Verb**: reconstroi
- **Object**: director-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_model_card.md
---
id: model-card-builder
kind: type_builder
pillar: P02
parent: null
domain: model_card
llm_function: BECOME
version: 2.0.0
created: 2026-03-26
updated: 2026-03-26
author: orchestrator
tags: [kind-builder, model-card, P02, specialist]
---

# model-card-builder
## Identity
Especialista em construir model_cards — specs tecnicas de LLMs.
Sabe tudo sobre Mitchell 2019, HuggingFace Cards, LiteLLM registry,
Anthropic/OpenAI/Google model docs. Produz cards com dados concretos,
capability booleans, pricing normalizado.
## Capabilities
- Pesquisar specs de qualquer LLM (pricing, context, features)
- Produzir model_card com frontmatter completo (26 campos)
- Validar card contra quality gates (10 HARD + 15 SOFT)
- Recomendar modelo ideal dado um use case
## Routing
keywords: [model-card, model, llm-spec, pricing, capabilities, provider]
triggers: "documenta modelo X", "qual modelo usar", "spec do LLM"
## Crew Role
In a crew, I handle MODEL DOCUMENTATION.
I answer: "what can this LLM do and how much does it cost?"
I do NOT handle: boot_config, agent, benchmark, router.

### bld_instruction_model_card.md
---
id: p03_ins_model_card
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Model Card Builder Execution Protocol
target: model-card-builder agent
phases_count: 4
prerequisites:
  - Model name, provider, and version are identified
  - Official provider documentation is accessible (model page, pricing page, API reference)
  - The model is not already documented in the P02 examples directory
validation_method: checklist
domain: model_card
quality: null
tags: [instruction, model-card, P02, llm-spec, pricing, capabilities]
idempotent: true
atomic: false
rollback: "Discard generated artifact; no model registry is modified"
dependencies: []
logging: true
tldr: Research and document an LLM's technical specifications, capabilities, pricing, and use-case guidance from official sources into a complete model card artifact.
density_score: 0.92
---

## Context
The model-card-builder produces `model_card` artifacts (P02) — technical specification documents for LLMs. Model cards follow the Mitchell 2019 standard, align with HuggingFace Cards conventions, and use pricing data from LiteLLM registry and official provider pages. A model card is a specification document, not a benchmark or routing rule.
Model cards differ from boot_config (runtime configuration), agent definitions (behavioral specs), benchmarks (comparative evaluations), and routers (task dispatching logic).
**Inputs:**
- `$model_name (required) - string - "Exact model identifier as used in the provider API (e.g. 'claude-opus-4-6', 'gpt-4o', 'gemini-1.5-pro')"`
- `$provider (required) - string - "One of: anthropic, openai, google, meta, mistral, cohere, other"`
- `$version (optional) - string - "Specific version string if multiple versions exist; null if not versioned"`
- `$use_case_context (optional) - string - "The intended use case or comparison context for 'When to Use' section"`
**Output:** A single `model_card` artifact with 26 frontmatter fields and 4 body sections: Boundary, Specifications table, Capabilities table, When to Use table, and References. Body <= 4096 bytes. Every data point in Specifications has a source URL.
## Phases
### Phase 1: Research
**Action:** Gather all specification data from official sources. Every data point requires a source URL.
1. Identify the model: exact API name, provider, version (if versioned).
2. Locate official documentation pages:
   - Provider model page (capabilities description)
   - Pricing page (input/output token costs)
   - API reference (context window, rate limits, parameter constraints)
   - Changelog or release notes (if version-specific details needed)
3. Extract all 26 SCHEMA.md fields from official sources:
   - `context_window`: integer, in tokens
   - `input_cost_per_1k`: float, USD per 1K input tokens (BASE TIER only)
   - `output_cost_per_1k`: float, USD per 1K output tokens (BASE TIER only)
   - `max_output_tokens`: integer
   - `training_cutoff`: date string
   - Feature booleans: `supports_vision`, `supports_function_calling`, `supports_streaming`, `supports_json_mode`, `supports_system_prompt`, `supports_batch`, `supports_fine_tuning`, `supports_embeddings`
4. Rule: if a data point is unavailable from any official source, set field to `null` — never infer or estimate.
5. Check for existing model_card artifacts for the same model to avoid duplicates.
6. Note the `provider` enum value: one of `anthropic`, `openai`, `google`, `meta`, `mistral`, `cohere`, `other`.
**Verification:** Every non-null specification field has a source URL identified. Pricing uses BASE TIER (not enterprise or volume pricing).
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 4096-byte body limit.
1. Read `SCHEMA.md` — source of truth for all 26 fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Fill frontmatter: all 26 fields (`null` valid for optional; `quality: null` mandatory).
4. Set all feature booleans: `true`, `false`, or `null` if unknown (no strings like "yes").
5. Write `## Boundary` section — adapt from `ARCHITECTURE.md`: what this card IS and IS NOT.
6. Write `## Specifications` table — every row must have a Source URL column, never empty:
   | Field | Value | Source |
   |-------|-------|--------|
   Rows: context_window, input_cost_per_1k, output_cost_per_1k, max_output_tokens, training_cutoff, provider, version.
7. Write `## Capabilities` table — exactly 8 rows matching feature boolean fields:
   | Capability | Supported |
   |-----------|-----------|
   Rows: vision, function_calling, streaming, json_mode, system_prompt, batch, fine_tuning, embeddings.
8. Write `## When to Use` table — >= 5 scenarios:
   | Scenario | Recommendation | Alternative |
   |----------|---------------|-------------|
   Each row: a concrete use case, whether to use this model, and what to use instead if not.
9. Write `## References` — >= 1 official URL. List all source URLs used in Specifications.
Byte budget pseudocode:
```
body_bytes = len(encode_utf8(body_content))
# if body_bytes > 4096: compress When to Use rows, shorten Boundary prose
```
**Verification:** Every Specifications row has a non-empty Source column. Capabilities table has exactly 8 rows. When to Use has >= 5 rows. Body <= 4096 bytes.
### Phase 3: Validate
**Action:** Run all 10 HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches expected pattern for model_card |
| H03 | `kind` is literal string `model_card` |
| H04 | `quality` is `null` |
| H05 | `provider` is one of the recognized enum values |
| H06 | `context_window` is an integer or `null` |
| H07 | `input_cost_per_1k` and `output_cost_per_1k` are floats or `null` |
| H08 | All feature booleans are `true`, `false`, or `null` (no strings) |
| H09 | Every Specifications row has a non-empty Source URL |
| H10 | Body <= 4096 bytes |
Score all 15 SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.

### bld_knowledge_card_model_card.md
---
kind: knowledge_card
id: bld_knowledge_card_model_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for model_card production — atomic searchable facts
sources: model-card-builder MANIFEST.md + SCHEMA.md, Mitchell 2019, LiteLLM, HuggingFace
---

# Domain Knowledge: model_card
## Executive Summary
Model cards are technical specification artifacts for LLMs — they encode pricing, context limits, capability booleans, and use-case guidance into a structured, sourced document. Every specification row must cite a source URL; no self-scoring at creation. They differ from benchmarks (which measure performance), boot configs (which configure runtime), and agents (which define capabilities) by being static reference specs used for model selection and comparison.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (design-time spec) |
| Kind | `model_card` (exact literal) |
| ID pattern | `p02_mc_{provider}_{model_slug}` |
| Required frontmatter | 26 fields |
| Quality gates | 10 HARD + 15 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Domain field | always `model_selection` |
| Modalities | 5 booleans (text_input, text_output, image_input, audio_input, pdf_input) |
| Features | 8 booleans (tool_calling, structured_output, reasoning, etc.) |
| Min When-to-Use rows | 5 |
| Provider enum | anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other |
## Patterns
| Pattern | Application |
|---------|-------------|
| Pricing normalization | Per 1M tokens, USD; `null` for open-weight, `0.00` for free-tier |
| Capability booleans | Always true/false, never string or null |
| Sourced specifications | Every spec row MUST have a source URL — never `-` |
| Identity/Capability/Economics split | Immutable identity, mutable capabilities, volatile pricing |
| Status lifecycle | active -> deprecated -> sunset |
| Freshness gate | 90 days (providers update pricing/features quarterly) |
| Tiered pricing | Lowest tier in frontmatter; document higher tiers in body |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Pricing `0` for open-weight model | Must be `null`; 0 implies free API |
| Spec row without source URL | Fails HARD gate — every row needs citation |
| Modality as string "yes"/"no" | Must be boolean true/false |
| `domain: llm` | Must be literal `model_selection` |
| Self-assigned quality score | `quality` must be null |
| When-to-Use table with < 5 rows | Fails HARD gate — insufficient guidance |
| Capability as prose paragraph | Must be structured boolean fields |
## Application
1. Set `id: p02_mc_{provider}_{model_slug}` — must equal filename stem
2. Populate all 26 required frontmatter fields; set `quality: null`
3. Set `pricing`: base tier per 1M tokens; `null` for open-weight
4. Fill `modalities` (5 booleans) and `features` (8 booleans) from official docs
5. Write `## Specifications` table with Value + Source URL per row
6. Write `## When to Use` decision table with >= 5 rows
7. Validate: body <= 4096 bytes, all specs sourced, 10 HARD + 15 SOFT gates
## References
- model-card-builder SCHEMA.md v2.0.0
- Mitchell et al. 2019 "Model Cards for Model Reporting"
- HuggingFace Model Cards documentation
- LiteLLM model registry (2593 models)

### bld_quality_gate_model_card.md
---
id: p11_qg_model_card
kind: quality_gate
pillar: P11
title: "Gate: Model Card"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: model_card
quality: null
tags: [quality-gate, model-card, llm-spec, P02, provider]
tldr: "Quality gate for model_card artifacts: enforces provider, context window, pricing, and capabilities fields."
density_score: 0.85
---

# Gate: Model Card
## Definition
A `model_card` is a technical spec for a language model: provider, context window, pricing in $/1M tokens, and boolean capability flags. Reference artifact only — not a tutorial. Gates ensure traceability to official sources, comparable pricing, and freshness within 90 days.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mc_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"model_card"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present and non-empty: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `provider`, `model_name`, `context_window`, `pricing`, `capabilities`, `tags`, `tldr` | Incomplete artifact |
| H07 | `provider` matches a known provider enum (Anthropic, OpenAI, Google, Meta, Mistral, Cohere, or documented custom) | Prevents typos that break routing |
| H08 | `context_window` is a positive integer | Core spec field — must be exact |
| H09 | `pricing` field present with at least `input` and `output` keys (numeric $/1M tokens, or `null` for open-weight) | Non-comparable pricing blocks cost analysis |
| H10 | `capabilities` field is a map of boolean flags | Capability claims require verifiable binary form |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names provider + model + primary use case |
| S02 | Pricing normalized to $/1M tokens | 1.0 | Both `input` and `output` prices in $/1M tokens; `null` for open-weight |
| S03 | Capabilities list complete | 1.0 | Flags: vision, audio, function_calling, streaming, fine_tuning, json_mode, code, reasoning |
| S04 | Benchmarks referenced | 1.0 | >= 1 public benchmark (MMLU, HumanEval, MATH) with score and date |
| S05 | Limitations documented | 1.0 | >= 2 specific limitations: context degradation, refusal patterns, knowledge cutoff |
| S06 | `tags` includes `"model-card"` | 0.5 | Minimum tag for routing |
| S07 | Use-case recommendations present | 1.0 | >= 3 recommended use cases and >= 1 not-recommended |
| S08 | API endpoint documented | 0.5 | Names the model identifier string used in API calls |
| S09 | Comparison to alternatives noted | 0.5 | >= 1 comparable model named with key difference stated |
| S10 | Version and spec date accurate | 1.0 | `updated` within 90 days; `data_source` is a live URL |
| S11 | `max_output` field present and positive integer | 0.5 | Required for prompt budget calculations |
| S12 | Density >= 0.85 | 1.0 | No narrative: "great for", "one of the best", "in summary" |
| S13 | `linked_artifacts` field present | 0.5 | Lists related model cards, lenses, or routing rules |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|

### bld_schema_model_card.md
---
kind: schema
id: bld_schema_model_card
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for model_card — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: model_card
## Frontmatter Fields
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p02_mc_{provider}_{slug}) | YES | — | CEX naming |
| kind | literal "model_card" | YES | — | CEX |
| pillar | literal "P02" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| model_name | string | YES | — | Mitchell 2019 |
| provider | enum (see below) | YES | — | LiteLLM |
| model_type | enum (text-generation/embedding/multimodal) | YES | — | HF pipeline_tag |
| status | enum (active/deprecated/sunset) | YES | active | CEX-ext |
| release_date | date or null | REC | null | HF, Meta |
| knowledge_cutoff | YYYY-MM or null | REC | null | Mitchell |
| context_window | integer > 0 | YES | — | Universal |
| max_output | integer > 0 | YES | — | Anthropic SDK |
| modalities | object (5 bools) | YES | — | LangChain |
| features | object (8 bools) | YES | — | LiteLLM |
| pricing | object (see Pricing Policy) | YES | — | LiteLLM |
| domain | literal "model_selection" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| when_to_use | string | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |
## Provider Enum
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
## Pricing Policy
Frontmatter uses BASE TIER (lowest published price for standard API access).
If provider has tiered pricing (e.g., Google <=200K / >200K), use lowest tier.
Document higher tiers in body Specifications table.
```yaml
pricing:
  input: float    # base tier, per 1M tokens, USD. null if open-weight.
  output: float   # base tier, per 1M tokens, USD. null if open-weight.
  cache_read: float or null   # null if provider has no caching
  cache_write: float or null  # null if provider has no symmetric cache write
  unit: per_1M_tokens         # ALWAYS this value
```
Rule: open-weight = null (not 0). Free commercial tier = 0.00 (not null).
## Modalities Object
```yaml
modalities:
  text_input: bool
  text_output: bool
  image_input: bool
  audio_input: bool
  pdf_input: bool
```
## Features Object
```yaml
features:
  tool_calling: bool
  structured_output: bool
  reasoning: bool
  prompt_caching: bool
  code_execution: bool
  web_search: bool
  fine_tunable: bool
  batch_api: bool
```
## Body Structure (required sections)
1. `## Boundary` — model_card EH / NAO EH
2. `## Specifications` — table with Value + Source columns
3. `## Capabilities` — boolean table matching features object
4. `## When to Use` — decision table >= 5 rows with alternatives
5. `## References` — >= 1 official URL
## Constraints
- max_bytes: 4096 (body only, excl frontmatter)
- naming: p02_mc_{provider}_{model_slug}.md
- id == filename stem
- every Specifications row MUST have Source URL (never `-`)
- all modalities/features values MUST be boolean

### bld_examples_model_card.md
---
kind: examples
id: bld_examples_model_card
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of model_card artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: model-card-builder
## Golden Example
INPUT: "Documenta o Claude Sonnet 4 pra decidir roteamento"
OUTPUT:
```yaml
id: p02_mc_anthropic_sonnet_4
kind: model_card
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
model_name: "claude-sonnet-4-20250514"
provider: "anthropic"
model_type: "text-generation"
status: "active"
release_date: "2025-05-14"
knowledge_cutoff: "2025-04"
context_window: 200000
max_output: 16000
modalities:
  text_input: true
  text_output: true
  image_input: true
  audio_input: false
  pdf_input: true
features:
  tool_calling: true
  structured_output: true
  reasoning: true
  prompt_caching: true
  code_execution: true
  web_search: false
  fine_tunable: false
  batch_api: true
pricing:
  input: 3.00
  output: 15.00
  cache_read: 0.30
  cache_write: 3.75
  unit: per_1M_tokens
domain: model_selection
quality: null
tags: [model-card, anthropic, claude-4, sonnet, balanced]
tldr: "Sonnet 4 — anthropic, 200K ctx, $3/$15 per 1M, melhor custo-beneficio analise/pesquisa"
when_to_use: "Analise e pesquisa onde opus eh overkill e haiku insuficiente"
keywords: [anthropic, claude-sonnet-4, balanced]
linked_artifacts:
  primary: null
  related: [p02_mc_anthropic_opus_4]
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
## Boundary
model_card EH: spec tecnica do Sonnet 4 (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.
## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | claude-sonnet-4-20250514 | https://docs.anthropic.com/en/docs/about-claude/models |
| Context | 200K tokens | https://docs.anthropic.com/en/docs/about-claude/models |
| Max Output | 16K tokens | https://docs.anthropic.com/en/docs/about-claude/models |
| Cutoff | Apr 2025 | https://docs.anthropic.com/en/docs/about-claude/models |
| Pricing (input) | $3.00 per 1M | https://docs.anthropic.com/en/docs/about-claude/pricing |
| Pricing (output) | $15.00 per 1M | https://docs.anthropic.com/en/docs/about-claude/pricing |
## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
| Tool Calling | true | parallel supported |
| Structured Output | true | JSON mode |
| Reasoning | true | budget-controlled |
| Prompt Caching | true | 0.1x read cost |
| Code Execution | true | sandbox |
| Web Search | false | — |
| Fine Tuning | false | — |
| Batch API | true | 50% discount |
## When to Use
| Scenario | Sonnet? | Alternative |
|----------|---------|-------------|
| Research + analysis | YES | — |
| Complex architecture, multi-file refactor | NO | Opus ($15/$75) |
| Simple classification, formatting | NO | Haiku ($0.25/$1.25) |
| Vision: PDF/image analysis | YES | — |
| High-volume batch processing | YES | 50% discount via Batch API |
## References
- source: https://docs.anthropic.com/en/docs/about-claude/models
- pricing: https://docs.anthropic.com/en/docs/about-claude/pricing
```
WHY THIS IS GOLDEN:
- Every Spec row has Source URL (never `-`)
- Capabilities: 8 rows, all booleans
- Pricing: concrete, base tier, per_1M_tokens
- quality: null
- When to Use: 5 rows with concrete alternatives and pricing
- Frontmatter strings quoted consistently
## Anti-Example
INPUT: "Documenta o GPT-4"
BAD OUTPUT:
```yaml
id: gpt4_card
kind: model_card
model_name: GPT-4
provider: OpenAI
context_window: "128K"
quality: 9.5
tags: "gpt, openai"
GPT-4 is a powerful model by OpenAI. It can do many things.
Pricing varies by usage tier. Contact OpenAI for details.
```
FAILURES:
1. id: no `p02_mc_` prefix, no provider in id → H02 FAIL
2. provider: uppercase → H08 FAIL
3. context_window: string not integer → H09 FAIL
4. quality: self-assigned 9.5 → H06 FAIL
5. tags: string not list → S02 FAIL
6. lp: missing → H05 FAIL
7. features: missing entirely → S05 FAIL
8. pricing: "varies" → S03 FAIL

### bld_config_model_card.md
---
kind: config
id: bld_config_model_card
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: model_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mc_{provider}_{slug}.md` | `p02_mc_google_gemini_2_5_pro.md` |
| Builder directory | kebab-case | `model-card-builder/` |
| Frontmatter fields | snake_case | `context_window`, `max_output` |
| Provider values | lowercase single word | `anthropic`, `openai`, `google` |
| Model slug | snake_case, no provider prefix | `opus_4`, `gpt_4o`, `gemini_2_5_pro` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
- Output: `cex/P02_model/examples/p02_mc_{provider}_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_mc_{provider}_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Frontmatter: ~800-1200 bytes (26 fields)
- Body: max 4096 bytes (excl frontmatter)
- Total: max 5300 bytes
- Density: >= 0.85
## Provider Enum (same as SCHEMA)
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
If provider not in list: use "other" and add provider name in tags.
## Pricing Policy (aligned with SCHEMA)
- Frontmatter: BASE TIER only (lowest published standard API price)
- If tiered: document higher tiers in body Specifications table
- ALWAYS per_1M_tokens, USD only
- open-weight: null (not 0, not "free")
- commercial free tier: 0.00 (not null)
- cache_write: null if provider has no symmetric cache write price
## Freshness
- updated field must be within 90 days of current date
- If model deprecated: status = "deprecated", linked_artifacts must point to replacement
- Stale cards (>90d) flagged by lifecycle_rule for review

### bld_output_template_model_card.md
---
kind: output_template
id: bld_output_template_model_card
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a model_card
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: model_card
```yaml
id: p02_mc_{{provider}}_{{model_slug}}
kind: model_card
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
model_name: "{{official_model_id}}"
provider: "{{anthropic|openai|google|meta|mistral|cohere|deepseek|alibaba|ai21|other}}"
model_type: "{{text-generation|embedding|multimodal}}"
status: "{{active|deprecated|sunset}}"
release_date: "{{YYYY-MM-DD_or_null}}"
knowledge_cutoff: "{{YYYY-MM_or_null}}"
context_window: {{integer}}
max_output: {{integer}}
modalities:
  text_input: {{bool}}
  text_output: {{bool}}
  image_input: {{bool}}
  audio_input: {{bool}}
  pdf_input: {{bool}}
features:
  tool_calling: {{bool}}
  structured_output: {{bool}}
  reasoning: {{bool}}
  prompt_caching: {{bool}}
  code_execution: {{bool}}
  web_search: {{bool}}
  fine_tunable: {{bool}}
  batch_api: {{bool}}
pricing:
  input: {{float_or_null}}
  output: {{float_or_null}}
  cache_read: {{float_or_null}}
  cache_write: {{float_or_null}}
  unit: per_1M_tokens
domain: model_selection
quality: null
tags: [model-card, {{provider}}, {{model_family}}, {{key_feature}}]
tldr: "{{model_name}} — {{provider}}, {{context}}K ctx, ${{in}}/${{out}} per 1M, {{highlight}}"
when_to_use: "{{one_sentence_decision_condition}}"
keywords: [{{provider}}, {{model_name}}, {{domain_terms}}]
linked_artifacts:
  primary: null
  related: [{{other_model_cards_or_null}}]
data_source: "{{provider_docs_url}}"
## Boundary
model_card EH: spec tecnica de {{model_name}} (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.
## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | {{official_id}} | {{url}} |
| Provider | {{provider}} | {{provider_url}} |
| Context Window | {{ctx}} tokens | {{url}} |
| Max Output | {{max}} tokens | {{url}} |
| Knowledge Cutoff | {{cutoff}} | {{url}} |
| Pricing (input) | ${{in}} per 1M | {{pricing_url}} |
| Pricing (output) | ${{out}} per 1M | {{pricing_url}} |
## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
| Tool Calling | {{bool}} | {{detail_or_dash}} |
| Structured Output | {{bool}} | {{detail_or_dash}} |
| Reasoning | {{bool}} | {{detail_or_dash}} |
| Prompt Caching | {{bool}} | {{detail_or_dash}} |
| Code Execution | {{bool}} | {{detail_or_dash}} |
| Web Search | {{bool}} | {{detail_or_dash}} |
| Fine Tuning | {{bool}} | {{detail_or_dash}} |
| Batch API | {{bool}} | {{detail_or_dash}} |
## When to Use
| Scenario | Use This Model? | Why / Alternative |
|----------|-----------------|-------------------|
| {{scenario_1}} | {{YES/NO/MAYBE}} | {{reason}} |
| {{scenario_2}} | {{YES/NO/MAYBE}} | {{reason}} |
| {{scenario_3}} | {{YES/NO/MAYBE}} | {{reason}} |
| {{scenario_4}} | {{YES/NO/MAYBE}} | {{reason}} |
| {{scenario_5}} | {{YES/NO/MAYBE}} | {{reason}} |
## References
- source: {{provider_docs_url}}
- pricing: {{pricing_page_url}}
```

### bld_architecture_model_card.md
---
kind: architecture
id: bld_architecture_model_card
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of model_card — inventory, dependencies, and architectural position
---

# Architecture: model_card in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 26-field metadata header (id, kind, pillar, provider, model_id, etc.) | model-card-builder | active |
| capabilities_table | Boolean feature matrix (vision, function_calling, streaming, etc.) | author | active |
| pricing_block | Normalized cost per million tokens (input/output/cached) | author | active |
| context_window | Maximum token capacity and effective context details | author | active |
| provider_info | API provider, endpoints, authentication requirements | author | active |
| limitations | Known weaknesses, failure modes, and unsupported scenarios | author | active |
| recommended_uses | Optimal use cases matched to model strengths | author | active |
## Dependency Graph
```
provider_docs  --produces-->  model_card  --consumed_by-->  boot_config
model_card     --consumed_by-->  agent     --referenced_by-> router
model_card     --signals-->      cost_estimate
```
| From | To | Type | Data |
|------|----|------|------|
| provider_docs (external) | model_card | data_flow | official specs, pricing, and capability data |
| model_card | boot_config (P02) | consumes | model selection parameters for agent configuration |
| model_card | agent (P02) | data_flow | capability awareness for task feasibility checks |
| model_card | router (P02) | data_flow | model capabilities inform routing decisions |
| model_card | cost_estimate | produces | token cost projection for budget planning |
| rag_source (P01) | model_card | dependency | external documentation URLs tracked for freshness |
## Boundary Table
| model_card IS | model_card IS NOT |
|---------------|-------------------|
| A technical specification of an LLM with concrete data | An agent identity or persona definition (agent P02) |
| Pricing normalized per million tokens for comparison | A boot-time configuration for a specific satellite (boot_config P02) |
| Feature matrix with boolean capability flags | A routing decision tree (mental_model P02) |
| Provider-specific with API endpoint details | A performance benchmark with measured results (benchmark P07) |
| Updated when provider releases new model versions | A static document — must track provider changes |
| Scoped to one model version from one provider | A comparison table of multiple models |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | provider_docs, rag_source | Official documentation and tracking URLs |
| Identity | frontmatter, provider_info | Model name, version, provider, and API details |
| Specification | capabilities_table, context_window, pricing_block | Technical specs, features, and cost data |
| Guidance | recommended_uses, limitations | Optimal and suboptimal usage patterns |
| Consumers | boot_config, agent, router | Systems that select and configure models |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `model-card-builder` for pipeline function `BECOME`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
