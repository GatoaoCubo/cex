---
id: p11_tools_curation_nudge
kind: toolkit
pillar: P04
llm_function: CALL
purpose: F5 CALL tools for curation_nudge builder
quality: 8.3
title: "Tools: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [tools, curation_nudge, builder, p04, memory, hermes]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F5 CALL tools for curation_nudge builder"
density_score: 0.87
related:
  - bld_tools_model_architecture
  - bld_tools_training_method
  - doctor
  - bld_tools_kind
  - p11_qg_knowledge
  - bld_tools_memory_architecture
  - bld_tools_consolidation_policy
  - skill
  - bld_manifest_memory_type
  - bld_tools_agent_computer_interface
---

## Tool Inventory (F5 CALL)

### Build Tools

| Tool | Command | When |
|------|---------|------|
| Compile | `python _tools/cex_compile.py {path}` | After writing artifact |
| Doctor | `python _tools/cex_doctor.py` | After compilation to verify |
| Retriever | `python _tools/cex_retriever.py --kind curation_nudge` | F3: find similar nudges |
| Memory select | `python _tools/cex_memory_select.py` | F3: inject relevant memory |

### Validation Tools

| Tool | Command | When |
|------|---------|------|
| Schema check | `python _tools/cex_hooks.py validate {path}` | Before F7 GOVERN |
| Quality score | `python _tools/cex_score.py {path}` | F7 GOVERN scoring |
| Sanitize | `python _tools/cex_sanitize.py --check {path}` | Pre-commit gate |

### Discovery Tools

```bash
# Find existing curation_nudge artifacts
python _tools/cex_retriever.py --kind curation_nudge

# Discover related memory builders
python _tools/cex_query.py "memory persistence nudge proactive"

# Check builder health
python _tools/cex_doctor.py --builder curation-nudge-builder
```

### F3 INJECT Tool Sequence

```bash
# 1. Load KC for domain knowledge
cat N00_genesis/P01_knowledge/library/kind/kc_curation_nudge.md

# 2. Find similar existing nudges for reference
python _tools/cex_retriever.py --kind curation_nudge --top 3

# 3. Load builder ISOs
ls archetypes/builders/curation-nudge-builder/

# 4. Load memory context
python _tools/cex_memory_select.py --query "curation nudge memory persistence"
```

### Runtime Integration

```python
# Programmatic nudge evaluation (agent session loop)
def evaluate_nudge(nudge_config, session_state):
    trigger = nudge_config["trigger"]
    cadence = nudge_config["cadence"]

    if session_state["nudge_count"] >= cadence["max_per_session"]:
        return None  # cap reached

    turns_since_last = session_state["turns_since_last_nudge"]
    if turns_since_last < cadence["min_interval_turns"]:
        return None  # anti-spam

    if trigger["type"] == "turn_count":
        if session_state["turn_count"] % trigger["threshold"] == 0:
            return nudge_config["prompt_template"]

    return None
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_architecture]] | related | 0.34 |
| [[bld_tools_training_method]] | related | 0.32 |
| [[doctor]] | downstream | 0.31 |
| [[bld_tools_kind]] | related | 0.31 |
| [[p11_qg_knowledge]] | downstream | 0.30 |
| [[bld_tools_memory_architecture]] | related | 0.29 |
| [[bld_tools_consolidation_policy]] | related | 0.29 |
| [[skill]] | downstream | 0.27 |
| [[bld_manifest_memory_type]] | upstream | 0.27 |
| [[bld_tools_agent_computer_interface]] | related | 0.27 |
