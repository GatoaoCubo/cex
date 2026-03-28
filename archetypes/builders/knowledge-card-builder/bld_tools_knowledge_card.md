---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for knowledge_card production
---

# Tools: knowledge-card-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| validate_kc.py | Validate KC: 10 HARD + 20 SOFT gates | Phase 3 | CONDITIONAL |
| brain_query [MCP] | Search existing KCs in pool | Phase 1 | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | — | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alt compose | [PLANNED] |

## validate_kc.py Usage
```bash
# Single file
python _tools/validate_kc.py path/to/p01_kc_topic.md

# Directory (batch)
python _tools/validate_kc.py P01_knowledge/examples/ --summary

# JSON output (machine-readable)
python _tools/validate_kc.py path/to/file.md --json
```

Output: HARD pass/fail + SOFT score 0-10 + verdict.
Fix suggestions provided for failed gates.

## brain_query Usage
```python
brain_query("knowledge card about {topic}")
# Returns: existing KCs matching topic
# Purpose: avoid duplicates, find linked_artifacts
```

## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P01_knowledge/_schema.yaml | KC field definitions |
| CEX Examples | P01_knowledge/examples/ | 63+ real KCs |
| CEX Template | P01_knowledge/templates/tpl_knowledge_card.md | Fillable template |
| CEX Pool | records/pool/ (source repository) | 1957+ published artifacts |

## Interim Validation
validate_kc.py is ACTIVE — always run before committing.
No manual gate-checking needed (unlike model-card-builder).
