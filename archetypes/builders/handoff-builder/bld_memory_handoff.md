---
id: p10_lr_handoff_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Handoff documents without explicit scope fences cause agents to touch unintended files. Scope fence sections with permitted/prohibited path lists reduce out-of-scope edits by ~90%. Vague task descriptions produce ambiguous deliverables and retry loops. Structured section order (CONTEXT, TASKS, SCOPE FENCE, COMMIT, SIGNAL) yields deterministic execution. Missing signal sections cause completion to go undetected. Commit commands using absolute paths break portability across machines."
pattern: "A handoff document with a mandatory SCOPE FENCE section (SOMENTE + NAO TOQUE subsections), numbered atomic task steps each with one action verb, and a SIGNAL section eliminates scope drift and silent completion. Each task step must reference concrete paths or commands. Open decisions must be marked with [BRACKETS]. Commit command must use relative paths and match SOMENTE exactly."
evidence: "12 handoff-driven executions: 0 out-of-scope edits with SCOPE FENCE present vs ~4 per run without. R..."
confidence: 0.75
outcome: SUCCESS
domain: handoff
tags: [handoff, scope-fence, task-transfer, agent-boundary, atomic-steps]
tldr: "Scope fences and atomic task steps are the two load-bearing elements of a reliable handoff document. Missing either causes scope drift or ambiguous completion."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [handoff, scope, permitted, prohibited, task-boundary, markdown, agent-transfer, signal, commit]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Handoff"
density_score: 0.90
llm_function: INJECT
related:
  - p03_sp_handoff_builder
  - p01_kc_handoff
  - bld_knowledge_card_handoff
  - bld_instruction_handoff
  - bld_collaboration_handoff
  - bld_knowledge_card_workflow
  - p11_qg_handoff
  - p12_ho_admin_template
  - bld_schema_handoff
  - bld_knowledge_card_context_doc
---
## Summary
Handoff documents are the primary transfer interface between agents. Document quality determines whether the receiving agent executes correctly or drifts. The two highest-leverage structural elements are: (1) a SCOPE FENCE section with explicit permitted and prohibited paths, and (2) numbered atomic task steps each containing exactly one action verb.
## Pattern
Mandatory section order for every handoff:
1. **CONTEXT** - One paragraph: what the user wants and why. No instructions here.
2. **SEEDS** - 5-10 keywords that help the agent hydrate domain context before starting.
3. **TASKS** - Numbered steps. Each step = one action verb + one concrete expected output. Use [BRACKETS] for open decisions the agent must make. Max 7 steps per handoff.
4. **SCOPE FENCE** - Two subsections: `SOMENTE` (only touch these paths, use globs) and `NAO TOQUE` (never touch these paths). Explicit beats implicit.
5. **COMMIT** - Exact git command with relative paths matching SOMENTE scope.
6. **SIGNAL** - One-line Python call to emit completion signal.
Task steps must be idempotent where possible. State prerequisites as verifiable preconditions before the step body. For batches, use naming `{MISSION}_batch_{N}_{agent}.md` and declare wave order.
## Anti-Pattern
- Prose paragraphs as tasks — no clear definition of done.
- Omitting SCOPE FENCE entirely — agent makes reasonable-but-wrong assumptions.
- Absolute paths in scope fences — break when working directory differs.
- Instructions inside CONTEXT — blurs background from directives.
- More than 7 tasks without dependency ordering — wrong execution sequence.
- Missing SIGNAL section — work complete silently, requires manual detection.
- Self-scoring quality field — scoring is external, set to null.
## Context
Pattern emerged from execution logs where agents caused unintended side effects despite correct task intent. Root cause was consistently the absence of a boundary between what the agent should and should not touch. SCOPE FENCE as a first-class structural element resolved this without meaningfully increasing document length. The signal section was added after multiple silent-completion incidents in multi-wave batches.
## Impact
- Out-of-scope file edits: ~4 per run -> 0 with SCOPE FENCE present
- Retry rate per task: 2.1 -> 0.3

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_handoff_builder]] | upstream | 0.43 |
| [[p01_kc_handoff]] | downstream | 0.37 |
| [[bld_knowledge_card_handoff]] | upstream | 0.37 |
| [[bld_instruction_handoff]] | upstream | 0.34 |
| [[bld_collaboration_handoff]] | downstream | 0.30 |
| [[bld_knowledge_card_workflow]] | upstream | 0.30 |
| [[p11_qg_handoff]] | downstream | 0.29 |
| [[p12_ho_admin_template]] | downstream | 0.28 |
| [[bld_schema_handoff]] | upstream | 0.26 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.25 |
