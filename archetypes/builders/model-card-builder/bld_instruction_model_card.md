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

---

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

**Cross-check:** Is every SCHEMA field populated or explicitly `null`? Does the Capabilities table have exactly 8 rows? Does When to Use have >= 5 rows?

### Phase 4: Output

**Action:** Emit the final artifact at the correct path.

1. Write file to the path defined in `CONFIG.md` for model_card artifacts.
2. Confirm filename stem matches `id` field.
3. Confirm all 5 body sections present and non-empty.
4. Confirm body byte count is <= 4096.
5. Confirm pricing data is BASE TIER (document higher tiers in Specifications notes if relevant).

---

## Output Contract

```
---
id: {{model_card_id_per_schema}}
kind: model_card
pillar: P02
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
model_name: "{{exact_api_identifier}}"
provider: {{anthropic|openai|google|meta|mistral|cohere|other}}
model_version: {{version_string_or_null}}
context_window: {{integer_or_null}}
max_output_tokens: {{integer_or_null}}
input_cost_per_1k: {{float_or_null}}
output_cost_per_1k: {{float_or_null}}
training_cutoff: {{YYYY-MM_or_null}}
supports_vision: {{true|false|null}}
supports_function_calling: {{true|false|null}}
supports_streaming: {{true|false|null}}
supports_json_mode: {{true|false|null}}
supports_system_prompt: {{true|false|null}}
supports_batch: {{true|false|null}}
supports_fine_tuning: {{true|false|null}}
supports_embeddings: {{true|false|null}}
status: active
tags: [model-card, P02, {{provider_tag}}, llm-spec]
quality: null
---

## Boundary
{{what_this_card_is_and_is_not}}

## Specifications
| Field | Value | Source |
|-------|-------|--------|
{{all_spec_rows_with_source_urls}}

## Capabilities
| Capability | Supported |
|-----------|-----------|
{{exactly_8_rows}}

## When to Use
| Scenario | Recommendation | Alternative |
|----------|---------------|-------------|
{{minimum_5_rows}}

## References
{{minimum_1_official_url_all_sources_used}}
```

---

## Validation

- [ ] `kind` is literal string `model_card`
- [ ] `quality` is `null`
- [ ] `provider` is one of the recognized enum values
- [ ] `context_window` and cost fields are integers/floats or `null`
- [ ] All 8 feature booleans are `true`, `false`, or `null` (no strings)
- [ ] Every Specifications row has a non-empty Source URL
- [ ] Capabilities table has exactly 8 rows
- [ ] When to Use table has >= 5 rows
- [ ] All 5 body sections present and non-empty
- [ ] Body <= 4096 bytes
- [ ] Soft gate score >= 8.0 before output

---

## Metacognition

**Does:**
- Research LLM specifications exclusively from official provider sources
- Produce concrete, data-driven model cards with sourced pricing and capability booleans
- Recommend use cases with explicit alternatives for when not to use this model

**Does NOT:**
- Infer or estimate missing data — marks unknown fields `null`
- Generate runtime configuration — route to boot-config-builder
- Perform comparative benchmarking — only documents individual model specs
- Handle agent behavioral definitions — route to agent-builder

**Chaining:** [model selection decision / agent design] -> THIS -> [routing table update / agent tool configuration]
