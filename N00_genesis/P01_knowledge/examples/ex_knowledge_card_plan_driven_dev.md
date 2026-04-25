---
id: p01_kc_plan_driven_dev
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Plan-Driven Development — Plans as Executable Prompts for Sub-Agents"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: engineering_process
quality: 9.1
tags: [plan-driven, subagent, task-granularity, tdd, execution-plan]
tldr: "Plans are prompts: 2-5 min tasks with exact paths, verification steps, and TDD — directly executable by sub-agents without human interpretation"
when_to_use: "Decomposing features into sub-agent-executable tasks or reviewing plan quality before dispatch"
keywords: [plan-driven-development, subagent-execution, task-decomposition, implementation-plan]
long_tails:
  - "How to write implementation plans that sub-agents can execute autonomously"
  - "What granularity should tasks have for LLM sub-agent execution"
axioms:
  - "ALWAYS write explicit verification for each task"
  - "NEVER create tasks longer than 5 minutes of execution"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become, p01_kc_cex_function_reason]
density_score: null
data_source: "https://martinfowler.com/bliki/TestDrivenDevelopment.html"
related:
  - kc_workflow_run_crate
  - p10_mem_benchmark_suite_builder
  - p01_kc_action_prompt
  - p01_kc_handoff
  - action-prompt-builder
  - kc_n07_orchestrator
  - p03_pt_orchestration_task_dispatch
  - continuous_batching_report
  - bld_instruction_benchmark_suite
  - bld_collaboration_instruction
---

## Summary

Plan-driven development treats plans as executable prompts, not design documents.
Each 2-5 minute task contains exact paths, complete code, verification steps and explicit dependencies.
Complete cycle: brainstorm -> write-plan -> execute-plan -> verify.
Target audience: "junior engineer with no context and no judgment" -- if the plan is not clear for this profile, it is not ready.
Two execution modes: subagent-driven (parallel, no human intervention) and sequential (fallback with human checkpoints).

## Spec

| Aspect | Value | Reason |
|--------|-------|--------|
| Granularity | 2-5 min per task | Larger tasks cause drift |
| Fields per task | paths, code, verification, deps | Sub-agent does not infer context |
| Audience | Junior with no context | Forces maximum clarity |
| TDD | Mandatory | Tests first, always |
| Status contract | DONE, CONCERNS, BLOCKED, NEEDS_CTX | Standard post-task protocol |
| Parallel mode | 1 sub-agent per task | Fast for independent tasks |
| Sequential mode | Fallback without sub-agents | Human checkpoints per batch |
| Plan output | plans/YYYY-MM-DD-topic.md | Traceable by date and topic |
| Pre-exec review | Mandatory | Granularity + deps + verifications |

Design principles: mandatory TDD, ruthless YAGNI, DRY in design, isolation for parallelism. Plan must be critically reviewed before execution -- tasks with correct granularity, clear dependencies, testable verifications, and existing file paths or with a creation task.

## Patterns

| Trigger | Action |
|---------|--------|
| Feature approved | Brainstorm -> design doc -> executable plan |
| Task involves code | Write RED test before implementing |
| Tasks without mutual dependency | Dispatch in parallel via sub-agents |
| Plan ready | Review: granularity, deps, verifications |
| Sub-agent reports BLOCKED | Stop chain, resolve external dependency |
| Insufficient context | Sub-agent returns NEEDS_CONTEXT (does not invent) |

## Code

<!-- lang: python | purpose: plan-to-prompt conversion for subagent dispatch -->
```python
# Controller converte task do plano em prompt executavel
def task_to_prompt(task, plan):
    dep = plan.get_task(task.depends_on)
    return f"""You are implementing Task {task.id}: {task.name}.

    **Task Description**
    {task.full_text}

    **Context**
    Follows Task {dep.id} ({dep.summary}).
    Files: {', '.join(task.file_paths)}

    **Your Job**
    1. Write failing tests first (TDD)
    2. Implement exactly what the task specifies
    3. Run verification: {task.verification}
    4. Commit with message: "{task.commit_msg}"
    5. Report: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT"""

# Dispatch: paralelo para independentes, sequencial para dependentes
for batch in plan.dependency_batches():
    results = parallel_execute(
        [task_to_prompt(t, plan) for t in batch],
        tools=["read", "write", "edit", "bash"]
    )
    if any(r.status == "BLOCKED" for r in results):
        escalate(blocked=[r for r in results if r.status == "BLOCKED"])
    for r in results:
        if r.status == "DONE_WITH_CONCERNS":
            log_concerns(r.task_id, r.concerns)
```

Typical flow: plan loader reads `.md` file, parser extracts tasks with metadata (files, deps, verification), dispatcher groups by dependency into batches, executor dispatches entire batch in parallel. Each task result feeds the next wave context.

## Anti-Patterns

- Plan as design doc without executable steps (sub-agent does not know what to do)
- Tasks of 30+ minutes (loss of focus, drift from objective)
- Missing verification ("implement X" without "confirm via Y")
- Skipping brainstorming and going straight to plan (unvalidated design)
- Referencing nonexistent files without a prior creation task

## References

- source: https://martinfowler.com/bliki/TestDrivenDevelopment.html
- source: https://docs.anthropic.com/en/docs/agents-and-tools
- related: p01_kc_cex_function_become
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_workflow_run_crate]] | related | 0.24 |
| [[p10_mem_benchmark_suite_builder]] | downstream | 0.24 |
| [[p01_kc_action_prompt]] | sibling | 0.24 |
| [[p01_kc_handoff]] | sibling | 0.23 |
| [[action-prompt-builder]] | downstream | 0.23 |
| [[kc_n07_orchestrator]] | sibling | 0.22 |
| [[p03_pt_orchestration_task_dispatch]] | downstream | 0.22 |
| [[continuous_batching_report]] | related | 0.21 |
| [[bld_instruction_benchmark_suite]] | downstream | 0.20 |
| [[bld_collaboration_instruction]] | downstream | 0.18 |
