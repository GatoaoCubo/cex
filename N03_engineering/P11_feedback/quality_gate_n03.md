---
id: p11_qg_n03_primary
kind: quality_gate
pillar: P11
title: "Quality Gate -- N03 Primary Build Gate"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 8.9
tags: [quality-gate, N03, primary, 8F, governance, F7, hard-gates]
tldr: "Primary quality gate for all N03 artifact builds. 7 hard gates (all must pass) + 12LP soft checklist. Gates are checked at F7 GOVERN. Any hard gate failure triggers retry or reject -- no exceptions."
density_score: 0.92
updated: "2026-04-17"
---

# Quality Gate: N03 Primary Build Gate

## Purpose

The quality gate is the last defense before an artifact is saved and signaled.
Applied at F7 GOVERN for EVERY artifact. No artifact exits N03 without passing.

**Inventive Pride rule:** if it's not gate-worthy, it does not ship.

## Hard Gates (H01-H07) -- All Must Pass

Failure of ANY hard gate blocks the artifact. No retry credit used -- F6 must fix it.

| Gate | ID | Check | Error |
|------|----|-------|-------|
| H01 | YAML_VALID | Frontmatter parses as valid YAML | FrontmatterParseError |
| H02 | ID_PATTERN | `id` matches `^p[0-9]{2}_[a-z]{2}_[a-z0-9_]+$` | IDPatternError |
| H03 | KIND_KNOWN | `kind` in `.cex/kinds_meta.json` | UnknownKindError |
| H04 | NO_SELF_SCORE | `quality` field is exactly `null` | SelfScoringError |
| H05 | BODY_MIN | Body content >= 512 bytes | BodyTooShortError |
| H06 | NO_PLACEHOLDER | No TODO/FIXME/TBD/`{{...}}` in body | PlaceholderError |
| H07 | PILLAR_MATCH | Artifact `pillar` matches kind canonical pillar | PillarMismatchError |

## Soft Gates (12LP Checklist) -- Score Each

Each point scored 0-1. Soft gate minimum: 10/12 to pass.

| # | Point | Weight | Check |
|---|-------|--------|-------|
| LP01 | Intent mapped | 1x | kind+pillar resolved from intent before F6 |
| LP02 | Builder loaded | 1x | F2 BECOME confirmed >= 13 ISOs |
| LP03 | KC injected | 1x | kind's KC loaded in F3 INJECT |
| LP04 | Example present | 1x | At least 1 concrete example in body |
| LP05 | Density target | 1x | density_score >= 0.85 |
| LP06 | Sections named | 1x | At least 2 H2 sections with canonical names |
| LP07 | Cross-refs valid | 1x | All referenced file paths use canonical format |
| LP08 | ASCII clean | 1x | No non-ASCII in embedded code blocks |
| LP09 | Title length | 1x | Title 5-120 chars |
| LP10 | Tldr present | 1x | tldr field 20-300 chars |
| LP11 | Tags non-empty | 1x | >= 2 tags in frontmatter |
| LP12 | Version valid | 1x | Version matches `\d+\.\d+\.\d+` |

## Gate Execution Order

```
1. Parse frontmatter (prerequisite for all gates)
   -> fail: FrontmatterParseError -> REJECT immediately
2. H01-H07 in sequence
   -> any fail: gate_failures list + status=FAIL
3. If hard gates pass: run 12LP checklist
   -> score 0/1 per item
4. Compute soft gate score: sum(lp_scores) / 12
5. Determine final status:
   -> all H pass + soft >= 10/12: PASS
   -> all H pass + soft in [8, 9]: WARN
   -> any H fail OR soft < 8: FAIL
```

## Retry Protocol

| Status | Action |
|--------|--------|
| PASS | Proceed to F8 COLLABORATE |
| WARN | Log warning; proceed to F8 (artifact saved with warning flag) |
| FAIL (retry_count=0) | Return to F6 with failures injected; retry_count=1 |
| FAIL (retry_count=1) | Return to F6 with ALL failures + STRICT mode; retry_count=2 |
| FAIL (retry_count=2) | Write REJECT signal; do not save artifact; escalate to N07 |

## Strict Mode (Retry 2)

On second retry, F6 receives:
```
STRICT MODE ACTIVE -- Previous 2 attempts failed.
Failures: {list of failed gates + LP items}
Requirements:
- Address EVERY failure explicitly
- density_score target raised to 0.90
- All hard gates must pass on first parse
- If quality is accidentally not null, correct it
Do not add new sections -- fix the failures.
```

## Gate Report Format

```yaml
gate_report:
  nucleus: n03
  artifact_id: p06_is_build_contract
  kind: input_schema
  timestamp: 2026-04-17T14:30:00
  hard_gates:
    H01: pass
    H02: pass
    H03: pass
    H04: pass
    H05: pass
    H06: pass
    H07: pass
  soft_gates:
    lp01: 1  lp02: 1  lp03: 1  lp04: 1
    lp05: 1  lp06: 1  lp07: 1  lp08: 1
    lp09: 1  lp10: 1  lp11: 1  lp12: 1
  soft_score: 12/12
  status: pass
  retry_count: 0
```

## Integration with 5D Scoring Rubric

The quality gate is a BINARY prerequisite for the 5D scoring rubric.
Only artifacts that PASS the quality gate receive a 5D score.
The 5D score is then the input to the LLM judge (if L1+L2 >= 8.5).

```
F7 GOVERN flow:
  quality_gate.run() -> pass/fail
  if pass: scoring_rubric.score() -> D1..D5 -> composite
  if composite >= 8.5: llm_judge.evaluate() -> semantic score
  final_score = weighted_composite(l1, l2, l3)
```
