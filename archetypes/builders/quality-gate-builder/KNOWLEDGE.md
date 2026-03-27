---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for designing quality gates that reliably filter artifacts
sources: [Cooper 1990, SonarQube, DORA, 5 production quality gate files]
---

# Domain Knowledge: quality_gate

## Origin and Purpose

Quality gates originate from manufacturing stage-gate processes (Cooper 1990). In software: CI/CD gates (lint, test, coverage thresholds). In AI artifact systems: pre-publish validation that decides whether an artifact meets the bar.

A quality gate defines WHAT must pass and at what threshold. It does NOT implement the check (that's a validator). It does NOT define evaluation dimensions (that's a scoring rubric). The gate is the policy; the validator is the enforcement.

## The HARD/SOFT Pattern

The proven architecture splits gates into two tiers:

### HARD Gates (Binary, Non-Negotiable)

HARD gates are pass/fail checks. If ANY single HARD gate fails, the artifact is rejected regardless of other scores. They protect structural integrity — the artifact can't function if these fail.

**Universal HARD gates** that appear across all artifact kinds:

| Gate | Check | Why It's Universal |
|------|-------|--------------------|
| H01 | Frontmatter parses without error | Broken structure = unusable artifact |
| H02 | ID matches namespace pattern (regex) | Search, routing, dedup depend on ID format |
| H03 | ID equals filename stem | Lookup-by-ID requires this invariant |
| H04 | Kind field matches expected literal | Type integrity for routing and validation |
| H05 | Quality field is null | Producer must never self-score |
| H06 | All required fields present and non-empty | Completeness baseline |

**Kind-specific HARD gates** are added based on what's structurally essential:

| Example | Gate | Rationale |
|---------|------|-----------|
| system_prompt | Body has ## Identity section | Identity IS the prompt |
| system_prompt | Body has ## Rules with numbered items | Rules are the behavioral contract |
| agent | llm_function == "BECOME" | Agent is identity, not callable function |
| agent | Satellite field is set | Every agent belongs to an execution context |
| skill | Body has ## Workflow Phases with >= 2 subsections | Phases ARE the skill |
| action_prompt | edge_cases has >= 2 entries | Robustness requirement |
| knowledge_card | Body size 200-5120 bytes | Too small = empty; too large = unfocused |
| knowledge_card | No internal paths in body | Portability across environments |

### Optimal HARD Gate Count

Production data shows **8-10 HARD gates per artifact kind** is the sweet spot:

- < 6: too permissive, lets broken artifacts through
- 8-10: catches structural failures without being oppressive
- > 12: diminishing returns, gates start overlapping or become impossible to satisfy simultaneously

### SOFT Gates (Weighted, Scored)

SOFT gates contribute to a numeric quality score. Each gate has a weight reflecting its importance. Passing all SOFT gates isn't required — they allow tradeoffs.

**Weight assignment pattern** from production:

| Weight | Meaning | Examples |
|--------|---------|---------|
| 1.0 | High impact — directly affects artifact utility | Density >= 0.80, no filler phrases, field counts match body |
| 0.5 | Moderate impact — improves quality but not critical | Tags include kind name, has external URLs, format extras |

**Never use weights below 0.5** — if a check matters so little, it shouldn't be a gate at all.

### Optimal SOFT Gate Count

| Kind | SOFT gates | Notes |
|------|-----------|-------|
| Simple artifacts | 10-12 | Sufficient for format + content checks |
| Complex artifacts | 15-20 | More dimensions to validate |
| Maximum observed | 20 | knowledge_card (most mature, most validated) |

Beyond 20 SOFT gates, individual gate weights become too small to meaningfully affect the score.

## Scoring Formula

The universal formula:

```
hard_pass = ALL hard gates pass (boolean AND)
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0
```

If any HARD gate fails, the final score is 0 regardless of SOFT performance. This makes HARD gates truly non-negotiable.

### Score-to-Tier Mapping

| Tier | Threshold | Meaning |
|------|-----------|---------|
| GOLDEN | >= 9.5 | Exemplary — all HARD + 95% SOFT |
| PUBLISH | >= 8.0 | Production-ready — all HARD + 80% SOFT |
| REVIEW | >= 7.0 | Acceptable with notes — all HARD + 70% SOFT |
| REJECT | < 7.0 | Needs rework, or any HARD fail |

These thresholds are not arbitrary. They reflect production experience:
- 9.5+ artifacts serve as golden examples for other builders
- 8.0+ artifacts function correctly in all standard use cases
- 7.0-7.9 artifacts work but have rough edges (missing metadata, thin sections)
- Below 7.0, the artifact actively misleads or breaks downstream processes

## Weight Distribution Strategies

Two proven strategies:

**Equal weights** (simpler, used by knowledge_card):
```
All SOFT gates: weight 1.0
Score = passed_count / total_count * 10
```
Pro: Simple to reason about. Each gate contributes equally.
Con: Can't express that density matters more than having external URLs.

**Differentiated weights** (nuanced, used by system_prompt/agent/skill):
```
High-impact gates: weight 1.0
Moderate gates: weight 0.5
Score = sum(passed * weight) / sum(all_weights) * 10
```
Pro: Reflects real importance differences.
Con: Weight tuning requires iteration; initial guesses are often wrong.

**Rule of thumb**: Start with equal weights. Switch to differentiated only when you observe that artifacts pass overall but fail on the dimensions that matter most.

## Bypass Protocol

Gates must have a bypass mechanism for emergency situations:

```
## Bypass
- Condition: [when bypass is acceptable]
- Approver: [who can authorize]
- Audit: [what gets logged]
- Expiry: [how long bypass lasts]
```

Bypass is NOT "turn off the gate." It's "acknowledge the failure, document why, and set a deadline to fix." Every bypass must be logged and time-limited.

**When bypass is appropriate**:
- Blocking a critical deployment for a cosmetic SOFT gate failure
- New artifact kind where gates are still being calibrated
- Temporary regression while migrating to new schema version

**When bypass is NEVER appropriate**:
- HARD gate H01 (broken YAML — artifact is literally unusable)
- HARD gate H05 (quality self-scoring — corrupts evaluation pipeline)
- Any gate during golden example production (examples must be perfect)

## Designing New Gates

### Step 1: Classify as HARD or SOFT

Ask: "If this check fails, is the artifact fundamentally broken or just lower quality?"
- Broken → HARD
- Lower quality → SOFT

### Step 2: Write the Check as a Predicate

Every gate must be expressible as a boolean function:
```
check(artifact) -> true | false
```

If you can't write this function, the gate is too subjective. "Is the content good?" is not a gate. "Body has >= 4 sections" is.

### Step 3: Assign Weight (SOFT only)

Does this gate catch failures that impact artifact utility? → weight 1.0
Does this gate catch failures that impact artifact polish? → weight 0.5

### Step 4: Write the "Why"

Every gate needs a one-line justification. "Namespace compliance" or "Brain search relies on this." If you can't explain why in one line, the gate may be unnecessary.

## Pre-Production Checklist Pattern

Every quality gate file should end with a pre-production checklist — steps to verify BEFORE running the gates:

```
## Pre-Production Checklist
- [ ] Target artifact kind identified
- [ ] No existing gate for this kind (dedup check)
- [ ] HARD gates cover structural integrity (6-10 gates)
- [ ] SOFT gates cover content quality (10-20 gates)
- [ ] Weights sum correctly (verify formula)
- [ ] Bypass conditions documented
```

This prevents running gates on artifacts that were never meant to pass (wrong kind, wrong schema version, etc.).

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Gates that require human judgment | Can't automate, bottleneck | Rewrite as measurable predicate |
| Scoring without explicit weights | Hidden preferences, inconsistent results | Declare every weight |
| Threshold without rationale | Arbitrary cutoff, no trust | Document why 8.0 (not 7.5 or 8.5) |
| HARD gate on style preference | Rejects valid artifacts for taste | Move to SOFT with weight 0.5 |
| > 12 HARD gates | Gate overlap, impossible to satisfy all | Merge overlapping gates, demote weak ones to SOFT |
| Equal weights when dimensions differ | Important checks have same power as trivial ones | Use differentiated weights |
| No bypass mechanism | Emergency deploys get blocked | Add bypass with audit trail |
| Gate checks artifact producer | "Author must be senior" — not a quality check | Gates check the artifact, not the person |
| Circular dependency | Gate A requires gate B's output which requires gate A | Topologically sort gates, break cycles |

## References

- Cooper, R. G. (1990). Stage-gate systems: A new tool for managing new products. Business Horizons.
- SonarQube Quality Gates: https://docs.sonarqube.org/latest/user-guide/quality-gates/
- DORA Metrics: https://dora.dev/
- Google Test Automation Pyramid: https://testing.googleblog.com/
