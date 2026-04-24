---
id: kc_agents_md
kind: knowledge_card
8f: F3_inject
title: Agents.md Project-Root Manifest
version: 1.0.0
quality: 8.5
pillar: P01
description: |
  Project-root manifest for AAIF/OpenAI AGENTS.md: setup/test/lint commands, PR format, deploy rules, coding-agent conventions
density_score: 1.0
related:
  - bld_output_template_agents_md
  - p01_kc_nixpacks_buildpacks
  - bld_examples_agents_md
  - p04_output_github_actions
  - bld_output_template_contributor_guide
  - agents-md-builder
  - bld_instruction_agents_md
  - p03_sp_deploy_ops
  - spec_zero_install
  - p02_agent_deploy_ops
---

## Setup/Testing/Linting
- `npm install` - Install dependencies
- `npm test` - Run unit tests
- `npm lint` - Lint code with ESLint
- `npm format` - Format code with Prettier

## PR Format
- Title: `[TYPE]: brief description` (e.g., `feat: add agent registry`)
- Description: 
  1. Motivation
  2. Proposed solution
  3. Testing instructions
  4. Related issues

## Deploy Rules
- Staging: `npm run deploy:staging`
- Production: `npm run deploy:production`
- Requires 2 approvals for production deploys

## Coding-Agent Conventions
- Use `// TODO` for pending tasks
- Document API endpoints in `docs/api.md`
- Follow 2-space indentation
- Add type annotations to all functions
- Include error handling for all API calls
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_agents_md]] | downstream | 0.28 |
| [[p01_kc_nixpacks_buildpacks]] | sibling | 0.25 |
| [[bld_examples_agents_md]] | downstream | 0.23 |
| [[p04_output_github_actions]] | downstream | 0.22 |
| [[bld_output_template_contributor_guide]] | downstream | 0.20 |
| [[agents-md-builder]] | downstream | 0.18 |
| [[bld_instruction_agents_md]] | downstream | 0.17 |
| [[p03_sp_deploy_ops]] | downstream | 0.17 |
| [[spec_zero_install]] | related | 0.17 |
| [[p02_agent_deploy_ops]] | downstream | 0.17 |
