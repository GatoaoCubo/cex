---
kind: examples
id: bld_examples_prompt_compiler
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_compiler artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.0
title: "Examples Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, examples, P03]
tldr: "Golden and anti-examples for prompt_compiler construction showing ideal structure and common pitfalls."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---

# Examples: prompt-compiler-builder
## Golden Example (excerpt -- Kind Resolution Table row)
INPUT: "Build a prompt compiler for CEX universal intent resolution"
OUTPUT (excerpt):
```yaml
id: p03_pc_cex_universal
kind: prompt_compiler
pillar: P03
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "n03_builder"
title: "CEX Universal Prompt Compiler"
domain: "intent_resolution"
coverage: 124
languages: [pt-br, en]
quality: null
tags: [prompt_compiler, intent-resolution, cex, bilingual]
tldr: "Resolves natural language input into {kind, pillar, nucleus, verb} for all 124 CEX kinds in PT-BR and EN"
density_score: 0.91
```
### P01 Knowledge (excerpt)
| Kind | Nucleus | Patterns (EN) | Patterns (PT) | Verb | 8F | Boundary |
|------|---------|---------------|---------------|------|----|----------|
| knowledge_card | N04 | document, write KC, knowledge card | documentar, criar KC | create | INJECT | Atomic knowledge. NOT context_doc (long-form) |
| chunk_strategy | N04 | chunking, split docs | chunking, dividir docs | configure | CONSTRAIN | Chunk rules. NOT embedding_config |
| embedding_config | N04 | embeddings, vector config | embeddings, config vetorial | configure | GOVERN | Embed settings. NOT chunk_strategy |

WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p03_pc_ pattern (H02 pass) | kind: prompt_compiler (H04 pass)
- coverage: 124 matches table (H08 pass) | languages: [pt-br, en] (H06 pass)
- All 124 kinds mapped (S01 pass) | Bilingual >= 80% (S02 pass)
- Boundary notes present (S03 pass) | Verb table >= 30 (H09 pass)
## Anti-Example
INPUT: "Make intent resolver"
BAD OUTPUT:
```yaml
id: intent_resolver
kind: router
pillar: P02
quality: 8.5
coverage: 15
```
Map user input to agents.
FAILURES:
1. id: no `p03_pc_` prefix -> H02 FAIL
2. kind: "router" not "prompt_compiler" -> H04 FAIL
3. pillar: P02 not P03 -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. coverage: 15 (only 15 of 124 kinds) -> H07 FAIL (< 120)
6. Missing: title, languages, tags, tldr -> H06 FAIL
7. No Kind Resolution Table -> H07 FAIL
8. No Verb Resolution Table -> H09 FAIL
9. No ambiguity resolution -> S04 FAIL
10. No fallback heuristics -> S05 FAIL
