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
