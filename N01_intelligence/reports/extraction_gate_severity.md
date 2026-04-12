---
id: extraction_gate_severity
kind: knowledge_card
pillar: P01_knowledge
title: "Extraction: Quality Gate Severity Levels from aiox-core"
version: 1.0
quality: null
tags: [extraction, quality_gate, severity, aiox, port]
created: 2026-04-12
author: n01_intelligence
domain: quality governance
source: SynkraAI/aiox-core
tldr: "aiox-core uses 4 severity levels (CRITICAL/HIGH/MEDIUM/LOW) with configurable block/warn/document behaviors per level. CEX quality_gate kind should extend from binary pass/fail to severity-aware."
---

# Extraction: Quality Gate Severity Levels (A3) from aiox-core

## 1. Severity Model

aiox-core defines 4 severity levels used consistently across 3 quality gate layers:

| Severity | Pipeline Impact | Block behavior |
|----------|----------------|---------------|
| **CRITICAL** | Immediate halt | Always blocks -- no override |
| **HIGH** | Escalates or blocks | Blocks if `blocking: true`, else needs review |
| **MEDIUM** | Needs revision | Does not block by default -- informational |
| **LOW** | Documentation only | Never blocks -- logged for trends |

### Configurable behavior per severity (quality-gate-config.yaml)

```yaml
coderabbit:
  blockOn:     [CRITICAL]      # these severities halt the pipeline
  warnOn:      [HIGH]          # these produce warnings but continue
  documentOn:  [MEDIUM]        # logged, no action
  ignoreOn:    [LOW]           # discarded
```

## 2. Three-Layer Quality Gate Architecture

### Layer 1: Pre-commit (layer1-precommit.js)

Fast, automated, fail-fast:

```yaml
layer1:
  enabled: true
  failFast: true           # stop on first failure
  checks:
    lint:
      enabled: true
      command: "npm run lint"
      failOn: "error"      # error | warning
      timeout: 60000
    test:
      enabled: true
      command: "npm test"
      timeout: 300000
      coverage:
        minimum: 80        # percent
    typecheck:
      enabled: true
      command: "npm run typecheck"
      timeout: 120000
```

Result structure:
```javascript
{
  check: "lint" | "test" | "typecheck",
  pass: boolean,
  exitCode: number,
  errors: number,
  warnings: number,
  coverage?: number,
  duration: number,
  message: string
}
```

### Layer 2: PR Automation (layer2-pr-automation.js)

AI-assisted review with severity parsing:

```javascript
// Severity parsing from CodeRabbit output
const patterns = [
  { regex: /\bCRITICAL\b[:\s]+([^\n]+)/gi, severity: 'CRITICAL' },
  { regex: /\bHIGH\b[:\s]+([^\n]+)/gi, severity: 'HIGH' },
  { regex: /\bMEDIUM\b[:\s]+([^\n]+)/gi, severity: 'MEDIUM' },
  { regex: /\bLOW\b[:\s]+([^\n]+)/gi, severity: 'LOW' },
];
```

Result includes severity breakdown:
```javascript
{
  check: "coderabbit",
  pass: boolean,           // !hasBlockingIssues
  issues: {
    critical: 0, high: 0, medium: 0, low: 0, total: 0
  },
  details: [{ severity, message }]
}
```

### Layer 3: Human Review (layer3-human-review.js)

Severity determination logic:
```javascript
determineSeverity(result) {
  if (result.check === 'test') return 'CRITICAL';
  if (result.check === 'lint') return 'HIGH';
  if (result.check === 'typecheck') return 'HIGH';
  if (result.issues?.critical > 0) return 'CRITICAL';
  if (result.issues?.high > 0) return 'HIGH';
  return 'MEDIUM';
}
```

## 3. Gate Evaluator (gate-evaluator.js)

Alternative gate for epic transitions -- uses a **verdict system**:

```javascript
const GateVerdict = {
  APPROVED: 'approved',            // all criteria met
  NEEDS_REVISION: 'needs_revision', // return to previous step
  BLOCKED: 'blocked'               // critical issue, halt
};
```

Verdict determination logic:

```javascript
_determineVerdict(result, gateConfig) {
  // Strict mode: any failure = blocked
  if (this.strictMode && result.issues.length > 0) return BLOCKED;

  // Critical issues always block
  if (result.issues.filter(i => i.severity === 'critical').length > 0) return BLOCKED;

  // Score below minimum
  if (gateConfig.minScore && result.score < gateConfig.minScore) {
    return gateConfig.blocking ? BLOCKED : NEEDS_REVISION;
  }

  // High severity issues
  if (result.issues.filter(i => i.severity === 'high').length > 0) {
    return gateConfig.blocking ? BLOCKED : NEEDS_REVISION;
  }

  // Allow minor issues if configured
  if (gateConfig.allowMinorIssues &&
      result.issues.every(i => i.severity === 'low' || i.severity === 'medium')) {
    return APPROVED;
  }

  // Any remaining issues
  if (result.issues.length > 0) return NEEDS_REVISION;

  return APPROVED;
}
```

## 4. CEX Integration Plan

### Current state

CEX `quality_gate` kind (P11) is **binary pass/fail with numeric score**:

```yaml
# P11_feedback/_schema.yaml
quality_gate:
  description: "Barreira de qualidade (pass/fail com score)"
  machine_format: yaml
  naming: p11_qg_{{gate}}.yaml
  constraints:
    max_bytes: 4096
  llm_function: GOVERN
```

CEX scoring is 3-layer (structural 30% + rubric 30% + semantic 40%) with
a hard floor at 8.0 and target at 9.0. But all failures are equal --
a missing frontmatter field and a completely wrong artifact get the same
"FAIL" treatment.

### Proposed: Severity-aware quality gates

#### 4.1 Extend quality_gate schema

Add to `P11_feedback/_schema.yaml`:

```yaml
quality_gate:
  constraints:
    max_bytes: 4096
    severity_values: [critical, high, medium, low]  # NEW
    verdict_values: [approved, needs_revision, blocked]  # NEW
  frontmatter_required:
    - id
    - kind
    - rules          # NEW: array of {check, severity, threshold}
    - verdict_mode   # NEW: strict | standard | lenient
```

#### 4.2 Rule structure with severity

```yaml
# Example: p11_qg_artifact_publish.yaml
id: qg_artifact_publish
kind: quality_gate
title: "Artifact publish gate"
verdict_mode: standard
rules:
  - check: frontmatter_complete
    severity: critical        # missing frontmatter = blocked
    threshold: 1.0
  - check: structural_score
    severity: high            # low structural = needs revision
    threshold: 0.7
  - check: density
    severity: medium          # low density = warning, not blocking
    threshold: 0.85
  - check: ascii_clean
    severity: critical        # non-ASCII in code = blocked
    threshold: 1.0
  - check: spelling
    severity: low             # typos = documented, not blocking
    threshold: 0.9
```

#### 4.3 Verdict determination for cex_score.py

```python
def determine_verdict(results: list[dict], mode: str) -> str:
    """Map severity-tagged check results to a verdict."""
    criticals = [r for r in results if r["severity"] == "critical" and not r["pass"]]
    highs = [r for r in results if r["severity"] == "high" and not r["pass"]]
    mediums = [r for r in results if r["severity"] == "medium" and not r["pass"]]

    if criticals:
        return "blocked"  # always

    if mode == "strict":
        if highs or mediums:
            return "blocked"

    if highs:
        return "needs_revision"

    if mode == "lenient":
        return "approved"  # mediums and lows don't matter

    if mediums:
        return "needs_revision"  # standard mode

    return "approved"
```

#### 4.4 Integration with existing scoring

Current flow:
```
cex_score.py -> structural (30%) + rubric (30%) + semantic (40%) -> score -> pass/fail at 8.0
```

Proposed flow:
```
cex_score.py -> structural + rubric + semantic -> score
            -> severity checks -> tagged results
            -> determine_verdict(results, mode) -> approved | needs_revision | blocked
            -> if blocked: reject
            -> if needs_revision: warn + allow publish with flag
            -> if approved: publish clean
```

This means artifacts can be published with warnings (e.g., "density 0.82, below
0.85 target, but no critical issues"). Currently everything below 8.0 is rejected
equally.

### Files to create/modify

| File | Action | Lines est. |
|------|--------|-----------|
| `P11_feedback/_schema.yaml` | MODIFY -- add severity_values, verdict_values, new frontmatter | ~15 |
| `_tools/cex_score.py` | MODIFY -- add severity tagging + verdict determination | ~60 |
| `_tools/cex_hooks.py` | MODIFY -- use verdict instead of binary pass/fail | ~20 |
| `.cex/kinds_meta.json` | MODIFY -- update quality_gate entry | ~5 |
| `archetypes/builders/quality-gate-builder/` | MODIFY -- update ISOs for severity | ~30 |
| `P01_knowledge/library/kind/kc_quality_gate.md` | MODIFY -- document severity model | ~40 |

### Estimated effort

- **Complexity**: Low-Medium (scoring logic change + schema extension)
- **Lines of code**: ~60 new in cex_score.py + ~110 modified across 6 files
- **Dependencies**: None
- **Risk**: Medium -- changes scoring behavior (but verdict is additive, score unchanged)

## 5. Comparative Analysis

| Dimension | aiox-core gates | CEX quality_gate (current) | Proposed CEX severity gates |
|-----------|----------------|---------------------------|---------------------------|
| Severity levels | 4 (CRITICAL/HIGH/MEDIUM/LOW) | None (binary pass/fail) | 4 (critical/high/medium/low) |
| Verdict types | 3 (APPROVED/NEEDS_REVISION/BLOCKED) | 2 (pass/fail) | 3 (approved/needs_revision/blocked) |
| Verdict modes | strict + configurable | Fixed 8.0 threshold | strict/standard/lenient |
| Per-rule severity | Yes (blockOn/warnOn/documentOn) | No | Yes (per rule in YAML) |
| Score integration | Separate from severity | Score IS the gate | Score + severity = verdict |
| Layer architecture | 3 layers (precommit/PR/human) | 3 layers (structural/rubric/semantic) | Keep CEX's 3 layers + add severity |
| Persistence | `.aiox/qa-status.json` | Frontmatter `quality` field | Frontmatter + verdict field |

### What NOT to port

1. **3-layer gate architecture** -- CEX's 3-layer scoring (structural/rubric/semantic) is different from aiox's (precommit/PR/human) -- keep CEX's approach
2. **CodeRabbit integration** -- external tool dependency, not needed
3. **Human review orchestration** -- CEX uses peer review via cex_score.py, not PR-based
4. **Notification system** -- CEX uses signals, not notifications
5. **24h sign-off expiry** -- CEX's quality is permanent once scored

## 6. Key Code References in aiox-core

| File (relative to aiox-core/) | What it contains |
|-------------------------------|-----------------|
| `core/quality-gates/quality-gate-manager.js` | Main orchestrator + verdict logic |
| `core/quality-gates/quality-gate-config.yaml` | blockOn/warnOn/documentOn config |
| `core/quality-gates/layer1-precommit.js` | Lint/test/typecheck checks |
| `core/quality-gates/layer2-pr-automation.js` | Severity parsing from AI review output |
| `core/quality-gates/layer3-human-review.js` | Severity determination per check type |
| `core/quality-gates/base-layer.js` | Abstract base class for gate layers |
| `core/orchestration/gate-evaluator.js` | Verdict determination (APPROVED/NEEDS_REVISION/BLOCKED) |
| `quality/schemas/quality-metrics.schema.json` | Severity breakdown in metrics |
