---
id: smoke_test_gemini_20260415
kind: smoke_eval
title: Gemini Smoke Test 2026-04-15
version: 1
quality: 8.5
pillar: P07
nucleus: N04
runtime: gemini-2.5-flash
tags: [gemini, smoke-test, boris-merge, multi-runtime]
density_score: 0.84
related:
  - p02_mc_google_gemini_2_5_pro
  - showoff_w2_n05_gemini
  - showoff_w5_n06_gemini
  - showoff_w5_n02_gemini
  - output_sdk_validation_audit
  - dispatch
  - n07_memory_grid_ops
  - p01_kc_orchestration_best_practices
  - p12_sc_admin_orchestrator
  - p03_sp_orchestration_nucleus
---

# Gemini Smoke Test 2026-04-15

Result: gemini boot works without --include-directories
Signed: N04 gemini

## Context

Validates that `boot/n0*_gemini.ps1` can spawn a gemini nucleus and commit
work after two fixes applied 2026-04-15:

1. Removed `--include-directories $cexRoot` (was forcing full-repo pre-index).
2. Switched model `gemini-2.5-pro` -> `gemini-2.5-flash` (higher RPM, cheaper).

With both fixes, N04 gemini produced this file and signalled complete,
re-enabling 4-runtime grid dispatch (claude + codex + gemini + ollama).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_mc_google_gemini_2_5_pro]] | upstream | 0.51 |
| [[showoff_w2_n05_gemini]] | sibling | 0.42 |
| [[showoff_w5_n06_gemini]] | sibling | 0.42 |
| [[showoff_w5_n02_gemini]] | sibling | 0.41 |
| [[output_sdk_validation_audit]] | related | 0.33 |
| [[dispatch]] | downstream | 0.30 |
| [[n07_memory_grid_ops]] | downstream | 0.30 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.28 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.27 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.23 |
