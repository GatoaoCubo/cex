---
kind: output_template
id: bld_output_template_reasoning_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for reasoning_strategy production
quality: 9.1
title: "Output Template Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, output_template]
tldr: "Template with vars for reasoning_strategy production"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reasoning_strategy
  - p03_sp_reasoning_strategy_builder
  - bld_instruction_reasoning_strategy
  - p03_qg_reasoning_strategy
  - bld_config_reasoning_strategy
  - p11_qg_chain
  - kc_reasoning_strategy
  - reasoning-strategy-builder
  - bld_collaboration_reasoning_strategy
  - bld_instruction_chain
---

```yaml
id: p03_rs_{{slug}}               # e.g. p03_rs_chain_of_thought
kind: reasoning_strategy
pillar: P03
title: "{{Descriptive Strategy Name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_team}}"
domain: "{{application domain, e.g. legal reasoning, code debugging}}"
quality: null                     # NEVER self-score
tags: [reasoning_strategy, "{{domain_tag}}", "{{method_tag}}"]
tldr: "{{One concrete sentence: what reasoning pattern, for what context}}"
reasoning_type: "{{deductive|inductive|abductive}}"
strategy_depth: {{1-5}}           # 1=basic heuristic, 5=formal logic chain
```

## Overview

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
<!-- Purpose: what problem this reasoning strategy solves.
     Scope: what input types it applies to.
     Contrast: how it differs from similar strategies. -->

## Core Components
<!-- Numbered steps of the reasoning chain.
     Each step: input -> transformation -> output.
     Include decision points and branching conditions. -->
| Step | Operation | Input | Output |
|------|-----------|-------|--------|
| 1 | `{{operation}}` | {{input_type}} | `{{output_type}}` |

## Validation Criteria
<!-- Measurable checks that confirm the strategy worked correctly.
     At least 3 concrete criteria with pass/fail conditions. -->
- PASS: `{{concrete measurable condition}}`
- FAIL: `{{failure indicator}}`

## Application Scope
<!-- When to use: specific trigger conditions.
     When NOT to use: boundary conditions and anti-patterns. -->
| Use | Condition |
|-----|-----------|
| Apply | `{{specific trigger}}` |
| Skip | `{{boundary condition}}` |

## Quality Metrics
| Metric | Target | Method |
|--------|--------|--------|
| Logical soundness | 100% | Formal verification or peer review |
| Step completeness | All steps traced | Audit against schema |
| Domain coverage | >= 3 examples | Examples ISO cross-check |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reasoning_strategy]] | downstream | 0.33 |
| [[p03_sp_reasoning_strategy_builder]] | upstream | 0.33 |
| [[bld_instruction_reasoning_strategy]] | upstream | 0.33 |
| [[p03_qg_reasoning_strategy]] | downstream | 0.33 |
| [[bld_config_reasoning_strategy]] | downstream | 0.32 |
| [[p11_qg_chain]] | downstream | 0.30 |
| [[kc_reasoning_strategy]] | upstream | 0.29 |
| [[reasoning-strategy-builder]] | upstream | 0.28 |
| [[bld_collaboration_reasoning_strategy]] | downstream | 0.28 |
| [[bld_instruction_chain]] | upstream | 0.28 |
