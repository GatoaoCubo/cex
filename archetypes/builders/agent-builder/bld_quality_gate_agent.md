---
id: p11_qg_agent
kind: quality_gate
pillar: P11
title: "Gate: agent"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: agent
quality: null
tags: [quality-gate, agent, P11, P02, governance, identity, agent-package]
tldr: "Gates for agent artifacts — persona + capabilities + iso_vectorstore packages ready for deploy."
density_score: 0.90
---

# Gate: agent
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | identity completeness + iso_vectorstore navigability |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all agent artifacts (P02)                           |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken agent boot |
| H02 | id matches `^p02_agent_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "agent" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 10 required fields present: id, kind, pillar, title, version, agent_node, domain, quality, tags, tldr | Completeness |
| H07 | llm_function == "BECOME" | Agent is identity construct, not callable |
| H08 | agent_node field is set (not blank or null) | Every agent belongs to a agent_node |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 |
| S02 | tags is list, len >= 3, includes "agent" | 0.5 |
| S03 | iso_vectorstore section lists >= 10 ISO files | 1.0 |
| S04 | routing_keywords is list, len >= 4 | 0.5 |
| S05 | body has ## File Structure with correct ISO naming convention | 1.0 |
| S06 | capabilities_count matches actual bullets in Architecture section | 1.0 |
| S07 | domain is specific (not "general" or "everything") | 0.5 |
| S08 | body has ## When to Use with explicit NOT-when exclusions | 0.5 |
| S09 | density_score >= 0.80 | 0.5 |
| S10 | No filler phrases ("this document", "in summary", "can help with") | 1.0 |
Weights sum: 7.5. Normalize: divide each by 7.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference agent definition |
| >= 8.0 | PUBLISH — register in routing index, deploy iso_vectorstore |
| >= 7.0 | REVIEW — complete iso_vectorstore or sharpen domain boundary |
| < 7.0  | REJECT — rework identity and capability scope |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical agent_node gap requiring immediate agent deploy |
| approver | p02-chief |
| audit_trail | Log in records/audits/ with justification and timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
