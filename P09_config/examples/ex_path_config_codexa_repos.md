---
id: p09_path_organization_repos
kind: path_config
pillar: P09
title: "Path Config: organization Multi-Repo System"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [path, config, multi-repo, organization]
tldr: "Canonical paths for all 3 organization repos — organization-core (BRAIN), fresh-start (FACE), gato-cubo (BODY) — never commit to wrong repo"
max_bytes: 512
density_score: 0.90
source: organization-core/.claude/rules/multi_repo.md + CLAUDE.md KEY PATHS
linked_artifacts:
  rule: p09_perm_multi_repo
---

# Path Config: organization Multi-Repo System

## Repos

```yaml
repos:
  organization_core:
    alias: BRAIN
    path: C:/Users/PC/Documents/GitHub/organization-core
    purpose: agents, workflows, knowledge, prompts
    identity_file: REPO_IDENTITY.md

  fresh_start:
    alias: FACE
    path: C:/Users/PC/Documents/GitHub/fresh-start
    purpose: React site, UI components, frontend
    identity_file: REPO_IDENTITY.md

  gato_cubo:
    alias: BODY
    path: C:/Users/PC/Documents/GitHub/gato-cubo-commerce
    purpose: e-commerce, Supabase, Shopify, product data
    identity_file: REPO_IDENTITY.md
```

## Key Paths (organization-core)

```yaml
key_paths:
  agent_group_primes: records/agent_groups/{name}/PRIME_{NAME}.md
  agents: records/agents/{name}/
  skills: records/skills/{name}/SKILL.md
  pool_index: records/pool/POOL_INDEX.md
  handoffs: .claude/handoffs/
  signals: .claude/signals/
  spawn_scripts: records/framework/powershell/spawn_*.ps1
  knowledge_index: records/core/brain/mcp-organization-brain/
  learning: records/core/learning/memory/
  mental_models: .claude/mental_models/
```

## Safe Git Protocol

```bash
# BEFORE any git operation:
pwd                     # confirm correct repo
git remote -v           # confirm correct remote
cat REPO_IDENTITY.md    # confirm identity

# Wrong repo recovery (before push):
git reset --soft HEAD~1 && git stash
cd ../correct-repo && git stash pop
```

## Content Routing

| Content | ONLY in | Never in |
|---------|---------|----------|
| `records/agents/*.md` | organization-core | fresh-start, gato-cubo |
| `*.tsx`, React components | fresh-start | organization-core, gato-cubo |
| Supabase migrations | gato-cubo | organization-core, fresh-start |
