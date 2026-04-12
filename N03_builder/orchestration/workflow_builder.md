---
id: p12_wf_builder_construction
kind: workflow
pillar: P12
title: "Builder Workflows — Single Artifact, Batch, AutoResearch"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 9.0
tags: [workflow, builder, N03, 8F, construction, pipeline, batch]
tldr: "3 builder workflows — single artifact (8F), batch construction, and AutoResearch loop — with concrete tool commands."
steps_count: 8
execution: sequential
agent_groups: [builder]
timeout: 1800
retry_policy: per_step
depends_on: [dispatch_rule_builder]
signals: [complete, error, progress]
spawn_configs: [spawn_config_builder]
density_score: 0.95
---

# Builder Workflows

## Purpose

Three workflows that N03 Builder executes. Single Artifact for one-off builds,
Batch Construction for multiple artifacts in sequence, and AutoResearch for
autonomous improvement loops. All workflows use the 8F pipeline.

## Workflow A: Single Artifact (8F Pipeline)

Build one artifact from intent to compiled output.

### Step 1: Read Handoff [builder]
- **Action**: Read `.cex/runtime/handoffs/n03_task.md`
- **Action**: Read decision manifest if referenced
- **Output**: Task understanding + scope fence
- **Depends on**: N07 handoff exists

### Step 2: F1 CONSTRAIN [builder]
- **Action**: Resolve intent to kind + pillar
- **Command**: `python _tools/cex_query.py "{intent}"`
- **Output**: kind name, pillar code, schema path
- **Depends on**: Step 1

### Step 3: F2 BECOME [builder]
- **Action**: Load 13 builder ISOs
- **Command**: `python _tools/cex_skill_loader.py {kind}`
- **Output**: Builder persona + constraints absorbed
- **Depends on**: Step 2

### Step 4: F3 INJECT [builder]
- **Action**: Load brand config, memory, linked artifacts
- **Command**: `python _tools/cex_memory_select.py "{kind}"`
- **Output**: Full context assembled
- **Depends on**: Step 3

### Step 5: F4 REASON [builder]
- **Action**: Plan artifact structure
- **GDP gate**: If subjective decisions needed → check decision manifest
- **Output**: Structural plan
- **Depends on**: Step 4

### Step 6: F5 CALL + F6 PRODUCE [builder]
- **Action**: Enrich with tools, generate artifact with frontmatter
- **Output**: `{path}/artifact.md` with valid YAML frontmatter
- **Constraint**: `quality: null` always, body under max_bytes
- **Depends on**: Step 5

### Step 7: F7 GOVERN [builder]
- **Action**: Validate frontmatter, check schema compliance
- **Command**: `python _tools/cex_hooks.py {path}`
- **Output**: PASS or FAIL with error details
- **Depends on**: Step 6

### Step 8: F8 COLLABORATE [builder]
- **Action**: Compile, commit, signal
- **Commands**:
  - `python _tools/cex_compile.py {path}`
  - `git add {path} && git commit -m "[N03] {description}"`
  - `python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"`
- **Output**: Compiled .yaml + git commit + signal
- **Depends on**: Step 7 PASS

## Workflow B: Batch Construction

Multiple artifacts in sequence, committing every 3-4 files.

### Execution
1. Read batch intent file or handoff with multiple targets
2. For each artifact: execute Workflow A (Steps 2-7)
3. After every 3-4 artifacts: execute Step 8 (commit batch)
4. Final signal after all artifacts complete

### Commands
```bash
python _tools/cex_batch.py --file intents.txt --nucleus n03
```

## Workflow C: AutoResearch Loop

Autonomous artifact improvement — evolve existing artifacts.

### Execution
1. Scan target artifacts for quality scores and gaps
2. For each artifact below threshold: plan improvement
3. Execute 8F pipeline with existing artifact as context (F3 INJECT)
4. Compare old vs new — keep if improved, discard if not
5. Commit improved artifacts, signal complete

### Commands
```bash
python _tools/cex_evolve.py --path {artifact_path} --threshold 8.5
```

## Error Recovery

| Error | Recovery |
|-------|----------|
| Schema validation fails | Fix frontmatter, retry from F7 |
| Compile error | Fix YAML syntax, re-compile |
| Kind not found | Ask N07 for intent clarification |
| GDP gate blocks | Read decision manifest or signal N07 |

## References

- Dispatch rule: N03_builder/orchestration/dispatch_rule_builder.md
- Quality gate: N03_builder/quality/quality_gate_builder.md
- N07 workflow: N07_admin/orchestration/workflow_admin.md
