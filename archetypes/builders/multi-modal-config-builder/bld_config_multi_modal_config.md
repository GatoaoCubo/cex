---
kind: config
id: bld_config_multi_modal_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
---
# Config: multi_modal_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_mmc_{capability_slug}.yaml` | `p04_mmc_document_analysis.yaml` |
| Builder directory | kebab-case | `multi-modal-config-builder/` |
| Frontmatter fields | snake_case | `supported_modalities`, `routing_model` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `P04_tools/examples/p04_mmc_{capability}.yaml`
- Compiled: `P04_tools/compiled/p04_mmc_{capability}.yaml`
## Size Limits
- Total file: max 2048 bytes
- tldr: <= 160 chars
## Modality Defaults
| Modality | Default Resolution/Duration | Token Estimate |
|----------|---------------------------|----------------|
| Image (low) | 768x768 | ~400 tokens |
| Image (med) | 1024x1024 | ~750 tokens |
| Image (high) | 2048x2048 | ~1500 tokens |
| Audio | 600s max | ~300 tokens/min (transcribed) |
| Video | 60s max | ~1500 tokens (keyframes) |
| Document (PDF) | per page | ~1200 tokens/page |
