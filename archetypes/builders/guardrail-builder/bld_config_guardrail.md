---
kind: config
id: bld_config_guardrail
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for guardrail production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: guardrail Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_gr_{scope_slug}.md | p11_gr_destructive_commands.md |
| Builder dir | kebab-case | guardrail-builder/ |
| Fields | snake_case | bypass_approver, applies_to |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P11_feedback/examples/p11_gr_{scope_slug}.md
- Compiled: cex/P11_feedback/compiled/p11_gr_{scope_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
## Severity-Enforcement Matrix
| Severity | Default enforcement | Bypass allowed |
|----------|-------------------|----------------|
| critical | block | Yes, orchestrator only |
| high | block | Yes, satellite chief |
| medium | warn | Yes, any senior agent |
| low | log | Yes, any agent |
