---
kind: tools
id: bld_tools_openapi_spec
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for openapi_spec production
quality: null
title: "Tools OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, tools]
tldr: "Tools: cex_compile, cex_doctor, cex_score. Data sources: OAS 3.x spec, existing API contracts, components.schemas."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Tools: openapi-spec-builder

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar openapi_spec artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_openapi_spec.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `openapi_spec`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/openapi-spec-builder/bld_examples_openapi_spec.md` | Reference examples | F3 INJECT |
| `archetypes/builders/openapi-spec-builder/bld_schema_openapi_spec.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing openapi_spec artifacts
python _tools/cex_retriever.py --query "openapi api contract oas3"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```

## External References

| Reference | Purpose |
|-----------|---------|
| spec.openapis.org/oas/v3.1.0 | OAS 3.1 official specification |
| swagger.io/tools/swagger-editor | Interactive OAS editor for validation |
| openapi-generator.tech | Code generation from OAS spec |
| stoplight.io/spectral | OAS linting and validation rules |
| redocly.com/docs | OAS documentation rendering |

## Validation Commands

| Command | Purpose | When |
|---------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml | F8 |
| `python _tools/cex_doctor.py` | Check builder health | F7 |
| `python _tools/cex_score.py {path} --apply` | Peer review + apply score | F7 |
| `python _tools/cex_retriever.py --query "oas api"` | Find similar artifacts | F5 |
| `git add {path} && git commit` | Version artifact | F8 |
| `python _tools/cex_index.py` | Update artifact index | F8 |
| `python _tools/cex_retriever.py --similar {path}` | Find duplicate schemas | F5 |
