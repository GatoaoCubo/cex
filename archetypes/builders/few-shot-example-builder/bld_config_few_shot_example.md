---
kind: config
id: bld_config_few_shot_example
pillar: P09
llm_function: CONSTRAIN
purpose: File system and operational configuration for few_shot_example artifacts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: few_shot_example
## File Naming
| Component | Rule | Example |
|-----------|------|---------|
| Prefix | p01_fse_ (fixed) | p01_fse_ |
| Topic slug | lowercase, underscores, no hyphens | kc_frontmatter |
| Extension | .md (primary) + .yaml (machine) | p01_fse_kc_frontmatter.md |
| Full name | p01_fse_{topic_slug}.md | p01_fse_kc_frontmatter.md |
## File Paths
| File type | Path |
|-----------|------|
| Primary (md) | `cex/P01_knowledge/examples/p01_fse_{topic}.md` |
| Machine (yaml) | `cex/P01_knowledge/examples/p01_fse_{topic}.yaml` |
| Builder | `cex/archetypes/builders/few-shot-example-builder/` |
## Size Constraints
| Constraint | Value | Scope |
|------------|-------|-------|
| max_bytes | 1024 | Body only (not frontmatter) |
| tldr max | 160 chars | tldr field |
| tags min | 3 items | tags list |
| input min | 1 char | input field (non-empty) |
| output min | 1 char | output field (non-empty) |
## Difficulty Enum
| Value | Meaning | When to use |
|-------|---------|-------------|
| easy | Canonical happy-path | First example for a format |
| medium | Realistic variation | Second example, different domain |
| hard | Edge case or ambiguous | Third example, boundary testing |
## Input/Output Constraints
- input: string — the task request a real user would send
- output: string — the complete ideal response (may be multiline with YAML block scalar)
- Both fields MUST be non-empty
- Output MUST demonstrate format, not describe it
## ID Constraint
```
id == filename stem
p01_fse_kc_frontmatter.md -> id: p01_fse_kc_frontmatter
```
