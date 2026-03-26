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

## Crew Compositions (when I participate)

### Crew: "Build New Agent from Scratch"
```
STELLA receives: "preciso de um agent pra monitorar precos"
  1. model-card-builder  → "qual modelo? sonnet: $3/$15, 200K ctx, tool_calling"
  2. agent-builder       → "define identidade: price-monitor, capabilities..."
  3. system-prompt-builder → "escreve system prompt com persona + rules"
  4. skill-builder       → "define skills: scrape, alert, compare"
  5. quality-gate-builder → "define gates: price accuracy >= 95%"
  6. iso-package-builder → "empacota tudo em ISO portable"
```
My output (model_card) feeds into: agent-builder (limits), boot-config-builder (initialization).

### Crew: "Evaluate Model for Migration"
```
  1. model-card-builder  → "documenta modelo candidato"
  2. model-card-builder  → "documenta modelo atual" (comparison_card variant)
  3. benchmark-builder   → "define benchmark suite"
  4. scoring-rubric-builder → "define criterios de comparacao"
```

### Crew: "Bootstrap New Satellite"
```
  1. model-card-builder     → "spec do modelo do satellite"
  2. satellite-spec-builder → "define satellite role, MCPs, domain"
  3. boot-config-builder    → "configura inicializacao"
  4. system-prompt-builder  → "escreve PRIME do satellite"
```

## Handoff Protocol
### I Receive
- seeds: model name, provider (minimum)
- optional: use case (informs When to Use table)
- optional: comparison targets (triggers comparison_card variant)

### I Produce
- model_card artifact (spec_card or comparison_card)
- committed to: cex/P02_model/examples/p02_mc_{provider}_{slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. model-card-builder is INDEPENDENT (layer 0 infrastructure).
I can be invoked standalone without any other builder.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| boot-config-builder | Needs model specs for initialization params |
| router-builder | Needs pricing/capabilities for routing rules |
| fallback-chain-builder | Needs model specs to order fallback priority |
| agent-builder | References model limits in agent definition |
| iso-package-builder | Includes model_card as deploy dependency |
