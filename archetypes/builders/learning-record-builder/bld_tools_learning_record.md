---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for learning_record production
---

# Tools: learning-record-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing learning_records | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| memory_bridge.py | Sync learning to CODEXA memory | Post-production | ACTIVE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for P10 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: topic, outcome, pattern, score |
| Learning memory | records/core/learning/memory/ | Existing patterns |
| Signal history | .claude/signals/ | Satellite completion signals |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
- [ ] YAML frontmatter parses without error
- [ ] id matches `p10_lr_` pattern
- [ ] kind == "learning_record"
- [ ] quality == null
- [ ] outcome in [SUCCESS, PARTIAL, FAILURE]
- [ ] score is numeric 0.0-10.0
- [ ] pattern section has concrete steps (not vague advice)
