---
pillar: P12
llm_function: COLLABORATE
purpose: Crew roles and handoff contracts for context-doc-builder
---

# Collaboration: context-doc-builder

## Role in Crew
DOMAIN CONTEXT SPECIALIST.
I answer: "what background context does this domain need for prompt hydration?"
I produce: context_doc (.md + .yaml) ready for INJECT into system_prompt or action_prompt.

## What I Do NOT Do
- Distill atomic facts into knowledge_card (density gate, single-fact structure)
- Define controlled vocabulary terms (glossary_entry)
- Write step-by-step execution protocols (instruction)
- Compose agent personas (system_prompt)
- Configure embedding or indexing (knowledge_card metadata)

## Crew Compositions

### "Domain Hydration" Crew
```
context-doc-builder     -> produces context_doc (background)
knowledge-card-builder  -> produces knowledge_card (atomic facts)
system-prompt-builder   -> consumes both, produces agent system_prompt
```
Trigger: "build full domain context package for [domain] agent"

### "Onboarding Pack" Crew
```
context-doc-builder     -> domain context_doc
glossary-entry-builder  -> key term glossary_entries
knowledge-card-builder  -> critical fact knowledge_cards
```
Trigger: "create onboarding knowledge set for [domain]"

### "Solo" (no crew needed)
Single context_doc request: context-doc-builder operates independently.
No hard dependencies on other builders.

## Handoff Protocol

### Receives (inputs)
- domain label (snake_case)
- scope sentence (or raw description to derive scope from)
- optional: stakeholder list, constraint notes, seed words from SEED_BANK

### Produces (outputs)
- `p01_ctx_{topic_slug}.md` — markdown artifact with full frontmatter + body
- `p01_ctx_{topic_slug}.yaml` — companion machine-readable file

### Signals to Next Builder
After producing context_doc, pass to consuming builder:
```
artifact_id: p01_ctx_{topic_slug}
kind: context_doc
domain: {domain_value}
scope: {scope_value}
status: ready_for_inject
```

## Dependencies
- Hard: none (independent builder)
- Soft: brain_query availability (for duplicate check in Phase 1)
- Downstream: system-prompt-builder, action-prompt-builder (consumers)
