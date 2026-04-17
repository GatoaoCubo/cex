---
id: p11_qg_plugin
kind: quality_gate
pillar: P11
title: "Gate: plugin"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: plugin
quality: 9.0
tags: [quality-gate, plugin, P11, P04, governance, extensibility, lifecycle]
tldr: "Gates for plugin artifacts — interface contract, lifecycle hooks, API surface, and isolation level defined."
density_score: 0.85
llm_function: GOVERN
---
# Gate: plugin

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Definition
| Field     | Value                                              |
|-----------|----------------------------------------------------|
| metric    | interface contract clarity + lifecycle completeness |
| threshold | 8.0                                                |
| operator  | >=                                                 |
| scope     | all plugin artifacts (P04)                         |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = plugin not loadable |
| H02 | id matches `^p04_plug_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "plugin" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | interface field names the host interface or base class this plugin implements | A plugin without a declared interface is an orphan |
| H08 | lifecycle block declares at least on_load and on_unload handlers | Minimum lifecycle for safe load and teardown |
| H09 | api_surface list has >= 1 entry, each with method name, signature, and return type | Callers need a concrete API, not a description |
| H10 | If hot_reload: true, lifecycle MUST include on_config_change handler | Hot-reload without config handler causes stale state |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "plugin" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | config_schema block defines >= 1 field with type and default value | 1.0 |
| S05 | dependencies list is present (empty list is valid if none) | 0.5 |
| S06 | isolation_level field states scope of side effects (process, thread, sandboxed, or none) | 1.0 |
| S07 | hot_reload field explicitly set to true or false | 0.5 |
| S08 | version_constraints field states compatible host version range (semver) | 1.0 |
| S09 | error_handling block describes behavior on lifecycle failure (log-and-continue, halt, or retry) | 1.0 |
| S10 | performance_impact field estimates resource overhead (negligible, low, medium, high) | 0.5 |
| S11 | security_notes block states whether plugin has network, filesystem, or subprocess access | 1.0 |
| S12 | No filler phrases ("this plugin", "designed to extend", "various capabilities") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference plugin implementation for this interface |
| >= 8.0 | PUBLISH — register in plugin registry and enable for loading |
| >= 7.0 | REVIEW — complete config_schema, isolation level, or error handling |
| < 7.0  | REJECT — rework interface contract and lifecycle ofclarations |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical capability gap requiring plugin in production before full review when interface is stable |
| approver | p04-chief |
| audit_trail | Log in records/audits/ with interface name, host version, and timestamp |
| expiry | 48h — plugin must pass all gates before next release tag |
| never_bypass | H01 (YAML), H05 (quality null) |
