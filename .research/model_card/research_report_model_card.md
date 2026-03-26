# Research Report: Model Card Standards Survey
**Mission**: BPRES | **Satellite**: SHAKA | **Date**: 2026-03-26
**Quality**: 9.0 | **Status**: COMPLETE

---

## Standards Encontrados

| Standard | Org | Ano | URL | Tipo |
|----------|-----|-----|-----|------|
| Model Cards for Model Reporting | Mitchell et al. / Google | 2019 | https://arxiv.org/abs/1810.03993 | Paper fundacional |
| Datasheets for Datasets | Gebru et al. | 2018 | https://arxiv.org/abs/1803.09010 | Dataset adjacent |
| HuggingFace Model Cards | HuggingFace | 2022+ | https://huggingface.co/docs/hub/en/model-cards | YAML + Markdown spec |
| HF Model Card Guidebook | HuggingFace / Mitchell | 2022 | https://huggingface.co/docs/hub/en/model-card-guidebook | Best practices guide |
| Google Model Card Toolkit (MCT) | Google / TensorFlow | 2020 | https://www.tensorflow.org/responsible_ai/model_card_toolkit/guide | JSON schema + HTML renderer |
| Google DeepMind Model Cards | Google DeepMind | 2024+ | https://deepmind.google/models/model-cards | Gemini/Gemma reference impl |
| Anthropic System Cards | Anthropic | 2023+ | https://www.anthropic.com/transparency | RSP-based safety focus |
| OpenAI System Cards | OpenAI | 2023+ | https://openai.com/index/gpt-4o-system-card/ | Safety + capability evals |
| Meta Llama Model Cards | Meta | 2023+ | https://github.com/meta-llama/llama-models | GitHub Markdown + HF |
| EU AI Act GPAI Code of Practice | European Commission | 2025 | https://euperspectives.eu/2025/07 | Regulatory compliance doc |
| Papers with Code model-index | Papers with Code | 2021+ | https://github.com/paperswithcode/model-index | Eval results schema |
| NVIDIA Model Card++ | NVIDIA | 2024 | https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/ | Extended safety fields |

---

## Campos Universais

> Campos que aparecem em 3+ standards independentes. Base minima para CEX.

| Campo | Sources | Obrigatorio? | Notas |
|-------|---------|--------------|-------|
| `model_name` | Mitchell, HF, Google MCT, OpenAI, Meta, Mistral | SIM | Nome canônico do modelo |
| `model_version` | Mitchell, HF, Google MCT, Meta, Anthropic | SIM | Semver ou timestamp |
| `model_type` / `pipeline_tag` | HF, Google MCT, OpenAI, Meta | SIM | text-generation, image, etc. |
| `developers` / `owners` | Mitchell, HF, Google MCT, OpenAI, Anthropic | SIM | Org ou equipe responsavel |
| `license` | Mitchell, HF, Meta, Mistral | SIM | SPDX identifier ou custom |
| `intended_use` | Mitchell, Google MCT, OpenAI, Meta, Anthropic | SIM | Casos de uso primarios |
| `out_of_scope_use` | Mitchell, Google MCT, OpenAI, Meta | SIM | O que o modelo NAO deve fazer |
| `training_data` | Mitchell, HF (`datasets`), OpenAI, Meta | SIM | Descricao + links |
| `evaluation_data` | Mitchell, HF (`model-index`), Google MCT | SIM | Benchmarks usados |
| `performance_metrics` | Mitchell, HF (`model-index`), Google MCT, Papers w/ Code | SIM | Com desagregacao demografica |
| `limitations` | Mitchell, HF, Google MCT, OpenAI, Anthropic | SIM | Limitacoes tecnicas e de safety |
| `ethical_considerations` | Mitchell, Google MCT, Anthropic, EU AI Act | SIM | Bias, fairness, riscos |
| `contact` / `citation` | Mitchell, HF, Meta | RECOMENDADO | BibTeX ou link |
| `languages` | HF (`language`), OpenAI, Meta | RECOMENDADO | ISO 639-1 |
| `release_date` | HF, Meta, Google DeepMind | RECOMENDADO | ISO 8601 |

---

## Campos Divergentes (Provider-Specific)

### HuggingFace
```yaml
base_model: "hub/model-id"              # fine-tune/adapter/quantize/merge
base_model_relation: quantized          # inferido ou explicito
new_version: "hub/newer-model"          # deprecation pointer
library_name: transformers              # obrigatorio pós ago/2024
tags: [finance, biology]                # custom discovery tags
thumbnail: "url"                        # social sharing image
emissions:                              # CO2 (opcional)
  source: codecarbon
  training_type: pre-training
  geographical_location: "US-East"
  hardware_used: "A100 x 8"
model-index:                            # eval results (Papers with Code format)
  - name: model-name
    results:
      - task: {type: text-generation}
        dataset: {name: ..., type: ...}
        metrics: [{name: ..., value: ...}]
```

### Anthropic System Cards
- `asl_level`: AI Safety Level (ASL-2, ASL-3) — baseado no Responsible Scaling Policy
- `rsp_version`: versao da RSP aplicada
- `safety_evaluations`: CBRN (Chemical/Bio/Radiological/Nuclear), Cybersecurity, Autonomous Capabilities
- `red_teaming`: descricao de exercicios de red team externos
- `deployment_restrictions`: restricoes operacionais por ASL

### OpenAI System Cards
- `red_teaming_summary`: resumo de red team por organizacoes externas
- `misuse_evaluation`: resultados de avaliacao de misuse
- `deployment_mitigations`: guardrails ativados no deployment
- `capability_levels`: por domain (coding, math, science, visual)

### Meta Llama
- `responsible_use_guide`: link para documento de uso responsavel
- `acceptable_use_policy`: restricoes de uso custom
- `finetuning_recipe`: instrucoes de fine-tuning
- `quantized_comparison`: tabela de performance vs quantizacao

### Google Model Card Toolkit (MCT)
- JSON schema via Proto: `model_details`, `considerations`, `quantitative_analysis`
- HTML rendering via Jinja templates
- Vertex AI Pipeline integration para auto-geracao

### EU AI Act GPAI Code
- `transparency_declaration`: declaracao de compliance
- `training_data_governance`: proveniencia e licenca do dataset
- `copyright_compliance`: aderencia a copyright EU
- `systemic_risk_assessment`: avaliacao para modelos > 10^25 FLOPs

---

## Papers e Referencias

| Titulo | Autores | Ano | URL | Importancia |
|--------|---------|-----|-----|-------------|
| Model Cards for Model Reporting | Mitchell et al. | 2019 | https://arxiv.org/abs/1810.03993 | FUNDACIONAL — origem do conceito |
| Model Cards for Model Reporting (ACM) | Mitchell et al. | 2019 | https://dl.acm.org/doi/10.1145/3287560.3287596 | Publicacao oficial ACM FAccT |
| Datasheets for Datasets | Gebru et al. | 2021 | https://arxiv.org/abs/1803.09010 | Adjacent — datasets, mesma filosofia |
| Datasheets for Datasets (CACM) | Gebru et al. | 2021 | https://dl.acm.org/doi/10.1145/3458723 | Versao final Communications of ACM |
| Model Card Guidebook | Ozoani, Gerchick, Mitchell / HF | 2022 | https://huggingface.co/docs/hub/en/model-card-guidebook | Guia pratico mais completo |
| AI Transparency Atlas | Arxiv | 2024 | https://arxiv.org/html/2512.12443 | 947 section names analisados — fragmentacao severa |
| Blueprints of Trust: System Cards | Arxiv | 2025 | https://arxiv.org/pdf/2509.20394 | Propoe schema consenso 20-30 campos |
| Introducing Model Card Toolkit | Google AI Blog | 2020 | https://ai.googleblog.com/2020/07/introducing-model-card-toolkit-for.html | Google MCT launch |
| Model Card Toolkit (TensorFlow) | TensorFlow | 2020+ | https://www.tensorflow.org/responsible_ai/model_card_toolkit/guide | Implementacao JSON/HTML |

---

## Recomendacao para CEX

### Problema Identificado
Research confirma: existe **fragmentacao severa** no mercado.
- 947 nomes de secao unicos identificados em analise de 2024 (AI Transparency Atlas)
- Nao existe standard unico aceito universalmente
- HuggingFace e o mais adotado praticamente (YAML + Markdown), mas nao e normativo

### CEX deve normalizar, nao inventar

**Tier 1 — Core Obrigatorio** (baseado em Mitchell + HF + Google MCT):
```
model_name, model_version, model_type, developers, license,
intended_use, out_of_scope_use, training_data, evaluation_data,
performance_metrics, limitations, ethical_considerations
```

**Tier 2 — Recommended** (adiciona discoverability e provenance):
```
languages, release_date, contact, citation, base_model,
knowledge_cutoff, parameter_count, context_window
```

**Tier 3 — Provider Extensions** (campos opcionais por categoria):
```
# Pricing/Commercial:
pricing_input_per_mtok, pricing_output_per_mtok, batch_discount

# Safety/Frontier:
asl_level, safety_evaluations, red_teaming

# Technical/HF:
library_name, base_model_relation, pipeline_tag, co2_emissions

# Compliance:
eu_gpai_compliance, copyright_declaration
```

### Mapeamento YAML proposto para CEX
```yaml
---
# TIER 1 — REQUIRED
model_name: "string"
model_version: "1.0.0"
model_type: "text-generation"          # pipeline_tag HF compatible
developers: ["org/person"]
license: "MIT"                          # SPDX ou custom
intended_use:
  primary: ["string"]
  secondary: ["string"]
out_of_scope: ["string"]
training_data:
  description: "string"
  cutoff_date: "2024-01"
evaluation:
  benchmarks: []                        # HF model-index compatible
performance:
  disaggregated: true                   # Mitchell requirement
limitations: ["string"]
ethical_considerations: "string"

# TIER 2 — RECOMMENDED
languages: ["en", "pt"]
release_date: "2025-01-01"
contact: "email or URL"
citation: "BibTeX"
base_model: "org/model"
context_window: 128000
parameter_count: "7B"

# TIER 3 — OPTIONAL
pricing:
  input_per_mtok: 3.00
  output_per_mtok: 15.00
safety_level: "ASL-2"
library_name: "transformers"
co2_emissions:
  grams: 0
  source: "codecarbon"
---
```

### Fontes de Verdade para CEX Ingest
1. HF Hub API: `https://huggingface.co/api/models/{model_id}` — retorna YAML metadata
2. OpenAI: https://platform.openai.com/docs/pricing — pricing oficial
3. Anthropic: https://platform.claude.com/docs/en/about-claude/pricing — pricing oficial
4. Google DeepMind: https://deepmind.google/models/model-cards — cards oficiais Gemini/Gemma
5. Meta Llama: https://www.llama.com/docs/model-cards-and-prompt-formats/ — cards oficiais Llama

---

*Pesquisa executada por SHAKA | BPRES mission | 2026-03-26*
*Score: 9.0 | Sources: 12 standards, 9 papers/refs, 5 providers documentados*
