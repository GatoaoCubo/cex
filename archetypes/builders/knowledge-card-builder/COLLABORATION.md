---
lp: P12
llm_function: COLLABORATE
purpose: How knowledge-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: knowledge-card-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the atomic fact about X?"
I do not route queries. I do not build agents. I do not write prompts.
I DISTILL knowledge so other builders and agents can consume it.

## Crew Compositions

### Crew: "Research and Document New Domain"
```
  1. SHAKA (research)                  -> raw findings, URLs, data
  2. knowledge-card-builder (THIS)     -> distill into atomic KCs
  3. indexer-builder [PLANNED]         -> index KCs into Brain
  4. quality-gate-builder [PLANNED]    -> validate KC quality
```

### Crew: "Build Agent Knowledge Base"
```
  1. knowledge-card-builder (THIS)     -> produce domain KCs
  2. few-shot-builder [PLANNED]        -> produce examples from KCs
  3. context-doc-builder [PLANNED]     -> produce context docs
  4. agent-builder [PLANNED]           -> assemble agent with KCs
```

### Crew: "Knowledge Maintenance Cycle"
```
  1. knowledge-card-builder (THIS)     -> update stale KCs
  2. validate_kc.py                    -> validate quality gates
  3. Brain rebuild                     -> re-index updated KCs
```

## Handoff Protocol
### I Receive
- seeds: topic, domain (minimum)
- optional: source URLs, raw research, target body structure
- optional: related KCs to link via linked_artifacts

### I Produce
- knowledge_card artifact (p01_kc_{topic}.md)
- committed to: cex/P01_knowledge/examples/p01_kc_{topic}.md

### I Signal
- signal: complete (with validator verdict from validate_kc.py)
- if HARD fail: signal retry with gate failures
- if score < 8.0: signal needs_improvement with SOFT failures

## Builders I Depend On
None. knowledge-card-builder is INDEPENDENT (layer 1 content).
It consumes raw research but does not depend on other builders.

## Builders That Depend On Me [PLANNED]
| Builder | Why |
|---------|-----|
| few-shot-builder | Uses KC content to generate examples |
| context-doc-builder | References KC facts for context hydration |
| agent-builder | Injects KC knowledge into agent identity |
| indexer-builder | Indexes KCs into Brain for retrieval |
| iso-package-builder | Bundles KCs as agent knowledge dependencies |
