---
kind: config
id: bld_config_checkpoint
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: checkpoint Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_ckpt_{workflow}.md` | `p12_ckpt_research_pipeline.md` |
| Builder directory | kebab-case | `checkpoint-builder/` |
| Frontmatter fields | snake_case | `workflow_ref`, `parent_checkpoint` |
| Workflow slug | snake_case, lowercase, no hyphens | `research_pipeline`, `data_ingest` |
| Step names | snake_case, verb or noun phrase | `fetch_sources`, `embed_chunks`, `validate_output` |
| ID prefix | `p12_ck_` | `p12_ck_research_pipeline_embed` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P12_orchestration/examples/p12_ckpt_{workflow}.md`
- Compiled: `cex/P12_orchestration/compiled/p12_ckpt_{workflow}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4096 bytes
- Density: >= 0.80 (no filler)
## TTL Conventions
| Value | When to use |
|-------|-------------|
| 1h | Short-lived interactive session checkpoints |
| 24h | Single-run batch workflow checkpoints |
| 7d | Multi-day research or processing pipelines |
| 30d | Long-running audit or compliance workflows |
| none | Permanent archival checkpoints (use sparingly) |
Rule: every checkpoint MUST define ttl. Unbounded checkpoints (ttl: none) require
explicit justification comment in the description field.
## State Size Budget
| State size | Guidance |
|------------|----------|
| < 512 bytes | Preferred — ids, counters, flags, small maps |
| 512–1024 bytes | Acceptable — short lists, nested maps |
| 1024–2048 bytes | Max allowed — must justify in ## State section |
| > 2048 bytes | HARD FAIL — checkpoint body exceeds max_bytes |
Rule: state map in frontmatter contains schema (key + type), NOT raw values.
Raw state values live in the backend store (SQLite, Postgres, S3), not in the artifact.
