---
id: p12_ct_brand_audit.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: brand_audit
purpose: Coordinate a 3-role crew that audits brand consistency across all nucleus outputs -- scan assets, score coherence, produce actionable audit report
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "scanner -> checker -> reporter"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "Brand Audit Crew Template"
version: "1.0.0"
author: n02_marketing
tags: [crew_template, brand_audit, marketing, composable, crewai, brand_consistency]
tldr: "3-role sequential crew: scan brand assets -> score consistency across 6 dimensions -> produce audit report with fix priorities"
domain: "brand consistency auditing"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_brand_scanner.md
  - p02_ra_consistency_checker.md
  - p02_ra_audit_reporter.md
  - p12_ct_product_launch.md
  - p12_ct_content_campaign.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
---

## Overview
Instantiate when brand drift is suspected or on a quarterly cadence to verify
that all nucleus outputs match the canonical brand voice, visual identity, and
messaging framework defined in `.cex/brand/brand_config.yaml`. The crew runs
three roles in strict sequence: scanner collects brand-relevant artifacts across
all N01-N06 outputs, consistency_checker scores each artifact against 6 brand
dimensions (voice, tone, palette, typography, messaging, terminology), and the
reporter synthesizes findings into a prioritized audit report with specific
remediation actions. Producer is N02 (marketing); consumers are all nuclei
(each receives their own remediation section).

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| brand_scanner | p02_ra_brand_scanner.md | Crawl all nucleus outputs, extract brand-relevant artifacts + snippets |
| consistency_checker | p02_ra_consistency_checker.md | Score each artifact on 6 brand dimensions, flag violations |
| audit_reporter | p02_ra_audit_reporter.md | Synthesize scores into prioritized audit report with fix actions |

## Process
Topology: `sequential`. Rationale: checker cannot score without the scanner's
artifact inventory; reporter cannot synthesize without the checker's dimension
scores. Parallelism would produce an incomplete audit (checker scoring artifacts
the scanner hasn't found yet).

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| brand_scanner | shared | per-crew-instance (artifact list is ephemeral) |
| consistency_checker | shared | persistent (scores saved to P11 regression_check) |
| audit_reporter | shared | persistent (report saved to P01 as knowledge_card) |

## Handoff Protocol
`a2a-task-sequential` -- scanner emits `artifact_inventory_id` with file paths
and snippet hashes. Checker reads inventory, scores each, emits `score_matrix_id`.
Reporter reads score matrix, produces audit report with per-nucleus remediation.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Scanner inventory covers >= 5 nuclei with >= 3 artifacts each
- [ ] Checker scores all 6 dimensions for every inventoried artifact
- [ ] Reporter audit report includes per-nucleus remediation priority (P0/P1/P2)
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] Overall brand consistency score computed (weighted avg of 6 dimensions)

## Instantiation
```bash
python _tools/cex_crew.py run brand_audit \
    --charter N02_marketing/P12_orchestration/crews/team_charter_brand_audit.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_brand_scanner.md]] | upstream | 0.52 |
| [[p02_ra_consistency_checker.md]] | upstream | 0.50 |
| [[p02_ra_audit_reporter.md]] | upstream | 0.48 |
| [[p12_ct_product_launch.md]] | sibling | 0.38 |
| [[p12_ct_content_campaign.md]] | sibling | 0.36 |
| [[bld_instruction_crew_template]] | related | 0.31 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.27 |
