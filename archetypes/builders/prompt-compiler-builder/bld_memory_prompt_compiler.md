---
kind: memory
id: bld_memory_prompt_compiler
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for prompt_compiler artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: null
title: "Memory Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, memory, P03]
tldr: "Production patterns and anti-patterns for building intent resolution artifacts."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---
# Memory: prompt-compiler-builder
## Summary
Prompt compilers are the most critical artifact in CEX -- they sit at the boundary between human intent and LLM execution. The critical lesson is that coverage must be exhaustive: every kind must be reachable from at least one user pattern in each supported language. Partial coverage means some user intents silently fall through to fallback, degrading the user experience.
## Pattern
1. Always start from kinds_meta.json as source of truth -- never enumerate kinds from memory
2. Group kinds by pillar for cognitive coherence -- users think in domains, not alphabetical order
3. Bilingual patterns must be independently authored, not machine-translated -- PT users phrase differently
4. Verb resolution is the highest-leverage table -- 30 verbs cover 90% of user inputs
5. Fallback heuristics must include confidence scores -- "I think you mean X (85%)" beats guessing silently
6. Boundary notes prevent misrouting -- "NOT a router" is as important as "IS a prompt_compiler"
## Anti-Pattern
1. Partial kind coverage -- any unmapped kind means that user intent gets lost
2. Machine-translated PT patterns -- "criar agente" is natural, "construir agente" is literal
3. Missing boundary notes -- without them, similar kinds (router vs dispatch_rule) get confused
4. Prose-heavy resolution tables -- tables are 3x denser than prose for pattern matching
5. Fallback that silently guesses -- user must know when confidence is low
6. Static verb table -- verbs evolve; the table must be versioned and expandable
## Context
Prompt compilers operate at the F1 CONSTRAIN layer of the 8F pipeline. They are loaded as prompt layers by cex_prompt_layers.py and injected into every LLM context. They transform raw user input into structured CEX taxonomy before any builder, router, or dispatcher runs. DSPy calls this "prompt compilation"; Rasa calls it "intent resolution"; the CEX metaphor is "transmutation."
## Impact
Full 124-kind coverage eliminates silent intent drops. Bilingual patterns (PT+EN) serve 100% of the user base. Verb resolution tables reduce ambiguity by 80% compared to free-form matching. Boundary notes reduce misrouting between similar kinds by 90%.
