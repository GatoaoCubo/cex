---
id: p06_enum_llm_providers
kind: enum_def
8f: F1_constrain
pillar: P06
title: "LLM Providers Enum — Multi-Provider Routing Registry"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: schema
quality: 9.1
tags: [enum, llm-providers, routing, multi-provider, registry]
tldr: "Enumeracao canonica dos 7 provedores LLM suportados para routing, config, e validacao de modelo"
when_to_use: "Quando qualquer componente precisa referenciar um provedor LLM — usar este enum como unica fonte de verdade"
keywords: [enum-def, llm-providers, provider-registry, model-routing]
name: llm_providers
values:
  - openai
  - anthropic
  - google
  - aws_bedrock
  - azure
  - cohere
  - mistral
description: "Supported LLM providers for multi-provider routing"
density_score: 1.0
related:
  - bld_examples_model_provider
  - model-provider-builder
  - bld_tools_model_provider
  - p01_kc_model_provider
  - p03_sp_model_provider_builder
  - bld_memory_model_provider
  - bld_tools_model_card
  - bld_collaboration_model_provider
  - bld_config_model_provider
  - bld_examples_model_card
---

## TL;DR

Enum canonica que lista os 7 provedores LLM suportados pelo organization para routing multi-modelo. Qualquer configuracao que referencia um provedor deve usar exatamente um destes valores. Novas adicoes passam por review (impacto em routing, billing, e fallback chains).

## Conceito Central

Uma enum_def e uma lista finita e fechada de valores validos. Diferente de type_def (define estrutura), enum define OPCOES. Toda referencia a provedor LLM no sistema — em configs, routing tables, model cards, billing — DEVE usar um valor desta enum.

Isso previne inconsistencias como `"open_ai"` vs `"openai"` vs `"OpenAI"` em arquivos diferentes.

### Definicao Completa

```yaml
enum:
  id: p06_enum_llm_providers
  name: llm_providers
  description: "Supported LLM providers for multi-provider routing"

  values:
    openai:
      display: "OpenAI"
      api_base: "https://api.openai.com/v1"
      auth_type: api_key
      env_var: OPENAI_API_KEY
      models: [gpt-4o, gpt-4o-mini, o1, o3, o4-mini]
      billing: per_token
      status: active

    anthropic:
      display: "Anthropic"
      api_base: "https://api.anthropic.com/v1"
      auth_type: api_key
      env_var: ANTHROPIC_API_KEY
      models: [claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5-20251001]
      billing: per_token
      status: active  # PRIMARY provider for organization

    google:
      display: "Google AI"
      api_base: "https://generativelanguage.googleapis.com/v1"
      auth_type: api_key
      env_var: GOOGLE_AI_API_KEY
      models: [gemini-2.5-pro, gemini-2.5-flash]
      billing: per_token
      status: active

    aws_bedrock:
      display: "AWS Bedrock"
      api_base: "regional"
      auth_type: iam_role
      env_var: AWS_REGION  # uses IAM, not API key
      models: [claude-via-bedrock, titan-embed]
      billing: per_token
      status: available  # configured but not primary

    azure:
      display: "Azure OpenAI"
      api_base: "https://{deployment}.openai.azure.com"
      auth_type: api_key
      env_var: AZURE_OPENAI_API_KEY
      models: [gpt-4o-via-azure]
      billing: per_token
      status: available

    cohere:
      display: "Cohere"
      api_base: "https://api.cohere.ai/v2"
      auth_type: api_key
      env_var: COHERE_API_KEY
      models: [command-r-plus, embed-v4]
      billing: per_token
      status: experimental

    mistral:
      display: "Mistral AI"
      api_base: "https://api.mistral.ai/v1"
      auth_type: api_key
      env_var: MISTRAL_API_KEY
      models: [mistral-large, codestral]
      billing: per_token
      status: experimental

  constraints:
    case: snake_case          # always lowercase with underscores
    extensible: false         # new providers require PR review
    default: anthropic        # used when provider not specified
    validation: exact_match   # no fuzzy matching allowed
```

## Exemplo Pratico

**Uso em router config** (P02):
```yaml
# p02_router_complexity.yaml
routing_table:
  simple_tasks:
    provider: anthropic        # VALID enum value
    model: claude-haiku-4-5-20251001
  complex_tasks:
    provider: anthropic        # VALID enum value
    model: claude-opus-4-6
  fallback:
    provider: openai           # VALID enum value
    model: gpt-4o
```

**Uso em fallback chain** (P02):
```yaml
# p02_fc_model_cascade.yaml
chain:
  - provider: anthropic       # try first
    model: claude-sonnet-4-6
  - provider: openai          # fallback
    model: gpt-4o
  - provider: google          # last resort
    model: gemini-2.5-flash
```

**Validacao** (rejeita valores invalidos):
```python
VALID_PROVIDERS = ["openai", "anthropic", "google",
                   "aws_bedrock", "azure", "cohere", "mistral"]

def validate_provider(value: str) -> bool:
    if value not in VALID_PROVIDERS:
        raise ValueError(
            f"Invalid provider '{value}'. "
            f"Must be one of: {VALID_PROVIDERS}"
        )
    return True

# validate_provider("open_ai")   -> ValueError!
# validate_provider("anthropic") -> True
```

## Fronteira com Outros Kinds

| Kind | Diferenca |
|------|-----------|
| type_def (P06) | Define ESTRUTURA de dados — enum define VALORES possiveis |
| model_card (P02) | Descreve UM modelo em detalhe — enum lista provedores |
| router (P02) | USA o enum para rotear — enum nao roteia, apenas valida |
| input_schema (P06) | Contrato de entrada — pode CONTER enums, mas nao e um |

## Anti-Patterns

- Strings livres ao inves de enum (`"provider": "whatever"` sem validacao)
- Case misto (`"OpenAI"` vs `"openai"` em configs diferentes)
- Adicionar provider sem atualizar enum (routing table quebra silenciosamente)
- Enum mutavel em runtime (provider list deve ser estatica, configurada em deploy)
- Colocar modelos dentro da enum (modelos mudam frequentemente — provedores nao)

## Referencias

- schema: P06/_schema.yaml (enum_def)
- related: p02_mc_model_card, p02_rt_router, p06_td_type_def

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_model_provider]] | downstream | 0.46 |
| [[model-provider-builder]] | upstream | 0.36 |
| [[bld_tools_model_provider]] | upstream | 0.34 |
| [[p01_kc_model_provider]] | upstream | 0.34 |
| [[p03_sp_model_provider_builder]] | upstream | 0.33 |
| [[bld_memory_model_provider]] | downstream | 0.33 |
| [[bld_tools_model_card]] | upstream | 0.32 |
| [[bld_collaboration_model_provider]] | upstream | 0.31 |
| [[bld_config_model_provider]] | downstream | 0.31 |
| [[bld_examples_model_card]] | downstream | 0.30 |
