---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for boot_config validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: boot_config

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken config |
| H02 | id matches `^p02_boot_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Discovery relies on this |
| H04 | kind == "boot_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 15 required fields present (id, kind, pillar, version, created, updated, author, provider, identity, constraints, tools, domain, quality, tags, tldr) | Completeness |
| H07 | identity object has name, role, satellite | Identity completeness |
| H08 | constraints object has max_tokens, context_window, timeout_seconds | Constraints completeness |
| H09 | tools is non-empty list | Agent needs at least one tool |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "boot-config" | 0.5 | 10 |
| S03 | model field is set | 0.5 | 10 |
| S04 | temperature is float 0.0-2.0 | 0.5 | 10 |
| S05 | flags list present and non-empty | 0.5 | 10 |
| S06 | mcp_config present when provider supports MCP | 1.0 | 10 |
| S07 | body has ## Constraints table with rationale | 1.0 | 10 |
| S08 | body has ## Tools Configuration table | 1.0 | 10 |
| S09 | density >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases | 1.0 | 10 |

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
Primary: validate_artifact.py --kind boot_config [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target provider identified with known runtime characteristics
- [ ] No existing boot_config for this provider (brain_query checked)
- [ ] Provider documentation accessible for constraints reference
- [ ] Tools/MCPs confirmed available for target provider
