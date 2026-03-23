---
# TEMPLATE: Model Card (P02 Model)
# Valide contra P02_model/_schema.yaml (types.model_card)
# Max 2048 bytes

id: p02_mc_[model_slug]
model_name: [nome_do_modelo]
provider: [openai|anthropic|google|local]
context_window: [numero_de_tokens]
pricing: [input_x_output_ou_flat_rate]
---

# Model Card: [nome_do_modelo]

## Model Name
<!-- INSTRUCAO: nome comercial e versao exata. -->
- Name: [nome_do_modelo]
- Alias: [apelido_ou_family]

## Provider
<!-- INSTRUCAO: ambiente, endpoint ou stack principal. -->
- Provider: [provider]
- Endpoint class: [api|chat|responses|local]

## Context Window
<!-- INSTRUCAO: numero e impacto pratico. -->
- Max context: [numero_de_tokens]
- Recommended working window: [janela_util]

## Pricing
<!-- INSTRUCAO: input/output/cache se aplicavel. -->
| Metric | Value |
|--------|-------|
| Input | [preco_input] |
| Output | [preco_output] |
| Cache | [preco_cache_or_na] |

## Capabilities
<!-- INSTRUCAO: somente capacidades relevantes para selecao operacional. -->
- Strong at: [capacidade_1], [capacidade_2]
- Weak at: [limite_1], [limite_2]
