---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for knowledge_card production
sources: validate_kc.py v2.0 + _schema.yaml v4.0 + 63 real examples
---

# Domain Knowledge: knowledge_card

## Core Concept

Knowledge cards are ATOMIC SEARCHABLE FACTS — smallest unit in a retrieval system. Each answers ONE question about ONE topic. Density > 0.80 = >80% concrete data (no filler).

## Frontmatter: The Retrieval Surface

| Field | Retrieval Role | Pattern |
|-------|---------------|---------|
| tldr | Primary match (BM25 + embedding) | Specific: "Execute CLI via subprocess, retry 3x, JSONL parse" NOT "How to use CLI" |
| tags | Faceted filtering, clustering | 3-7 tags, mix domain + technique + scope |
| keywords | BM25 exact match boost | 2-5 terms user would literally type |
| long_tails | Semantic/vector search | Full phrases: "how to handle concurrent token refresh" |
| when_to_use | Agent activation trigger | Specific context, not "when needed" |

## Body: Dense Information

**Density hierarchy** (most to least info/token):
1. Tables — comparisons, specs, mappings
2. Code blocks — implementation patterns
3. Bullet lists — facts, rules, steps
4. ASCII diagrams — flows, architectures
5. Short paragraphs — only when tables can't express

**Effective sections**: Overview (2-3 dense sentences), Classification tables, Pattern descriptions (name + when + code + tradeoffs), Anti-patterns (what fails + WHY), References.

## Density Gate

```
density = data_lines / total_non_empty_lines
Target: >= 0.80 (ideally 0.85-0.95)
```

**Density < 0.80 = card fails** regardless of other quality.

Killers: transition sentences, restating title, generic QA, filler, boilerplate.
Maximizers: unique facts per table row, real code, fact-first bullets, numbers over qualitative.

## Size: 50-120 Lines

- 50-80: focused single-concept, highest density scores
- 80-120: multi-pattern with tables, still dense
- 200+: split into 2 cards. Body max: 5120 bytes

## Tags & Keywords

- **Tags** (3-7): mix abstraction levels, domain + technique
- **Keywords**: terms user literally types, include abbreviations
- **Long_tails**: 5-15 word phrases, natural language questions

## Axioms

Well-formed: `ALWAYS/NEVER/IF-THEN` with condition + action + consequence.
Weak: vague ("be careful"), no threshold, no specific action.

## Two Body Structures

- **domain_kc**: external knowledge (tech, APIs). Sections: Quick Ref, Key Concepts, Strategy, Golden Rules, Flow, References
- **meta_kc**: system-internal. Sections: Exec Summary, Spec Table, Patterns, Anti-Patterns, Application, References

## Quality & Scoring

| Tier | Score | Gate |
|------|-------|------|
| GOLDEN | >= 9.5 | All HARD + 95% SOFT |
| PUBLISH | >= 8.0 | All HARD + 80% SOFT |
| ACCEPTABLE | >= 7.0 | All HARD + 70% SOFT |
| REJECTED | -- | Any HARD fails |

5 dimensions (2 pts each): D1 Frontmatter, D2 Density (evaluate first), D3 Axioms, D4 Structure, D5 Format.

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Vague tldr | Add specifics: model, method, metrics |
| Prose body | Convert to tables, bullets, code |
| Template residue | Fill or remove every placeholder |
| Frontmatter echo in body | Body adds depth, not repetition |
| Giant monolith (300+) | Split into focused atomic cards |

## Boundary

| Type | KC differs because |
|------|-------------------|
| model_card | KC = external research, MC = LLM specs |
| learning_record | KC = research, LR = internal experience |
