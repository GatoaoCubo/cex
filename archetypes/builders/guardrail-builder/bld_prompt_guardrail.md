---
kind: instruction
id: bld_instruction_guardrail
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for guardrail
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_guardrail_builder
  - p11_qg_guardrail
  - p03_sp_guardrail_builder
  - guardrail-builder
  - bld_knowledge_card_guardrail
  - bld_architecture_guardrail
  - bld_tools_guardrail
  - bld_instruction_golden_test
  - bld_collaboration_guardrail
  - bld_instruction_output_validator
---

# Instructions: How to Produce a guardrail
## Phase 1: RESEARCH
1. Identify the threat or risk to guard against — what harm, misuse, or failure mode does this guardrail prevent?
2. Classify severity: critical (system-breaking or data-destroying), high (significant operational impact), medium (quality degradation), low (minor policy deviation)
3. Determine enforcement mode: block (reject the operation), warn (proceed with logged alert), log (silent audit trail)
4. Define scope of application — which agents, pipelines, operations, or domains does this guardrail cover?
5. Catalog violation examples — collect at least 2 concrete inputs or actions that would trigger this guardrail
6. Check existing guardrails for coverage gaps — avoid duplicating a guardrail that already covers this threat
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required fields, quality: null (never self-score), severity and enforcement set from research
4. Write Threat section: what risk this guardrail addresses and why it matters in this domain
5. Write Rules section: specific restrictions as declarative statements — each rule must be concrete and independently enforceable
6. Write Severity section: classification (critical/high/medium/low) with one-paragraph justification
7. Write Enforcement section: enforcement mode (block/warn/log) and the implementation mechanism that detects violations
8. Write Violations section: at least 2 concrete examples of inputs or actions that trigger this guardrail
9. Write Bypass Policy section: under what conditions this can be overridden (if ever), who must approve, and what audit trail is required
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p11_gr_[a-z][a-z0-9_]+`
   - [ ] kind == `guardrail`
   - [ ] quality == null
   - [ ] severity is one of: critical, high, medium, low
   - [ ] enforcement mode is one of: block, warn, log
   - [ ] at least 2 violation examples present
3. SOFT gates: rules are concrete not aspirational, bypass policy defined, scope of application specified
4. Cross-check: safety boundary not access control (that is permission)? Not an operational law? Not quality scoring (that is quality_gate)? Every rule enforceable without subjective judgment?
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify guardrail
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | guardrail construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_guardrail_builder]] | downstream | 0.48 |
| [[p11_qg_guardrail]] | downstream | 0.47 |
| [[p03_sp_guardrail_builder]] | related | 0.46 |
| [[guardrail-builder]] | downstream | 0.44 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.43 |
| [[bld_architecture_guardrail]] | downstream | 0.43 |
| [[bld_tools_guardrail]] | downstream | 0.37 |
| [[bld_instruction_golden_test]] | sibling | 0.36 |
| [[bld_collaboration_guardrail]] | downstream | 0.36 |
| [[bld_instruction_output_validator]] | sibling | 0.35 |
