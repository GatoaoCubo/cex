---
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to handoff production
---

# Tools: handoff-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Search for existing handoffs and related artifacts | Phase 1 | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
| `signal_writer.py` | Signal completion mechanism referenced in handoffs | Signal section | CONDITIONAL |

## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, limits |
| Handoff template | `P12_orchestration/templates/tpl_handoff.md` | human reference |
| Handoff directory | `.claude/handoffs/` | primary output location |
| Compiled output | `P12_orchestration/compiled/p12_ho_{task}.md` | secondary output |

## Interim Validation
Until a generic validator exists, validate manually:
- filename matches `p12_ho_{task}.md`
- YAML frontmatter parses
- required fields present
- autonomy in enum (`full`, `supervised`, `assisted`)
- all 5 body sections exist
- scope fence has SOMENTE + NAO TOQUE
- payload fits `handoff`, not `action_prompt` or `signal`
- size <= 4096 bytes
