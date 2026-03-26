---
lp: P12
llm_function: COLLABORATE
purpose: How model-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: model-card-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what can this LLM do and how much does it cost?"
I do not decide routing. I do not configure boot. I do not define identity.
I INFORM other builders so they can make better decisions.

## Crew Compositions

### Crew: "Build New Agent from Scratch"
```
  1. model-card-builder        → "qual modelo? sonnet: $3/$15, 200K ctx"
  2. agent-builder [PLANNED]   → "define identidade: price-monitor..."
  3. system-prompt-builder [PLANNED] → "escreve system prompt"
  4. skill-builder [PLANNED]   → "define skills: scrape, alert"
  5. quality-gate-builder [PLANNED]  → "define gates: accuracy >= 95%"
  6. iso-package-builder [PLANNED]   → "empacota tudo"
```

### Crew: "Bootstrap New Satellite"
```
  1. model-card-builder             → "spec do modelo do satellite"
  2. satellite-spec-builder [PLANNED] → "define satellite role, MCPs"
  3. boot-config-builder [PLANNED]  → "configura inicializacao"
  4. system-prompt-builder [PLANNED] → "escreve PRIME"
```

## Handoff Protocol
### I Receive
- seeds: model name, provider (minimum)
- optional: use case (informs When to Use table)

### I Produce
- model_card artifact (spec_card)
- committed to: cex/P02_model/examples/p02_mc_{provider}_{slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. model-card-builder is INDEPENDENT (layer 0 infrastructure).

## Builders That Depend On Me [PLANNED]
| Builder | Why |
|---------|-----|
| boot-config-builder | Needs model specs for initialization params |
| router-builder | Needs pricing/capabilities for routing rules |
| fallback-chain-builder | Needs model specs to order fallback priority |
| agent-builder | References model limits in agent definition |
| iso-package-builder | Includes model_card as deploy dependency |
