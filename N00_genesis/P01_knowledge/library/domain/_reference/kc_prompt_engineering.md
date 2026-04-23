---
id: p01_kc_prompt_engineering
kind: knowledge_card
type: domain
pillar: P01
title: "Prompt Engineering — Instructions, Versioning, Context Docs, Glossary Entries"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: prompts
origin: manual
quality: 9.1
tags: [prompt, instruction, versioning, context, glossary, template, few-shot, chain-of-thought]
tldr: "Prompt engineering manages the full lifecycle of LLM instructions — authoring, versioning, A/B testing, context assembly, and term standardization via glossaries"
when_to_use: "Building or classifying components that author, version, test, or manage prompts and their supporting context"
keywords: [instruction, prompt_version, context_doc, glossary_entry, template, few-shot, cot]
long_tails:
  - "How to version and A/B test prompts mapped to CEX prompt_version kind"
  - "Which context assembly patterns map to CEX context_doc kind"
  - "How glossary entries standardize terminology across agent prompts"
axioms:
  - "Prompts are code — they deserve version control, testing, and review"
  - "Context windows are finite — every token must earn its place through relevance"
  - "Glossary terms eliminate ambiguity across agents and prevent semantic drift"
linked_artifacts:
  primary: null
  related: [p01_kc_agent_identity, p01_kc_langchain_patterns, p01_kc_routing_resilience]
feeds_kinds:
  - instruction      # System prompts, task instructions, behavioral constraints
  - prompt_version   # Versioned prompt variants, A/B test candidates, changelog
  - context_doc      # Reference documents assembled into context windows
  - glossary_entry   # Term definitions, canonical names, synonym mappings
density_score: 0.86
related:
  - prompt-version-builder
  - p01_kc_prompt_version
  - bld_collaboration_action_prompt
  - bld_collaboration_prompt_version
  - bld_collaboration_context_doc
  - action-prompt-builder
  - bld_examples_prompt_version
  - p01_kc_prompt_engineering_best_practices
  - context-doc-builder
  - bld_collaboration_prompt_template
---

# Prompt Engineering

## Quick Reference
```yaml
topic: Prompt Lifecycle Management
scope: Instruction authoring, prompt versioning, context assembly, glossary management
source: cross-domain (Anthropic docs, prompt engineering guides, organization HOPs)
criticality: high
```

## Key Concepts

| Concept | Category | CEX Kind | Role |
|---------|----------|----------|------|
| System Prompt | Authoring | instruction | Top-level behavioral instructions for the LLM |
| Task Instruction | Authoring | instruction | Step-by-step directions for a specific task |
| Few-Shot Examples | Authoring | instruction | Input/output demonstrations that guide format and quality |
| Chain-of-Thought | Authoring | instruction | Reasoning scaffolding ("think step by step") |
| Constraint Block | Authoring | instruction | NEVER/ALWAYS rules that bound behavior |
| Prompt Template | Versioning | prompt_version | Parameterized prompt with {{variable}} slots |
| Version Tag | Versioning | prompt_version | Semantic version (v1.2.0) for prompt tracking |
| A/B Variant | Versioning | prompt_version | Competing prompt versions evaluated on metrics |
| Changelog | Versioning | prompt_version | What changed and why between prompt versions |
| Eval Suite | Versioning | prompt_version | Test cases that validate prompt quality |
| Reference Doc | Assembly | context_doc | Static knowledge injected into context window |
| Dynamic Context | Assembly | context_doc | Retrieved documents (RAG) assembled at runtime |
| Context Budget | Assembly | context_doc | Token allocation strategy across context sections |
| Priority Ranking | Assembly | context_doc | Importance ordering for context truncation |
| Term Definition | Glossary | glossary_entry | Canonical meaning of a domain-specific term |
| Synonym Map | Glossary | glossary_entry | Alternative names that resolve to the same concept |
| Disambiguation | Glossary | glossary_entry | Clarification when a term has multiple meanings |

## Patterns

| Trigger | Action |
|---------|--------|
| Author new prompt | Define role -> write constraints -> add few-shot examples -> test on eval suite |
| Version a prompt | Tag current as vN -> create variant -> run A/B eval -> promote winner |
| Assemble context | Rank documents by relevance -> allocate token budget -> truncate lowest priority |
| Add glossary term | Define canonical name -> list synonyms -> add disambiguation if needed |
| Optimize for cost | Reduce few-shot examples -> compress context docs -> measure quality delta |
| Prevent prompt drift | Lock production prompt version -> require eval pass before promotion |
| Handle context overflow | Prioritize recent + relevant -> compress old context -> summarize if needed |

## Anti-Patterns

- Editing production prompts without versioning (no rollback path)
- Stuffing context window without relevance filtering (wastes tokens, degrades quality)
- Using inconsistent terminology across agent prompts (semantic drift)
- Writing prompts without eval suites (no way to detect regressions)
- Hardcoding examples instead of parameterizing templates
- Ignoring the "lost in the middle" effect — critical info should be at start or end

## CEX Mapping

```text
[glossary_entry] -> standardizes -> [instruction] -> parameterized as -> [prompt_version]
[context_doc] -> assembled into -> context_window -> fed to -> [instruction + prompt_version]
[prompt_version] -> evaluated by -> [eval_suite] -> promoted or rolled back
```

## References

- source: Anthropic prompt engineering guide, organization records/pool/recipes/HOP_*
- related: p01_kc_agent_identity, p01_kc_langchain_patterns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-version-builder]] | downstream | 0.43 |
| [[p01_kc_prompt_version]] | sibling | 0.38 |
| [[bld_collaboration_action_prompt]] | downstream | 0.38 |
| [[bld_collaboration_prompt_version]] | downstream | 0.38 |
| [[bld_collaboration_context_doc]] | downstream | 0.35 |
| [[action-prompt-builder]] | downstream | 0.34 |
| [[bld_examples_prompt_version]] | downstream | 0.32 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.32 |
| [[context-doc-builder]] | related | 0.31 |
| [[bld_collaboration_prompt_template]] | downstream | 0.31 |
