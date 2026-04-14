---
kind: output_template
id: bld_output_template_contributor_guide
pillar: P05
llm_function: PRODUCE
purpose: Canonical Markdown template for contributor_guide artifacts with all required sections
quality: null
title: "Contributor Guide Output Template"
version: "1.1.0"
author: n02_hybrid_review7
tags: [contributor_guide, builder, output_template]
tldr: "Full CONTRIBUTING.md scaffold with sections for setup, workflow, standards, PR process, review, and CLA"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Usage Notes

Replace all `{{placeholder}}` tokens with real content before delivery.
Remove this Usage Notes section from the final artifact.
All code blocks are examples -- replace commands with project-specific commands.
Sections marked REQUIRED must be present for H04-H08 gates to pass.

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

{{one paragraph: what the project is, why contributions matter, and who this
guide is written for. Keep it welcoming and specific to this project.}}

---

## Getting Started  [REQUIRED -- H04]

### Prerequisites

- {{Language runtime}}: version {{X.Y}} or higher
- {{Package manager}}: version {{X.Y}} or higher
- {{Other dependency, e.g., Docker}}: version {{X.Y}} or higher

### Installation

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/{{your-username}}/{{repo-name}}.git
cd {{repo-name}}

# 2. Add the upstream remote
git remote add upstream https://github.com/{{org}}/{{repo-name}}.git

# 3. Install dependencies
{{install_command}}    # e.g., npm install / pip install -e ".[dev]" / go mod download

# 4. Verify the setup -- all tests should pass
{{test_command}}       # e.g., npm test / pytest / go test ./...
```

If setup fails, open an issue with the output of `{{debug_command}}` and your OS version.

---

## Contribution Workflow  [REQUIRED -- H05]

We use a **fork-and-pull-request** workflow. No contributor has direct push access
to the main repository.

1. **Sync your fork** before starting work:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b {{branch-prefix}}/{{short-description}}
   # Example: feat/add-csv-export or fix/null-pointer-on-empty-list
   ```

3. **Make your changes** following the Coding Standards below.

4. **Run tests** before committing:
   ```bash
   {{test_command}}
   {{lint_command}}
   ```

5. **Commit** your changes (see Commit Messages below).

6. **Push** your branch:
   ```bash
   git push origin {{branch-prefix}}/{{short-description}}
   ```

7. **Open a Pull Request** against `{{target_branch}}` (usually `main` or `develop`).

---

## Coding Standards  [REQUIRED -- H06]

This project uses **{{style_guide_name}}** for code style enforcement.

```bash
# Run the linter
{{lint_command}}    # e.g., npm run lint / flake8 . / golangci-lint run

# Auto-format
{{format_command}}  # e.g., prettier --write . / black . / gofmt -w .
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

{{Choose ONE: CLA or DCO. Delete the section that does not apply.}}

### Option A: Contributor License Agreement (CLA)

This project requires all contributors to sign the **{{CLA Name}}**.
Sign here: {{CLA URL}}

Corporate contributors: your employer must sign the corporate CLA if the
contribution is made on company time or uses company resources.

### Option B: Developer Certificate of Origin (DCO)

This project uses the **Developer Certificate of Origin (DCO)**.
You certify each commit by adding a sign-off line:

```bash
git commit -s -m "feat: add CSV export"
# This adds: Signed-off-by: Your Name <your@email.com>
```

The DCO text is at https://developercertificate.org/
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
