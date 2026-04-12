---
id: p01_kc_builder_construction
kind: knowledge_card
pillar: P01
title: "CEX Builder — Artifact Construction via 8F Pipeline"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 9.0
tags: [knowledge-card, builder, N03, 8F, construction, ISOs, pipeline]
tldr: "N03 builds all 123 CEX kinds via 8F pipeline — load ISOs, inject context, produce with frontmatter, compile to YAML."
when_to_use: "When understanding how CEX builds artifacts, what the 8F pipeline does, or how builder ISOs work."
keywords: [builder, 8F, pipeline, ISO, artifact, kind, construct, compile, frontmatter, schema]
long_tails:
  - "how does N03 build a CEX artifact"
  - "what are builder ISOs and how are they loaded"
  - "what happens at each step of the 8F pipeline"
  - "how to add a new kind to the CEX system"
axioms:
  - "ALWAYS execute full 8F pipeline — no step may be skipped"
  - "ALWAYS set quality: null — builders never self-score"
  - "ALWAYS compile after save — .md and .yaml must stay in sync"
  - "IF subjective decision at F4 THEN GDP gate — ask user first"
linked_artifacts:
  primary: "N03_builder/agents/agent_builder.md"
  related:
    - N03_builder/prompts/system_prompt_builder.md
    - N03_builder/architecture/agent_card_builder.md
    - archetypes/builders/_shared/skill_guided_decisions.md
density_score: 0.96
data_source: "archetypes/builders/ + .cex/kinds_meta.json"
---

# CEX Builder — Artifact Construction via 8F Pipeline

## Quick Reference

```yaml
nucleus: N03
sin: Soberba (Pride)
virtue: Inventive Pride
kinds_supported: 123
builders: 125
isos_per_builder: 13
pipeline: 8F (F1→F8)
quality_floor: 9.0
```

## Key Concepts

### Builder ISOs

Each of the 125 builders has 13 ISO files that define its construction blueprint:

| ISO | Purpose |
|-----|---------|
| `01_identity.md` | Kind name, pillar, domain |
| `02_schema.md` | Required frontmatter fields |
| `03_constraints.md` | Size limits, format rules |
| `04_examples.md` | Golden examples |
| `05_anti_patterns.md` | What NOT to do |
| `06_linked_kinds.md` | Related kinds |
| `07_output_format.md` | Body structure template |
| `08_tools.md` | Tools this builder uses |
| `09_memory.md` | Relevant memory entries |
| `10_brand.md` | Brand injection points |
| `11_quality.md` | Quality criteria |
| `12_workflow.md` | Build sequence |
| `13_finalize.md` | Post-build steps |

### 8F Pipeline Steps

1. **F1 CONSTRAIN**: Map intent → kind + pillar. Lock scope via schema.
2. **F2 BECOME**: Load 13 ISOs. Builder absorbs the kind's persona.
3. **F3 INJECT**: Add brand config, relevant memory, linked artifacts.
4. **F4 REASON**: Plan artifact structure. GDP gate for subjective decisions.
5. **F5 CALL**: Enrich with tool outputs (retriever, similar artifacts).
6. **F6 PRODUCE**: Generate artifact with valid YAML frontmatter.
7. **F7 GOVERN**: Schema validation + `quality: null` enforcement.
8. **F8 COLLABORATE**: Save → compile → commit `[N03]` → signal complete.

### Kind Registry

`.cex/kinds_meta.json` maps all 123 kinds to their pillar, domain, and builder path.
The builder uses `cex_query.py` to resolve free-text intent to the correct kind.

## Anti-Patterns

- Skipping F2 (ISO loading) — produces generic, unstructured artifacts
- Self-scoring quality — only peer review via `cex_score.py` assigns quality
- Skipping F8 compilation — leaves `.md` and `.yaml` out of sync
- Building outside scope fence — artifacts must match handoff task
- Treating this as a standalone reference without loading builder ISOs

## References

- Builder ISOs: `archetypes/builders/{kind}-builder/`
- Kind registry: `.cex/kinds_meta.json`
- Shared skills: `archetypes/builders/_shared/`
- Quality gate: N03_builder/quality/quality_gate_builder.md
