---
kind: collaboration
id: bld_collaboration_memory_type
pillar: P12
llm_function: COLLABORATE
---

# Collaboration: memory_type

## Produces For
- entity-memory-builder: memory types classify entity observations
- memory-scope-builder: type informs scope (correction=global, context=session)
- memory-summary-builder: type determines summarization strategy

## Consumes From
- agent-builder: agent definitions include memory preferences
- system-prompt-builder: identity prompts reference memory behavior
