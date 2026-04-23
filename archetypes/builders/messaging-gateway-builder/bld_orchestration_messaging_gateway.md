---
kind: collaboration
id: bld_collaboration_messaging_gateway
pillar: P12
llm_function: COLLABORATE
purpose: F8 COLLABORATE protocol for messaging_gateway builder -- save, compile, commit, signal
pattern: Standard CEX F8 with gateway-specific file set and signal format
quality: 8.6
title: "Collaboration: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, collaboration, p12, hermes_origin]
tldr: "F8: compile 19 files, doctor check, git add targeted paths, commit [N03] HERMES W1.2, signal mission=HERMES_W1_messaging_gateway."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_tools_kind
  - bld_examples_handoff
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_collaboration_builder
  - p04_ct_validate_builder
  - bld_tools_builder
  - wave2_quality_report
  - bld_instruction_kind
---

# Collaboration: messaging_gateway Builder

## F8 COLLABORATE Steps (in order)

### Step 1: Verify Deliverables
All 19 files must exist before proceeding:
```
N00_genesis/P04_tools/kind_messaging_gateway/kind_manifest_n00.md
N00_genesis/P04_tools/tpl_messaging_gateway.md
N00_genesis/P01_knowledge/library/kind/kc_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_manifest_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_instruction_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_system_prompt_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_schema_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_examples_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_architecture_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_config_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_knowledge_card_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_memory_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_output_template_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_quality_gate_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_tools_messaging_gateway.md
archetypes/builders/messaging-gateway-builder/bld_collaboration_messaging_gateway.md
.claude/agents/messaging-gateway-builder.md
.cex/kinds_meta.json (patched with messaging_gateway entry)
N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md (P04 section updated)
```

### Step 2: Validate JSON
```bash
python -m json.tool .cex/kinds_meta.json > /dev/null && echo "[OK] JSON valid"
```

### Step 3: Compile
```bash
python _tools/cex_compile.py --all
```

### Step 4: Doctor Check
```bash
python _tools/cex_doctor.py
```

### Step 5: Git Commit
```bash
git add N00_genesis/P04_tools/kind_messaging_gateway/ \
        N00_genesis/P04_tools/tpl_messaging_gateway.md \
        N00_genesis/P01_knowledge/library/kind/kc_messaging_gateway.md \
        archetypes/builders/messaging-gateway-builder/ \
        .claude/agents/messaging-gateway-builder.md \
        .cex/kinds_meta.json \
        N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md
git commit -m "[N03] HERMES W1.2: messaging_gateway archetype (stub, 6 platforms, 13 ISOs)"
```

### Step 6: Signal
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, mission='HERMES_W1_messaging_gateway')"
```

## Downstream Consumers
| Consumer | What they get | When |
|----------|--------------|------|
| N05 Operations | messaging-gateway-builder ISOs to scaffold deployments | Wave 3 |
| N07 Orchestrator | complete signal -> dispatch next wave | Immediately after signal |
| .claude/agents/ sub-agent system | messaging-gateway-builder.md for dispatch | Available immediately |
| cex_retriever.py | 16 new documents indexed | After cex_compile --all |

## Signal Format
```json
{
  "nucleus": "n03",
  "status": "complete",
  "score": 9.0,
  "mission": "HERMES_W1_messaging_gateway",
  "timestamp": "2026-04-18T...",
  "deliverables": 19
}
```

## Rollback (if needed)
```bash
git revert HEAD  # revert the W1.2 commit
# No kinds_meta.json surgery needed -- git tracks the full file
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | upstream | 0.43 |
| [[bld_examples_handoff]] | upstream | 0.41 |
| [[bld_architecture_kind]] | upstream | 0.38 |
| [[kind-builder]] | upstream | 0.37 |
| [[bld_collaboration_kind]] | sibling | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.32 |
| [[p04_ct_validate_builder]] | upstream | 0.28 |
| [[bld_tools_builder]] | upstream | 0.27 |
| [[wave2_quality_report]] | upstream | 0.24 |
| [[bld_instruction_kind]] | upstream | 0.23 |
