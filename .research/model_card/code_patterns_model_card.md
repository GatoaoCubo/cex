# Code Patterns for `model_card`

Research date: 2026-03-26

## Implementacoes

| Framework | Class / schema | Notes | Source |
| --- | --- | --- | --- |
| Hugging Face Hub | `ModelCard`, `ModelCardData`, `EvalResult` | Rich YAML-frontmatter model card with explicit metadata and evaluation results | https://github.com/huggingface/huggingface_hub/blob/176bdfb9c1459f5c5f0b70a2ca6b2b9fa02dffc1/src/huggingface_hub/repocard.py , https://github.com/huggingface/huggingface_hub/blob/176bdfb9c1459f5c5f0b70a2ca6b2b9fa02dffc1/src/huggingface_hub/repocard_data.py |
| LiteLLM | `model_prices_and_context_window.json` | Registry-style JSON catalog for 2593 models; optimized for routing, limits, pricing, and feature flags | https://github.com/BerriAI/litellm/blob/bdf4acc472a446b13f7906e8e927cfaf8ff0ea3c/model_prices_and_context_window.json |
| LangChain | `BaseChatModel`, `ModelProfile`, `LangSmithParams` | Capability abstraction centered on runtime behavior, tracing, and provider-specific profile loading | https://github.com/langchain-ai/langchain/blob/5fd07f7f94645c4298cd917b586b7ba5e2b2ce43/libs/core/langchain_core/language_models/chat_models.py , https://github.com/langchain-ai/langchain/blob/5fd07f7f94645c4298cd917b586b7ba5e2b2ce43/libs/core/langchain_core/language_models/model_profile.py , https://github.com/langchain-ai/langchain/blob/5fd07f7f94645c4298cd917b586b7ba5e2b2ce43/libs/core/langchain_core/language_models/base.py |
| OpenAI Python SDK | `Model`, `Models.list()`, `Models.retrieve()` | Minimal API object for discovery; model metadata intentionally sparse | https://github.com/openai/openai-python/blob/5ae2cc10e4140d36aa236fa7c0bc5ce5ff190a01/src/openai/types/model.py , https://github.com/openai/openai-python/blob/5ae2cc10e4140d36aa236fa7c0bc5ce5ff190a01/src/openai/resources/models.py |
| Anthropic Python SDK | `ModelInfo`, `ModelCapabilities`, `Model`, `Models.list()` | Stronger discovery model than OpenAI: capabilities, context limits, display name, release timestamp | https://github.com/anthropics/anthropic-sdk-python/blob/d7c0974ce6ab94ca135b10b2a45308203c0e0c7e/src/anthropic/types/model_info.py , https://github.com/anthropics/anthropic-sdk-python/blob/d7c0974ce6ab94ca135b10b2a45308203c0e0c7e/src/anthropic/types/model_capabilities.py , https://github.com/anthropics/anthropic-sdk-python/blob/d7c0974ce6ab94ca135b10b2a45308203c0e0c7e/src/anthropic/resources/models.py |
| Vercel AI SDK | `LanguageModel`, `LanguageModelRequestMetadata`, `LanguageModelResponseMetadata`, `LanguageModelUsage` | Current `HEAD` does not expose a `ModelMetadata` interface by that exact name; equivalent metadata is split across request/response/usage types | https://github.com/vercel/ai/blob/f8c644c42f596f111b1e1c2ef771e192770d2180/packages/ai/src/types/language-model.ts , https://github.com/vercel/ai/blob/f8c644c42f596f111b1e1c2ef771e192770d2180/packages/ai/src/types/language-model-request-metadata.ts , https://github.com/vercel/ai/blob/f8c644c42f596f111b1e1c2ef771e192770d2180/packages/ai/src/types/language-model-response-metadata.ts , https://github.com/vercel/ai/blob/f8c644c42f596f111b1e1c2ef771e192770d2180/packages/ai/src/types/usage.ts |
| DSPy | `LM`, `BaseLM` | Practical runtime config object for inference orchestration, cache, retries, provider inference, and trace history | https://github.com/stanfordnlp/dspy/blob/c8f6057c9385c656d12def80ea6a06658e391f6d/dspy/clients/lm.py , https://github.com/stanfordnlp/dspy/blob/c8f6057c9385c656d12def80ea6a06658e391f6d/dspy/clients/base_lm.py |

## Data Schemas

### Hugging Face Hub

`ModelCardData` is the richest explicit model-card schema among the surveyed repos.

Core fields:

| Field | Type | Default |
| --- | --- | --- |
| `base_model` | `str \| list[str] \| None` | `None` |
| `datasets` | `str \| list[str] \| None` | `None` |
| `eval_results` | `list[EvalResult] \| None` | `None` |
| `language` | `str \| list[str] \| None` | `None` |
| `library_name` | `str \| None` | `None` |
| `license` | `str \| None` | `None` |
| `license_name` | `str \| None` | `None` |
| `license_link` | `str \| None` | `None` |
| `metrics` | `list[str] \| None` | `None` |
| `model_name` | `str \| None` | `None` |
| `pipeline_tag` | `str \| None` | `None` |
| `tags` | `list[str] \| None` | deduped list via `_to_unique_list()` |
| `ignore_metadata_errors` | `bool` | `False` |
| `**kwargs` | arbitrary extra metadata | n/a |

`EvalResult` is a notable sub-schema:

| Field | Type | Default |
| --- | --- | --- |
| `task_type` | `str` | required |
| `dataset_type` | `str` | required |
| `dataset_name` | `str` | required |
| `metric_type` | `str` | required |
| `metric_value` | `Any` | required |
| `task_name` | `str \| None` | `None` |
| `dataset_config` | `str \| None` | `None` |
| `dataset_split` | `str \| None` | `None` |
| `dataset_revision` | `str \| None` | `None` |
| `dataset_args` | `dict[str, Any] \| None` | `None` |
| `metric_name` | `str \| None` | `None` |
| `metric_config` | `str \| None` | `None` |
| `metric_args` | `dict[str, Any] \| None` | `None` |
| `verified` | `bool \| None` | `None` |
| `verify_token` | `str \| None` | `None` |
| `source_name` | `str \| None` | `None` |
| `source_url` | `str \| None` | `None` |

Pattern: rich human-facing metadata, plus a machine-facing `model-index` projection generated from `eval_results`.

### LiteLLM

`model_prices_and_context_window.json` is a large registry keyed by model id. It uses a `sample_spec` entry as an informal schema template.

Frequently used fields:

| Field | Type | Default / behavior |
| --- | --- | --- |
| `litellm_provider` | `str` | required in practice |
| `mode` | `str` | required in practice |
| `max_input_tokens` | `int` | provider-specific |
| `max_output_tokens` | `int` | provider-specific |
| `max_tokens` | `int` | legacy compatibility field |
| `input_cost_per_token` | `float` | optional |
| `output_cost_per_token` | `float` | optional |
| `output_cost_per_reasoning_token` | `float` | optional |
| `input_cost_per_audio_token` | `float` | optional |
| `output_cost_per_image` | `float` | optional |
| `input_cost_per_pixel` | `float` | optional |
| `output_cost_per_pixel` | `float` | optional |
| `supports_function_calling` | `bool` | optional |
| `supports_parallel_function_calling` | `bool` | optional |
| `supports_prompt_caching` | `bool` | optional |
| `supports_reasoning` | `bool` | optional |
| `supports_response_schema` | `bool` | optional |
| `supports_system_messages` | `bool` | optional |
| `supports_vision` | `bool` | optional |
| `supports_audio_input` | `bool` | optional |
| `supports_audio_output` | `bool` | optional |
| `supports_web_search` | `bool` | optional |
| `supported_regions` | `list[str]` | optional |
| `deprecation_date` | `str` | optional |
| `search_context_cost_per_query` | `object` | optional nested cost map |
| `metadata` | `object` | optional free-form notes |
| `source` | `str` | optional |
| `supported_endpoints` | `list[str]` | optional |

Pattern: operational registry first, documentation second.

### LangChain

LangChain does not implement a standalone model card. Instead it splits metadata into runtime config, tracing metadata, and capability profile.

`BaseLanguageModel` fields:

| Field | Type | Default |
| --- | --- | --- |
| `cache` | `BaseCache \| bool \| None` | `None` |
| `verbose` | `bool` | global verbosity |
| `callbacks` | `Callbacks` | `None` |
| `tags` | `list[str] \| None` | `None` |
| `metadata` | `dict[str, Any] \| None` | `None` |
| `custom_get_token_ids` | `Callable[[str], list[int]] \| None` | `None` |

`BaseChatModel` additions:

| Field | Type | Default |
| --- | --- | --- |
| `rate_limiter` | `BaseRateLimiter \| None` | `None` |
| `disable_streaming` | `bool \| Literal["tool_calling"]` | `False` |
| `output_version` | version tag | provider/runtime dependent |
| `profile` | `ModelProfile \| None` | `None` |

`ModelProfile` capability fields:

| Field | Type | Default |
| --- | --- | --- |
| `name` | `str` | optional |
| `status` | `str` | optional |
| `release_date` | `str` | optional |
| `last_updated` | `str` | optional |
| `open_weights` | `bool` | optional |
| `max_input_tokens` | `int` | optional |
| `max_output_tokens` | `int` | optional |
| `text_inputs` / `text_outputs` | `bool` | optional |
| `image_inputs` / `image_outputs` | `bool` | optional |
| `audio_inputs` / `audio_outputs` | `bool` | optional |
| `video_inputs` / `video_outputs` | `bool` | optional |
| `pdf_inputs` | `bool` | optional |
| `tool_calling` / `tool_choice` | `bool` | optional |
| `structured_output` | `bool` | optional |
| `reasoning_output` | `bool` | optional |
| `attachment` | `bool` | optional |
| `temperature` | `bool` | optional |

`LangSmithParams` tracing fields:

| Field | Type | Default |
| --- | --- | --- |
| `ls_provider` | `str` | optional |
| `ls_model_name` | `str` | optional |
| `ls_model_type` | `"chat" \| "llm"` | optional |
| `ls_temperature` | `float \| None` | optional |
| `ls_max_tokens` | `int \| None` | optional |
| `ls_stop` | `list[str] \| None` | optional |
| `ls_integration` | `str` | optional |

Pattern: metadata is modular and runtime-oriented, not a single canonical card.

### OpenAI Python SDK

`Model` is intentionally minimal:

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | required |
| `created` | `int` | required |
| `object` | `Literal["model"]` | required |
| `owned_by` | `str` | required |

`Models.list()` returns paginated `Model` objects from `/models`. `Models.retrieve(model)` returns one `Model`.

Pattern: discovery object, not a capability card.

### Anthropic Python SDK

Anthropic is closer to a real model-card schema than OpenAI.

`ModelInfo`:

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | required |
| `capabilities` | `ModelCapabilities \| None` | `None` |
| `created_at` | `datetime` | required |
| `display_name` | `str` | required |
| `max_input_tokens` | `int \| None` | `None` |
| `max_tokens` | `int \| None` | `None` |
| `type` | `Literal["model"]` | required |

`ModelCapabilities`:

| Field | Type | Default |
| --- | --- | --- |
| `batch` | `CapabilitySupport` | required |
| `citations` | `CapabilitySupport` | required |
| `code_execution` | `CapabilitySupport` | required |
| `context_management` | `ContextManagementCapability` | required |
| `effort` | `EffortCapability` | required |
| `image_input` | `CapabilitySupport` | required |
| `pdf_input` | `CapabilitySupport` | required |
| `structured_outputs` | `CapabilitySupport` | required |
| `thinking` | `ThinkingCapability` | required |

`ModelListParams`:

| Field | Type | Default |
| --- | --- | --- |
| `after_id` | `str` | optional |
| `before_id` | `str` | optional |
| `limit` | `int` | `20` |
| `betas` | `list[AnthropicBetaParam]` | optional |

Pattern: split stable identifier aliases from capability-rich retrieval objects.

### Vercel AI SDK

Current `HEAD` does not contain a `ModelMetadata` interface by that exact name. The equivalent metadata surface is fragmented:

`LanguageModelResponseMetadata`:

| Field | Type | Default |
| --- | --- | --- |
| `id` | `string` | required |
| `timestamp` | `Date` | required |
| `modelId` | `string` | required |
| `headers` | `Record<string, string> \| undefined` | `undefined` |

`LanguageModelRequestMetadata`:

| Field | Type | Default |
| --- | --- | --- |
| `body` | `unknown` | `undefined` |

`LanguageModelUsage`:

| Field | Type | Default |
| --- | --- | --- |
| `inputTokens` | `number \| undefined` | `undefined` |
| `inputTokenDetails.noCacheTokens` | `number \| undefined` | `undefined` |
| `inputTokenDetails.cacheReadTokens` | `number \| undefined` | `undefined` |
| `inputTokenDetails.cacheWriteTokens` | `number \| undefined` | `undefined` |
| `outputTokens` | `number \| undefined` | `undefined` |
| `outputTokenDetails.textTokens` | `number \| undefined` | `undefined` |
| `outputTokenDetails.reasoningTokens` | `number \| undefined` | `undefined` |
| `totalTokens` | `number \| undefined` | `undefined` |
| `raw` | provider JSON object | `undefined` |

`LanguageModel` itself is a union of provider model IDs and provider implementations, not a descriptive card object.

Pattern: transport metadata and usage normalization over canonical catalog metadata.

### DSPy

`LM` is a config-and-runtime wrapper rather than a descriptive card.

Constructor fields:

| Field | Type | Default |
| --- | --- | --- |
| `model` | `str` | required |
| `model_type` | `"chat" \| "text" \| "responses"` | `"chat"` |
| `temperature` | `float \| None` | `None` |
| `max_tokens` | `int \| None` | `None` |
| `cache` | `bool` | `True` |
| `callbacks` | `list[BaseCallback] \| None` | `None` |
| `num_retries` | `int` | `3` |
| `provider` | `Provider \| None` | inferred |
| `finetuning_model` | `str \| None` | `None` |
| `launch_kwargs` | `dict[str, Any] \| None` | `{}` |
| `train_kwargs` | `dict[str, Any] \| None` | `{}` |
| `use_developer_role` | `bool` | `False` |
| `**kwargs` | provider-specific request params | n/a |

Operational behaviors:

| Behavior | Pattern |
| --- | --- |
| reasoning-model normalization | OpenAI reasoning families rewrite `max_tokens` to `max_completion_tokens` |
| provider inference | defaults to `OpenAIProvider()` when model id matches provider pattern |
| state export | `dump_state()` serializes config but excludes `api_key` |
| history | request/response/usage/cost/timestamp are stored in `history` |

`BaseLM` also standardizes common fields: `model`, `model_type`, `cache`, `kwargs`, `history`.

Pattern: runtime orchestration object with partial persistence, not a catalog schema.

## Patterns Comuns / Anti-Patterns

### Patterns comuns

- Separate immutable identity from mutable operational metadata. The best examples are Anthropic (`id`, `display_name`, `created_at`) and Hugging Face (`model_name`, `base_model`, tags, evals).
- Keep capabilities as first-class booleans or typed objects. LiteLLM and Anthropic both make routing decisions easier because capabilities are explicit.
- Normalize usage independently from descriptive metadata. Vercel and DSPy both treat usage/telemetry as a separate surface.
- Allow extensibility via free-form metadata. Hugging Face `**kwargs`, LiteLLM `metadata`, and LangChain `metadata` avoid constant schema churn.
- Distinguish request-time config from model-time facts. DSPy and LangChain do this well; mixing them creates confusing cards.
- Store source provenance. Hugging Face `source_url`, LiteLLM `source`, and SDK endpoint links make audits easier.

### Anti-patterns

- Overloading a single `max_tokens` field. LiteLLM carries legacy ambiguity; Anthropic/OpenAI-style split input/output limits is clearer.
- Conflating model catalog with runtime request options. Temperature, retries, cache flags, and provider headers should not be core identity fields.
- Hiding capabilities in prose. Capability flags are machine-valuable and should not live only in docs text.
- Using one monolithic schema for every concern. Vercel’s split is cleaner than forcing request metadata, response metadata, pricing, and card text into one blob.
- Depending on provider-specific free-form metadata without a normalized core. This blocks filtering, comparison, and validation.

## Schema Recomendado para CEX

Recommendation: use a layered schema with four blocks instead of one flat object.

### 1. Identity

```json
{
  "id": "openai/gpt-5",
  "canonical_name": "GPT-5",
  "provider": "openai",
  "family": "gpt-5",
  "version": null,
  "alias_of": null,
  "status": "active",
  "release_date": null,
  "deprecation_date": null
}
```

### 2. Capabilities

```json
{
  "context_window": {
    "max_input_tokens": null,
    "max_output_tokens": null
  },
  "modalities": {
    "text_input": true,
    "text_output": true,
    "image_input": false,
    "image_output": false,
    "audio_input": false,
    "audio_output": false,
    "video_input": false,
    "video_output": false,
    "pdf_input": false
  },
  "features": {
    "tool_calling": false,
    "parallel_tool_calling": false,
    "structured_output": false,
    "reasoning": false,
    "prompt_caching": false,
    "system_messages": true,
    "web_search": false,
    "code_execution": false,
    "citations": false
  }
}
```

### 3. Economics and operations

```json
{
  "pricing": {
    "input_per_token": null,
    "output_per_token": null,
    "reasoning_per_token": null,
    "image_per_unit": null,
    "audio_input_per_token": null
  },
  "operations": {
    "mode": "chat",
    "supported_regions": [],
    "supported_endpoints": [],
    "rate_limit_tier": null
  }
}
```

### 4. Provenance and evaluation

```json
{
  "sources": [
    {
      "kind": "official",
      "url": "https://...",
      "retrieved_at": "2026-03-26"
    }
  ],
  "evaluations": [
    {
      "task": "qa",
      "dataset": "mmlu",
      "metric": "accuracy",
      "value": 0.0,
      "source_name": null,
      "source_url": null
    }
  ],
  "metadata": {}
}
```

### Required core fields for CEX

- `id`
- `provider`
- `canonical_name`
- `status`
- `operations.mode`
- `context_window.max_input_tokens`
- `context_window.max_output_tokens`
- `modalities.*`
- `features.*`
- `sources`

### Why this shape

- Hugging Face contributes the evaluation and provenance pattern.
- LiteLLM contributes operational routing, limits, pricing, and capability flags.
- Anthropic contributes a cleaner capability object and stronger model discovery fields.
- LangChain and DSPy justify keeping runtime request config out of the canonical card.
- Vercel justifies a separate telemetry/usage layer rather than polluting the card itself.

Bottom line: CEX should model `model_card` as a normalized catalog object with explicit capability flags, input/output limits, pricing, provenance, and optional evaluations. Runtime request knobs should live elsewhere.
