---
id: p11_qg_curation_nudge
kind: quality_gate
pillar: P11
llm_function: GOVERN
purpose: F7 GOVERN quality gates for curation_nudge artifacts
quality: 8.5
title: "Quality Gate: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [quality_gate, curation_nudge, builder, p11, memory, f7]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F7 GOVERN quality gates for curation_nudge artifacts"
density_score: 0.91
target_kind: curation_nudge
delivery_threshold: 0.85
bypass_policy: owner
related:
  - p11_qg_creation_artifacts
  - p03_sp_quality_gate_builder
  - p03_ins_quality_gate
  - bld_knowledge_card_quality_gate
  - bld_examples_memory_summary
  - bld_collaboration_memory_type
  - p11_qg_engineering_artifacts
  - bld_memory_quality_gate
  - bld_examples_memory_scope
  - p11_qg_marketing_artifacts
---

## Quality Gate

## HARD Gates (all must pass)

| ID | Criterion | Failure Action |
|----|-----------|---------------|
| H01 | `kind == "curation_nudge"` | block |
| H02 | `trigger.threshold >= 5` (positive integer, minimum 5) | block |
| H03 | `trigger.type` in `{turn_count, density_threshold, tool_call_count, user_correction}` | block |
| H04 | `target_memory.destination` in `{MEMORY.md, entity_memory, knowledge_card}` | block |
| H05 | `prompt_template` contains `{{observation}}` | block |
| H06 | `quality == null` (never self-score) | block |

## SOFT Gates (weighted, sum = 1.0)

| ID | Criterion | Weight | Scoring Method |
|----|-----------|--------|---------------|
| S01 | Boundaries section present with all 4 NOT-items | 0.25 | binary |
| S02 | `cadence.min_interval_turns >= 5` AND `cadence.max_per_session <= 5` | 0.25 | binary |
| S03 | Usage in agent session code block present in body | 0.25 | binary |
| S04 | `tags` includes `hermes_origin` | 0.25 | binary |

## Scoring Formula

```
aggregate_score = S01*0.25 + S02*0.25 + S03*0.25 + S04*0.25
PASS: all H gates pass AND aggregate_score >= 0.85
FAIL: any H gate fails OR aggregate_score < 0.85
```

## Actions

| Outcome | Consequence |
|---------|-------------|
| PASS | Artifact proceeds to F8 COLLABORATE (compile + commit + signal) |
| H-FAIL | Artifact returned with specific HARD gate failure detail; fix and retry |
| S-FAIL | Artifact returned with soft gate breakdown; improve and retry (max 2 retries) |

## Bypass Policy

- Who may override: `owner` (N03 builder or N04 knowledge nucleus)
- Conditions: only H06 (quality: null) may be bypassed in peer-review mode (peer sets actual score)
- All other HARD gates: no bypass permitted
- Audit: log bypass with actor, timestamp, and justification

## Examples

## Golden Example 1: Turn Count Nudge (HERMES Default)

```yaml
---
id: cn_turn_count
kind: curation_nudge
pillar: P11
title: "Curation Nudge: Every 10 Turns"
trigger:
  type: turn_count
  threshold: 10
cadence:
  min_interval_turns: 5
  max_per_session: 3
prompt_template: "Notei {{observation}}. Devo persistir em MEMORY.md?"
target_memory:
  destination: MEMORY.md
  auto_write_if_confirmed: true
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory]
upstream_source: "NousResearch/hermes-agent"
---

## Nudge: Every 10 Turns

### Trigger Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Trigger type | turn_count | Fire every N conversation turns |
| Threshold | 10 | Check after 10 turns |
| Min interval | 5 turns | Prevents nudge spam |
| Max per session | 3 | Hard cap per session |

### Prompt Template

    Notei [OBSERVATION]. Devo persistir em MEMORY.md?

### Target Memory

| Field | Value | Description |
|-------|-------|-------------|
| Destination | MEMORY.md | Write confirmed knowledge here |
| Auto-write | true | Persist immediately on confirmation |

### Boundaries

- NOT `guardrail` (P11): guardrails BLOCK actions; nudges ASK
- NOT `quality_gate` (P11): quality_gate is pass/fail; nudge is informational
- NOT `notifier` (P04): notifiers broadcast externally; nudge is in-session
- NOT `memory_summary` (P10): summary compresses; nudge triggers persistence decision

### Usage in agent session

```yaml
curation_nudge:
  nudge_ref: cn_turn_count
  fire_every: 10 turns
  on_confirm: write_to MEMORY.md
  on_reject: continue_session
```
```

**Why it works:** threshold=10 is well above the minimum (5), cadence prevents spam,
prompt_template contains the observation placeholder (H05), all 4 boundary NOT-items present.

## Golden Example 2: User Correction Nudge

```yaml
---
id: cn_user_correction
kind: curation_nudge
pillar: P11
title: "Curation Nudge: User Correction"
trigger:
  type: user_correction
  threshold: 1
cadence:
  min_interval_turns: 3
  max_per_session: 5
prompt_template: "O usuario corrigiu: {{observation}}. Persistir preferencia em MEMORY.md?"
target_memory:
  destination: MEMORY.md
  auto_write_if_confirmed: true
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory, correction]
---
```
**Why it works:** `user_correction` trigger uses threshold=1 (correct -- fire on every correction).
min_interval_turns=3 prevents rapid-fire corrections from flooding MEMORY.md.
prompt_template includes the observation placeholder required by H05.

## Golden Example 3: Density Threshold for Research Sessions

```yaml
---
id: cn_density_threshold
kind: curation_nudge
pillar: P11
title: "Curation Nudge: High Information Density"
trigger:
  type: density_threshold
  threshold: 5
cadence:
  min_interval_turns: 10
  max_per_session: 2
prompt_template: "Observei {{observation}} novos fatos nesta sessao. Persistir em entity_memory?"
target_memory:
  destination: entity_memory
  auto_write_if_confirmed: true
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory, research]
---
```
**Why it works:** density_threshold fires when the agent observes 5 new facts -- ideal for
research sessions. max_per_session=2 is conservative; research sessions can be long and
frequent nudges break flow. Destination is entity_memory (structured, not flat text file).

## Anti-Example 1: Threshold Below Minimum

```yaml
---
id: cn_too_frequent
kind: curation_nudge
trigger:
  type: turn_count
  threshold: 2
prompt_template: "Persistir?"
---
```
**Why it fails (H02 + H05):** threshold=2 is below the minimum of 5 -- fires every 2 turns,
spam-level frequency. Also, prompt_template is missing the observation placeholder (H05) --
runtime substitution fails silently, producing generic unactionable nudges.

## Anti-Example 2: Wrong boundary -- using nudge as a guardrail

```yaml
---
id: cn_block_dangerous_action
kind: curation_nudge
trigger:
  type: turn_count
  threshold: 1
prompt_template: "BLOCK: {{observation}} is dangerous"
---
```
**Why it fails:** A nudge that fires every turn and says "BLOCK" is trying to be a guardrail.
Route to `guardrail-builder` instead. Nudges INFORM and ASK; they never block.

## Anti-Example 3: Invalid destination

```yaml
---
id: cn_bad_dest
kind: curation_nudge
target_memory:
  destination: slack_channel
  auto_write_if_confirmed: true
---
```
**Why it fails (H04):** `slack_channel` is not a valid destination. Only
`MEMORY.md`, `entity_memory`, and `knowledge_card` are allowed. For external
channels, use `notifier-builder` (P04).

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
