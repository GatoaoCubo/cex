---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for designing quality gates that reliably filter artifacts
sources: [Cooper 1990, SonarQube, DORA, 5 production quality gate files]
---

# Domain Knowledge: quality_gate

## Core Concept
Quality gates are pre-publish validation policies from manufacturing stage-gates (Cooper 1990). A gate defines WHAT must pass at what threshold. It does NOT implement checks (validator) or define dimensions (rubric). Gate = policy; validator = enforcement.

## HARD Gates (Binary, Non-Negotiable)

Any HARD fail = artifact rejected. Protect structural integrity.

| Gate | Check | Why Universal |
|------|-------|--------------|
| H01 | Frontmatter parses | Broken structure = unusable |
| H02 | ID matches namespace regex | Search/routing/dedup depend on it |
| H03 | ID equals filename stem | Lookup-by-ID invariant |
| H04 | Kind matches expected literal | Type integrity for routing |
| H05 | Quality field is null | Producer must never self-score |
| H06 | All required fields present | Completeness baseline |

Kind-specific examples: system_prompt requires `## Identity`; skill requires `## Workflow Phases >= 2`; knowledge_card body 200-5120 bytes.

**Optimal count**: 8-10 per kind. <6 too permissive, >12 diminishing returns.

## SOFT Gates (Weighted, Scored)

Contribute to numeric score. Allow tradeoffs.

| Weight | Meaning | Examples |
|--------|---------|---------|
| 1.0 | High impact on utility | Density >= 0.80, no filler |
| 0.5 | Moderate, improves polish | Tags include kind, has URLs |

Never use weight < 0.5. Optimal: 10-12 simple kinds, 15-20 complex. Max 20.

Start equal weights. Switch to differentiated only when important dimensions get drowned out.

## Scoring

```
hard_pass = ALL hard gates pass (AND)
soft_score = sum(gate * weight) / sum(weights)
final = hard_pass ? soft_score : 0
```

| Tier | Threshold | Meaning |
|------|-----------|---------|
| GOLDEN | >= 9.5 | Exemplary, golden example |
| PUBLISH | >= 8.0 | Production-ready |
| REVIEW | >= 7.0 | Acceptable with notes |
| REJECT | < 7.0 | Rework or any HARD fail |

## Bypass Protocol
- Only for emergency (cosmetic SOFT fail blocking deploy, calibrating new kind)
- NEVER bypass H01 (broken YAML) or H05 (self-scoring)
- Requires: condition, approver, audit log, expiry
- Bypass = acknowledge + document + deadline, not "turn off"

## Designing New Gates
1. **HARD or SOFT?** "Broken or just lower quality?" Broken=HARD, Lower=SOFT
2. **Write as predicate**: `check(artifact) -> bool`. If too subjective, not a gate
3. **Assign weight** (SOFT): utility impact=1.0, polish=0.5
4. **Write one-line "why"**: if you can't, gate may be unnecessary

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Gates requiring human judgment | Rewrite as measurable predicate |
| Scoring without explicit weights | Declare every weight |
| Threshold without rationale | Document why 8.0 not 7.5 |
| HARD gate on style preference | Move to SOFT weight 0.5 |
| >12 HARD gates | Merge overlapping, demote weak to SOFT |
| No bypass mechanism | Add bypass with audit trail |
| Gate checks producer not artifact | Gates check the artifact |
