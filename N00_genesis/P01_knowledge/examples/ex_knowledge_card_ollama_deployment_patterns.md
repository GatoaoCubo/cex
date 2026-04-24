---
id: p01_kc_ollama_deployment_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Ollama Deployment Patterns para Modelos Locais Customizados"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: execution
quality: 9.1
tags: [ollama, deployment, gguf, lora, modelfile, local-llm]
tldr: "Deploy Ollama depende de casar base e adapter, preservar template e escolher quantizacao entre memoria e qualidade."
when_to_use: "Empacotar modelo fine-tuned para Ollama ou diagnosticar output ruim em deploy local"
keywords: [ollama_deployment, modelfile, gguf_import, lora_adapter, quantization]
long_tails:
  - "Como subir modelo customizado no Ollama sem degradar output"
  - "Quando usar GGUF unico vs base mais adapter no Ollama"
axioms:
  - "SEMPRE usar o mesmo base model do treinamento ao aplicar adapter"
  - "NUNCA trocar template de chat entre treino e inferencia"
linked_artifacts:
  primary: null
  related: [p01_kc_zero_touch_execution, p01_kc_cicd_pipeline_architecture]
density_score: 1.0
data_source: "https://docs.ollama.com/modelfile"
related:
  - kc_ollama_deployment_guide
  - p02_fc_cex_model_fallback
  - p03_sp_finetune_config_builder
  - n05_readme_install
  - p01_kc_finetune_config
  - bld_collaboration_finetune_config
  - claude_vs_free_decision_matrix
  - bld_tools_model_provider
  - bld_instruction_finetune_config
  - n05_output_monetization_infra
---

## Quick Reference

topic: local LLM deployment | scope: Ollama + GGUF/adapter | criticality: high
pipeline: export -> convert -> Modelfile -> ollama create -> validate

## Conceitos Chave

- Mismatch entre base e adapter gera output erratico
- Template de chat precisa casar com o do treino
- GGUF unico simplifica; base+adapter facilita swap
- Q4_K_M equilibra memoria, velocidade e qualidade

## Comparativo

| Padrao | Estrutura | Vantagem | Desvantagem |
|--------|-----------|----------|-------------|
| GGUF unico | `FROM ./model.gguf` | Build simples | Adapter nao troca |
| Base+adapter | `FROM base` + `ADAPTER` | Swap rapido | Base precisa casar |
| Registry HF | `ollama run hf.co/...` | Setup minimo | Depende de rede |

| Quantizacao | Reducao | Perda | Caso de uso |
|-------------|---------|-------|-------------|
| Q8_0 | ~50% | Minima | Qualidade-first |
| Q5_K_M | ~62% | Baixa | Balanceado plus |
| Q4_K_M | ~75% | Baixa | Padrao recomendado |
| Q4_0 | ~75% | Moderada | Speed-first |
| Q2_K | ~87% | Alta | Hardware extremo |

| Sintoma | Causa provavel | Correcao |
|---------|----------------|----------|
| Output erratico | Base diferente do treino | Usar base exato |
| Formato errado | Template incorreto | Setar TEMPLATE |
| Lentidao | Fallback pra CPU | Checar ollama ps |
| OOM | Context grande demais | Reduzir num_ctx |
| Adapter ignorado | Path relativo | Usar path absoluto |

| Cenario | Padrao ideal | Quantizacao |
|---------|-------------|-------------|
| Prototipo rapido | Registry HF | Q4_K_M |
| Producao interna | GGUF unico | Q4_K_M ou Q8_0 |
| Multi-adapter dev | Base+adapter | Q4_K_M |
| Edge device | GGUF unico | Q2_K |
| Alta fidelidade | GGUF unico | Q8_0 |

## Regras de Ouro

- SEMPRE validar FROM contra o base exato do fine-tune
- SEMPRE fixar num_ctx e SYSTEM no Modelfile de prod
- NUNCA assumir que adapter compensa template incorreto
- SEMPRE testar latencia e sanidade antes de expor API

## Code

<!-- lang: dockerfile | purpose: stable Ollama packaging -->
```dockerfile
FROM llama3.2:8b-instruct-q4_K_M
ADAPTER ./sales-assistant.gguf
PARAMETER num_ctx 4096
PARAMETER temperature 0.2
SYSTEM You answer as a concise e-commerce assistant.
```

<!-- lang: bash | purpose: build and smoke-test -->
```bash
ollama create organization-sales -f Modelfile
ollama run organization-sales "Resuma riscos de margem em 3 linhas."
ollama ps
```

## References

- external: https://docs.ollama.com/modelfile
- external: https://docs.ollama.com/import
- external: https://docs.ollama.com/cli
- deepens: p01_kc_zero_touch_execution
- deepens: p01_kc_cicd_pipeline_architecture


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_ollama_deployment_guide]] | sibling | 0.35 |
| [[p02_fc_cex_model_fallback]] | downstream | 0.24 |
| [[p03_sp_finetune_config_builder]] | downstream | 0.21 |
| [[n05_readme_install]] | downstream | 0.21 |
| [[p01_kc_finetune_config]] | sibling | 0.20 |
| [[bld_collaboration_finetune_config]] | downstream | 0.19 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.19 |
| [[bld_tools_model_provider]] | downstream | 0.18 |
| [[bld_instruction_finetune_config]] | downstream | 0.18 |
| [[n05_output_monetization_infra]] | downstream | 0.18 |
