---
id: p03_ins_prompt_compiler
kind: instruction
pillar: P03
version: 1.0.0
created: "2026-04-12"
updated: "2026-04-12"
author: n03_builder
title: "Prompt Compiler Builder Instructions"
target: "prompt-compiler-builder agent"
phases_count: 4
prerequisites:
  - "kinds_meta.json loaded (124 kinds)"
  - "n07-input-transmutation.md read for existing mappings"
  - "Target languages identified (minimum PT-BR + EN)"
validation_method: checklist
domain: prompt_compiler
quality: 9.1
tags: [instruction, prompt_compiler, P03, intent-resolution]
idempotent: true
atomic: false
rollback: "Delete the produced prompt_compiler file. No resolution behavior changes until loaded as prompt layer."
dependencies: []
logging: true
tldr: "Build intent resolution tables mapping all 124 kinds to user patterns in PT-BR+EN with verb resolution, ambiguity protocol, and fallback heuristics."
density_score: 0.91
llm_function: REASON
---
## Context
A **prompt_compiler** artifact defines intent-to-artifact transmutation rules: given natural language user input, which {kind, pillar, nucleus, verb} should handle it? It contains a kind resolution table (all 124 kinds), verb resolution (user verbs to canonical actions), ambiguity resolution (multi-match protocol), and fallback heuristics (unrecognized input).
**Inputs**
| Field | Type | Description |
|---|---|---|
| `kinds_registry` | JSON | `.cex/kinds_meta.json` -- all 124 kinds with pillar, llm_function, boundary |
| `existing_mappings` | markdown | `.claude/rules/n07-input-transmutation.md` -- existing user-to-kind tables |
| `languages` | list | Target languages for pattern matching (minimum: [pt-br, en]) |
| `domain` | string | Scope of this compiler (e.g., `cex_universal` for full coverage) |
**Output**
A single `.md` file with YAML frontmatter + body containing: Preamble, Kind Resolution Table, Verb Resolution Table, Ambiguity Resolution, Fallback Heuristics, Nucleus Routing Matrix, Behavioral Instructions. Body must be <= 16384 bytes.
**Boundary rules**
- prompt_compiler = intent resolution rules with kind/pillar/nucleus mapping (this builder)
- router = provider-to-provider routing with confidence thresholds (different builder)
- dispatch_rule = task-to-agent keyword mapping (different builder)
- prompt_template = template with `{{variables}}` for prompt generation (different builder)
## Phases
### Phase 1: Research -- Kind Inventory
Load and analyze all 124 kinds before writing.
```
READ .cex/kinds_meta.json
FOR each kind:
  extract: pillar, llm_function, boundary, description, naming
  determine: primary nucleus (N01-N07) based on domain
  identify: 2-5 user input patterns in EN
  identify: 2-5 user input patterns in PT-BR
  note: boundary (when NOT to pick this kind)
READ .claude/rules/n07-input-transmutation.md
MERGE existing patterns with new patterns (expand, never reduce)
```
Deliverable: full kind inventory with patterns, nucleus assignment, and boundary.
### Phase 2: Classify -- Boundary Check
```
IF caller needs provider routing with confidence thresholds:
  RETURN "Route to router-builder -- provider routing, not intent resolution."
IF caller needs task-to-agent keyword mapping:
  RETURN "Route to dispatch-rule-builder -- simple dispatch, not compilation."
IF caller needs a template with {{variables}}:
  RETURN "Route to prompt-template-builder -- template filling, not resolution."
IF caller needs intent-to-{kind,pillar,nucleus,verb} resolution:
  PROCEED as prompt_compiler
```
### Phase 3: Compose -- Build the Prompt Compiler
```
ID: p03_pc_{slug}
Frontmatter: id, kind=prompt_compiler, pillar=P03, title, version, created, updated,
  author, domain, coverage=124, languages=[pt-br,en], quality=null, tags, tldr
Body sections (in order):
  ## Preamble -- what this artifact is, how LLMs use it
  ## Kind Resolution Table -- ALL 124 kinds, grouped by pillar
    Columns: Kind | Pillar | Nucleus | Patterns (EN) | Patterns (PT) | Verb | 8F Fn | Boundary
  ## Verb Resolution Table -- 30+ verbs, PT+EN, canonical action, 8F function
  ## Ambiguity Resolution -- multi-match protocol (context, specificity, frequency, GDP)
  ## Fallback Heuristics -- TF-IDF, semantic similarity, confidence threshold
  ## Nucleus Routing Matrix -- 124-kind x 7-nucleus table (compressed)
  ## Behavioral Instructions -- rules for LLM operating as prompt compiler
```
### Phase 4: Validate -- Quality Gates
```
CHECK: all 124 kinds present in Kind Resolution Table
CHECK: bilingual coverage >= 80%
CHECK: every kind has at least 1 EN pattern and 1 PT pattern
CHECK: verb table has >= 30 entries
CHECK: ambiguity resolution protocol defined
CHECK: fallback heuristics defined
CHECK: body <= 16384 bytes
CHECK: quality: null
CHECK: id == filename stem
```
