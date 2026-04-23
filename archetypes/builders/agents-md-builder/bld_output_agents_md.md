---
kind: output_template
id: bld_output_template_agents_md
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for agents_md production
quality: 8.8
title: "Output Template Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, output_template]
tldr: "Template with vars for AGENTS.md production"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_agents_md
  - kc_agents_md
  - bld_instruction_agents_md
  - bld_schema_agents_md
  - bld_output_template_contributor_guide
  - p03_sp_agents_md_builder
  - p04_output_github_actions
  - bld_sp_tools_software_project
  - p01_kc_ruff_uv
  - agents-md-builder
---

```markdown
---
id: p02_am_{{name}}.md
kind: agents_md
pillar: P05
project_root: {{project_root}}      <!-- repo absolute path -->
primary_stack: {{primary_stack}}    <!-- 'node' | 'python' | 'rust' | 'go' -->
quality: null
---

# AGENTS.md -- {{project_name}}

{{one_paragraph_repo_summary}}

## Setup commands
```bash
{{setup_command}}                   <!-- e.g., npm install  /  pip install -e . -->
```

## Test commands
```bash
{{test_command}}                    <!-- e.g., npm test  /  pytest -q -->
```

## Lint commands
```bash
{{lint_command}}                    <!-- e.g., npm run lint  /  ruff check . -->
```

## PR format
- Commit grammar: {{commit_grammar}}   <!-- e.g., Conventional Commits -->
- Branch prefix: {{branch_prefix}}     <!-- e.g., feat/, fix/, chore/ -->
- Review: {{review_rule}}              <!-- e.g., 1 approval + CI green -->

## Deploy rules
- Approver: {{deploy_approver}}
- Rollback: {{rollback_command}}

## Security rules
- NEVER force-push to {{protected_branch}}
- NEVER delete protected branches
- NEVER rewrite published history
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_agents_md]] | downstream | 0.45 |
| [[kc_agents_md]] | upstream | 0.34 |
| [[bld_instruction_agents_md]] | upstream | 0.34 |
| [[bld_schema_agents_md]] | downstream | 0.33 |
| [[bld_output_template_contributor_guide]] | sibling | 0.27 |
| [[p03_sp_agents_md_builder]] | upstream | 0.26 |
| [[p04_output_github_actions]] | upstream | 0.24 |
| [[bld_sp_tools_software_project]] | upstream | 0.24 |
| [[p01_kc_ruff_uv]] | upstream | 0.23 |
| [[agents-md-builder]] | related | 0.22 |
