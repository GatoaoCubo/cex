---
kind: examples
id: bld_examples_builder
pillar: P03
llm_function: GOVERN
purpose: Reference examples of well-built builders
quality: 9.0
title: "Examples Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_kind
  - _builder-builder
  - kind-builder
  - bld_collaboration_builder
  - bld_config_builder
  - bld_output_template_builder
  - bld_collaboration_kind
  - polish_fixes_20260413
  - bld_collaboration_effort_profile
  - bld_collaboration_retriever
---
# Examples: _builder-builder

## Example 1: Minimal Skeleton Builder
Builder: `memory-scope-builder` (13 files, 24KB)
1. Created via Validation Registry spec
2. Skeleton pattern: minimal content per ISO
3. All universal fields present
4. Doctor: PASS, 0 WARN

## Example 2: Full-Featured Builder
Builder: `agent-builder` (13 files, 42KB)
1. Full content in all ISOs
2. 212 crew compositions in bld_collaboration
3. Non-default overrides: effort=high, permission_scope=pillar
4. Doctor: PASS, 0 WARN

## Example 3: Domain-Specific Builder
Builder: `content-monetization-builder` (13 files, 45KB)
1. Hotmart + Digistore24 parity in tools
2. Platform-specific quality gates
3. effort=high, permission_scope=nucleus
4. Doctor: PASS, 0 WARN

## Anti-Example: Missing Universal Fields
❌ Builder without keywords in manifest → doctor WARN
❌ Builder without memory_scope → hydration required
❌ Builder with effort but no model mapping → runtime failure

## Injection

```yaml
loader: cex_skill_loader
stage: F3_compose
role: exemplar
max_examples: 3
```

```bash
python _tools/cex_retriever.py --kind examples --top 3
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P03 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.43 |
| [[_builder-builder]] | upstream | 0.42 |
| [[kind-builder]] | downstream | 0.39 |
| [[bld_collaboration_builder]] | downstream | 0.39 |
| [[bld_config_builder]] | downstream | 0.34 |
| [[bld_output_template_builder]] | related | 0.32 |
| [[bld_collaboration_kind]] | downstream | 0.32 |
| [[polish_fixes_20260413]] | downstream | 0.32 |
| [[bld_collaboration_effort_profile]] | downstream | 0.31 |
| [[bld_collaboration_retriever]] | downstream | 0.29 |
