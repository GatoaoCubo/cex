# SSML Speech Synthesis Markup | Voice Technology

**Domain**: voice_technology
**Type**: concept
**Quality**: 0.85

SSML permite controle fino sobre a fala sintetizada.

## Tags Principais

```xml
<speak>
  <prosody rate="slow" pitch="+2st">
    Texto mais lento e agudo.
  </prosody>
  <break time="500ms"/>
  <emphasis level="strong">Importante!</emphasis>
</speak>
```

## Prosody (Entonacao)
- **rate**: x-slow, slow, medium, fast, x-fast
- **pitch**: x-low, low, medium, high, x-high
- **volume**: silent, x-soft, soft, medium, loud, x-loud

## Outros Elementos
- break: Pausas (time="500ms")
- emphasis: Enfase (level="strong")
- say-as: Interpretacao (cardinal, ordinal, date)
- phoneme: Pronuncia fonetica

## Suporte por Plataforma

| Tag | ElevenLabs | OpenAI | Edge |
|-----|------------|--------|------|
| prosody | Sim | Nao | Sim |
| break | Sim | Sim | Sim |
| emphasis | Sim | Nao | Sim |

---
**Generated**: 2025-12-11
**Source**: voice_agent FONTES enrichment
