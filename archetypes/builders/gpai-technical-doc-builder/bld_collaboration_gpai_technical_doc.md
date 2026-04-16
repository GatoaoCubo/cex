---
kind: collaboration
id: bld_collaboration_gpai_technical_doc
pillar: P12
llm_function: COLLABORATE
purpose: How gpai_technical_doc-builder works in crews with other builders
quality: 8.9
title: "Collaboration GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, collaboration, GPAI, EU-AI-Act, Annex-IV, Article-53]
tldr: "How gpai_technical_doc-builder works in crews with other builders"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role
Produces EU AI Act GPAI technical documentation (Article 53 / Annex IV) for submission to the EU AI Office, covering training data, compute, energy, evaluation, intended purpose, and downstream limits.

## Receives From
| Builder | What | Format |
|---------|------|--------|
| model_card-builder | Informal model metadata as source material | Markdown |
| eval_framework-builder | Evaluation methodology and benchmark results | Markdown |
| compliance_framework-builder | EU AI Act obligations mapping | Markdown |
| N01 Intelligence | EU AI Act regulatory intelligence and deadline tracking | Knowledge Card |

## Produces For
| Builder | What | Format |
|---------|------|--------|
| compliance_framework-builder | GPAI compliance status feeding broader EU compliance | Markdown |
| safety_policy-builder | Downstream-limit clauses feeding safety policies | Markdown |
| api_client-builder | Downstream-limit terms for API terms of service | Markdown |
| conformity_assessment-builder | Technical doc as input to high-risk system assessment | Markdown |

## Boundary
Does NOT handle NIST AI-RMF profiles (use ai_rmf_profile-builder), conformity assessments for high-risk AI systems (separate artifact), or informal model cards (use model_card-builder). EU AI Office submission logistics and legal certification are managed by legal/compliance teams.
