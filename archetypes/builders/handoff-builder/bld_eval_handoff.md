---
kind: quality_gate
id: p11_qg_handoff
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of handoff artifacts
pattern: few-shot learning for delegation instruction packaging
quality: 9.0
title: "Gate: Handoff"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, handoff, delegation, orchestration, scope-fence]
tldr: "Gates ensuring handoff artifacts carry complete delegation context: task, scope fence, commit instructions, and size discipline."
domain: "handoff — task delegation packages for agent_group execution"
created: "2026-03-27"
updated: "2026-03-27"
last_reviewed: "2026-04-18"
density_score: 0.88
related:
  - p11_qg_instruction
  - p11_qg_input_schema
  - p11_qg_agent_computer_interface
  - p11_qg_knowledge_card
  - p01_kc_handoff
  - p11_qg_agent_package
  - p11_qg_interface
  - p11_qg_quality_gate
  - p02_qg_training_method
  - bld_collaboration_handoff
---

## Quality Gate

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

## Examples

# Examples: handoff-builder
## Golden Example
INPUT: "Create handoff for edison to build 3 archetype builders in wave 19"
OUTPUT (`p12_ho_wave19_builders.md`):
```yaml
id: p12_ho_wave19_builders
kind: handoff
lp: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "stella"
agent_group: "edison"
mission: "wave19"
autonomy: "full"
quality_target: 9.0
domain: "orchestration"
quality: null
tags: [handoff, edison, wave19, builders, archetype]
tldr: "Edison builds 3 archetype builders (session-state, dag, handoff) with 13 ISO each"
dependencies: []
seeds: [builder, archetype, session_state, dag, handoff, P10, P12]
agent: "builder-builder"
batch: "batch_06"
wave: 19
keywords: [wave19, builders, archetype, edison]
linked_artifacts:
  primary: "archetypes/builders/"
  related: ["archetypes/builders/_builder-builder/", "archetypes/SEED_BANK.yaml"]
```
# builder_agent — WAVE19: Build 3 Builders
**Full Autonomy** | **Quality 9.0+**
**REGRA: Commit and signal ANTES de qualquer pausa.**
## Context
Wave 19 requires 3 new archetype builders for types session_state (P10),
dag (P12), and handoff (P12). Each builder follows the 13-ISO pattern
established by _builder-builder. Reference builders: signal-builder, workflow-builder.
## Tasks
### Step 1: Read References
Read _builder-builder/BUILDER_NORMS.md, signal-builder/, and workflow-builder/.
### Step 2: Build session-state-builder
Create 13 builder spec files in archetypes/builders/session-state-builder/.
### Step 3: Commit session-state-builder
Run: git add archetypes/builders/session-state-builder/ && git commit
### Step 4: Build dag-builder
Create 13 builder spec files in archetypes/builders/dag-builder/.
### Step 5: Commit dag-builder
Run: git add archetypes/builders/dag-builder/ && git commit
### Step 6: Build handoff-builder
Create 13 builder spec files in archetypes/builders/handoff-builder/.
### Step 7: Commit handoff-builder
Run: git add archetypes/builders/handoff-builder/ && git commit
## Scope Fence
- SOMENTE: archetypes/builders/session-state-builder/, archetypes/builders/dag-builder/, archetypes/builders/handoff-builder/
- NAO TOQUE: archetypes/builders/_builder-builder/, archetypes/builders/signal-builder/, P12_orchestration/_schema.yaml
## Commit
```bash
git add archetypes/builders/session-state-builder/
git commit -m "archetype: session-state-builder -- 13 ISO (P10, Wave 19)"
git add archetypes/builders/dag-builder/
git commit -m "archetype: dag-builder -- 13 ISO (P12, Wave 19)"
git add archetypes/builders/handoff-builder/
git commit -m "archetype: handoff-builder -- 13 ISO (P12, Wave 19)"
```
## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', 9.0)"
```
WHY GOLDEN: filename `p12_ho_*`, 19+ frontmatter fields, all 5 body sections, specific tasks, SOMENTE+NAO TOQUE, exact git commands, signal mechanism, no prompt/event/routing drift.
## Anti-Example
BAD OUTPUT (`p03_ap_build_stuff.md`):
```yaml
id: p03_ap_build_stuff
kind: action_prompt
lp: P03
persona: "You are a helpful builder"
response_format: "markdown"
Build some archetype builders. Use your best judgment.
Make sure they are good quality. Commit when done.
Try to finish everything today if possible.
```
FAILURES:
1. wrong kind: `action_prompt` instead of `handoff` (H02)
2. wrong pillar: `P03` instead of `P12` (H01)
3. wrong id prefix: `p03_ap_` instead of `p12_ho_` (H01)
4. contains `persona`: prompt engineering -> action_prompt drift (H08)
5. contains `response_format`: prompt constraint -> action_prompt drift (H08)
6. missing required fields: `agent_group`, `mission`, `autonomy`, `quality_target`, `quality`, `tags`, `tldr` (H03)
7. vague tasks: "Build some archetype builders" is not specific (H09)
8. no scope fence section: missing SOMENTE/NAO TOQUE (H10)
9. no commit section: missing exact git commands (H10)

## Golden Example 2 (HERMES — Handoff with Revision Policy Fields)
INPUT: "Create handoff for n03 to enrich 6 builder schemas with HERMES-compat fields; max 3 revisions, escalate to senior_nucleus if stuck"
OUTPUT (`p12_ho_hermes_w2_enrichments.md`):
```yaml
id: p12_ho_hermes_w2_enrichments
kind: handoff
lp: P12
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n07_orchestrator"
agent_group: "n03"
mission: "HERMES_W2"
autonomy: "full"
quality_target: 9.0
domain: "engineering"
quality: null
tags: [handoff, hermes, w2, enrichment, schema]
tldr: "N03 enriches 6 builder schemas with HERMES fields; max 3 revisions, security-first priority"
dependencies: ["p12_ho_hermes_w1_archetypes"]
seeds: [skill, session_state, sandbox_config, schedule, agent, handoff, HERMES]
wave: 2
max_revisions: 3
escalation_target: senior_nucleus
revision_priority_order: [security, quality, implementation]
```
# n03 -- HERMES W2: Enrich 6 Schemas
**Full Autonomy** | **Quality 9.0+** | **Max 3 revisions**
## Context
HERMES W2 enriches existing builder schemas with new optional fields for autonomous skill creation,
session search, cloud sandboxes, NL schedules, thinking budgets, and revision policies.
## Tasks
1. Patch bld_schema_*.md for skill, session_state, sandbox_config, schedule, agent, handoff
2. Add HERMES example to bld_examples_*.md for each kind
3. Bump spec_version to 1.0.1 in kinds_meta.json for all 6 kinds
## Scope Fence
- SOMENTE: archetypes/builders/{skill,session-state,sandbox-config,schedule,agent,handoff}-builder/, .cex/kinds_meta.json
- NAO TOQUE: archetypes/builders/_builder-builder/, N0X_*/
## Commit
```bash
git add archetypes/builders/ .cex/kinds_meta.json
git commit -m "[N03] HERMES W2: enrich 6 kinds with HERMES-compat fields"
```
## Signal
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, mission='HERMES_W2')"
```
WHY GOLDEN (HERMES revision fields):
- `max_revisions: 3`: caps autonomous retry loops; prevents infinite quality-chasing
- `escalation_target: senior_nucleus`: when stuck, N03 escalates to N07 (not user-interrupting)
- `revision_priority_order: [security, quality, implementation]`: if revision budget is tight, fix security issues first, then quality gates, then implementation polish
- These fields integrate with `revision_loop_policy` kind (P11) for system-wide enforcement

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
