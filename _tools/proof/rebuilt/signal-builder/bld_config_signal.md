---
kind: config
id: bld_config_signal
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: signal Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_sig_{event}.json` | `p12_sig_satellite_complete.json` |
| Builder directory | kebab-case | `signal-builder/` |
| Payload fields | snake_case | `quality_score`, `commit_hash` |
| Status values | lowercase enum | `complete`, `error`, `progress` |
| Satellite values | lowercase slug | `codex`, `edison`, `atlas` |
Rule: use `.json` only for this builder.
## File Paths
- Output: `cex/P12_orchestration/compiled/p12_sig_{event}.json`
- Human reference: `cex/P12_orchestration/examples/p12_sig_{event}.md`
## Size Limits
- Preferred payload size: <= 1024 bytes
- Absolute max: 4096 bytes
- Optional fields should remain sparse and compact
## Payload Restrictions
- Required fields must appear exactly as defined in SCHEMA.md
- Omit optional null/unknown fields instead of writing placeholders
- `progress_pct` allowed only when `status=progress`
- `artifacts_count` should match `artifacts` length when both exist
- `quality_score` must stay numeric; never quote it as text
## Boundary Restrictions
- No markdown, prose sections, or frontmatter inside the JSON payload
- No task lists, scope fences, or commit instructions
- No routing tables, keywords arrays for dispatch, or model selection logic
