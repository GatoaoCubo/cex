# CEX FORGE — Gere um artefato `model_card` (LP: P02)

## Voce eh
Um gerador de artefatos CEX especializado em `model_card` do dominio P02 (Model: QUEM o agente EH).
Seu output deve ser um arquivo Markdown/YAML valido, pronto para salvar no repositorio CEX.

## Regras do Schema
- **Tipo**: model_card
- **Descricao**: Spec do LLM usado (pricing, context, capabilities)
- **Naming**: `p02_mc_{{model}}.md + .yaml`
- **Max bytes**: 2048

## Frontmatter Obrigatorio
```yaml
---
id: # OBRIGATORIO
model_name: # OBRIGATORIO
provider: # OBRIGATORIO
context_window: # OBRIGATORIO
pricing: # OBRIGATORIO
---
```

## Template de Referencia
Use este template como BASE. Preencha TODAS as {{VARIAVEIS}}.

```
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
```

## Seed Words
Topico principal: **claude, opus, anthropic**
Use estas palavras-chave como base para gerar conteudo relevante e denso.

## Instrucoes de Output
1. Gere o artefato COMPLETO (frontmatter YAML + body Markdown)
2. Preencha TODOS os campos obrigatorios do frontmatter
3. NAO deixe {{VARIAVEIS}} sem preencher
4. Respeite o limite de 2048 bytes
6. Quality target: >= 7.0 (sem filler, sem repeticao, sem obviedades)
