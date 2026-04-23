---
quality: 8.2
quality: 7.8
kind: tools
id: bld_tools_terminal_backend
pillar: P04
llm_function: CALL
purpose: Tools used by terminal_backend builder during 8F pipeline
title: "Tools Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, tools]
tldr: "Builder tools: cex_compile, cex_doctor, kinds_meta lookup, secret_config reference checker"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.88
related:
  - bld_tools_kind
  - p11_qg_knowledge
  - doctor
  - p11_qg_artifact
  - p04_ct_cex_compile
  - bld_tools_model_architecture
  - skill
  - p01_kc_cex_tooling_master
  - p11_qg_admin_orchestration
  - bld_tools_knowledge_graph
---

## Tools Used in Pipeline
| Tool | Phase | Purpose |
|------|-------|---------|
| `python _tools/cex_compile.py {path}` | F8 | Compile .md -> .yaml |
| `python _tools/cex_doctor.py` | F8 | Health check after build |
| `python -m json.tool .cex/kinds_meta.json` | F7 | Validate kinds_meta JSON after patch |
| `python _tools/cex_retriever.py terminal_backend` | F3 | Find similar artifacts for context |
| `grep -r "terminal_backend" archetypes/` | F3 | Check for prior examples |

## F5 Tool Checklist
```bash
# Verify kinds_meta has terminal_backend entry
python -c "import json; d=json.load(open('.cex/kinds_meta.json')); print('terminal_backend' in d)"

# Compile the new artifact
python _tools/cex_compile.py N00_genesis/P09_config/kind_terminal_backend/

# Doctor check
python _tools/cex_doctor.py --quick

# Validate schema patch
python -m json.tool .cex/kinds_meta.json > /dev/null && echo "JSON valid"
```

## Secret Config Integration
When `auth.method != none`, the builder should verify the referenced secret_config exists:

```bash
grep -r "id: {{secret_ref}}" N00_genesis/P09_config/ .cex/
```

If not found, N03 creates a stub secret_config artifact or documents the requirement.

## Signal Tool
```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', 9.0, mission='HERMES_W1_terminal_backend')
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | sibling | 0.33 |
| [[p11_qg_knowledge]] | downstream | 0.30 |
| [[doctor]] | downstream | 0.30 |
| [[p11_qg_artifact]] | downstream | 0.29 |
| [[p04_ct_cex_compile]] | related | 0.28 |
| [[bld_tools_model_architecture]] | sibling | 0.27 |
| [[skill]] | downstream | 0.26 |
| [[p01_kc_cex_tooling_master]] | upstream | 0.25 |
| [[p11_qg_admin_orchestration]] | downstream | 0.25 |
| [[bld_tools_knowledge_graph]] | sibling | 0.25 |
