---
kind: config
id: bld_config_workflow
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
---
# Config: workflow Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_wf_{name_slug}.md` | `p12_wf_research_build_mission.md` |
| Builder directory | kebab-case | `workflow-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `retry_policy` |
| Name slug | snake_case, lowercase | `research_build_mission`, `content_pipeline` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P12_orchestration/examples/p12_wf_{name_slug}.md`
- Compiled: `cex/P12_orchestration/compiled/p12_wf_{name_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~5000 bytes
- Density: >= 0.80
## Execution Enum
| Value | When to use | Example |
|-------|-------------|---------|
| sequential | Steps must run in order (each depends on prior) | Research -> Build -> Deploy |
| parallel | Steps are independent, run simultaneously | 3 agent_nodes researching different topics |
| mixed | Some steps parallel, some sequential (wave pattern) | Wave 1: [A, B] parallel, then Wave 2: C |
## Retry Policy Enum
| Value | When to use | Example |
|-------|-------------|---------|
| none | Steps are not retried on failure | One-shot operations |
| per_step | Failed step retried individually (max 1) | API calls, transient errors |
| global | Entire workflow retried from start | Idempotent missions |
## Step Structure Requirements
- Agent: agent_node name (lowercase) or "stella" for orchestrator steps
- Action: 1-sentence description of what the step does
- Input: what the step receives (from prior step or external)
- Output: what the step produces (for next step or final output)
- Signal: signal emitted on completion (reference signal-builder)
- Depends on: list of step numbers or "none"
