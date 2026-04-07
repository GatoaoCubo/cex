---
id: p01_kc_self_healing_skill
kind: knowledge_card
type: domain
pillar: P01
title: "Self-Healing Skill"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, self-healing, auto-fix, recovery, validation-loop]
tldr: "Detect own errors, diagnose root cause, apply targeted fix, retry up to 3x. Escalate if unresolved. Log every fix as a learning record."
when_to_use: "When an LLM-generated artifact fails validation, a tool returns an error, or output deviates from expected schema."
keywords: [self-healing, auto-fix, validation-loop, recovery, retry, escalation]
density_score: 0.95
---

# Self-Healing Skill

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Detect failure → diagnose → fix → retry (max 3) → escalate |
| Trigger | Validation failure, tool error, schema mismatch, quality < threshold |
| Benefit | Reduces human intervention by 60-80% for recoverable errors |
| Risk if skipped | Broken outputs propagate, manual debugging bottleneck |

## Lifecycle Flow

```
generate -> validate -> [pass] -> done
                    -> [fail] -> diagnose -> fix -> retry (max 3)
                                                -> [still fail] -> escalate to user
```

## Healing Strategy Matrix

| Error Type | Diagnosis Method | Fix Strategy | Success Rate |
|------------|-----------------|--------------|-------------|
| Missing frontmatter field | Schema diff | Insert default + flag | ~95% |
| Quality below threshold | Score decomposition | Targeted pass (density, structure) | ~80% |
| Tool execution error | stderr parsing | Retry with adjusted params | ~70% |
| Format violation | Regex validation | Reformat output section | ~90% |
| Hallucinated content | Source triangulation | Strip unverifiable claims | ~60% |
| Encoding error | Byte inspection | Re-encode to UTF-8 | ~99% |

## Retry Protocol

| Attempt | Strategy | Escalation |
|---------|----------|-----------|
| 1 | Same approach, fix identified error | None |
| 2 | Alternative approach (different prompt/tool) | Log warning |
| 3 | Minimal viable output + detailed error report | Flag for review |
| 4+ | **Never** — escalate to user immediately | Create incident |

## Key Principles

- **Fail fast, heal fast**: detect errors at the earliest validation gate
- **One fix per retry**: never change multiple things simultaneously
- **Always log**: every heal attempt → learning_record (even failures)
- **Preserve original**: keep the broken version for diff analysis
- **Budget-aware**: healing costs tokens — abort if budget exceeded

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Infinite retry loop | No max attempts, burns tokens forever |
| Silent healing | Fixes without logging, loses learning signal |
| Shotgun fix | Changes everything at once, can't attribute improvement |
| Heal without diagnosis | Random edits hoping to pass validation |
| Escalation avoidance | Retrying 10+ times instead of asking user |

## CEX Integration

| Concept | CEX artifact / tool |
|---------|-------------------|
| Error detection | `cex_compile.py`, `cex_doctor.py` |
| Fix application | `cex_evolve.py` (heuristic mode) |
| Learning capture | `cex_feedback.py` → `.cex/learning_records/` |
| Quality gate | `cex_score.py` → quality field in frontmatter |
| Escalation signal | `signal_writer.py` → `needs_user` signal |

## Linked Artifacts

- `p01_kc_iterative_refinement_skill` — multi-pass improvement (complementary)
- `p01_kc_confidence_scoring` — threshold-based decision on heal vs escalate
- `p01_kc_gap_detection` — find what's missing before attempting fix
