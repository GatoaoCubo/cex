---
pillar: P08
llm_function: CONSTRAIN
purpose: Structural position of context_doc in the CEX knowledge architecture
---

# Architecture: context_doc

## What context_doc IS
Domain background document for prompt hydration. Function: INJECT — loaded into agent
context to provide situational awareness before task execution. Layer: content (P01).
Allows narrative prose, multiple facts, stakeholder framing.

## What context_doc IS NOT
- NOT knowledge_card: KC is atomic single-fact with mandatory density gate (>= 0.80)
- NOT glossary_entry: glossary_entry defines exactly one controlled-vocabulary term
- NOT instruction: instruction is step-by-step execution protocol (P03, REASON)
- NOT system_prompt: system_prompt defines agent persona (P03, BECOME)

## Position in Knowledge Flow

```
Raw Domain Input
      |
      v
[context-doc-builder]
      |
      v
context_doc (.md + .yaml)     <-- P01, INJECT, layer: content
      |
      +---> system_prompt (BECOME)   -- agent loads context at boot
      |
      +---> action_prompt (REASON)   -- agent loads context per task
      |
      +---> agent boot sequence      -- satellite pre-loads domain context
```

## Dependency Graph

```
context_doc
  consumes:   raw domain notes, stakeholder interviews, regulation docs
  produces:   structured domain context for injection
  consumed_by: system_prompt, action_prompt, agent boot, orchestrator handoff
  siblings:   knowledge_card (atomic), glossary_entry (term)
  parent:     P01 knowledge layer
```

## Fractal Position

| Dimension | Value |
|-----------|-------|
| Pillar | P01 |
| LLM Function | INJECT |
| Layer | content |
| Core 24 | YES |
| machine_format | yaml |
| max_bytes | 2048 |

## When to Choose context_doc vs Siblings

| Need | Use |
|------|-----|
| Background for a domain (multiple facts, narrative ok) | context_doc |
| Single atomic fact at high density | knowledge_card |
| Single term definition for controlled vocab | glossary_entry |
| Step-by-step execution protocol | instruction |
| Agent persona + operational rules | system_prompt |
