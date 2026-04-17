---
id: p11_qg_agent_package
kind: quality_gate
pillar: P11
title: "Gate: ISO Package"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "agent_package — portable self-contained agent bundles with tier-validated file inventories"
quality: 9.0
tags: [quality-gate, agent-package, packaging, portable, bundle, tier, distribution]
tldr: "Gates ensuring agent_package artifacts are self-contained, tier-compliant, portability-enforced bundles with valid manifests and correct LP file mappings."
density_score: 0.93
llm_function: GOVERN
---
# Gate: ISO Package
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: agent_package` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | `manifest.yaml` parses as valid YAML | Parse error anywhere in manifest |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem or package directory name | ID `weather_agent` in package dir `news_agent/` |
| H04 | Kind equals literal `agent_package` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All 14 required manifest fields present | Any required field absent from manifest.yaml |
| H07 | Tier is one of: `minimal`, `standard`, `complete`, `whitelabel` | Unknown or costm tier value |
| H08 | File count matches tier (minimal=3, standard=7, complete=10, whitelabel=12) | File count off by any amount |
| H09 | No hardcoded absolute paths in any bundled file | Any `/home/`, `C:\`, `~`, or machine-specific path found |
| H10 | `system_instruction.md` is <= 4096 tokens | Token count exceeds limit |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | LP mapping accuracy | 1.0 | Every file lists correct pillar-layer mapping in inventory | Most files mapped; some gaps | LP mapping absent |
| S02 | Self-containment | 1.0 | Package requires no external files to function at stated tier | Minor external deps documented | Undocumented external dependencies |
| S03 | LLM-agnostic instructions | 1.0 | `system_instruction.md` avoids model-specific syntax or API references | Minor model-specific hints | Instructions tied to one LLM vendor |
| S04 | Portability enforcement | 1.0 | All internal references use relative paths | Most relative; a few absolute slipped through | Absolute paths in multiple files |
| S05 | Tier justification | 0.5 | README or manifest explains why this tier was chosen | Tier stated, no rationale | No tier explanation |
| S06 | File inventory completeness | 1.0 | Every file in the package is listed in manifest inventory | Most listed; fewer than 2 missing | Inventory incomplete or absent |
| S07 | Token budget discipline | 1.0 | `system_instruction.md` uses 80-100% of 4096-token budget efficiently | 50-79% utilization (underused) | Under 50% or over budget |
| S08 | Version pinning | 0.5 | Manifest version pinned; changelog entry present | Version present, no changelog | No version |
| S09 | Whitelabel readiness | 0.5 | If tier=whitelabel: branding slots documented and parameterized | Partial parameterization | Not applicable or missing entirely |
| S10 | Distribution metadata | 0.5 | `author`, `license`, and `contact` all present in manifest | Partial metadata | None |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to distribution pool as golden package template |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
