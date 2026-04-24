---
id: p01_kc_creation_best_practices
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Creation Best Practices for LLM Artifact Engineering"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "knowledge-card-builder"
domain: artifact_engineering
quality: 9.1
tags: [creation, best-practices, artifact-engineering, 8f-pipeline, density, quality-gates, knowledge]
tldr: "8F pipeline (F1-F8 in order) + density >= 0.80 via tables/bullets + quality:null = publishable artifact; F7 gate is non-negotiable"
when_to_use: "When building, reviewing, or debugging any CEX artifact or LLM knowledge artifact"
keywords: [creation, best-practices, artifact, 8f-pipeline, density, quality-gate]
long_tails:
  - How to achieve density >= 0.80 when creating a knowledge card
  - Why does artifact creation fail the 8F quality gate
  - What is the correct pipeline order for CEX artifact creation
axioms:
  - ALWAYS run F1→F8 in sequence — skipping any function invalidates the artifact
  - NEVER self-score quality — assign null; peer review scores externally
  - IF density < 0.80 THEN replace prose paragraphs with tables and bullets before proceeding
  - ALWAYS compile and commit at F8 — .md without .yaml is an incomplete artifact
linked_artifacts:
  primary: null
  related: [p03_system_prompt_create_system_prompt_for_creation_nucleus]
density_score: 0.87
data_source: "https://docs.anthropic.com/en/docs/build-with-claude"
related:
  - p01_kc_artifact_quality_evaluation_methods
  - p01_kc_knowledge_best_practices
  - bld_knowledge_card_knowledge_card
  - p10_lr_knowledge_card_builder
  - p03_sp_n03_creation_nucleus
  - skill
  - agent_card_engineering_nucleus
  - p07_qg_12_point_validation
  - p03_sp_builder_nucleus
  - bld_instruction_knowledge_card
---
# Creation Best Practices for LLM Artifact Engineering

## Executive Summary
Artifact creation quality rests on three variables: pipeline discipline (8F in strict order), information density (>= 0.80), and external validation (quality: null, scored by peer review). The most common failure modes are skipping F7, writing prose instead of tables, and self-assigning quality scores. A run passing all 8 functions and scoring >= 8.0 on peer review is publishable.

## Spec Table
| Property | Value |
|----------|-------|
| Pipeline | F1 CONSTRAIN → F2 BECOME → F3 INJECT → F4 REASON → F5 CALL → F6 PRODUCE → F7 GOVERN → F8 COLLABORATE |
| Min density | 0.80 (data_lines / total_non_empty_lines) |
| Quality field | `null` always — peer review assigns score |
| HARD gates | 10 (all must pass; any fail = immediate reject) |
| SOFT gates | 20 weighted (>= 7.0 to publish, >= 8.0 for pool) |
| Max body | 5120 bytes |
| Retry limit | F6 max 2 retries before escalating |
| F8 commit | Mandatory — save + compile + git commit + signal |

## Patterns

### 8F Execution Map
| Function | Action | Pass Condition |
|----------|--------|---------------|
| F1 CONSTRAIN | Load kind from `kinds_meta.json` + schema | Kind resolved, max_bytes known |
| F2 BECOME | Load all 13 builder ISOs | Builder identity active, role confirmed |
| F3 INJECT | Load domain KC + scan examples | Template match score >= 60% |
| F4 REASON | Plan sections + approach (template/hybrid/fresh) | Section count + strategy decided |
| F5 CALL | Inventory tools + find similar artifacts | N similar artifacts found, tools ready |
| F6 PRODUCE | Generate complete artifact with inline density check | Bytes + sections + density reported |
| F7 GOVERN | Run H01-H10 HARD + 20 SOFT + 12LP + 5D scoring | Score reported, gates pass/fail listed |
| F8 COLLABORATE | Save + compile + commit + signal | Path confirmed, signal emitted |

### Density Boosting Hierarchy
| Format | Info/Line Ratio | Use When |
|--------|-----------------|---------|
| Tables | ~3× vs prose | Comparisons, mappings, enumerations |
| Code blocks | Exact specs | APIs, configs, CLI syntax, flows |
| Bullets (1 fact, <= 80 chars) | ~2× vs prose | Enumerable facts without relationships |
| ASCII diagrams | Visual flow | State machines, pipelines, decision trees |
| Paragraphs | 1× (baseline) | Only for context that cannot be tabularized |

### Frontmatter Retrieval Roles
| Field | Retrieval Role | High-Density Pattern |
|-------|---------------|---------------------|
| `tldr` | Primary BM25 + embedding match | Specific: "Execute X via Y, retry 3×" |
| `tags` | Faceted filtering | 3-7 tags mixing domain + technique |
| `keywords` | Exact-match BM25 boost | Terms user would literally type |
| `long_tails` | Semantic/vector search | Full question phrases |
| `when_to_use` | Agent activation trigger | Specific context, not "when needed" |
| `axioms` | Rule injection into prompts | ALWAYS/NEVER/IF-THEN imperatives |

## Anti-Patterns
| Anti-Pattern | Root Cause | Fix |
|-------------|-----------|-----|
| Skipping F7 | Time pressure | F7 is mandatory — catching early costs less than rewrite |
| `quality: 8.5` in frontmatter | Misunderstanding pipeline | Set `quality: null`; scoring is external |
| Prose body paragraphs | Default writing instinct | Convert every paragraph to bullets or table rows |
| Bullets > 80 chars | Over-compressing into one bullet | Split into 2 bullets or use a table row |
| Missing F8 compile | Saving .md without .yaml | Run `python _tools/cex_compile.py {path}` always |
| Template residue (`{{placeholder}}`) | Incomplete fill | Grep for `{{` before saving |
| Internal paths in body | Copy-paste from local env | No `records/`, `.claude/`, `C:\` in any field |
| Card > 300 lines | Scope creep during creation | Split into 2+ focused atomic cards |
| Axiom as observation | Misunderstanding axiom format | "ALWAYS declare TTL" not "caching is important" |
| `tags: "ai, ml"` as string | YAML type error | Tags must be a YAML list: `[ai, ml]` |

## Application

```text
[Builder receives intent]
        |
   [F1] Resolve kind + load schema (naming, max_bytes)
        |
   [F2] Load 13 builder ISOs (identity active)
        |
   [F3] Inject domain KC + examples (match >= 60%?)
        |
   [F4] Plan sections: template / hybrid / fresh
        |
   [F5] Inventory tools + scan N similar artifacts
        |
   [F6] Generate artifact (density check inline)
        |
   [F7] Validate H01-H10 → score >= 7.0?
        |         \
       YES         NO → fix + retry F6 (max 2×)
        |
   [F8] Save + compile + git commit + signal complete
```

Pre-save checklist:
- [ ] `id` matches `p01_kc_` prefix + filename stem
- [ ] `quality: null` (never a number)
- [ ] `density_score` >= 0.80
- [ ] >= 4 sections, each >= 3 non-empty lines
- [ ] >= 1 table, >= 1 code block, >= 1 external URL
- [ ] No bullets > 80 chars
- [ ] No internal paths (`records/`, `.claude/`, `C:\`)
- [ ] Axioms in `ALWAYS`/`NEVER`/`IF-THEN` form
- [ ] `tldr` <= 160 chars, no self-reference ("this card...")

## References
- CEX 8F pipeline: `.claude/rules/n03-8f-enforcement.md`
- Validator: `_tools/validate_kc.py v2.0` (10 HARD + 20 SOFT gates)
- Quality gates: `archetypes/builders/knowledge-card-builder/bld_quality_gate_knowledge_card.md`
- Builder ISOs: `archetypes/builders/knowledge-card-builder/` (13 files)
- Source: https://docs.anthropic.com/en/docs/build-with-claude

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_artifact_quality_evaluation_methods]] | sibling | 0.44 |
| [[p01_kc_knowledge_best_practices]] | sibling | 0.40 |
| [[bld_knowledge_card_knowledge_card]] | sibling | 0.40 |
| [[p10_lr_knowledge_card_builder]] | downstream | 0.34 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.33 |
| [[skill]] | downstream | 0.28 |
| [[agent_card_engineering_nucleus]] | downstream | 0.27 |
| [[p07_qg_12_point_validation]] | downstream | 0.26 |
| [[p03_sp_builder_nucleus]] | downstream | 0.26 |
| [[bld_instruction_knowledge_card]] | downstream | 0.26 |
