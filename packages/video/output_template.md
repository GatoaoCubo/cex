# Video Agent — Output Template

**Version**: 1.0.0 | **Purpose**: Standard output format

---

## VIDEO PRODUCTION PACKAGE

### Produto: {{PRODUCT_NAME}}
### Duracao: {{DURATION}}s
### Estilo: {{STYLE}}
### Plataforma: {{PLATFORM}}

---

## OUTPUT 1: STORYBOARD

### Visao Geral

| # | Shot | Timing | Phase | Descricao Resumida |
|---|------|--------|-------|-------------------|
| 1 | Hook | 0-3s | HOOK | [DESC] |
| 2 | Problem | 3-7s | BUILD | [DESC] |
| 3 | Context | 7-12s | BUILD | [DESC] |
| 4 | Demo 1 | 12-16s | BENEFIT | [DESC] |
| 5 | Demo 2 | 16-20s | BENEFIT | [DESC] |
| 6 | Proof | 20-25s | PROOF | [DESC] |
| 7 | CTA | 25-30s | CTA | [DESC] |

### Detalhamento por Shot

#### SHOT N: [Name] ([Timing])

**Fase**: [PHASE]
**Visual**: [detailed description]
**Camera**: [camera movement]
**Framing**: [framing details]
**Proposito**: [why this shot]

---

## OUTPUT 2: SCRIPT

### Narracao

| Shot | Texto | Palavras | Max |
|------|-------|----------|-----|
| 1 | "[text]" | X | Y |

### Text Overlays

| Shot | Overlay | Posicao | Animacao |
|------|---------|---------|----------|
| 1 | [TEXT] | center | slam_in |

### Audio Timeline

| Timing | Music | SFX |
|--------|-------|-----|
| 0-3s | Attention sting | Whoosh |
| 3-12s | Building tension | - |
| 12-20s | Uplifting | Product sounds |
| 20-25s | Confident | Number ticks |
| 25-30s | Resolution | Click |

### Volume Levels

| Layer | Level |
|-------|-------|
| Narration | 100% |
| Music | 30% (ducking on) |
| SFX | 50% |

---

## OUTPUT 3: VISUAL PROMPTS

### Generator: {{GENERATOR}}
### Style: {{STYLE}}

### SHOT N: [Name] ([Timing])

**Phase**: [PHASE]
**Duration**: [X]s

**Prompt**:
```
[COMPLETE_PROMPT_TEXT]
```

**Technical**:
- Camera: [movement]
- Lighting: [style]
- Motion Strength: [value]

### Generation Settings

| Setting | Value |
|---------|-------|
| Generator | Runway Gen-3 |
| Resolution | 1080x1920 |
| Aspect Ratio | 9:16 |
| Duration/shot | 4s |
| FPS | 24 |
| Motion Strength | [by style] |
| Guidance Scale | 12 |

---

## VALIDACAO (5D Score)

| Dimensao | Score | Criterios |
|----------|-------|-----------|
| narrative_arc | [X.X]/10 | Hook em 3s, fases presentes, CTA claro |
| visual_quality | [X.X]/10 | Camera especificada, estilo consistente |
| platform_compliance | [X.X]/10 | Duracao correta, aspect ratio, safe zones |
| engagement_potential | [X.X]/10 | Forca do hook, potencial de loop |
| production_feasibility | [X.X]/10 | Prompts AI-compativeis, realistas |
| **TOTAL** | **[X.X]/10** | |

**Status**: [PASS / FAIL]
**Pronto para Producao**: [SIM / NAO]

---

## PROXIMOS PASSOS

1. **Geracao de Video**: Use os prompts do OUTPUT 3 no {{GENERATOR}}
2. **Narracao TTS**: Use o script do OUTPUT 2 no ElevenLabs
3. **Montagem**: Combine clips + audio no FFmpeg ou editor
4. **Publicacao**: Exporte para {{PLATFORM}} com specs corretos
