---
id: p01_kc_prompt_compiler
kind: knowledge_card
type: kind
pillar: P03
title: "Prompt Compiler -- Deep Knowledge"
version: 1.0.0
created: "2026-04-12"
updated: "2026-04-12"
author: n03_builder
domain: prompt_compiler
quality: 9.2
tags: [prompt_compiler, P03, CONSTRAIN, kind-kc, intent-resolution]
tldr: "Intent-to-artifact transmutation rules compiling vague user input into structured {kind, pillar, nucleus, verb} tuples"
when_to_use: "Building, reviewing, or reasoning about prompt_compiler artifacts"
keywords: [intent-resolution, transmutation, prompt-compilation, DSPy, NLU, bilingual]
feeds_kinds: [prompt_compiler]
density_score: 0.93
linked_artifacts:
  primary: P03_prompt/p03_pc_cex_universal.md
  related:
    - .claude/rules/n07-input-transmutation.md
    - N03_engineering/P01_knowledge/kc_intent_resolution_map.md
related:
  - bld_knowledge_card_prompt_compiler
  - prompt-compiler-builder
  - p03_sp_prompt_compiler_builder
  - p01_kc_input_intent_resolution
  - p03_ins_prompt_compiler
  - bld_architecture_prompt_compiler
  - bld_collaboration_prompt_compiler
  - p01_report_intent_resolution
  - bld_memory_prompt_compiler
  - bld_examples_prompt_compiler
---

# Prompt Compiler

## Spec
```yaml
kind: prompt_compiler
pillar: P03
llm_function: CONSTRAIN
max_bytes: 16384
naming: p03_pc_{{name}}.md
core: true
```

## What It Is

A prompt compiler is an artifact that sits at the boundary between human intent and LLM execution. It resolves natural language input into structured {kind, pillar, nucleus, verb} tuples before any builder, router, or dispatcher runs. It is the **first function** in every 8F pipeline (F1 CONSTRAIN).

The term comes from **DSPy** (Stanford NLP), which uses "prompt compilation" to mean optimizing signatures into efficient LLM prompts. In CEX, the concept is broader: compiling user intent into the correct CEX taxonomy action.

## How It Differs From Similar Kinds

| Kind | What it does | When to use instead |
|------|-------------|-------------------|
| **prompt_compiler** (P03) | Resolves WHAT the user wants: {kind, pillar, nucleus, verb} | Always first; before routing or dispatching |
| router (P02) | Routes WHERE: task-to-provider with confidence thresholds | After kind is resolved; for provider selection |
| dispatch_rule (P12) | Dispatches WHO: keyword-to-agent mapping | After nucleus is resolved; for task assignment |
| prompt_template (P03) | Fills HOW: template with {{variables}} for generation | After intent is resolved; for content production |

## The 3-Layer Resolution Stack

| Layer | Industry Term | Domain | CEX 8F Stage | What It Does |
|-------|-------------|--------|-------------|-------------|
| L1 Intent Resolution | NLU (Rasa, Dialogflow, Lex) | User input -> structured action | F1 CONSTRAIN | Determines {kind, pillar, nucleus} |
| L2 Query Rewriting | Search/RAG (LlamaIndex, ES) | Fuzzy input -> precise query | F3 INJECT | Optimizes retrieval for context |
| L3 Prompt Optimization | LLM (DSPy compilation) | Intent -> optimized LLM prompt | F6 PRODUCE | Generates best prompt for task |

A prompt_compiler artifact primarily handles **L1** but informs L2 and L3.

## Key Design Decisions

| Decision | Rule | Rationale |
|----------|------|-----------|
| Bilingual minimum | PT-BR + EN patterns required | CEX user base is bilingual; PT users phrase differently than EN |
| Coverage floor | >= 120 of 124 kinds mapped | Partial coverage means lost user intents |
| Table-first density | Tables over prose | LLMs parse tables 3x faster than prose for pattern matching |
| Boundary notes | Required per kind | "NOT this kind" prevents misrouting between similar kinds |
| Verb canonicalization | 30+ verbs mapped | Reduces ambiguity: "build", "create", "make" -> single action |
| Confidence reporting | Required on fallback | User must know when resolution is uncertain |

## Industry References

| System | Concept | Relationship |
|--------|---------|-------------|
| DSPy (Stanford) | Prompt compilation, Signature | Direct inspiration: compile declarations into optimized prompts |
| Rasa Open Source | Intent classification, NLU pipeline | Same function: text -> structured intent with confidence |
| Google Dialogflow | Intent matching, Entity extraction | Same function: natural language -> action parameters |
| Amazon Lex | Intent resolution, Slot filling | Same function: utterance -> intent + slots |
| LlamaIndex | Query engine, Query rewriting | Related: optimizes retrieval queries (L2 in stack) |
| Elasticsearch | Query DSL, Analyzers | Related: transforms fuzzy input into precise search (L2) |
| CEX 8F Pipeline | F1 CONSTRAIN | This IS F1: first function determining what to build |

## Architecture Position

```
User Input (natural language)
       |
       v
  [prompt_compiler]  <-- F1 CONSTRAIN (this kind)
       |
       v
  {kind, pillar, nucleus, verb}
       |
       +-- F2 BECOME (load builder ISOs)
       +-- F3 INJECT (load KCs, examples)
       +-- F4 REASON (plan approach)
       +-- F5 CALL (use tools)
       +-- F6 PRODUCE (generate artifact)
       +-- F7 GOVERN (quality gate)
       +-- F8 COLLABORATE (save, compile, signal)
```

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Execute user input literally | Bypasses intent resolution; wrong kind selected |
| Partial kind coverage | Unmapped kinds fall to fallback; user gets "I don't understand" |
| Machine-translated PT patterns | "construir agente" (literal) vs "criar agente" (natural) |
| No boundary notes | Similar kinds confused: router vs dispatch_rule |
| Silent fallback | User doesn't know resolution was uncertain |
| Hardcoded kind list | kinds_meta.json is the source of truth; list goes stale |

## Application Checklist

1. Read kinds_meta.json for current kind inventory (source of truth)
2. For each kind: author EN patterns, PT patterns, nucleus, verb, boundary
3. Build verb resolution table (>= 30 entries, both languages)
4. Define ambiguity protocol (context -> specificity -> boundary -> GDP)
5. Define fallback heuristics (TF-IDF -> semantic -> confidence -> ask)
6. Set coverage field = actual count; verify coverage == kinds in table
7. Validate body <= 16384 bytes; quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_prompt_compiler]] | sibling | 0.55 |
| [[prompt-compiler-builder]] | related | 0.49 |
| [[p03_sp_prompt_compiler_builder]] | related | 0.48 |
| [[p01_kc_input_intent_resolution]] | sibling | 0.47 |
| [[p03_ins_prompt_compiler]] | related | 0.43 |
| [[bld_architecture_prompt_compiler]] | downstream | 0.41 |
| [[bld_collaboration_prompt_compiler]] | upstream | 0.40 |
| [[p01_report_intent_resolution]] | sibling | 0.39 |
| [[bld_memory_prompt_compiler]] | downstream | 0.36 |
| [[bld_examples_prompt_compiler]] | downstream | 0.34 |
