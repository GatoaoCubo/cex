---
id: quality_gate_intent_resolution
kind: quality_gate
8f: F7_govern
pillar: P11
title: Quality Gate -- Intent Resolution Validation
version: 1.0.0
created: 2026-04-08
author: n03_builder
domain: meta-construction/intent-resolution
quality: 9.2
tags: [quality-gate, intent-resolution, test-cases, transmutation, validation]
tldr: "20 test cases (10 EN, 10 PT) validating that user phrases correctly resolve to kind, pillar, and nucleus."
density_score: 0.93
related:
  - p03_pc_cex_universal
  - spec_seed_words
  - p01_kc_intent_resolution_benchmark
  - p01_kc_input_intent_resolution
  - p12_wf_create_orchestration_agent
  - kc_intent_resolution_map
  - p01_kc_prompt_compiler
  - p03_ins_prompt_compiler
  - p12_dr_builder_nucleus
  - report_intent_resolution_testing
---

# Quality Gate: Intent Resolution

## Purpose

Validates that the intent resolution pipeline (intent resolution rule + cex_8f_motor.py + cex_query.py)
correctly maps natural language user input to the expected kind, pillar, and nucleus.

## Gate Criteria

| Criterion | Threshold | Measurement |
|-----------|-----------|-------------|
| Kind accuracy | >= 90% (18/20) | Correct kind resolved |
| Pillar accuracy | >= 95% (19/20) | Correct pillar resolved |
| Nucleus accuracy | >= 90% (18/20) | Correct nucleus routed |
| Verb resolution | >= 85% (17/20) | Correct action parsed |
| Zero false-positives | 0 wrong kind returned | No misrouted intents |

## Test Cases: English (10)

| # | User Input | Expected Kind | Expected Pillar | Expected Nucleus | Expected Action |
|---|-----------|---------------|-----------------|------------------|-----------------|
| E01 | "create an agent for customer support" | agent | P02 | N03 | create |
| E02 | "set up a webhook for Stripe payments" | webhook | P04 | N05 | create |
| E03 | "write a scoring rubric for my evals" | scoring_rubric | P07 | N05 | create |
| E04 | "add a safety guardrail for content" | guardrail | P11 | N03 | create |
| E05 | "build a landing page for my product" | landing_page | P05 | N03 | create |
| E06 | "configure rate limits for the API" | rate_limit_config | P09 | N05 | configure |
| E07 | "analyze the workflow dependencies" | dag OR workflow | P12 | N03 | analyze |
| E08 | "test the prompt chain end to end" | e2e_eval | P07 | N05 | test |
| E09 | "define an input schema for the form" | input_schema | P06 | N03 | create |
| E10 | "schedule a nightly optimization run" | schedule | P12 | N07 | schedule |

## Test Cases: Portuguese (10)

| # | User Input | Expected Kind | Expected Pillar | Expected Nucleus | Expected Action |
|---|-----------|---------------|-----------------|------------------|-----------------|
| P01 | "criar agente de vendas" | agent | P02 | N03 | create |
| P02 | "documentar como funciona o RAG" | knowledge_card | P01 | N04 | document |
| P03 | "melhorar a qualidade dos artefatos" | optimizer | P11 | N05 | improve |
| P04 | "validar o schema de entrada" | input_schema OR validator | P06 | N03 | validate |
| P05 | "configurar embedding para busca" | embedding_config | P01 | N04 | configure |
| P06 | "testar o pipeline de ponta a ponta" | e2e_eval | P07 | N05 | test |
| P07 | "criar template de prompt para ads" | prompt_template | P03 | N03 | create |
| P08 | "montar diagrama de arquitetura" | diagram | P08 | N03 | create |
| P09 | "agendar tarefa de limpeza semanal" | schedule | P12 | N07 | schedule |
| P10 | "monetizar curso no Hotmart" | content_monetization | P11 | N06 | create |

## Validation Protocol

### Manual Validation (human or N07)

For each test case:
1. Feed the user input to `python _tools/cex_8f_motor.py --intent "{input}"`
2. Compare output `kind` to expected
3. Compare output `pillar` to expected
4. Verify nucleus routing matches expected (requires routing table check)
5. Check verb_action matches expected action

### Automated Validation (future)

```bash
# When cex_e2e_test.py supports intent resolution:
python _tools/cex_e2e_test.py --suite intent_resolution --cases 20
```

### Scoring

| Result | Score |
|--------|-------|
| 20/20 correct | 10.0 |
| 18-19/20 correct | 9.0 |
| 16-17/20 correct | 8.0 |
| 14-15/20 correct | 7.0 |
| < 14/20 correct | FAIL -- fix pipeline |

## Edge Cases (bonus validation)

| # | User Input | Challenge | Expected Resolution |
|---|-----------|-----------|---------------------|
| X01 | "quero melhorar os artefatos que estao ruins" | PT informal + vague target | action: improve, tool: cex_evolve.py |
| X02 | "make me something for tracking bugs" | Ambiguous -- bugloop or issue tracker? | kind: bugloop (closest CEX kind) |
| X03 | "webhook + API client for Stripe" | Multi-kind intent | kind: [webhook, api_client], pillar: P04 |
| X04 | "research pipeline STORM style" | Specific pattern reference | kind: research_pipeline, pillar: P04 |
| X05 | "" (empty input) | No input | Graceful error, no crash |

## Gate Pass/Fail Decision

```
IF kind_accuracy >= 90% AND pillar_accuracy >= 95%:
    PASS -- intent resolution is reliable
ELSE IF kind_accuracy >= 80%:
    WARN -- add missing mappings to OBJECT_TO_KINDS
ELSE:
    FAIL -- intent resolution needs structural fix
```

## References

- `N03_engineering/P01_knowledge/kc_intent_resolution_map.md` -- exhaustive 123-kind mapping
- `_tools/cex_8f_motor.py` -- OBJECT_TO_KINDS and parse_intent()
- `_tools/cex_query.py` -- TF-IDF fallback
- `.claude/rules/n07-input-transmutation.md` -- intent resolution protocol

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pc_cex_universal]] | upstream | 0.46 |
| [[spec_seed_words]] | upstream | 0.30 |
| [[p01_kc_intent_resolution_benchmark]] | upstream | 0.28 |
| [[p01_kc_input_intent_resolution]] | upstream | 0.27 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.27 |
| [[kc_intent_resolution_map]] | upstream | 0.27 |
| [[p01_kc_prompt_compiler]] | upstream | 0.26 |
| [[p03_ins_prompt_compiler]] | upstream | 0.26 |
| [[p12_dr_builder_nucleus]] | downstream | 0.26 |
| [[report_intent_resolution_testing]] | upstream | 0.26 |
