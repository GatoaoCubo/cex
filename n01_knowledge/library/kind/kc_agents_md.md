---
id: kc_agents_md
kind: knowledge_card
title: Agents.md Project Root Manifest
version: 1.0.0
quality: null
pillar: P01
---

# Agents.md Project Root Manifest

## Setup/Commands
- `setup`: Initialize project with dependencies and config
- `test`: Run unit/integration tests
- `lint`: Validate code style and formatting
- `deploy`: Deploy to production environment

## PR Format
- Title: [TYPE] - [DESCRIPTION] (e.g., `feat - add agent logging`)
- Description: Explain changes, link related issues
- Checklist: 
  - [ ] Tests passed
  - [ ] Linted
  - [ ] Docs updated

## Deploy Rules
- Environment-specific deployment (dev/staging/prod)
- Require 2 approvals for production changes
- Blue-green deployment preferred

## Coding-Agent Conventions
- Use `agent_` prefix for function names
- Follow PEP8 for Python code
- Document all public APIs
- Include type hints
- Use `# noqa` for intentional lint skips
```