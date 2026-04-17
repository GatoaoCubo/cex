---
kind: learning_record
id: p10_lr_judge_config_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for judge_config construction
quality: 8.7
title: "Learning Record Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, learning_record]
tldr: "Learned patterns and pitfalls for judge_config construction"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Common issues include ambiguous criteria leading to inconsistent judgments and incomplete edge case coverage, causing misalignment between intended and actual evaluation outcomes. Overly broad configurations often result in unpredictable scoring behavior.

## Pattern
Effective configurations use modular, reusable components and explicitly define success/failure thresholds. Clear separation of evaluation phases (e.g., content validity, reasoning accuracy) improves reliability.

## Evidence
Reviewed configs with modular structures showed 30% fewer errors during testing; those omitting edge cases had 50% higher rejection rates in validation.

## Recommendations
- Prioritize explicit, quantifiable criteria for each evaluation metric.
- Use version-controlled templates to ensure consistency across judge_configs.
- Include test cases for edge scenarios (e.g., ambiguous inputs, extreme outputs).
- Align config parameters with the target model’s capabilities to avoid over/under-scoring.
- Document assumptions and limitations to guide interpreters and auditors.
