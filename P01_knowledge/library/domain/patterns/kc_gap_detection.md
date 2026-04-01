---
id: p01_kc_gap_detection
kind: knowledge_card
type: domain
pillar: P01
title: "Gap Detection"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 8.4
tags: [pattern, skill, llm]
tldr: "Systematically find missing knowledge, tools, or artifacts. Compare current vs desired state."
keywords: [gap-detection, audit, completeness, missing]
density_score: 0.91
---

# Gap Detection

| Method | Detects | Tool |
|--------|---------|------|
| Schema | Missing fields | cex_compile.py |
| Builder audit | Missing specs | cex_doctor.py |
| Query miss | Missing KC | cex_query.py |
| Coverage | Untested tools | pytest --cov |
| User feedback | Missing capabilities | Conversation |
