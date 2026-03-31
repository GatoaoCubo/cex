---
kind: tools
id: bld_tools_builder
pillar: P04
llm_function: CALL
purpose: Tools, APIs, and data sources for the meta-builder
---
# Tools: _builder-builder

## CEX Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_schema_hydrate.py | Hydrate universal fields | After ISO generation |
| cex_compile.py | .md → .yaml compilation | After save |
| cex_doctor.py | Builder health check (13 ISOs, sizes) | After build |
| cex_hooks.py | Pre/post validation | Before commit |
| cex_materialize.py | Builder ISOs → sub-agent .md | After builder complete |
| cex_score.py | 5D quality scoring | Peer review |
| signal_writer.py | Inter-nucleus signals | After complete |

## Data Sources
| Source | Path | Data |
|--------|------|------|
| Meta-templates (13) | archetypes/builders/_builder-builder/bld_meta_*.md | ISO templates |
| TAXONOMY_LAYERS | archetypes/TAXONOMY_LAYERS.yaml | Kind→pillar mapping |
| KIND_META | .cex/kinds_meta.json | Kind registry |
| bld_norms | archetypes/builders/bld_norms.md | 23 validation rules |
| SEED_BANK | archetypes/SEED_BANK.yaml | Builder seeds |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
