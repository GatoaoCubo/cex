---
name: shared-file-proposal
description: Use a .proposal file instead of direct edits when concurrent nuclei need to change CLAUDE.md, kinds_meta.json, shared tools, rules, or other protected shared files.
when:
  - During grid or other concurrent dispatch when more than one nucleus is active.
  - When a change touches a protected shared file outside the nucleus-owned namespace.
  - When merge safety matters more than immediate in-wave mutation.
kind: skill
pillar: P04
nucleus: n03
quality: 8.7
version: 1.0.0
created: 2026-04-16
multi_runtime: true
runtimes: [claude, codex, gemini, ollama]
density_score: 0.8
related:
  - spec_infinite_bootstrap_loop
  - p01_kc_cex_orchestration_architecture
  - auto-accept-handoff
  - p03_sp_orchestration_nucleus
  - p12_wf_admin_orchestration
  - p01_kc_orchestration_best_practices
  - p12_wf_orchestration_pipeline
  - spec_n07_bootstrap_context
  - p08_ac_orchestrator
  - p01_ctx_cex_project
---

# Shared File Proposal

## When this fires
- A concurrent run needs to edit `CLAUDE.md`, `.cex/kinds_meta.json`, `.claude/rules/*.md`, shared tools, or other protected files.
- A nucleus is outside its own `N0x_*` namespace during a live grid.
- Post-wave merge coordination will be handled by N07 or another merge owner.

## What to do
1. If execution is concurrent, do not directly edit protected shared files. Write a proposal file at `.cex/runtime/proposals/{nucleus}_{timestamp}_{target_slug}.proposal.md` instead.
2. Include frontmatter with `nucleus`, `target`, `action`, `priority`, `created`, `depends_on`, and `idempotent`, then add a short description, payload, and rollback note.
3. Use the right action type: `merge_keys`, `append_lines`, `replace_section`, `patch_json`, or `full_replace`. Reserve `full_replace` for critical cases only.
4. Edit directly only when the run is solo, the file is inside the nucleus-owned namespace, the file is brand new, or the target is a handoff or signal file designed for concurrent writes.
5. For non-protected shared files that still need coordination, use `CexLock` around the read-modify-write block instead of the proposal pattern.
6. After the wave, merge proposals in priority then timestamp order, validate payloads, apply under lock, move applied proposals, and write conflicts to `.cex/runtime/proposals/conflicts/`.

## Example
- N04 wants to extend `.cex/kinds_meta.json` during a grid run. Trigger this skill and write a `.proposal.md` payload for N07 to merge after the wave instead of editing the registry directly.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.22 |
| [[auto-accept-handoff]] | downstream | 0.22 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.21 |
| [[p12_wf_admin_orchestration]] | downstream | 0.21 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.21 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.20 |
| [[spec_n07_bootstrap_context]] | related | 0.18 |
| [[p08_ac_orchestrator]] | downstream | 0.18 |
| [[p01_ctx_cex_project]] | upstream | 0.18 |
