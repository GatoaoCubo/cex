---
kind: config
id: bld_config_director
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: director Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_dir_{name_lower}.md` | `p08_dir_satellite_onboarding.md` |
| Builder directory | kebab-case | `director-builder/` |
| Frontmatter fields | snake_case | `entry_point`, `dag_edges`, `handoff_contracts` |
| Director names | kebab-case in name field | `satellite-onboarding`, `content-pipeline` |
| Name slugs | lowercase_underscore in id | `satellite_onboarding`, `content_pipeline` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P08_architecture/examples/p08_dir_{name_lower}.md`
- Compiled: `cex/P08_architecture/compiled/p08_dir_{name_lower}.md`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total: ~6000 bytes including frontmatter
- Density: >= 0.80
## Builder Reference Convention
- Always use exact builder id (kebab-case): `mental-model-builder`, `satellite-spec-builder`
- Never use display names or aliases in dag_edges or handoff_contracts
- Builder ids must match entries in the CEX builder catalog
## DAG Constraints
| Rule | Rationale |
|------|-----------|
| No cycles | Cyclic dependency = infinite loop; invalid crew |
| entry_point has no incoming edges | First builder cannot depend on any other in the crew |
| exit_point has no outgoing edges | Final builder produces the deliverable and terminates |
| Every edge has a data description | Implicit data passing causes type mismatches |
## Parallelism Defaults
| Field | Default | Max |
|-------|---------|-----|
| parallel_group size | 1 (sequential) | 3 (BSOD prevention) |
| max_retries per builder | 1 | 3 |
| estimated_duration | null | no hard limit (document realistic estimate) |
