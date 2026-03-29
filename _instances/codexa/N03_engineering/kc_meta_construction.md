---
id: p01_kc_meta_construction
kind: knowledge_card
type: domain
pillar: P01
title: "KC: Meta-Construction Patterns"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
domain: meta_construction
origin: manual
quality: null
tags: [knowledge-card, meta-construction, builder, pattern, engineering]
tldr: "Core patterns for building the things that build things — builder ISOs, template composition, 8F pipeline, quality gates"
keywords: [builder, iso, template, 8f, pipeline, quality, scaffold, meta]
feeds_kinds: [agent, system_prompt, instruction, workflow, quality_gate, pattern]
density_score: 0.88
---

# KC: Meta-Construction Patterns

## Quick Reference
```yaml
topic: Building artifacts that build artifacts
scope: Builder ISOs, templates, 8F pipeline, quality gates
criticality: high
```

## Key Concepts
| Concept | CEX Kind | Purpose |
|---------|----------|---------|
| Builder ISO | type_builder | 13 files that define how to build one kind |
| Template | prompt_template | Skeleton with {{vars}} for kind instances |
| 8F Pipeline | workflow | 8 functions that transform intent into artifact |
| Quality Gate | quality_gate | Hard gates (structural) + soft gates (semantic) |
| Frontmatter | interface | YAML header that every artifact must have |
| Kind | type_def | Canonical name for an artifact type (99 total) |

## Patterns
| Pattern | When |
|---------|------|
| Builder-first | Always check builder ISOs before manual creation |
| Example-guided | Read 2+ existing examples before generating new |
| Sequential multi-kind | Run runner per kind, not all at once |
| Doctor-after-batch | Run doctor after creating 3+ artifacts |
| Dry-run-first | Preview with --dry-run before committing LLM calls |

## Anti-Patterns
| Anti-Pattern | Why |
|-------------|-----|
| Manual artifact creation | Skips quality gates, misses builder knowledge |
| Copy-paste between kinds | Each kind has unique schema constraints |
| Batch generation without validation | Errors cascade across dependent artifacts |
