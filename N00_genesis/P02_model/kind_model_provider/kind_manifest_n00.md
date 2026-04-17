---
id: n00_model_provider_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Model Provider -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, model_provider, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Model Provider defines an LLM provider adapter that enables CEX to route requests to Claude, GPT, Gemini, or Ollama through a unified interface. It specifies the API endpoint, authentication method, supported models, rate limits, and SDK adapter class. The CALL function (F5) uses model_provider artifacts to select and invoke the correct provider at runtime.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `model_provider` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Provider name and environment |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider_name | enum | yes | anthropic\|openai\|google\|ollama\|litellm |
| base_url | string | yes | API base URL or local endpoint |
| auth_method | enum | yes | api_key\|oauth\|none\|bearer |
| rate_limit_rpm | int | no | Requests per minute limit |
| available_models | list | yes | Model identifiers this provider supports |
| local | bool | yes | Whether this is a local inference provider |

## When to use
- When adding a new LLM provider to the CEX routing layer
- When configuring provider-specific auth or rate limits
- When documenting a custom LiteLLM proxy setup

## Builder
`archetypes/builders/model_provider-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind model_provider --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N05 or N07)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- operators and infrastructure engineers
- `{{DOMAIN_CONTEXT}}` -- deployment environment and provider contract

## Example (minimal)
```yaml
---
id: model_provider_anthropic_prod
kind: model_provider
pillar: P02
nucleus: n05
title: "Anthropic Claude Production"
version: 1.0
quality: null
---
provider_name: anthropic
base_url: https://api.anthropic.com
auth_method: api_key
rate_limit_rpm: 50
available_models: [claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5]
local: false
```

## Related kinds
- `model_card` (P02) -- individual model documentation within this provider
- `fallback_chain` (P02) -- chains that use this provider
- `boot_config` (P02) -- nucleus boot referencing this provider
