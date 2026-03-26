---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for mcp_server validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: mcp_server

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_mcp_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "mcp_server" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, name, transport, tools_provided, resources_provided, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Tools, ## Resources, ## Transport & Auth | Core sections required |
| H08 | body <= 2048 bytes | Compact infrastructure spec |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "mcp_server" | 0.5 | 10 |
| S03 | tools_provided names match tool names in ## Tools section (zero drift) | 1.0 | 10 |
| S04 | resources_provided URI templates match ## Resources section (zero drift) | 1.0 | 10 |
| S05 | transport enum valid: stdio, sse, or http | 1.0 | 10 |
| S06 | Each tool in ## Tools has: name, description, parameters, return type | 1.0 | 10 |
| S07 | auth field present and valid enum value | 0.5 | 10 |
| S08 | No implementation code in body (spec only) | 1.0 | 10 |
| S09 | transport/auth pairing valid (stdio=none, sse/http=api_key/oauth/bearer) | 0.5 | 10 |
| S10 | description <= 200 chars and non-generic | 0.5 | 10 |
| S11 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S12 | Each resource has URI template, content-type, description | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 8 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind mcp_server [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Server name and domain identified
- [ ] Transport type selected (stdio/sse/http)
- [ ] All tools enumerated with concrete names
- [ ] All resources enumerated with URI templates
- [ ] No existing mcp_server for this domain (brain_query checked)
- [ ] Auth matches transport type
