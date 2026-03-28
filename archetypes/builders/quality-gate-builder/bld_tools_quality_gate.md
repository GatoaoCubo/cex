---
kind: tools
id: bld_tools_quality_gate
pillar: P04
llm_function: CALL
purpose: Tools available for quality_gate production
---

# Tools: quality-gate-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing quality_gates | Phase 1 (check duplicates) | CONDITIONAL |
| validate_kc.py | Reference pattern for HARD/SOFT gates | Design time | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |

## Reference Gates (existing)
| Gate | File | Domain |
|------|------|--------|
| CEX Quality Gate | P11_feedback/examples/p11_qg_cex_quality.md | Pre-commit |
| Shokunin Pool Gate | P11_feedback/examples/p11_qg_shokunin_pool.md | Pool entry |
| TDD Compliance | P11_feedback/examples/p11_qg_tdd_compliance.md | Testing |
