---
kind: knowledge_card
id: bld_knowledge_card_lens
pillar: P02
llm_function: INJECT
purpose: Domain knowledge for lens production — atomic searchable facts
sources: lens-builder MANIFEST.md + SCHEMA.md v1.0.0
quality: 9.1
title: "Knowledge Card Lens"
version: "1.0.0"
author: n03_builder
tags: [lens, builder, examples]
tldr: "Golden and anti-examples for lens construction, demonstrating ideal structure and common pitfalls."
domain: "lens construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_lens
  - p03_sp_lens_builder
  - bld_architecture_lens
  - p11_qg_lens
  - lens-builder
  - bld_collaboration_lens
  - bld_memory_lens
  - bld_schema_lens
  - bld_output_template_lens
  - p01_kc_lens
---

# Domain Knowledge: lens
## Executive Summary
Lenses are analytical perspectives applied to artifacts to filter, emphasize, or reinterpret information without modifying the source. Each lens declares ONE focus with explicit bias, scoped applies_to targets, and composable weight for multi-lens pipelines. They differ from agents (which act), mental models (which route decisions), scoring rubrics (which assign scores), and context docs (which provide background) by being purely declarative interpretation filters.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (design-time spec) |
| Kind | `lens` (exact literal) |
| ID pattern | `p02_lens_{slug}` |
| Required frontmatter | 20 fields |
| Quality gates | 8 HARD + 8 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | focus, filters, bias, applies_to, weight |
## Patterns
| Pattern | Application |
|---------|-------------|
| Single focus | Each lens addresses ONE analytical dimension, not a collection |
| Explicit bias | Declared upfront in frontmatter — never hidden |
| Scoped applies_to | Specific artifact kinds, not "everything" |
| Concrete filters | Named attributes, not abstract categories |
| Composable weight | Float 0.0-1.0 enabling multi-lens combination |
| Mandatory limitations | Every perspective has blind spots — document them |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Multiple unrelated filters in one lens | Violates single-focus principle |
| Hidden or implicit bias | Consumers cannot calibrate interpretation |
| applies_to: "all" | Overly broad; lens loses analytical value |
| Abstract filter names ("quality aspects") | Not actionable; name specific attributes |
| Missing limitations section | Every perspective has blind spots |
| Lens that modifies artifacts | Lenses FILTER, they do not ACT |
## Application
1. Define ONE analytical focus (e.g., "cost efficiency", "security posture")
2. Set `applies_to` with specific artifact kinds this lens targets
3. Declare `bias` explicitly (what this perspective favors/disfavors)
4. List `filters` as concrete named attributes
5. Set `weight` for multi-lens composition (0.0-1.0)
6. Document `limitations` — blind spots of this perspective
7. Validate: body <= 3072 bytes, density >= 0.80, 8 HARD + 8 SOFT gates
## References
- lens-builder SCHEMA.md v1.0.0
- Evans, Eric. Domain-Driven Design (2003) — Bounded Contexts
- Kiczales et al. Aspect-Oriented Programming (1997) — Cross-cutting concerns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_lens]] | downstream | 0.64 |
| [[p03_sp_lens_builder]] | downstream | 0.62 |
| [[bld_architecture_lens]] | downstream | 0.60 |
| [[p11_qg_lens]] | downstream | 0.59 |
| [[lens-builder]] | related | 0.58 |
| [[bld_collaboration_lens]] | related | 0.55 |
| [[bld_memory_lens]] | downstream | 0.54 |
| [[bld_schema_lens]] | downstream | 0.50 |
| [[bld_output_template_lens]] | downstream | 0.48 |
| [[p01_kc_lens]] | sibling | 0.43 |
