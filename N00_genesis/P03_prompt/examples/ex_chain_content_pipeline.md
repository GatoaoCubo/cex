---
id: p03_ch_content_pipeline
kind: chain
pillar: P03
title: Content Pipeline Chain (Research to Publish)
steps: 4
flow: research -> draft -> review -> publish
quality: 9.0
---

# Chain: Content Pipeline

## Purpose
Pipeline de 4 etapas para producao de conteudo de marketing: pesquisa de mercado, rascunho do conteudo, revisao de qualidade e formatacao para publicacao. Cada step recebe o output do anterior via data contract explicito. Se um step falhar, retry com fallback model antes de abortar.

## Steps

### Step 1: Research
**Modelo recomendado**: sonnet (rapido, bom para sintese)
**Fallback**: haiku (se sonnet indisponivel ou timeout > 30s)

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "topic": {"type": "string", "description": "Assunto principal do conteudo"},
    "target_audience": {"type": "string", "description": "Publico-alvo (ex: empreendedores BR 25-45)"},
    "content_type": {"type": "string", "enum": ["blog_post", "social_media", "email", "ad_copy"]},
    "keywords": {"type": "array", "items": {"type": "string"}, "minItems": 3, "maxItems": 10}
  },
  "required": ["topic", "target_audience", "content_type"]
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "market_context": {"type": "string", "maxLength": 500},
    "competitor_angles": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
    "key_insights": {"type": "array", "items": {"type": "string"}, "minItems": 3},
    "tone_recommendation": {"type": "string", "enum": ["formal", "casual", "provocative", "educational"]},
    "hooks": {"type": "array", "items": {"type": "string"}, "minItems": 2, "maxItems": 5}
  },
  "required": ["market_context", "key_insights", "tone_recommendation", "hooks"]
}
```

### Step 2: Draft
**Modelo recomendado**: opus (criatividade + qualidade)
**Fallback**: sonnet

**Input**: Output completo do Step 1 + input original (topic, target_audience, content_type, keywords)

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string", "maxLength": 100},
    "body": {"type": "string", "minLength": 200},
    "cta": {"type": "string", "description": "Call to action principal"},
    "hashtags": {"type": "array", "items": {"type": "string"}, "maxItems": 10},
    "estimated_read_time_min": {"type": "number"}
  },
  "required": ["title", "body", "cta"]
}
```

### Step 3: Review
**Modelo recomendado**: sonnet (analise critica objetiva)
**Fallback**: haiku

**Input**: Output do Step 2 + tone_recommendation do Step 1

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "score": {"type": "number", "minimum": 0, "maximum": 10},
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
          "location": {"type": "string"},
          "issue": {"type": "string"},
          "fix": {"type": "string"}
        }
      }
    },
    "approved": {"type": "boolean"},
    "revised_body": {"type": "string", "description": "Versao corrigida se approved=false"}
  },
  "required": ["score", "issues", "approved"]
}
```

### Step 4: Publish
**Modelo recomendado**: haiku (formatacao simples, rapido)
**Fallback**: nenhum (step determinista, nao deve falhar)

**Input**: Output do Step 3 (revised_body se existir, senao body original do Step 2) + content_type do Step 1

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "formatted_content": {"type": "string"},
    "platform_metadata": {
      "type": "object",
      "properties": {
        "platform": {"type": "string"},
        "char_count": {"type": "integer"},
        "within_limits": {"type": "boolean"},
        "scheduled_for": {"type": "string", "format": "date-time"}
      }
    },
    "status": {"type": "string", "enum": ["ready", "needs_revision", "published"]}
  },
  "required": ["formatted_content", "platform_metadata", "status"]
}
```

## Data Flow
```text
[User Input] --> Step 1: Research (sonnet)
                    |
                    v
              {market_context, key_insights, tone, hooks}
                    |
                    v
              Step 2: Draft (opus)
                    |
                    v
              {title, body, cta, hashtags}
                    |
                    v
              Step 3: Review (sonnet)
                    |
                   / \
                  /   \
           approved?   not approved?
              |             |
              v             v
         body original  revised_body
              \           /
               \         /
                v       v
              Step 4: Publish (haiku)
                    |
                    v
              {formatted_content, platform_metadata, status}
```

## Error Handling
| Step | Error | Action |
|------|-------|--------|
| Any | Model timeout (>30s) | Retry 1x with fallback model |
| Any | Fallback also fails | Return partial result with `status: "needs_revision"` and error log |
| Step 3 | score < 6.0 | Re-run Step 2 with issues as additional context (max 1 retry) |
| Step 4 | char_count > platform limit | Truncate with "..." and set `within_limits: false` |

## Research Base
- Chain pattern: output A -> input B com data contracts (MIPRO/DSPy)
- Knowledge-first ordering: research antes de draft (+0.91 task adherence)
- Fallback model strategy: degrade gracefully, nao abort
