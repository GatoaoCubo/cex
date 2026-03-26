---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for mental_model (P02) validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: mental_model

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML parses | Broken YAML = broken artifact |
| H02 | id matches `^p02_mm_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Discovery relies on this |
| H04 | kind == "mental_model" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present (id, kind, pillar, version, created, updated, author, agent, routing_rules, decision_tree, domain, quality, tags, tldr) | Completeness |
| H07 | pillar == "P02" (NOT P10) | Design-time, not runtime |
| H08 | routing_rules has >= 3 rules, each with keywords + action | Routing completeness |
| H09 | decision_tree has >= 2 conditions, each with condition + then | Decision completeness |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "mental-model" | 0.5 | 10 |
| S03 | priorities list present with >= 3 items | 1.0 | 10 |
| S04 | heuristics list present with >= 2 items | 0.5 | 10 |
| S05 | domain_map has covers and routes_to | 1.0 | 10 |
| S06 | personality object has tone, verbosity, risk_tolerance | 0.5 | 10 |
| S07 | tools_available list present and non-empty | 0.5 | 10 |
| S08 | constraints list present and non-empty | 0.5 | 10 |
| S09 | fallback object has action and escalate_to | 1.0 | 10 |
| S10 | density >= 0.80 | 0.5 | 10 |
| S11 | No filler phrases | 1.0 | 10 |
| S12 | routing_rules keywords are specific (not "general", "anything") | 0.5 | 10 |

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
Primary: validate_artifact.py --kind mental_model [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target agent identified with clear domain and routing needs
- [ ] No existing P02 mental_model for this agent (brain_query checked)
- [ ] Agent's routing patterns documented or observable
- [ ] Domain boundaries clear (what agent covers vs routes away)
- [ ] Confirmed this is design-time (P02), not runtime state (P10)
