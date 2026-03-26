---
# TEMPLATE: Brand Skill (P04 Tools)
# Source-of-truth propagation pattern: guidelines -> tokens -> CSS -> inject
# Based on KC_STUDY_BRAND_SKILL axioms
# Valide contra P04_tools/_schema.yaml (types.skill)
# Max 4KB | quality_min: 7.0

id: p04_skill_{{NAME_SLUG}}
name: {{BRAND_SKILL_NAME}}
description: {{ONE_LINE_WHAT_IT_DOES}}  # TRIGGER CONDITION — when agent should invoke this skill
version: 1.0.0
pillar: P04
kind: skill
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
domain: brand
quality: {{QUALITY_7_TO_10}}
tags: [brand, design-system, {{TAG3}}]
tldr: {{ONE_DENSE_SENTENCE}}
user_invocable: {{true_OR_false}}
trigger: {{COMO_ATIVAR}}
when_to_use: {{CONDICAO_DE_USO}}
when_not_to_use: {{QUANDO_NAO_USAR}}
phases:
  - edit
  - sync
  - generate
  - inject
examples:
  - {{EXEMPLO_USO_1}}
  - {{EXEMPLO_USO_2}}
density_score: {{0.80_TO_1.00}}
references_dir: references/
sub_skills: [{{SUBCMD_1}}, {{SUBCMD_2}}]
platforms: [claude]
stack_default: # optional
---

# {{BRAND_SKILL_DISPLAY_NAME}}

## Purpose
<!-- Brand como sistema vivo com propagacao de 4 fases -->
{{SKILL_NAME}} gerencia a **propagacao de identidade de marca** no CODEXA. Garante que guidelines sao a fonte-da-verdade e se propagam deterministicamente ate o contexto de prompt.

## Workflow Phases

### Phase 1: EDIT (Guidelines)
**Input**: Brand guidelines source file (`brand-guidelines.md`)
**Action**: Editar/atualizar guidelines (voz, personalidade, tons, regras visuais)
**Output**: Updated `brand-guidelines.md` (source-of-truth)
**Voice Framework**:
- Personality: {{TRACOS_DE_PERSONALIDADE}}
- Tone variations: {{TOM_FORMAL}}, {{TOM_CASUAL}}, {{TOM_URGENTE}}
- Language rules: {{REGRAS_DE_LINGUAGEM}}

### Phase 2: SYNC (Tokens)
**Input**: Updated `brand-guidelines.md`
**Action**: Extrair valores e sincronizar para `design-tokens.json` (DTCG format)
**Output**: `design-tokens.json` com primitives -> semantic -> component layers
**Token Naming**: `--{category}-{item}-{variant}-{state}`

### Phase 3: GENERATE (CSS)
**Input**: `design-tokens.json`
**Action**: Gerar CSS custom properties a partir dos tokens
**Output**: `design-tokens.css` (consumivel por frontend)
**Dark Mode**: Override apenas Semantic layer (primitives intocados)

### Phase 4: INJECT (Prompt Context)
**Input**: `brand-guidelines.md` + `design-tokens.json`
**Action**: Injetar contexto de marca em prompts de satellites (LILY, EDISON)
**Output**: Brand-aware prompt context para content generation

## Usage

```bash
# Atualizar guidelines
/{{TRIGGER}} edit --file brand-guidelines.md

# Sincronizar tokens apos editar guidelines
/{{TRIGGER}} sync

# Gerar CSS a partir dos tokens
/{{TRIGGER}} generate --format css

# Injetar contexto de marca em prompt
/{{TRIGGER}} inject --satellite lily --task "{{DESCRICAO}}"
```

## Anti-Patterns
- **Editar tokens diretamente**: SEMPRE editar guidelines primeiro, depois sync
- **Pular sync apos edit**: Tokens ficam desincronizados da fonte-da-verdade
- **Hardcoded brand values**: Usar tokens, nunca valores literais em prompts
- **Monolithic guidelines**: Separar em sub-arquivos via references/ quando > 200 linhas

## Hard Gates
<HARD-GATE>
brand-guidelines.md MUST exist before sync/generate/inject phases
</HARD-GATE>
<HARD-GATE>
design-tokens.json MUST be valid DTCG format after sync
</HARD-GATE>

## Integration
- **requires**: scout-agent (file discovery), design-tokens spec (DTCG)
- **called_by**: LILY (marketing content), EDISON (component generation), marca-agent

## Sub-skill Routing
| Sub-command | File | Description |
|-------------|------|-------------|
| edit | references/edit.md | Guidelines editing protocol |
| sync | references/sync.md | Token synchronization pipeline |
| generate | references/generate.md | CSS generation from tokens |
| inject | references/inject.md | Prompt context injection |

## Cross-References
- marca-agent: Brand strategy and identity creation
- styling-agent: CSS/Tailwind implementation of design tokens
- react-component-agent: Component generation consuming tokens

## References
- `references/edit.md` — Guidelines editing protocol and voice framework
- `references/sync.md` — Token synchronization and DTCG format spec
- `references/generate.md` — CSS custom property generation
- `references/inject.md` — Prompt context injection for satellites
