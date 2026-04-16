---
id: sch_validator_n01
kind: validator
pillar: P06
nucleus: n01
title: Comparative Evidence Validator
version: 1.0
quality: null
tags: [validator, quality_gate, evidence, research]
---

<!-- 8F: F1 constrain=P06/validator F2 become=validator-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_validator+P06_schema+validator template F4 reason=pre-commit gate for comparative evidence discipline F5 call=apply_patch+cex_compile F6 produce=4503 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/schemas/sch_validator_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Rule name | `comparative_evidence_required` |
| Execution stage | pre-commit and quality gate |
| Target scope | N01 markdown artifacts that make research or benchmark claims |
| Lens | Analytical Envy blocks artifacts that describe a topic without naming a comparison or proof path |
| Pass model | binary pass or fail with limited bypass |

## Schema

| Condition ID | Target | Field or Pattern | Operator | Value | On Fail |
|-------------|--------|------------------|----------|-------|---------|
| `c01` | body | `## Purpose` | contains | section header | block |
| `c02` | body | `## Rationale` | contains | section header | block |
| `c03` | body | `## Example` | contains | section header | block |
| `c04` | body | markdown table count | `>=` | `4` | block |
| `c05` | body | `comparison` or `peer` or `benchmark` | contains_any | keyword set | block |
| `c06` | body | `evidence` or `source` | contains_any | keyword set | block |
| `c07` | frontmatter | `quality` | equals | `null` | block |
| `c08` | filename | nucleus suffix | ends_with | `_n01.md` | block |
| `c09` | body | line count | `>=` | `80` | warn |
| `c10` | body | non-ascii identifier pattern | not_contains | accented identifier tokens | block |

## Rule Logic

| Branch | Outcome |
|-------|---------|
| any block condition fails | reject save or publish |
| only warn condition fails | allow local draft, deny final publish |
| all conditions pass | artifact is eligible for compile and review |
| bypass requested | requires N07 approval plus logged rationale |

## Error Handling

| Severity | Message | Manual Remediation |
|---------|---------|--------------------|
| error | "Artifact lacks comparative evidence structure." | add missing sections and tables |
| error | "Artifact never names a comparison axis or peer." | declare benchmark subject and rival |
| error | "Artifact does not expose evidence language." | add evidence or source tables |
| error | "quality must remain null." | remove self-score |
| warning | "Artifact is under 80 lines and may be too thin." | expand structured content, not filler |

## Bypass Policy

| Field | Value |
|------|-------|
| allowed when | emergency unblock for internal draft only |
| approver | `n07_orchestrator` |
| audit | true |
| expiration | same day as approval |
| forbidden cases | publish-ready outputs and external-facing claims |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| Require comparison keywords | N01 must compare, not merely summarize | Envy is directional and competitive |
| Require evidence language | Comparative claims without proof degrade trust | Rivalry must be earned with sources |
| Keep sections explicit | Dense structure helps later validators and humans | Strong analysis should be inspectable |
| Use one warning only | Thin drafts may exist briefly | Quality pressure stays high without freezing work |
| Filename and quality checks | Governance consistency supports automation | Formal rigor amplifies analytical rigor |

## Example

```yaml
validator_result:
  target_file: N01_intelligence/schemas/sch_input_schema_n01.md
  status: pass
  matched_conditions: [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10]
  note: "Artifact names comparison pressure, evidence thresholds, and retains quality null."
```

## Example Failure

| Missing Signal | Validator Response |
|---------------|--------------------|
| no benchmark or peer language | fail `c05` |
| no evidence or source language | fail `c06` |
| three tables only | fail `c04` |
| self-scored quality | fail `c07` |

## Properties

| Property | Value |
|----------|-------|
| Kind | `validator` |
| Pillar | `P06` |
| Nucleus | `n01` |
| Pre Commit | `true` |
| Auto Fix | `false` |
| Block Conditions | `9` |
| Warning Conditions | `1` |
| Quality Field | `null` |
