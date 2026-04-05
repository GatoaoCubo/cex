---
kind: manifest
id: bld_manifest_memory_type
pillar: P02
llm_function: BECOME
created: 2026-04-05
---

# Manifest: memory-type-builder

- **Kind**: memory_type
- **Pillar**: P10 (Memory)
- **Function**: INJECT
- **Builder**: memory-type-builder
- **ISOs**: 13
- **Status**: active
- **Dependencies**: cex_memory_types.py, cex_memory_age.py, cex_memory_update.py
- **Produces**: p10_mt_*.md artifacts (compiled to .yaml)
