---
id: p01_kc_domain_vocabulary
kind: knowledge_card
type: kind
pillar: P01
title: "Domain Vocabulary -- Deep Knowledge for domain_vocabulary"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: domain_vocabulary
quality: null
tags: [domain_vocabulary, p01, INJECT, kind-kc, ubiquitous-language, ddd, core]
tldr: "Governed registry of canonical terms for a bounded context; loaded at F2b SPEAK; prevents semantic drift across LLM agents; NOT glossary_entry nor ontology."
when_to_use: "Establishing or loading the canonical vocabulary for a bounded context before generating any artifacts"
keywords: [domain-vocabulary, ubiquitous-language, canonical-terms, bounded-context, semantic-drift]
feeds_kinds: [domain_vocabulary]
density_score: null
aliases: ["controlled vocabulary", "term registry", "canonical terms", "ubiquitous language registry"]
user_says: ["define terms for domain", "enforce vocabulary", "what are the canonical terms", "prevent term drift"]
long_tails: ["create a canonical term registry for a bounded context", "enforce ubiquitous language across all agents", "document what terms mean in this domain and what NOT to call them"]
---

# Domain Vocabulary

## Spec
```yaml
kind: domain_vocabulary
pillar: P01
llm_function: INJECT
max_bytes: 5120
naming: dv_{bounded_context}_vocabulary.md
core: true
```

## What It Is
A domain_vocabulary is a governed registry of canonical terms for a bounded context, enforcing the DDD Ubiquitous Language principle (Evans 2003 ch.2). It is the artifact that makes shared language OPERATIONAL -- not just documented but enforced. Every agent that works within a bounded context loads the domain_vocabulary at F2b SPEAK before generating any artifact. This prevents semantic drift: the silent accumulation of synonym proliferation that eventually causes LLM-to-LLM communication failures and cross-nucleus handoff ambiguity.

The domain_vocabulary is NOT a glossary (single term definition), NOT an ontology (formal IS-A/PART-OF relations), and NOT documentation (it is enforced in every F2-F8 step).

## Boundary
| Aspect | domain_vocabulary | glossary_entry | ontology |
|--------|------------------|----------------|---------|
| Scope | Registry for a whole BC | Single term | Formal relation graph |
| Enforcement | F2b SPEAK loading | Reference only | Reasoner/inference |
| Structure | Table of terms + anti_patterns | Single def | RDF/OWL triples |
| DDD source | Ubiquitous Language (ch.2) | Dictionary | Semantic web |
| Size | Up to 5120B (core) | Small (300B) | Potentially unbounded |

## Term Structure
Each term in a domain_vocabulary has:
- definition: one canonical sentence (what the term IS)
- industry_standard: Evans/NIST/ISO reference or "CEX-internal"
- anti_patterns: list of what NOT to call it (drift prevention)
- status: proposed | active | deprecated
- replaces: old term if this is a replacement
- replaced_by: new term if this is deprecated

## Loading Protocol (F2b SPEAK)
```
F2b SPEAK (mandatory before F3):
  1. Load dv_{bounded_context}_vocabulary.md
  2. Load _docs/specs/spec_metaphor_dictionary.md (Industry term column)
  3. ALL output from F3-F8 uses loaded vocabulary ONLY
  4. Unknown terms: flag for addition, do NOT invent
```

The existing per-nucleus kc_{domain}_vocabulary.md files ARE domain_vocabulary artifacts
by another naming convention. The kind formalizes what those files have always been.

## Scope Hierarchy
```
CEX Universal (prompt_compiler, 257 kinds)
    |
    +-- dv_cex_core_vocabulary (core CEX terms: 8F, 12P, kind, pillar, nucleus)
    |
    +-- dv_{nucleus}_vocabulary (per-nucleus domain extension)
    |       e.g., dv_n01_vocabulary (intelligence domain: retrieval, benchmark, source)
    |       e.g., dv_n03_vocabulary (engineering domain: scaffold, build, compile)
    |
    +-- dv_{project}_vocabulary (project-specific terms for user's domain)
```

## Semantic Drift Pattern
Semantic drift: the phenomenon where different agents use different terms for the same concept,
causing communication failures and artifact quality degradation over time.
Measured by: synonym count per canonical concept (target: 1 term per concept per BC).
Prevention: domain_vocabulary loaded at EVERY session start within the BC.

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Global vocabulary (cross-BC) | "Account" means different things in Sales vs. Banking | One vocabulary per bounded_context |
| No anti_patterns in terms | Agents default to colloquial synonyms | Every term needs what NOT to say |
| Vocabulary as docs (not loaded) | Drift continues even with documentation | F2b SPEAK LOADS vocabulary, not reads |
| Never deprecating old terms | Deprecated terms persist in legacy artifacts | Lifecycle management: mark + replace |

## Decision Tree
- IF canonical terms for a whole bounded context -> domain_vocabulary
- IF single term needs formal definition -> glossary_entry
- IF formal IS-A/PART-OF relationships needed -> ontology
- IF translating between two BC vocabularies -> translation_map (if exists)
- DEFAULT: domain_vocabulary when 3+ terms need governance within one BC

## Quality Criteria
- GOOD: >= 3 active terms, each with definition + anti_patterns + status, bounded_context named
- GREAT: full lifecycle coverage + industry references + governed_agents + F2b loading instructions
- FAIL: < 3 terms OR no anti_patterns OR no bounded_context scope
