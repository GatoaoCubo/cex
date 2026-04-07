---
kind: tools
id: bld_tools_axiom
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for axiom production
quality: 9.1
title: "Tools Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: axiom-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing axioms in pool | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for P10 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: rule, rationale, scope, enforcement |
| Existing axioms | P10_memory/examples/ | Reference artifacts |
| Builder Norms | archetypes/builders/BUILDER_NORMS.md | 12 mandatory rules |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
1. [ ] YAML frontmatter parses without error
2. [ ] id matches `p10_ax_` pattern
3. [ ] kind == "axiom"
4. [ ] quality == null
5. [ ] rule is ONE atomic sentence
6. [ ] scope names concrete domain boundary
7. [ ] density >= 0.80 (no filler phrases)

## Metadata

```yaml
id: bld_tools_axiom
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-axiom.md
```
