---
id: p01_kc_ollama_deployment_patterns
type: knowledge_card
lp: P01
title: "Ollama Deployment Patterns para Modelos Locais Customizados"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: SHAKA
domain: execution
quality: null
tags: [ollama, deployment, gguf, lora, modelfile, local-llm]
tldr: "Deploy confiavel em Ollama depende de casar base model e adapter, preservar template e escolher quantizacao pelo trade-off entre memoria e qualidade."
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
density_score: null
data_source: "https://docs.ollama.com/modelfile"
---

## Quick Reference

topic: local LLM deployment | scope: Ollama + GGUF/adapter | criticality: high
pipeline: export -> convert -> Modelfile -> ollama create -> validate

## Conceitos Chave

- Mismatch entre base e adapter gera output erratico
- Template de chat precisa ser igual ao usado no treino
- GGUF unico simplifica rollout; base+adapter facilita swap
- Q4_K_M costuma equilibrar memoria, velocidade e qualidade

## Comparativo

| Padrao | Estrutura | Vantagem | Risco |
|--------|-----------|----------|-------|
| GGUF unico | `FROM ./model.gguf` | build simples | adapter nao troca |
| Base+adapter | `FROM base` + `ADAPTER` | swap rapido | base precisa casar |
| Registry HF | `ollama run hf.co/...` | setup minimo | depende de rede |

| Quantizacao | Tamanho | Perda | Uso |
|-------------|---------|-------|-----|
| Q8_0 | maior | minima | qualidade-first |
| Q4_K_M | media | baixa | padrao recomendado |
| Q4_0 | media | moderada | speed-first |
| Q2_K | menor | alta | hardware extremo |

## Regras de Ouro

- SEMPRE validar `FROM` contra o base exato do fine-tune
- SEMPRE fixar `num_ctx` e `SYSTEM` no Modelfile de producao
- NUNCA assumir que adapter compensa template incorreto
- SEMPRE testar latencia e sanidade antes de expor API local

## Code

<!-- lang: dockerfile | purpose: stable Ollama packaging with matching base -->
```dockerfile
FROM llama3.2:8b-instruct-q4_K_M
ADAPTER ./sales-assistant.gguf
PARAMETER num_ctx 4096
PARAMETER temperature 0.2
SYSTEM You answer as a concise e-commerce operations assistant.
```

<!-- lang: bash | purpose: build and smoke-test the packaged model -->
```bash
ollama create codexa-sales -f Modelfile
ollama run codexa-sales "Resuma riscos de margem em 3 linhas."
ollama ps
```

## References

- external: https://docs.ollama.com/modelfile
- external: https://docs.ollama.com/import
- external: https://docs.ollama.com/cli
- deepens: p01_kc_zero_touch_execution
- deepens: p01_kc_cicd_pipeline_architecture
