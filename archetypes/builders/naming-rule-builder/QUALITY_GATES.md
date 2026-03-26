---
pillar: P11
llm_function: GOVERN
kind: quality_gates
domain: naming_rule
version: 1.0.0
---

# Quality Gates — Naming Rule Builder

## HARD Gates (H01–H08) — Blocking

All HARD gates must pass. Any single failure = artifact REJECTED.

| Gate | ID | Check | Failure Action |
|------|----|-------|---------------|
| ID pattern | H01 | `id` matches `^p05_nr_[a-z][a-z0-9_]+$` | REJECT — fix id |
| Kind fixed | H02 | `kind` == `naming_rule` (exact string) | REJECT — fix kind |
| Pillar fixed | H03 | `pillar` == `P05` (exact string) | REJECT — fix pillar |
| Semver | H04 | `version` matches `^\d+\.\d+\.\d+$` | REJECT — fix version |
| Scope present | H05 | `scope` is non-empty string, <= 120 chars | REJECT — add scope |
| Regex pattern | H06 | `pattern` is valid regex; all valid examples match; all invalid examples fail | REJECT — fix pattern |
| Enum values | H07 | `case_style` in allowed enum; `collision_strategy` in allowed enum | REJECT — fix enums |
| Required sections | H08 | Body contains all 4 sections: Scope, Pattern Definition, Examples, Collision Resolution | REJECT — add sections |

## SOFT Gates (S01–S10) — Scoring

Soft gates contribute to quality score. Failing soft gates reduces score but does not block.

| Gate | ID | Check | Score Impact |
|------|----|-------|-------------|
| Quality null | S01 | `quality: null` at creation | -1.0 if self-assigned |
| Density REC | S02 | `density_score: REC` at authoring | -0.5 if computed value set manually |
| Min valid examples | S03 | >= 3 valid examples with reasons | -0.5 per missing example |
| Min invalid examples | S04 | >= 2 invalid examples with violation reasons | -0.5 per missing example |
| Keywords count | S05 | 5–8 keywords present | -0.3 if out of range |
| Tags count | S06 | >= 3 tags, kebab-case | -0.3 if < 3 or wrong case |
| File size | S07 | Artifact <= 4096 bytes | -1.0 if exceeds limit |
| Segments table | S08 | Pattern Definition includes segments table | -0.5 if missing |
| tldr quality | S09 | tldr is one sentence, references scope and pattern | -0.3 if vague |
| Sibling consistency | S10 | Separator and case_style consistent with sibling naming rules in same pillar | -0.5 if inconsistent without documented rationale |

## Scoring Formula

```
base_score = 10.0
score = base_score - sum(soft_gate_penalties)
final = max(0.0, score)
```

| Score Range | Tier | Action |
|-------------|------|--------|
| >= 9.5 | Golden | Pool as Golden artifact |
| >= 8.0 | Skilled | Pool + remember() |
| >= 7.0 | Learning | Experimental pool |
| < 7.0 | Rejected | Rework required |

## Automation

Run gates via schema validator (when available):

```
Grep: pattern="^id: p05_nr_" path={artifact_path}
Grep: pattern="^kind: naming_rule" path={artifact_path}
Grep: pattern="^pillar: P05" path={artifact_path}
Grep: pattern="## Scope" path={artifact_path}
Grep: pattern="## Pattern Definition" path={artifact_path}
Grep: pattern="## Examples" path={artifact_path}
Grep: pattern="## Collision Resolution" path={artifact_path}
```

## Pre-Production Checklist

Before submitting artifact to pool:

- [ ] H01: ID matches regex pattern
- [ ] H02: kind = `naming_rule`
- [ ] H03: pillar = `P05`
- [ ] H04: version is semver
- [ ] H05: scope is clear and bounded
- [ ] H06: pattern is valid regex with tested examples
- [ ] H07: case_style and collision_strategy use valid enum values
- [ ] H08: all 4 body sections present
- [ ] S01: quality is null
- [ ] S02: density_score is REC
- [ ] S07: file size <= 4096 bytes
- [ ] OUTPUT_TEMPLATE drift check passed (all {{vars}} mapped to schema fields)
