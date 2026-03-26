---
lp: P04
llm_function: CALL
purpose: Tools and APIs available for knowledge_card production
---

# Tools: knowledge-card-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| validate_kc.py | Validate KC against 10 HARD + 20 SOFT gates | Phase 3 | ACTIVE |
| brain_query | Search existing KCs in pool, check duplicates | Phase 1 | ACTIVE |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## validate_kc.py Usage
```bash
# Single file
python _tools/validate_kc.py P01_knowledge/examples/p01_kc_topic.md

# Directory (batch)
python _tools/validate_kc.py P01_knowledge/examples/ --summary

# JSON output (machine-readable)
python _tools/validate_kc.py P01_knowledge/examples/ --json
```

## Gate Architecture (validate_kc.py v2.0)
| Gate | Severity | Check |
|------|----------|-------|
| H01 | HARD | Valid YAML frontmatter |
| H02 | HARD | id == filename stem |
| H03 | HARD | id matches p##_kc_ pattern |
| H04 | HARD | type == knowledge_card |
| H05 | HARD | quality == null |
| H06 | HARD | 12 required fields present (excl quality) |
| H07 | HARD | tags is list |
| H08 | HARD | body 200-5120 bytes |
| H09 | HARD | no internal paths (records/, .claude/) |
| H10 | HARD | author != STELLA |
| S01-S20 | SOFT | See QUALITY_GATES.md |

## Data Sources
| Source | What | When |
|--------|------|------|
| Official docs | Provider documentation, specs | Domain KCs |
| Code analysis | Pattern extraction from codebase | Meta KCs |
| Pool KCs (63+) | Reference examples, linked_artifacts | Phase 1 |
| _schema.yaml | Field definitions, constraints | Phase 2 |
