---
id: n01_readme_comparison
kind: output_template
pillar: P01
quality: 9.0
density_score: 0.95
title: "Output Readme Comparison"
version: 1.0.0
author: N01
tags: [output_template, intelligence, output]
tldr: "**Typed Knowledge**: Critical for enterprises with compliance requirements or knowledge workers who need guaranteed artifact structure and validation."
domain: intelligence
created: 2026-04-06
updated: 2026-04-07
related:
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - p06_schema_a11y_checklist
  - bld_schema_integration_guide
  - bld_schema_context_window_config
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_voice_pipeline
---

## Feature Comparison

| Feature             | CEX        | LangChain     | CrewAI        | AutoGen       | Semantic Kernel |
|---------------------|------------|---------------|---------------|---------------|-----------------|
| Typed Knowledge     | **Yes**    | No            | No            | No            | No              |
| Multi-Agent         | **Yes**    | Via extensions| **Yes**       | **Yes**       | **Yes**         |
| Quality Pipeline    | **Yes**    | No            | No            | No            | No              |
| Fine-Tune Ready     | **Yes**    | No            | No            | No            | No              |
| Offline/Local       | **Yes**    | Yes           | Yes           | Yes           | Yes             |
| Brand Injection     | **Yes**    | No            | No            | No            | No              |
| 100+ Builders       | **Yes**    | No            | No            | No            | No              |

## When It Matters

**Typed Knowledge**: Critical for enterprises with compliance requirements or knowledge workers who need guaranteed artifact structure and validation.

**Quality Pipeline**: Essential for production deployments where output consistency affects revenue (customer-facing content, automated reports).

**Brand Injection**: Game-changer for agencies serving multiple clients — eliminates manual style guide enforcement and ensures brand consistency across all outputs.

**100+ Builders**: Valuable for teams that need specialized output formats without custom prompt engineering (legal docs, technical specs, marketing materials).

**Fine-Tune Ready**: Important for organizations planning to train custom models on their proprietary processes and knowledge base.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | intelligence | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Intelligence artifacts follow CEX 8F pipeline from intent to publication
- Quality gates enforce minimum 8.0 threshold for all published artifacts
- Cross-nucleus references use explicit id-based linking, not path-based
- Version tracking enables rollback to any previous artifact state

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_bugloop]] | downstream | 0.48 |
| [[bld_schema_quickstart_guide]] | downstream | 0.45 |
| [[bld_schema_usage_report]] | downstream | 0.45 |
| [[bld_schema_reranker_config]] | downstream | 0.44 |
| [[p06_schema_a11y_checklist]] | downstream | 0.43 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_context_window_config]] | downstream | 0.42 |
| [[bld_schema_pitch_deck]] | downstream | 0.42 |
| [[bld_schema_dataset_card]] | downstream | 0.42 |
| [[bld_schema_voice_pipeline]] | downstream | 0.42 |
