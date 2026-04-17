---
kind: tools
id: bld_tools_kind
pillar: P04
llm_function: CALL
purpose: Tools and data sources available for builder package production
quality: 9.2
title: "Tools Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, tools, meta-builder]
tldr: "Tools for kind-builder: kinds_meta.json lookup, cex_compile, cex_score, cex_skill_loader, cex_doctor."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Tools: kind-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| kinds_meta.json lookup | Read target kind metadata (pillar, naming, max_bytes, llm_function, boundary) | Phase 1 (discover) | AVAILABLE |
| cex_compile.py | Compile produced ISOs to validate structure | Phase 4 (validate) | AVAILABLE |
| cex_score.py | Score produced ISOs against quality gates | Phase 4 (validate) | AVAILABLE |
| cex_skill_loader.py | Verify the 13-ISO package loads correctly | Phase 4 (validate) | AVAILABLE |
| cex_doctor.py | Run health check on the builder directory | Phase 4 (validate) | AVAILABLE |
| cex_materialize.py | Generate sub-agent .md from builder ISOs | Phase 3 (produce) | AVAILABLE |
| cex_retriever.py | Find similar existing builders for reference | Phase 2 (reference) | AVAILABLE |

## Data Sources

| Source | Path | Data |
|--------|------|------|
| Kind registry | .cex/kinds_meta.json | All 130+ kinds with pillar, naming, max_bytes, llm_function |
| Pillar schemas | P{01-12}_*/_schema.yaml | Field definitions per pillar, sibling kinds |
| Knowledge cards | P01_knowledge/library/kind/kc_{kind}.md | Domain knowledge per kind |
| Reference builders | archetypes/builders/{kind}-builder/ | Complete builder packages (13 ISOs each) |
| Sub-agent defs | .claude/agents/{kind}-builder.md | Existing sub-agent definitions |
| Shared ISOs | archetypes/builders/_shared/ | Cross-builder shared skills and patterns |
| Builder registry | archetypes/builders/ | All existing builder directories |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | No tools blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Key Lookups

### kinds_meta.json entry structure

```json
{
  "env_config": {
    "pillar": "P09",
    "description": "Environment variable specification with scope and validation",
    "naming": "p09_env_{scope_slug}.yaml",
    "max_bytes": 4096,
    "core": false,
    "llm_function": "GOVERN",
    "boundary": "Variable catalog. NOT a boot_config or feature_flag."
  }
}
```

### Builder directory discovery

```bash
ls archetypes/builders/ | grep -c builder  # count existing builders
ls archetypes/builders/{kind}-builder/     # check if target exists
```

### Validation commands

```bash
python _tools/cex_compile.py archetypes/builders/{kind}-builder/
python _tools/cex_doctor.py --scope archetypes/builders/{kind}-builder/
python _tools/cex_score.py --apply archetypes/builders/{kind}-builder/bld_manifest_{kind}.md
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_kind
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_kind.md
```
