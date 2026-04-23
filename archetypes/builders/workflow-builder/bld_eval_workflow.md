---
kind: quality_gate
id: p11_qg_workflow
pillar: P12
llm_function: GOVERN
purpose: Golden and anti-examples of workflow artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Workflow'
version: 1.0.0
author: builder
tags:
- eval
- P12
- quality_gate
- examples
tldr: Validates multi-step orchestration flows for steps, dependency ordering, completion
  signals, and recovery.
domain: workflow
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - bld_knowledge_card_workflow
  - bld_memory_workflow
  - bld_examples_workflow
  - workflow-builder
  - p01_kc_workflow
  - p03_ins_workflow
  - bld_architecture_workflow
  - bld_collaboration_workflow
  - bld_instruction_chain
  - p03_sp_workflow-builder
---

## Quality Gate

## Definition
A workflow defines a multi-step orchestration: ordered or parallel steps, the agent assigned to each, dependencies between steps, and completion signals. Workflows must be executable by automated runners without human interpretation. This gate ensures every workflow is acyclic, complete, and safe to run end-to-end.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p12_wf_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `workflow` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `steps`, `execution`, `signals` all defined and non-empty |
| H07 | Steps list has minimum depth | `steps` contains at least 2 entries |
| H08 | Dependency graph or ordering present | Each step either declares `depends_on` or body has an explicit sequential ordering |
| H09 | Completion signals defined | `signals` field names at least one completion signal per terminal step |
| H10 | steps_count matches body | The declared step count matches the number of steps actually present in the body |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | No prose restating what the steps table shows |
| Steps have agent assignment | 1.0 | Each step names the agent or component responsible |
| Dependency graph is acyclic | 1.0 | No step depends on a step that depends on it |
| Parallel vs sequential explicit | 0.5 | `execution` is set per step or globally |
| Error recovery per step | 1.0 | Each step has `on_failure` (retry, skip, abort, or escalate) |
| Tags include workflow | 0.5 | `tags` contains `"workflow"` |
| Wave ordering for parallel steps | 1.0 | Parallel steps declare a `wave` number |
| Timeout per step | 0.5 | Each step has `timeout_ms` or inherits a workflow-level timeout |
| Rollback strategy documented | 0.5 | Body describes how to undo completed steps on later failure |
| Signal references are valid | 1.0 | `signals` field references known signal kinds |
| No prompt chaining in body | 1.0 | Orchestration only; no LLM prompt text or task instructions |
Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference workflow |
| >= 8.0 | PUBLISH — safe for automated execution in production |
| >= 7.0 | REVIEW — runnable but recovery or signal references need work |
| < 7.0 | REJECT — do not run; steps are incomplete or dependencies are ambiguous |
## Bypass
| Field | Value |
|-------|-------|
| condition | Workflow is a one-time migration or incident response procedure that will not be re-run; formal gating would delay the response |
| approver | Lead engineer or on-call responsible for the affected system |
| audit_log | Entry required in `.claude/bypasses/workflow_{date}.md` with the incident or migration ticket ID |
| expiry | Single execution only; workflow must be archived or brought to PUBLISH score before any second run |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

## Examples

# Examples: workflow-builder
## Golden Example
INPUT: "Create workflow for research-then-build mission with research_agent and builder_agent"
OUTPUT:
```yaml
id: p12_wf_research_build_mission
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "Research Then Build Mission"
steps_count: 3
execution: mixed
directors: [shaka, edison]
timeout: 5400
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_shaka_solo_research, p12_spawn_edison_solo_build]
domain: "orchestration"
quality: 8.8
tags: [workflow, research, build, multi-director]
tldr: "3-step mixed workflow: research_agent researches, builder_agent builds from findings, orchestrator consolidates"
density_score: 0.90
```
## Purpose
Orchestrates a research-then-build mission where research_agent gathers market intelligence,
builder_agent implements based on findings, and orchestrator consolidates results. Steps 1-2 are
sequential (build depends on research), step 3 runs after both complete.
## Steps
### Step 1: Market Research [shaka]
- **Agent**: shaka (sonnet)
- **Action**: Research target market and produce knowledge cards
- **Input**: research brief from handoff file
- **Output**: 3-5 knowledge cards committed to records/pool/
- **Signal**: shaka_complete with quality score
- **Depends on**: none (first step)
### Step 2: Implementation [edison]
- **Agent**: edison (opus)
- **Action**: Build feature using research findings from Step 1
- **Input**: knowledge cards produced by research_agent
- **Output**: implemented feature with tests passing
- **Signal**: edison_complete with quality score
- **Depends on**: Step 1
### Step 3: Consolidation [orchestrator]
- **Agent**: orchestrator (opus)
- **Action**: Review outputs, archive handoffs, push to remote
- **Input**: signals from Steps 1-2, git log
- **Output**: consolidated commit, archived handoffs
- **Signal**: workflow_complete
- **Depends on**: Steps 1, 2
## Dependencies
- Handoff files must exist for research_agent and builder_agent before workflow starts
- spawn_configs referenced must be valid (p12_spawn_shaka_solo_research, p12_spawn_edison_solo_build)
## Signals
- **On step complete**: {sat}_complete signal emitted (see signal-builder)
- **On workflow complete**: workflow_complete signal with aggregate quality
- **On error**: {sat}_error signal, retry per step (max 1), then escalate to orchestrator
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p12_wf_ pattern (H02 pass)
- kind: workflow (H04 pass)
- 20 required fields present (H06 pass)
- body has Purpose + Steps + Dependencies + Signals (H07 pass)
- steps_count: 3 matches actual 3 steps (H08 pass)
- Each step has Agent/Action/Input/Output/Signal/Depends (S03 pass)
- Dependencies section lists prerequisites (S05 pass)
- Signals references signal-builder conventions (S06 pass)
- No prompt chaining in body (S08 pass)
## Anti-Example
INPUT: "Create a workflow for doing stuff"
BAD OUTPUT:
```yaml
id: my_workflow
kind: flow
steps: 3
quality: 8.5
```
This workflow does research and then builds things. First research_agent does research,
then builder_agent builds. It's a great workflow that produces high quality output.
FAILURES:
1. id: no `p12_wf_` prefix -> H02 FAIL
2. kind: "flow" not "workflow" -> H04 FAIL
3. pillar: missing -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, execution, directors, domain, tags, tldr -> H06 FAIL
6. No ## Steps section with structured steps -> H07 FAIL
7. Body is filler prose ("great workflow", "high quality") -> S10 FAIL
8. Steps lack Agent/Action/Input/Output structure -> S03 FAIL
9. No Dependencies or Signals sections -> S05, S06 FAIL
10. No signal references -> S09 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
