---
kind: quality_gate
id: p11_qg_pattern
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of pattern artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: pattern"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, pattern, P11, P08, governance, architecture, reuse]
tldr: "Gates for pattern artifacts — recurring problem, concrete solution, balanced forces, and documented anti-pattern."
domain: pattern
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - bld_knowledge_card_pattern
  - p11_qg_naming_rule
  - bld_architecture_pattern
  - p11_qg_builder
  - p01_kc_pattern
  - p03_ins_pattern
  - p11_qg_boot_config
  - pattern-builder
  - bld_schema_pattern
  - p11_qg_agent
---

## Quality Gate

# Gate: pattern
## Definition
| Field     | Value                                              |
|-----------|----------------------------------------------------|
| metric    | problem recurrence + solution concreteness + force balance |
| threshold | 8.0                                                |
| operator  | >=                                                 |
| scope     | all pattern artifacts (P08)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = pattern not discoverable |
| H02 | id matches `^p08_pat_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "pattern" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | problem field describes a recurring situation, not a one-off fix (contains recurrence signal word: "repeatedly", "often", "whenever", "each time", or equivalent) | One-off fixes are not patterns |
| H08 | solution field describes the approach at implementation level (not abstract advice) | "Use better design" is not a solution |
| H09 | forces list has >= 2 entries documenting opposing tensions that make the problem hard | No forces = no pattern, just a preference |
| H10 | consequences list includes >= 1 negative trade-off (cost, complexity, or constraint) | Benefits-only = marketing, not engineering |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "pattern" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | applicability block states both when-to-use AND when-not-to-use conditions | 1.0 |
| S05 | examples block has >= 2 concrete applications of the pattern in a real context | 1.0 |
| S06 | anti_pattern block documents >= 1 wrong approach that looks similar but fails | 1.0 |
| S07 | related_patterns block cross-references >= 1 other pattern with stated relationship | 0.5 |
| S08 | variants list documents known adaptations or specializations of the base pattern | 0.5 |
| S09 | code_or_pseudocode block provides a minimal working illustration | 1.0 |
| S10 | name is 2–5 words, title-case, and self-describing without context | 0.5 |
| S11 | No filler phrases ("this pattern", "in order to", "various scenarios") | 1.0 |
Weights sum: 8.5. Normalize: divide each by 8.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical reference pattern |
| >= 8.0 | PUBLISH — index in pattern catalog and cross-link from related patterns |
| >= 7.0 | REVIEW — strengthen forces, add anti-pattern, or provide concrete example |
| < 7.0  | REJECT — rework problem statement and solution into implementable form |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Pattern needed to unblock active architecture decision with no existing equivalent in catalog |
| approver | p08-chief |
| audit_trail | Log in records/audits/ with linked decision record and timestamp |
| expiry | 72h — pattern must pass all gates and be indexed before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

# Examples: pattern-builder
## Golden Example
INPUT: "Document the Continuous Batching pattern for multi-agent_group task processing"
OUTPUT:
```yaml
id: p08_pat_continuous_batching
kind: pattern
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "orchestration"
quality: null
tags: [pattern, batching, orchestration, parallel, multi-agent_group]
tldr: "Auto-refill agent_group slots from queue as tasks complete, eliminating idle between waves"
name: "Continuous Batching"
problem: "Sequential wave execution leaves agent_groups idle between batches"
solution: "Auto-refill available slots from queue as each agent_group complete"
context: "Multi-agent_group orchestration with >6 independent tasks"
forces: ["throughput vs resource limits", "parallelism vs git contention", "queue depth vs RAM ceiling"]
consequences: ["1.6x speedup over sequential", "zero idle between waves", "requires independent tasks", "max 3 concurrent agent_groups (RAM)"]
related_patterns: [p08_pat_wave_execution, p08_pat_signal_monitor]
anti_patterns: ["manual slot management", "unbounded parallelism"]
applicability: "Use when >6 independent tasks across <=3 agent_groups. Do NOT use for dependent tasks or shared-file edits."
keywords: [batching, parallel, queue, throughput, spawn]
```
## Problem
When orchestrating multi-agent_group work in waves (batch N complete, then batch N+1 starts), agent_groups sit idle between waves. If batch 1 has 3 tasks finishing at different times, the fastest agent_group waits for the slowest before batch 2 begins.
## Context
- Environment: Orchestrator managing 2-3 agent_groups via spawn scripts
- Frequency: every multi-agent_group mission with >6 tasks
- Severity: 40% throughput waste in sequential wave execution
## Forces
- **Throughput vs resources**: more parallelism = faster, but RAM limits to 3 agent_groups
- **Independence vs contention**: parallel tasks must not edit same files (git conflicts)
- **Queue depth vs complexity**: deeper queues need naming conventions and signal tracking
## Solution
Replace static wave execution with a queue-drain loop:
1. Fill all available slots (up to 3) with tasks from queue
2. Monitor signals for completion (poll every 15s)
3. When a agent_group complete, immediately assign next queued task
4. Repeat until queue empty
```text
Queue: [T1, T2, T3, T4, T5, T6, T7]
Slots: [SAT_A, SAT_B, SAT_C]
T=0:  SAT_A=T1, SAT_B=T2, SAT_C=T3  (queue: T4-T7)
T=5:  SAT_A done -> SAT_A=T4          (queue: T5-T7)
T=8:  SAT_C done -> SAT_C=T5          (queue: T6-T7)
...continues until queue empty
```
## Consequences
Benefits:
- 1.6x throughput over sequential waves (measured on ISOFIX 7/7)
- Zero idle time between task completions
- Auto-scales to available slots
Costs:
- Tasks MUST be independent (no shared file edits)
- Requires signal monitoring infrastructure
- Naming convention overhead ({MISSION}_batch_{N}_{SAT}.md)
## Examples
1. **ISOFIX Mission**: 7 batches across researcher+builder+knowledge-engine, 1.6x speedup confirmed
2. **CBTEST Mixed**: 3 agent_groups, mixed complexity, zero git contention
## Anti-Patterns
- **Manual Slot Management**: manually tracking which agent_group is free wastes orchestrator time
- **Unbounded Parallelism**: launching >3 agent_groups causes BSOD (RAM exhaustion)
## Related Patterns
- Wave Execution: predecessor pattern (static batches); continuous batching improves on it
- Signal Monitor: required infrastructure for detecting slot availability
## References
- records/skills/continuous_batching/SKILL.md
- spawn_grid.ps1 -mode continuous
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_pat_ pattern (H02 pass)
- kind: pattern (H04 pass)
- 21 fields present including all 14 required (H06 pass)
- name: 2 words "Continuous Batching" (H08 pass)
- problem describes recurring situation (H09 pass)
- forces has 3 tensions (S02 pass)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
