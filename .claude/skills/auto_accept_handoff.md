---
name: auto-accept-handoff
description: Set auto_accept on handoffs for autonomous grid or overnight execution so nuclei use recommended defaults for uncovered GDP gaps instead of re-prompting the user.
when:
  - Writing handoff frontmatter for grid dispatch when the user will not be present.
  - Dispatching overnight or autonomous missions after the decision manifest is locked.
  - Preventing nuclei from blocking on uncovered subjective choices during F4.
kind: skill
pillar: P04
nucleus: n03
quality: 8.7
version: 1.0.0
created: 2026-04-16
multi_runtime: true
runtimes: [claude, codex, gemini, ollama]
density_score: 0.79
related:
  - auto-accept-handoff
  - p03_sp_orchestration_nucleus
  - SPEC_07_gdp_enforcement
  - output_grid_test_n02
  - p01_kc_orchestration_best_practices
  - p12_wf_orchestration_pipeline
  - skill_guided_decisions
  - handoff-protocol-builder
  - handoff-builder
  - p08_ac_orchestrator
---

# Auto Accept Handoff

## When this fires
- N07 is dispatching a grid or overnight run where no user will answer follow-up GDP questions.
- The decision manifest is locked but some subjective edge case may still appear at runtime.
- A handoff must explicitly authorize autonomous continuation instead of re-prompting.

## What to do
1. Add `auto_accept: true` and a concrete `auto_accept_reason` to the handoff frontmatter once the manifest is locked and the work is fully specified.
2. When `auto_accept` is active, keep reading the decision manifest normally. For subjective gaps not covered there, apply the builder's `* Recommended` default and continue.
3. Log each autofilled decision to `.cex/runtime/decisions/autofilled/<timestamp>_<nucleus>.yaml` so the choice is auditable.
4. Never re-prompt the user while `auto_accept` is active. If no reasonable default exists, emit `BLOCKED` instead of asking.
5. Preserve all normal quality controls. `auto_accept` does not bypass F7 gates and does not authorize unsafe direct edits to protected shared files.
6. Propagate the flag through `CEX_AUTO_ACCEPT` in dispatch and boot wrappers so the nucleus can enforce the behavior at runtime.

## Example
- An overnight Wave B handoff sets `auto_accept: true` with reason `manifest locked for Wave B`. If N03 hits an uncovered subjective choice, it applies the recommended default, logs it, and keeps moving.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[auto-accept-handoff]] | downstream | 0.53 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.31 |
| [[SPEC_07_gdp_enforcement]] | upstream | 0.27 |
| [[output_grid_test_n02]] | downstream | 0.27 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.25 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.22 |
| [[skill_guided_decisions]] | related | 0.21 |
| [[handoff-protocol-builder]] | upstream | 0.21 |
| [[handoff-builder]] | downstream | 0.21 |
| [[p08_ac_orchestrator]] | downstream | 0.20 |
