---
kind: knowledge_card
id: bld_knowledge_card_hook_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for hook_config production
sources: pre-commit hook patterns, GitHub Actions event triggers, Webpack plugin lifecycle, 8F pipeline phase transitions, event-driven architecture patterns
quality: 9.0
title: "Knowledge Card Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_hook_config_builder
  - bld_examples_hook_config
  - bld_instruction_hook_config
  - p01_kc_hook_config
  - p03_sp_hook_config_builder
  - hook-config-builder
  - bld_collaboration_hook
  - bld_collaboration_hook_config
  - bld_architecture_hook_config
  - bld_instruction_hook
---

# Domain Knowledge: hook_config
## Executive Summary
Hook lifecycle configuration — declares which hooks fire at each build phase. Produced as P04 artifacts with concrete event bindings and conditions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 |
| llm_function | CONSTRAIN |
| Max bytes | 4096 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Phase-bound | Hooks bind to specific 8F phases (F1-F8) | Standard builder pipeline with known phases |
| Event-driven | Hooks fire on named events (pre-build, post-build, on-error) | Flexible pipeline with dynamic event sources |
| Conditional | Hooks fire only when condition is met (score < 8.0, error type) | Quality gates, error recovery, retry logic |
| Chained | Hook output feeds next hook input in sequence | Multi-step validation or transformation |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Embedding implementation | hook_config declares WHAT; hook implements HOW. Mixing creates tight coupling |
| Missing conditions | Unconditional hooks fire everywhere, causing noise and performance drag |
| Phase mismatch | Declaring hooks in wrong phase breaks execution order assumptions |
| Overlapping events | Multiple hooks on same event without priority causes race conditions |
## Application
1. Identify the target builder and its 8F pipeline phases
2. Select apownte hook events from the patterns above
3. Define concrete event bindings with phase, action, and condition
4. Validate against SCHEMA.md required fields
5. Check body size <= 4096 bytes
6. Verify id matches `^p04_hookconf_[a-z][a-z0-9_]+$`
## References
- pre-commit hook patterns, GitHub Actions event triggers, Webpack plugin lifecycle
- 8F pipeline phase transitions (F1 CONSTRAIN through F8 COLLABORATE)
- Event-driven architecture patterns (publish-subscribe, observer)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_hook_config_builder]] | downstream | 0.58 |
| [[bld_examples_hook_config]] | downstream | 0.53 |
| [[bld_instruction_hook_config]] | downstream | 0.49 |
| [[p01_kc_hook_config]] | sibling | 0.48 |
| [[p03_sp_hook_config_builder]] | downstream | 0.47 |
| [[hook-config-builder]] | downstream | 0.46 |
| [[bld_collaboration_hook]] | downstream | 0.46 |
| [[bld_collaboration_hook_config]] | downstream | 0.46 |
| [[bld_architecture_hook_config]] | downstream | 0.43 |
| [[bld_instruction_hook]] | downstream | 0.43 |
