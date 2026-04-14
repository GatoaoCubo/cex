---
id: p11_qg_handoff
kind: quality_gate
pillar: P11
title: "Gate: Handoff"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "handoff — task delegation packages for agent_group execution"
quality: 9.0
tags: [quality-gate, handoff, delegation, orchestration, scope-fence]
tldr: "Gates ensuring handoff artifacts carry complete delegation context: task, scope fence, commit instructions, and size discipline."
density_score: 0.88
llm_function: GOVERN
---
# Gate: Handoff
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: handoff` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: deploy_api` in file `setup.md` |
| H04 | Kind equals literal `handoff` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: task, context, scope_fence, commit, or signal |
| H07 | `scope_fence` contains both `allowed` and `prohibited` keys | Missing either key or both empty |
| H08 | `task` section has at least one numbered step | Narrative blob with no steps |
| H09 | `commit` section contains a valid git command | Section present but no `git commit` instruction |
| H10 | Body size <= 4096 bytes | Exceeds limit — handoff too verbose |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Task decomposition | 1.0 | Steps are atomic and independently verifiable | Steps exist but some are compound | Single block of instructions |
| S02 | Context completeness | 1.0 | Background, motivation, and prior state all present | Partial context (2/3) | Context absent |
| S03 | Scope fence precision | 1.0 | Exact paths listed in both allowed and prohibited | Paths listed for one side only | Vague scope description |
| S04 | Commit instruction quality | 0.5 | Stage command + message template + signal command present | Only commit message present | No commit guidance |
| S05 | Signal instruction | 0.5 | Signal call with agent_group, status, and score specified | Signal mentioned without params | Signal absent |
| S06 | Step ordering | 1.0 | Dependencies between steps are explicit | Steps ordered but implicit deps | Steps unordered |
| S07 | Open variable marking | 0.5 | All decision points marked `[OPEN_VARIABLE]` | Some decision points unmarked | No open variables marked |
| S08 | Size discipline | 1.0 | Body 1000-3000 bytes (dense, complete) | Body 3001-4096 bytes (verbose) | Body < 500 bytes (too sparse) |
| S09 | Autonomy framing | 0.5 | Explicit autonomy flag + quality target stated | Quality target stated without autonomy flag | Neither present |
| S10 | Retry/resilience guidance | 0.5 | Error handling or retry instructions included | Partial guidance | None |
| S11 | Naming convention | 0.5 | Filename follows `{MISSION}_{sat}.md` pattern | Filename partially correct | Arbitrary filename |
| S12 | No internal jargon leaked | 0.5 | No framework internals or unexplained acronyms | Minor internal refs | Heavy framework coupling |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden handoff template |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Time-critical incident response where full context is not yet known |
| Approver | Senior orchestrator (human) only |
