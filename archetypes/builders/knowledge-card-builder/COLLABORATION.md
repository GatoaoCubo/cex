---
pillar: P12
llm_function: COLLABORATE
purpose: How knowledge-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: knowledge-card-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the essential fact about this topic?"
I do not decide routing. I do not configure boot. I do not define identity.
I DISTILL knowledge so other builders and agents have factual context.

## Crew Compositions

### Crew: "Research and Document New Domain"
```
  1. knowledge-card-builder      -> "destila fatos atomicos do dominio"
  2. model-card-builder          -> "spec dos LLMs usados no dominio"
  3. agent-builder [PLANNED]     -> "define agente especialista"
  4. skill-builder [PLANNED]     -> "define skills do dominio"
```

### Crew: "Enrich Existing Agent"
```
  1. knowledge-card-builder      -> "KCs novos para domain context"
  2. system-prompt-builder [PLANNED] -> "atualiza prompt com novos KCs"
  3. quality-gate-builder [PLANNED]  -> "valida agent knowledge coverage"
```

### Crew: "Build Knowledge Base from Scratch"
```
  1. knowledge-card-builder (N instances) -> "1 KC per subtopic"
  2. iso-package-builder [PLANNED]       -> "empacota KCs em index"
```

## Handoff Protocol
### I Receive
- seeds: topic name, domain (minimum)
- optional: source URLs, related artifacts, target audience

### I Produce
- knowledge_card artifact (p01_kc_{topic}.md)
- committed to: cex/P01_knowledge/examples/p01_kc_{topic}.md
- validated by: validate_kc.py (score + verdict)

### I Signal
- signal: complete (with validator verdict)
- if REJECTED or NEEDS_WORK: signal retry with failed gates

## Builders I Depend On
None. knowledge-card-builder is INDEPENDENT (content layer).
It can receive context from research agents but has no builder dependencies.

## Builders That Depend On Me [PLANNED]
| Builder | Why |
|---------|-----|
| agent-builder | Needs domain KCs for agent knowledge base |
| system-prompt-builder | Injects KC facts into system prompts |
| skill-builder | References KC domain knowledge in skills |
| iso-package-builder | Bundles KCs as deploy dependencies |
