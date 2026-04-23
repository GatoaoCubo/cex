---
id: extraction_gate_severity
kind: knowledge_card
pillar: P01_knowledge
title: "Extraction: Quality Gate Severity Levels from aiox-core"
version: 1.0
quality: 8.9
tags: [extraction, quality_gate, severity, aiox, port, schema_extension]
created: 2026-04-13
author: n01_intelligence
domain: quality enforcement
source: SynkraAI/aiox-core
tldr: "aiox-core uses 4-level severity (CRITICAL/HIGH/MEDIUM/LOW) across a 3-layer quality pipeline (pre-commit/PR-automation/human-review). CEX quality_gate kind is binary pass/fail -- add severity field to enable publish-with-warnings, retry budgets, and graduated enforcement."
related:
  - p06_security_validation_schema
  - bld_knowledge_card_guardrail
  - p10_lr_guardrail_builder
  - p11_qg_guardrail
  - p11_qg_validator
  - p11_gr_{{SCOPE_SLUG}}
  - port_plan_external_repos
  - bld_instruction_guardrail
  - bld_examples_guardrail
  - p03_sp_guardrail_builder
---

# Extraction: Quality Gate Severity Levels (A3) from aiox-core

## 1. aiox-core Gate Architecture

aiox-core uses a **3-layer quality pipeline** with a severity taxonomy per check.
Source: `.aiox-core/core/quality-gates/`

### Pipeline layers

| Layer | File | What it runs | Fail behavior |
|-------|------|-------------|---------------|
| L1 Pre-commit | `layer1-precommit.js` | lint, test, typecheck | `failFast: true` -- stops on first error |
| L2 PR Automation | `layer2-pr-automation.js` | CodeRabbit, Quinn AI review | depends on severity |
| L3 Human Review | `layer3-human-review.js` | checklist sign-off | requires human approval |

### Severity definitions (quality-gate-config.yaml:36-54)

```yaml
# Layer 2 severity configuration
layer2:
  coderabbit:
    blockOn:   [CRITICAL]   # hard block -- pipeline stops
    warnOn:    [HIGH]        # flag in report, does NOT block
    documentOn: [MEDIUM]    # add to documentation/report
    ignoreOn:  [LOW]         # silently skip

  quinn:
    severity:
      block: ["CRITICAL"]
      warn:  ["HIGH", "MEDIUM"]
```

### Severity semantics

| Level | Code | Behavior | CEX equivalent |
|-------|------|----------|----------------|
| CRITICAL | `CRIT` | Blocks pipeline, cannot publish | score < 8.0 (hard reject) |
| HIGH | `HIGH` | Warns in report, passes | score 8.0-8.5 (publish + flag) |
| MEDIUM | `MED` | Documents in report, passes | score 8.5-9.0 (publish + note) |
| LOW | `LOW` | Silently ignored | score >= 9.0 (clean pass) |

## 2. Layer 1 Pre-commit Details

From `layer1-precommit.js` (failFast mode):

```javascript
// Sequential with early exit
const lintResult = await this.runLint(context);
if (!lintResult.pass && this.failFast) {
  return this.getSummary();  // stop -- don't run tests
}

const testResult = await this.runTests(context);
if (!testResult.pass && this.failFast) {
  return this.getSummary();  // stop -- don't run typecheck
}

// coverage threshold enforced per config:
coverage:
  enabled: true
  minimum: 80   // percent
```

**Key**: L1 is binary pass/fail with NO severity levels -- it's CRITICAL-only behavior.
Severity kicks in at L2.

## 3. Layer 2 Severity Flow

```
CodeRabbit scan
  |
  +-- CRITICAL issue found -> BLOCK (return failure immediately)
  +-- HIGH issue found     -> WARN (add to report, continue)
  +-- MEDIUM issue found   -> DOCUMENT (log, continue)
  +-- LOW issue found      -> IGNORE (skip)
  |
Quinn AI review (runs in parallel)
  |
  +-- CRITICAL -> block
  +-- HIGH     -> warn
  +-- MEDIUM   -> warn (quinn is stricter than coderabbit)
```

Source: `quality-gate-config.yaml:37-54`

## 4. Layer 3 Human Review

L3 requires **manual sign-off**:
- `requireSignoff: true`
- Default reviewer: `@architect`
- Sign-off expires after 24h (`expiry: 86400000`)
- Checklist: min 5 items from `strategic-review-checklist`

This layer has no automated severity — it's fully human-gated.

## 5. Base Layer Patterns (base-layer.js)

Common infrastructure for all 3 layers:

```javascript
class BaseLayer {
  reset()        // clear results
  startTimer()   // track duration
  stopTimer()    // record elapsed
  addResult(r)   // push check result
  getSummary()   // aggregate pass/fail + duration
  formatDuration(ms) // "2.3s" etc.
}
```

Layer results carry: `{ check, pass, skipped, message, duration }`

## 6. CEX Current State

CEX quality gates are **binary**: `cex_score.py` returns a float 0-10.
The enforcement is:
- `< 8.0`: REJECT (F7 GOVERN retries, max 2x)
- `>= 8.0`: ACCEPT

There is no warn-level or graduated severity. This causes two problems:
1. An artifact scoring 7.9 is indistinguishable from one scoring 5.0
2. No way to "publish with known issues" for time-sensitive releases

## 7. CEX Integration Plan: severity field for quality_gate kind

### Schema extension

Add to `P07_evals/_schema.yaml` under `quality_gate`:

```yaml
quality_gate:
  # ... existing fields ...
  rules:
    type: array
    items:
      type: object
      required: [id, check]
      properties:
        id:      { type: string }
        check:   { type: string }
        weight:  { type: number, default: 1.0 }
        severity:                        # NEW
          type: string
          enum: [error, warn, info]
          default: error
          description: |
            error: blocks publish (CRITICAL equivalent)
            warn:  allows publish, adds annotation to frontmatter
            info:  logs only, no annotation
```

### Impact on cex_score.py

```python
# Current behavior
def evaluate_gates(artifact, gates):
    for gate in gates:
        if not gate.passes(artifact):
            return FAIL

# Proposed behavior
def evaluate_gates(artifact, gates):
    errors = []
    warnings = []
    for gate in gates:
        if not gate.passes(artifact):
            severity = gate.get("severity", "error")
            if severity == "error":
                errors.append(gate.id)
            elif severity == "warn":
                warnings.append(gate.id)
            # info: log only

    if errors:
        return GateResult(blocked=True, errors=errors, warnings=warnings)
    return GateResult(blocked=False, errors=[], warnings=warnings)
```

### Impact on quality_gate artifact frontmatter

```yaml
# existing gate artifact
id: qg_density
rule: body must have density >= 0.85
severity: error   # NEW -- hard block

id: qg_examples
rule: at least one usage example
severity: warn    # NEW -- allowed to publish, adds warning annotation
```

### Annotation in published artifact

When a `warn` gate fails, the artifact frontmatter gets:

```yaml
quality_warnings:
  - gate: qg_examples
    message: "No usage example found -- consider adding one"
    timestamp: 2026-04-13
```

### Files to create/modify

| File | Action | Lines est. |
|------|--------|-----------|
| `P07_evals/_schema.yaml` | MODIFY -- add severity field to gate rule schema | ~15 |
| `_tools/cex_score.py` | MODIFY -- GateResult with blocked/warnings separation | ~50 |
| `P01_knowledge/library/kind/kc_quality_gate.md` | MODIFY -- document severity levels | ~20 |
| `archetypes/builders/quality-gate-builder/bld_instruction_quality_gate.md` | MODIFY -- add severity guidance | ~15 |

### Estimated effort

- **Complexity**: Low (additive schema field + score.py logic change)
- **Lines of code**: ~50 new + ~50 modified
- **Dependencies**: None
- **Risk**: Low -- additive, existing gates default to `error` (backward compatible)

## 8. Comparative Analysis

| Dimension | aiox-core (3 layers) | CEX (current) | Proposed CEX |
|-----------|---------------------|---------------|--------------|
| Severity levels | 4 (CRIT/HIGH/MED/LOW) | 2 (pass/fail) | 3 (error/warn/info) |
| Layer structure | Pre-commit/PR/Human | Single scoring pass | Single pass + severity |
| Human review gate | Yes (L3 sign-off) | No | Out of scope (no PR flow) |
| Per-check severity | Yes (per rule) | No | Yes (per gate rule) |
| Publish with warnings | Yes (HIGH/MED don't block) | No | Yes (warn gates) |
| Retry on failure | No (L1 failFast, L2 continues) | Yes (F7, max 2x) | Yes (on error only) |
| Coverage threshold | Yes (80% min, L1) | No | Out of scope (no test suite) |

### What NOT to port from aiox-core

1. **L1 pre-commit** -- CEX has no test runner; build artifacts are the unit
2. **L3 human review** -- no PR workflow in CEX's terminal-first pipeline
3. **CodeRabbit/Quinn integrations** -- CI/CD specific, irrelevant for artifact builds
4. **Coverage threshold** -- no code coverage concept for KCs and prompts
5. **24h sign-off expiry** -- no async review process in CEX

## 9. Key Code References in aiox-core

| File (relative to aiox-core/) | What it contains |
|-------------------------------|-----------------|
| `.aiox-core/core/quality-gates/quality-gate-config.yaml` | Severity config (blockOn/warnOn/documentOn/ignoreOn) |
| `.aiox-core/core/quality-gates/quality-gate-manager.js` | 3-layer orchestrator |
| `.aiox-core/core/quality-gates/layer1-precommit.js` | Pre-commit: lint, test, typecheck |
| `.aiox-core/core/quality-gates/layer2-pr-automation.js` | PR review: CodeRabbit, Quinn |
| `.aiox-core/core/quality-gates/layer3-human-review.js` | Human sign-off: checklist, expiry |
| `.aiox-core/core/quality-gates/base-layer.js` | Abstract base: timer, results, summary |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_security_validation_schema]] | related | 0.32 |
| [[bld_knowledge_card_guardrail]] | sibling | 0.29 |
| [[p10_lr_guardrail_builder]] | related | 0.28 |
| [[p11_qg_guardrail]] | related | 0.25 |
| [[p11_qg_validator]] | related | 0.25 |
| [[p11_gr_{{SCOPE_SLUG}}]] | related | 0.25 |
| [[port_plan_external_repos]] | related | 0.24 |
| [[bld_instruction_guardrail]] | related | 0.23 |
| [[bld_examples_guardrail]] | related | 0.23 |
| [[p03_sp_guardrail_builder]] | related | 0.23 |
