---
kind: quality_gate
id: p11_qg_prompt_compiler
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_compiler artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.0
title: 'Gate: Prompt Compiler'
version: 1.0.0
author: n03_builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for intent resolution artifacts: verifies kind coverage, multilingual
  patterns, verb table, ambiguity protocol, and fallback heuristics.'
domain: prompt_compiler
created: '2026-04-12'
updated: '2026-04-12'
density_score: 0.9
related:
  - bld_examples_prompt_compiler
  - p03_ins_prompt_compiler
  - prompt-compiler-builder
  - p03_sp_prompt_compiler_builder
  - bld_knowledge_card_prompt_compiler
  - bld_output_template_prompt_compiler
  - p01_kc_prompt_compiler
  - bld_schema_prompt_compiler
  - bld_architecture_prompt_compiler
  - bld_collaboration_prompt_compiler
---

## Quality Gate

## Definition
A prompt_compiler artifact maps natural language user input to structured {kind, pillar, nucleus, verb} tuples. It covers all 124 registered kinds with multilingual patterns (EN-first, community-extensible), provides verb canonicalization, defines ambiguity resolution for multi-kind matches, and includes fallback heuristics for unrecognized input. It is the first function in every 8F pipeline (F1 CONSTRAIN).
Scope: files with `kind: prompt_compiler`. Does not apply to routers (P02, provider routing), dispatch rules (P12, task-agent mapping), or prompt templates (P03, variable filling).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p03_pc_*` | `id.startswith("p03_pc_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `prompt_compiler` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present | id, kind, pillar, title, version, created, updated, author, domain, coverage, languages, tags, tldr |
| H07 | Kind Resolution Table present with >= 300 kinds mapped | count distinct kinds >= 120 |
| H08 | `coverage` field matches actual kinds in table | integer == count of table rows |
| H09 | Verb Resolution Table present with >= 30 verbs | count rows >= 30 |
## SOFT Scoring
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | All 300 kinds covered (not just 120 minimum) | 1.0 |
| 2  | Multilingual coverage >= 80% (community language patterns for >= 80% of EN patterns) | 1.0 |
| 3  | Every kind has boundary note (when NOT to pick) | 1.0 |
| 4  | Ambiguity resolution protocol defined with >= 3 steps | 1.0 |
| 5  | Fallback heuristics defined with TF-IDF + semantic + confidence | 1.0 |
| 6  | Nucleus routing matrix covers all kinds | 0.5 |
| 7  | Behavioral instructions section present with >= 5 rules | 0.5 |
| 8  | Tags list includes `prompt_compiler` | 0.5 |
| 9  | `density_score` field present and >= 0.80 | 0.5 |
| 10 | `tldr` is <= 160 characters | 0.5 |
| 11 | Body <= 16384 bytes | 1.0 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish as reference prompt compiler |
| PUBLISH | >= 8.0 | Publish; mark production-ready |
| REVIEW | >= 7.0 | Return to author with feedback; one revision |
| REJECT | < 7.0 | Full rewrite required |

## Examples

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
tags: [prompt_compiler, intent-resolution, cex, multilingual]
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
- All 300 kinds mapped (S01 pass) | Multilingual >= 80% (S02 pass)
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
5. coverage: 15 (only 15 of 300 kinds) -> H07 FAIL (< 120)
6. Missing: title, languages, tags, tldr -> H06 FAIL
7. No Kind Resolution Table -> H07 FAIL
8. No Verb Resolution Table -> H09 FAIL
9. No ambiguity resolution -> S04 FAIL
10. No fallback heuristics -> S05 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
