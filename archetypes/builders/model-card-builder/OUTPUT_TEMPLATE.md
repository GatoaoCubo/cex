---
lp: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a model_card
---

# Output Template: model_card

```yaml
---
id: p02_mc_{{provider}}_{{model_slug}}
type: model_card
lp: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
model_name: "{{official_model_id}}"
provider: "{{anthropic|openai|google|meta|mistral|cohere|deepseek}}"
model_type: "{{text-generation|embedding|image-generation|multimodal}}"
status: "{{active|deprecated|sunset}}"
release_date: "{{YYYY-MM-DD or null}}"
knowledge_cutoff: "{{YYYY-MM or null}}"
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
when_to_use: "{{decision_condition}}"
keywords: [{{provider}}, {{model_name}}, {{terms}}]
linked_artifacts:
  primary: null
  related: [{{other_model_cards}}]
data_source: "{{provider_docs_url}}"
---

## Boundary
model_card EH: spec tecnica de {{model_name}} (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.

## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | {{official_id}} | {{url}} |
| Provider | {{provider}} | — |
| Context Window | {{ctx}}K tokens | {{url}} |
| Max Output | {{max}}K tokens | {{url}} |
| Architecture | {{arch}} | {{url}} |
| Knowledge Cutoff | {{cutoff}} | {{url}} |

## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
{{for each feature: name | bool | detail}}

## When to Use
| Scenario | Use This Model? | Why / Alternative |
|----------|-----------------|-------------------|
{{>= 3 rows with concrete alternatives}}

## References
- source: {{provider_docs_url}}
- pricing: {{pricing_page_url}}
- related: {{linked_model_cards}}
```
