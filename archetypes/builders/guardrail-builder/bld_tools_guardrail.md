---
kind: tools
id: bld_tools_guardrail
pillar: P04
llm_function: CALL
purpose: Tools available for guardrail production
---

# Tools: guardrail-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing guardrails | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P11_feedback/_schema.yaml | Field definitions for guardrail |
| CEX Examples | P11_feedback/examples/ | Existing guardrail artifacts |
| CEX Laws | records/framework/docs/LAWS_v3_PRACTICAL.md | Operational laws (boundary reference) |
| OWASP LLM Top 10 | owasp.org | Security risk categories |
| SEED_BANK | archetypes/SEED_BANK.yaml | P11_guardrail seeds |
## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p11_gr_ prefix
- [ ] severity in [critical, high, medium, low]
- [ ] enforcement in [block, warn, log]
- [ ] Rules are concrete and enforceable
