---
id: p01_kc_software_project
kind: knowledge_card
type: kind
pillar: P02
title: "Software Project — Deep Knowledge for software_project"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: software_project
quality: 9.1
tags: [software_project, P02, BECOME, kind-kc, project, scaffold]
tldr: "Complete software project definition — architecture, dependencies, build config, deployment spec, and repo structure as a single artifact"
when_to_use: "Building, reviewing, or reasoning about software_project artifacts"
keywords: [software_project, repo, scaffold, architecture, deployment, build]
feeds_kinds: [software_project]
density_score: 1.0
axioms:
  - "AVOID: Mixing deployment scripts INTO the project definition (use separate deploy artifacts)"
  - "AVOID: Defining runtime behavior (that's dag or workflow)"
  - "AVOID: Embedding secrets in the artifact (use secret_config kind)"
linked_artifacts:
  primary: null
  related: []
---

# Software Project

## Spec
```yaml
kind: software_project
pillar: P02
llm_function: BECOME
max_bytes: 8192
naming: p02_software_project_{{slug}}.md + .yaml
core: false
```

## Purpose
Defines a complete software project as a structured artifact — including repo layout, tech stack, dependencies, build/test/deploy configs, and architecture decisions. Unlike individual code files or configs, a software_project artifact captures the **whole-project view** needed to scaffold, audit, or replicate a codebase.

## Boundary
| Pair | Boundary |
|------|----------|
| software_project vs agent_package | software_project = any software repo; agent_package = specifically an AI agent bundle with ISOs |
| software_project vs boot_config | software_project = full project definition; boot_config = just the startup/init config |
| software_project vs dag | software_project = static structure; dag = runtime execution graph |

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique identifier |
| kind | string | yes | Always "software_project" |
| pillar | string | yes | P02 |
| tech_stack | list | yes | Languages, frameworks, platforms |
| repo_structure | map | yes | Directory tree with purposes |
| dependencies | list | yes | External packages/services |
| build_config | map | no | Build tool, scripts, env vars |
| deploy_target | string | no | Cloud/edge/local target |

## Quality Gates
1. tech_stack lists at least 1 language + 1 framework
2. repo_structure has src/, tests/, docs/ at minimum
3. dependencies list exists (may be empty for zero-dep projects)
4. No conflicting build configs
5. Naming follows p02_software_project_{slug}.md

## Anti-Patterns
- Mixing deployment scripts INTO the project definition (use separate deploy artifacts)
- Defining runtime behavior (that's dag or workflow)
- Embedding secrets in the artifact (use secret_config kind)
