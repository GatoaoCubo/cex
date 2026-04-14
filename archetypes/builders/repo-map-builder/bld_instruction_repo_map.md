---
kind: instruction
id: bld_instruction_repo_map
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for repo_map
quality: null
title: "Instruction Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, instruction]
tldr: "Step-by-step production process for repo_map"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify codebase root directory and submodule boundaries.  
2. Parse `package.json`, `pyproject.toml`, or equivalent dependency files.  
3. Extract module paths, file types, and language-specific markers (e.g., `.ts`, `.py`).  
4. Map inter-module dependencies via import/export statements and API references.  
5. Document legacy systems, monorepo structures, or hybrid architectures.  
6. Flag unversioned assets (e.g., config files, documentation) for exclusion.  

## Phase 2: COMPOSE  
1. Initialize `repo_map` artifact with schema version from SCHEMA.md.  
2. Populate `modules` array with names, paths, and language metadata.  
3. Inject dependency graph using parsed import/export relationships.  
4. Annotate modules with injection points (e.g., hooks, plugins, middleware).  
5. Reference OUTPUT_TEMPLATE.md for required `metadata` fields (e.g., team, CI/CD).  
6. Embed codebase hierarchy as nested `submodules` objects.  
7. Validate against SCHEMA.md for required keys and data types.  
8. Generate human-readable summary in `overview` field.  
9. Finalize with checksum of source files for versioning.  

## Phase 3: VALIDATE  
- [ ] ✅ All module paths resolve to existing files.  
- [ ] ✅ Dependency graph matches static analysis results.  
- [ ] ✅ Schema compliance (no missing required fields).  
- [ ] ✅ Injection points align with codebase conventions.  
- [ ] ✅ Output template placeholders are fully populated.
