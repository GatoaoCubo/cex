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
