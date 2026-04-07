---
kind: tools
id: bld_tools_guardrail
pillar: P04
llm_function: CALL
purpose: Tools available for guardrail production
quality: 9.0
title: "Tools Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
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
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p11_gr_ prefix
3. [ ] severity in [critical, high, medium, low]
4. [ ] enforcement in [block, warn, log]
5. [ ] Rules are concrete and enforceable

## Metadata

```yaml
id: bld_tools_guardrail
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-guardrail.md
```
