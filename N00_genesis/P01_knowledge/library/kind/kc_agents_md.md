---
id: kc_agents_md
kind: knowledge_card
title: Agents.md Project-Root Manifest
version: 1.0.0
quality: 8.5
pillar: P01
description: |
  Project-root manifest for AAIF/OpenAI AGENTS.md: setup/test/lint commands, PR format, deploy rules, coding-agent conventions
density_score: 1.0
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