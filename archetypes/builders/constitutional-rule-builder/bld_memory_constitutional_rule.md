---
quality: 7.7
id: bld_memory_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Memory"
version: 1.0.0
quality: 7.3
tags: [builder, constitutional_rule, memory]
llm_function: INJECT
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_guardrail_builder
  - bld_architecture_guardrail
  - guardrail-builder
  - p11_qg_guardrail
  - bld_instruction_guardrail
  - bld_collaboration_guardrail
  - p10_lr_guardrail_builder
  - bld_schema_guardrail
  - bld_knowledge_card_guardrail
  - p03_ins_law
---
# Memory: constitutional_rule
## Session Patterns
- Bypass test first: before writing any constitutional_rule, ask "is there ANY bypass scenario?" If yes -> guardrail, not constitutional_rule.
- One rule, one prohibition: never bundle multiple prohibitions. A rule that says "never X or Y" should be two rules.
- Concrete principles: "never deny being an AI when sincerely asked" is good. "Be honest" is not a constitutional rule -- it is a value.
- Detection is mandatory: a constitutional rule without a detection method is not enforceable.
## Common Mistakes
- Writing bypass_policy with a value: immediately downgrades to guardrail. If you catch yourself writing ANY bypass, stop and reclassify.
- Overlapping with guardrail: constitutional rules cover absolute prohibitions; guardrails cover operational safety with approved exceptions.
- Multiple prohibitions in one principle: split into separate constitutional_rule artifacts.
- Missing concrete examples: "this rule would be violated if someone asked for X" must be stated explicitly.
## CAI Basis Reference
Constitutional AI (Anthropic, 2022) defined a set of principles for LLM safety training:
1. Harm avoidance: do not help with violence, CSAM, weapons of mass destruction
2. Honesty: do not deceive, do not deny AI identity
3. Autonomy: do not manipulate, preserve user's right to decide
4. Legality: do not assist with illegal actions
These map to the constitutional_basis enum values in this builder.
## Absoluteness Test
"Could a security researcher, law enforcement agent, or operator legitimately need to bypass this?"
If YES to any role -> guardrail. If NO to all roles -> constitutional_rule.

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_guardrail_builder]] | upstream | 0.30 |
| [[bld_architecture_guardrail]] | upstream | 0.29 |
| [[guardrail-builder]] | related | 0.28 |
| [[p11_qg_guardrail]] | related | 0.28 |
| [[bld_instruction_guardrail]] | upstream | 0.27 |
| [[bld_collaboration_guardrail]] | downstream | 0.26 |
| [[p10_lr_guardrail_builder]] | upstream | 0.26 |
| [[bld_schema_guardrail]] | upstream | 0.22 |
| [[bld_knowledge_card_guardrail]] | sibling | 0.22 |
| [[p03_ins_law]] | upstream | 0.21 |
