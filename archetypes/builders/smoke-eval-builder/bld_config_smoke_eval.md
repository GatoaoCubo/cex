---
kind: config
id: bld_config_smoke_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for smoke_eval production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: smoke_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_se_{scope_slug}.md | p07_se_brain_mcp.md |
| Builder dir | kebab-case | smoke-eval-builder/ |
| Fields | snake_case | critical_path, fast_fail |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/p07_se_{scope_slug}.md
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes (smaller than unit_eval)
- Density: >= 0.80
- Timeout: MUST be <= 30 seconds (non-negotiable)
## Fast-Fail Policy
- fast_fail: always true (smoke tests abort on first failure)
- No partial pass — either all checks pass or test fails
- On failure: log which check failed, suggest remediation
