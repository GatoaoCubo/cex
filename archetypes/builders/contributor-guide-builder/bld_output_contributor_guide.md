---
kind: output_template
id: bld_output_template_contributor_guide
pillar: P05
llm_function: PRODUCE
purpose: Canonical Markdown template for contributor_guide artifacts with all required sections
quality: 9.2
title: "Contributor Guide Output Template"
version: "1.1.0"
author: n02_hybrid_review7
tags: [contributor_guide, builder, output_template]
tldr: "Full CONTRIBUTING.md scaffold with sections for setup, workflow, standards, PR process, review, and CLA"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_contributor_guide
  - bld_instruction_contributor_guide
  - kc_git_workflow_for_agents
  - kc_contributor_guide
  - p04_output_github_actions
  - p04_tool_software_project
  - p12_wf_auto_ship
  - p11_qg_tdd_compliance
  - bld_output_template_agents_md
  - p01_kc_git_worktree_isolation
---

## Usage Notes

Replace `{{tokens}}` before delivery; remove this section from final output.
Code blocks are examples -- substitute project commands. Sections marked REQUIRED are H04-H08 gates.

## Template

```markdown
---
id: p05_cg_{{project_slug}}
kind: contributor_guide
pillar: P05
title: "Contributing to {{Project Name}}"
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{maintainer_name_or_team}}
domain: contributor guide
quality: null
tags: [contributor_guide, {{project_slug}}, oss]
tldr: "How to contribute to {{Project Name}}: setup, workflow, standards, and CLA."
---

# Contributing to {{Project Name}}

{{one paragraph: what the project is, why contributions matter, who this guide is for. Welcoming, specific.}}

---

## Getting Started  [REQUIRED -- H04]

### Prerequisites

- {{Language runtime}}: version {{X.Y}} or higher
- {{Package manager}}: version {{X.Y}} or higher
- {{Other dependency, e.g., Docker}}: version {{X.Y}} or higher

### Installation

```bash
# 1. Fork on GitHub, clone your fork
git clone https://github.com/{{your-username}}/{{repo-name}}.git
cd {{repo-name}}
# 2. Add upstream
git remote add upstream https://github.com/{{org}}/{{repo-name}}.git
# 3. Install deps
{{install_command}}    # npm install | pip install -e ".[dev]" | go mod download
# 4. Verify -- all tests must pass
{{test_command}}       # npm test | pytest | go test ./...
```

If setup fails, open an issue with `{{debug_command}}` output and your OS version.

---

## Contribution Workflow  [REQUIRED -- H05]

Fork-and-PR workflow. No direct push to main.

1. **Sync fork**: `git fetch upstream && git checkout main && git merge upstream/main`
2. **Branch**: `git checkout -b {{branch-prefix}}/{{short-description}}` (e.g., `feat/csv-export`, `fix/null-pointer`)
3. **Change code** per Coding Standards below.
4. **Test**: `{{test_command}} && {{lint_command}}`
5. **Commit** per Commit Messages below.
6. **Push**: `git push origin {{branch-prefix}}/{{short-description}}`
7. **Open PR** against `{{target_branch}}` (usually `main` or `develop`).

---

## Coding Standards  [REQUIRED -- H06]

This project uses **{{style_guide_name}}** for code style enforcement.

```bash
{{lint_command}}    # npm run lint | flake8 . | golangci-lint run
{{format_command}}  # prettier --write . | black . | gofmt -w .
```

| Standard | Tool | Config file |
|----------|------|-------------|
| Formatting | {{formatter}} | {{config_path}} |
| Linting | {{linter}} | {{config_path}} |
| Type checking | {{type_checker}} | {{config_path}} |

All code must pass the CI lint gate before a PR is eligible for review.

---

## Commit Messages

We follow **{{Conventional Commits / Custom spec}}**. Each commit message must have this format:

```
{{type}}({{scope}}): {{short description}}

{{optional body: explain why, not what}}

{{optional footer: references, breaking changes}}
```

| Type | When to use |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `test` | Adding or fixing tests |
| `chore` | Maintenance, tooling, dependencies |

**Breaking changes**: add `!` after the type (`feat!:`) and describe in the footer.

---

## Pull Request Process  [REQUIRED -- H05]

When your PR is ready for review:

1. Fill in the PR template completely. Incomplete PRs will be returned.
2. Reference the related issue: `Fixes #{{issue_number}}`.
3. Ensure all CI checks pass (lint, test, build).
4. Request review from {{who_reviews}} in GitHub.
5. Respond to feedback within **{{response_SLA}}** (e.g., 3 business days).

**Merge policy**: PRs are squash-merged after {{N}} approvals. The PR author
writes the squash commit message.

---

## Review Process  [REQUIRED -- H07]

Maintainers aim to provide initial review feedback within **{{review_SLA}}**.

Reviews assess:
- Correctness and test coverage
- Alignment with coding standards
- Documentation completeness
- Scope (does the PR do one thing?)

**Re-review**: after addressing feedback, re-request review by clicking
"Re-request review" on GitHub. Do not open a new PR for revisions.

---

## CLA / DCO  [REQUIRED -- H08]

{{Pick ONE; delete the other.}}

### Option A: CLA

Sign **{{CLA Name}}**: {{CLA URL}}. Corporate contributors: employer signs corporate CLA if contributing on company time.

### Option B: DCO

Certify each commit with a sign-off: `git commit -s -m "feat: add CSV export"` (adds `Signed-off-by: Name <email>`). Text at https://developercertificate.org/
```

## Section Annotations

| Section | Annotation |
|---------|-----------|
| Getting Started | Must include at least one code block with installation commands. |
| Contribution Workflow | Use numbered list for steps. Include commands for each step. |
| Coding Standards | Name the specific tool (ESLint, Black, etc.), not a generic reference. |
| Commit Messages | Show the exact format with a concrete example. |
| Pull Request Process | State the number of approvals required and who can approve. |
| Review Process | State the SLA in business days, not "as soon as possible." |
| CLA / DCO | Keep exactly one option. Delete the unused option block. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_contributor_guide]] | downstream | 0.37 |
| [[bld_instruction_contributor_guide]] | upstream | 0.32 |
| [[kc_git_workflow_for_agents]] | upstream | 0.32 |
| [[kc_contributor_guide]] | upstream | 0.26 |
| [[p04_output_github_actions]] | upstream | 0.25 |
| [[p04_tool_software_project]] | upstream | 0.25 |
| [[p12_wf_auto_ship]] | downstream | 0.25 |
| [[p11_qg_tdd_compliance]] | downstream | 0.25 |
| [[bld_output_template_agents_md]] | sibling | 0.24 |
| [[p01_kc_git_worktree_isolation]] | upstream | 0.24 |
