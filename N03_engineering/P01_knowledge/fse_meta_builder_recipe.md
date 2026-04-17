---
id: p01_fse_meta_builder_recipe
kind: few_shot_example
pillar: P01
title: Few-Shot Example -- The Meta-Builder Recipe
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.2
tags: [few-shot-example, meta-builder, agent-factory, recipe, how-to]
tldr: Complete worked example of building an agent from intent to published artifact. Shows every 8F step, every decision, every validation. The reference build.
density_score: 0.92
---

# The Meta-Builder Recipe: Building an Agent from Intent

This is a COMPLETE worked example. Follow it step-by-step.

## Input

```
User intent: "I need an agent that reviews code for security vulnerabilities"
```

## F1 CONSTRAIN: Load Schema

```yaml
resolved_kind: agent
target_pillar: P02
schema: P02_agents/_schema.yaml
max_bytes: 8192
naming: "{kind}_{domain}.md"
required_frontmatter: [id, kind, pillar, title, version, created, author, domain, quality, tags, tldr]
```

## F2 BECOME: Load Identity

```yaml
identity: N03 Builder Nucleus
axioms: [AX01-frontmatter-required, AX03-one-kind-one-pillar, AX06-quality-floor-8.0]
role: Meta-construction consultant
quality_floor: 8.5
```

## F3 INJECT: Load Knowledge

```
Loaded:
  - archetypes/builders/agent-builder/ISO_agent_001_MANIFEST.md
  - archetypes/builders/agent-builder/ISO_agent_002_INSTRUCTIONS.md
  - archetypes/builders/agent-builder/ISO_agent_003_EXAMPLES.md
  - P01_knowledge/library/kind/kc_agent.md
  - 3 existing agent examples from examples/
  - Construction Triad pattern (Template-First: search existing)

Template-First result: Found 2 similar agents (similarity: 0.72, 0.54)
  -> ADAPT mode: use highest match as starting structure
```

## F4 REASON: Plan

```
Plan:
  1. Adapt existing agent structure (0.72 match)
  2. Specialize for security domain
  3. Define capabilities: SAST, dependency audit, secret detection
  4. Define tools: grep, semgrep, git log
  5. Define quality: security-specific rubric
  6. Target score: 9.0+ (meta-construction floor)
```

## F5 CALL: Available Tools

```
Tools available:
  - cex_compile.py (post-save compilation)
  - cex_doctor.py (validation)
  - cex_index.py (re-index after save)
  - signal_writer.py (completion signal)
```

## F6 PRODUCE: Generate

```markdown
---
id: p02_agent_security_code_reviewer
kind: agent
pillar: P02
title: Security Code Review Agent
version: 1.0.0
created: 2026-03-30
author: builder_agent
domain: security
quality: 9.0
tags: [agent, security, code-review, SAST, vulnerability]
tldr: Reviews code for security vulnerabilities using SAST patterns,
  dependency auditing, and secret detection. Reports with severity scores.
density_score: 0.88
---

# Security Code Review Agent

## Capabilities

| Capability | Method | Tools |
|------------|--------|-------|
| Static analysis | Pattern matching against known vuln signatures | semgrep, grep |
| Dependency audit | Check versions against CVE database | pip-audit, npm-audit |
| Secret detection | Scan for hardcoded keys, tokens, passwords | trufflehog, grep |
| Git history | Review commits for accidentally committed secrets | git log, git diff |

## Workflow

1. Receive code path or diff
2. Run SAST scan (pattern matching)
3. Run dependency audit
4. Run secret detection
5. Aggregate findings with severity (CRITICAL/HIGH/MEDIUM/LOW)
6. Generate report with fix recommendations

## Quality Gate

| Check | Threshold |
|-------|-----------|
| False positive rate | < 10% |
| Coverage | > 80% of known vulnerability patterns |
| Report clarity | Actionable fixes, not just warnings |
```

## F7 GOVERN: Validate (12LP)

```
12LP Results:
  1. Frontmatter: PASS (all fields present)
  2. Kind Match: PASS (agent)
  3. Pillar Alignment: PASS (P02)
  4. Schema Compliance: PASS (capabilities, workflow, quality)
  5. Density: PASS (0.88)
  6. Completeness: PASS (no TODOs)
  7. Uniqueness: PASS (no duplicate)
  8. References: PASS (no external refs)
  9. Boundary: PASS (agent only, no workflow bleed)
  10. Size: PASS (2.1KB < 8KB max)
  11. Naming: PASS (agent_security_code_reviewer.md)
  12. Self-Test: PASS (a stranger could use this)

5D Score: D1=9 D2=9 D3=9 D4=9 D5=8 = 8.85
Tier: PUBLISH (>= 8.0)
```

## F8 COLLABORATE: Save + Signal

```bash
# Save
write to: N0x_domain/agents/agent_security_code_reviewer.md

# Compile
python _tools/cex_compile.py N0x_domain/agents/agent_security_code_reviewer.md

# Re-index
python _tools/cex_index.py

# Commit
git add -A && git commit -m "[N03] agent: security code reviewer (5D: 8.85)"

# Signal
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 8.85)"
```

## Key Decisions Made

| Decision | Tree Used | Choice | Why |
|----------|-----------|--------|-----|
| Template vs Custom | D_003 | ADAPT (0.72 match) | High similarity, adapt faster |
| Refactor vs Deliver | D_001 | DELIVER at 8.85 | Above 8.5 floor, specific, clear |
| Repository vs Local | D_004 | REPOSITORY | Score >= 8.0 |