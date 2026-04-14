---
kind: examples
id: bld_examples_repo_map
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of repo_map artifacts
quality: null
title: "Examples Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, examples]
tldr: "Golden and anti-examples of repo_map artifacts"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "repo_map for microservices-demo"
description: "Repository context map for microservices-demo project"
author: "Jane DevOps"
date: "2023-10-05"
version: "1.2"
---

**Repository Structure**
- `api/`: Public REST endpoints
- `services/`: Internal business logic
- `shared/`: Cross-service utilities
- `tests/`: Unit/integration tests

**Key Components**
1. `auth-service`: JWT handling and user management
2. `data-service`: Database interactions and caching
3. `event-bus`: Message queue for inter-service communication

**Dependencies**
- PostgreSQL (v14)
- Redis (v6)
- Kafka (v3)

**Context Extraction Rules**
- All API routes must reference corresponding service modules
- Shared utilities must be versioned in `shared/`
- Tests must mirror production code structure
```

## Anti-Example 1: Missing Frontmatter
```markdown
**Repository Structure**
- src/
- tests/
- README.md

**Key Components**
- frontend
- backend
```
## Why it fails
Lacks metadata for tracking authorship, date, and version. No standardized format for repository context, making it hard to integrate with CI/CD or documentation tools.

## Anti-Example 2: Vague Sections
```markdown
---
title: "repo_map"
---

**Structure**
- some folders

**Components**
- thing 1
- thing 2
```
## Why it fails
Sections lack specificity and actionable information. No clear mapping between code structure and functional components, making the artifact useless for context extraction or onboarding.
