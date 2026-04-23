---
kind: quality_gate
id: p11_qg_agent_package
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of agent_package artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: ISO Package"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, agent-package, packaging, portable, bundle, tier, distribution]
tldr: "Gates ensuring agent_package artifacts are self-contained, tier-compliant, portability-enforced bundles with valid manifests and correct LP file mappings."
domain: "agent_package — portable self-contained agent bundles with tier-validated file inventories"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.93
related:
  - bld_instruction_agent_package
  - bld_examples_agent_package
  - p03_sp_agent_package_builder
  - bld_knowledge_card_agent_package
  - agent-package-builder
  - bld_schema_agent_package
  - p10_lr_agent_package_builder
  - bld_config_agent_package
  - bld_output_template_agent_package
  - p11_qg_input_schema
---

## Quality Gate

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

## Examples

# Examples: agent-package-builder
## Golden Example
INPUT: "Package the data-analyst agent as a standard agent package bundle"
OUTPUT:
```yaml
id: p02_iso_data_analyst
kind: agent_package
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
agent_name: "data-analyst"
tier: "standard"
files_count: 7
domain: "data_analysis"
llm_function: BECOME
portable: true
lp_mapping:
  manifest.yaml: P02
  system_instruction.md: P03
  instructions.md: P03
  architecture.md: P08
  output_template.md: P05
  examples.md: P07
  error_handling.md: P11
system_instruction_tokens: 2840
quality: null
tags: [agent-package, data-analysis, analytics, P02]
tldr: "Standard 7-file ISO bundle for data-analyst agent with analysis pipeline and error handling"
density_score: 0.88
```
## Agent Identity
data-analyst is a data analysis specialist. Transforms raw datasets into structured
insights via statistical analysis, visualization, and pattern detection.
## File Inventory
| File | Pillar | Tier | Status |
|------|--------|------|--------|
| manifest.yaml | P02 | minimal | present |
| system_instruction.md | P03 | minimal | present |
| instructions.md | P03 | minimal | present |
| architecture.md | P08 | standard | present |
| output_template.md | P05 | standard | present |
| examples.md | P07 | standard | present |
| error_handling.md | P11 | standard | present |
| quick_start.md | P01 | complete | absent |
| input_schema.yaml | P06 | complete | absent |
| upload_kit.md | P04 | complete | absent |
## Tier Compliance
Declared: standard. Files present: 7/7. No gaps.
## Portability Notes
- Platform: platform_agnostic
- Hardcoded paths: none
- External dependencies: none (self-contained analysis prompts)
## References
- Source agent: agents/data_analyst/README.md
- Builder: agent-package-builder v1.0.0
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_iso_ pattern (H02 pass) | kind: agent_package (H04 pass)
- 19 fields in frontmatter (H06 pass) | 3 required files present (H07 pass)
- files_count: 7 matches directory (H08 pass) | system_instruction: 2840 tokens (H09 pass)
- No hardcoded paths (H10 pass) | tier "standard" matches 7 files (S03 pass)
- tldr: 82ch (S01 pass) | tags: 4 items with "agent-package" (S02 pass) | density: 0.88 (S06 pass)
- lp_mapping present for all 7 files (S08 pass) | File Inventory table complete (S10 pass)
## Anti-Example
INPUT: "Package my helper agent"
BAD OUTPUT:
```yaml
id: helper_package
kind: package
tier: large
files_count: 3
quality: 9.0
tags: [helper]
tldr: "This is a comprehensive package that contains all the necessary files for the helper agent to function properly across various platforms."
```
Files included: manifest.yaml, prompt.txt, readme.md
FAILURES:
1. id: no `p02_iso_` prefix -> H02 FAIL
2. kind: "package" not "agent_package" -> H04 FAIL
3. quality: 9.0 (not null) -> H05 FAIL
4. Missing 10 required fields (pillar, version, created, updated, author, agent_name, domain, quality as null, tags proper, tldr proper) -> H06 FAIL
5. Required files wrong names (prompt.txt not system_instruction.md, readme.md not instructions.md) -> H07 FAIL
6. tier: "large" not in enum [minimal, standard, complete, whitelabel] -> S03 FAIL
7. tags: only 1 item, missing "agent-package" -> S02 FAIL
8. tldr: 134ch with filler ("This is a comprehensive package that contains") -> S01+S09 FAIL
9. No lp_mapping -> S08 FAIL
10. No File Inventory table -> S10 FAIL
11. No portability check -> S11 FAIL
12. No Agent Identity section -> body structure FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
