---
kind: knowledge_card
id: bld_knowledge_card_handoff
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for handoff production — task delegation packaging
sources: orchestration patterns, delegation protocols, mission briefing design
---

# Domain Knowledge: handoff
## Executive Summary
Handoffs are self-contained delegation packages that tell a agent_node WHAT to do, with what context, within what scope, and how to commit and signal completion. They are instructions consumed by execution engines — not events (signals), not routing policies (dispatch rules), and not runtime orchestration (workflows). A handoff must be self-contained: the agent_node needs no external context.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| llm_function | COLLABORATE |
| Max size | 4096 bytes |
| Naming | p12_ho_{task}.md |
| Required body sections | Context, Tasks, Scope Fence, Commit, Signal |
| Autonomy levels | full, supervised, assisted |
| Key fields | agent_node, mission, autonomy, quality_target |
## Patterns
- **Autonomy levels**: define how independently the agent_node operates
| Level | Behavior | Use case |
|-------|----------|----------|
| full | Satellite decides all implementation details | Trusted, well-defined tasks |
| supervised | Checks back on key decisions | Complex tasks with trade-offs |
| assisted | Follows precise instructions, minimal deviation | Critical or risky tasks |
- **Five body sections**: each serves a specific purpose
| Section | Content | Rule |
|---------|---------|------|
| Context | WHY this work is needed | 2-4 sentences, motivation only |
| Tasks | WHAT to do | Numbered steps, action verbs |
| Scope Fence | WHERE allowed/forbidden | SOMENTE + NAO TOQUE paths |
| Commit | HOW to save work | Exact git add + commit commands |
| Signal | HOW to report completion | Signal writer call or file |
- **Self-contained**: agent_node needs no external context — everything is in the handoff
- **Scope fence**: explicitly lists allowed paths AND forbidden paths — prevents agent_node from touching wrong files
- **Action verb tasks**: every task starts with an action verb (create, read, validate, write)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague tasks ("do your best") | Satellite has no clear objective |
| Missing scope fence | Satellite modifies wrong files |
| External context required | Satellite fails when context unavailable |
| No commit section | Work done but not saved; lost on session end |
| No signal section | Orchestrator cannot detect completion |
| Over 4096 bytes | Too complex; split into multiple handoffs |
## Application
1. Define mission and agent_node assignment
2. Write context: 2-4 sentences on WHY this work is needed
3. List tasks: numbered, action-verb-first, specific deliverables
4. Set scope fence: SOMENTE (allowed) + NAO TOQUE (forbidden) paths
5. Write commit: exact git commands for saving work
6. Write signal: completion notification mechanism
## References
- Military briefing: OPORD (Operations Order) structure
- Agile: user story + acceptance criteria oflegation pattern
- Orchestration: task delegation and completion signaling protocols
- CI/CD: pipeline stage handoff and artifact passing
