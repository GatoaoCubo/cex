---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for plugin validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: plugin

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_plug_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "plugin" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 16 required fields present (id, kind, pillar, version, created, updated, author, interface, lifecycle, enabled, api_surface_count, dependencies, domain, quality, tags, tldr) | Completeness |
| H07 | api_surface_count matches methods in API Surface table AND >= 1 | Method integrity |
| H08 | lifecycle contains at least [on_load, on_unload] | Lifecycle minimum |
| H09 | If hot_reload: true, lifecycle MUST include on_config_change | Hot-reload contract |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "plugin" | 0.5 | 10 |
| S03 | Interface Contract section present with contract description | 1.0 | 10 |
| S04 | API Surface table has >= 1 row with all columns | 1.0 | 10 |
| S05 | Configuration section present with schema and defaults | 1.0 | 10 |
| S06 | Lifecycle Hooks section covers all declared lifecycle events | 1.0 | 10 |
| S07 | Dependencies section present (even if empty list) | 0.5 | 10 |
| S08 | Testing section present with unit and integration strategies | 0.5 | 10 |
| S09 | isolation level declared and appropriate for plugin scope | 0.5 | 10 |
| S10 | config_schema has at least 1 field with type and default | 0.5 | 10 |
| S11 | version_constraints declared (semver range) | 0.5 | 10 |
| S12 | No filler phrases ("this plugin", "designed to", "various capabilities") | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 9 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind plugin [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Interface contract identified and documented
- [ ] API surface designed with methods and signatures
- [ ] No existing plugin for this interface (brain_query checked)
- [ ] Dependencies identified with version constraints
- [ ] Lifecycle events determined (minimum: on_load, on_unload)
- [ ] Configuration schema designed with defaults
- [ ] Isolation level selected
