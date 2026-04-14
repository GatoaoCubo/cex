---
id: kc_agents_md
kind: knowledge_card
title: Agents.md Project Manifest
version: 1.0.0
quality: null
pillar: P01
---

# Agents.md Project Manifest

This document defines the structural and operational guidelines for the AAIF/OpenAI AGENTS.md project. It establishes standards for development, collaboration, and deployment across all contributors.

## Core Principles
- **Modular Architecture**: All agents must follow the `agent/` directory structure with explicit `setup/`, `test/`, and `lint/` subdirectories
- **Versioned Development**: Use semantic versioning for all agent implementations (e.g., `v1.2.3`)
- **Continuous Integration**: All pull requests must pass automated testing and linting before merging

## Project Setup
```bash
npm install
yarn add --dev eslint prettier
```

## Testing Protocol
1. Run unit tests: `npm test -- --watch`
2. Execute integration tests: `npm run test:integration`
3. Code coverage: `npm run coverage` (minimum 90% coverage required)

## Linting Standards
- Use ESLint with Airbnb config
- Prettier formatting (2 spaces, semicolons)
- No trailing whitespace
- Maximum line length: 120 characters

## Pull Request Format
1. Title: `[TYPE]: [description]` (e.g., `feat: add code-agent v2`)
2. Description: 
   - Problem statement
   - Proposed solution
   - Implementation details
   - Checklist of completed tasks
3. Include: 
   - Test results
   - Linting output
   - Code coverage report

## Deployment Rules
- **Staging**: Deploy to `staging` branch for 7 days
- **Production**: 
  - Requires 2 approvers
  - Must pass security audit
  - Must have rollback plan
- **Rollback**: Use `git revert` for minor issues, `git reset --hard` for critical failures

## Coding-Agent Conventions
1. **Naming**: 
   - Use `camelCase` for variables
   - Use `PascalCase` for classes
   - Use `snake_case` for file names
2. **Structure**: 
   - Each agent must have: 
     - `index.js` (main entry point)
     - `config.js` (configuration settings)
     - `utils.js` (helper functions)
3. **Collaboration**: 
   - Use `git rebase` for feature development
   - Use `git merge --no-ff` for merging
   - Always include `git commit --amend` for minor changes
```
```