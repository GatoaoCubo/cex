---
kind: architecture
id: bld_architecture_guardrail
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of guardrail — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| scope | The agents, artifact types, or execution contexts this guardrail applies to | guardrail | required |
| rules | Explicit list of prohibited actions or content patterns | guardrail | required |
| severity | Risk level of each rule: critical, high, medium, or low | guardrail | required |
| enforcement_mode | How violations are handled: block (halt), warn (continue), or log (record only) | guardrail | required |
| violation_examples | Concrete examples of what a violation looks like; used for detection calibration | guardrail | required |
| bypass_policy | Whether any role or condition may override the guardrail; default is none | guardrail | required |
| trigger_condition | Pattern or condition that activates enforcement (input match, output pattern, etc.) | guardrail | required |
| remediation | Action taken after a block: error message, fallback response, or escalation | guardrail | conditional |
## Dependency Graph
```
law (P08)          --produces--> guardrail
guardrail          --depends-->  hook (P04)
guardrail          --signals-->  quality_gate (P11)
guardrail          --produces--> feature_flag (P09)
permission (P09)   --depends-->  guardrail
```
| From | To | Type | Data |
|------|----|------|------|
| law (P08) | guardrail | produces | operational principles that ground safety rules |
| guardrail | hook (P04) | depends | pre/post execution checks that enforce the rules at runtime |
| guardrail | quality_gate (P11) | signals | compliance events and violation counts for monitoring |
| guardrail | feature_flag (P09) | produces | safety constraints that govern flag behavior and kill-switch policy |
| permission (P09) | guardrail | depends | access-control scope that guardrail rules operate within |
## Boundary Table
| guardrail IS | guardrail IS NOT |
|--------------|------------------|
| An external safety boundary agents cannot self-override | A quality score or pass/fail threshold (that is quality_gate) |
| Classified by severity (critical to low) with explicit enforcement mode | An access-control rule for read/write permissions |
| Capable of blocking, warning, or logging on violation | A bug-fix loop or iterative correction mechanism |
| Owner of bypass_policy — documents whether any override is possible | An operational law defining architectural principles |
| Applied at runtime via hooks (pre/post execution) | A lifecycle rule managing artifact freshness or expiry |
| Backed by concrete violation examples for detection calibration | A performance optimizer targeting metrics improvement |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Foundation | law (P08), permission (P09) | Anchor safety rules in operational principles and access scope |
| Definition | scope, rules, severity, trigger_condition | Specify what is prohibited, for whom, and how severe each rule is |
| Enforcement | enforcement_mode, hook (P04), remediation | Execute block/warn/log at runtime via pre/post hooks |
| Transparency | violation_examples, bypass_policy | Document what violations look like and whether overrides exist |
| Observability | quality_gate (P11) | Monitor compliance rates and surface violation signals |
