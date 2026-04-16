---
kind: tools
id: bld_tools_contributor_guide
pillar: P04
llm_function: CALL
purpose: Production, validation, and reference tools for the contributor_guide builder
quality: 9.1
title: "Contributor Guide Builder Tools"
version: "1.1.0"
author: n02_hybrid_review7
tags: [contributor_guide, builder, tools]
tldr: "CEX core tools plus hygiene checker, retriever, and OSS reference resources for contributor guide production"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools

CEX internal tools used during and after contributor_guide artifact construction.

| Tool | Command | When to use | Output |
|------|---------|-------------|--------|
| cex_compile.py | `python _tools/cex_compile.py {path}` | F8 COLLABORATE -- after saving .md file | Compiled .yaml in archetypes/builders/compiled/ |
| cex_score.py | `python _tools/cex_score.py --apply {path}` | F7 GOVERN -- peer scoring on publish | Quality score applied to frontmatter |
| cex_retriever.py | `python _tools/cex_retriever.py --query "contributor guide OSS workflow CLA"` | F3 INJECT -- find similar contributor guides | Top-N similar artifacts with similarity scores |
| cex_doctor.py | `python _tools/cex_doctor.py` | F8 COLLABORATE -- post-build system health check | PASS/FAIL report across all builders |
| cex_hygiene.py | `python _tools/cex_hygiene.py --check {path}` | F7 GOVERN -- frontmatter completeness check | List of missing or malformed fields |

## Validation Checks

These checks are performed manually or via grep during the F7 GOVERN phase.
They do not require separate tool files.

| Check | Method | Pass condition |
|-------|--------|---------------|
| Required sections present | Grep for section headers: "Getting Started", "Contribution Workflow", "Coding Standards", "Pull Request Process", "Review Process" | All 5 headers found |
| Code blocks present in setup | Grep for ``` in Getting Started section | At least 1 code block |
| CLA / DCO stated | Grep for "CLA" or "DCO" or "sign-off" | At least one match |
| ASCII compliance | `python _tools/cex_sanitize.py --check {path}` (if available) | Exit 0 |
| ID pattern | Python: `import re; re.match(r"^p05_cg_[a-z][a-z0-9_]+", artifact_id)` | Pattern match |

## Tool Execution Order (F5 CALL phase)

| Step | Tool | Purpose |
|------|------|---------|
| 1 | cex_retriever.py | Find similar contributor guides in the corpus for context injection |
| 2 | cex_hygiene.py --check | Verify frontmatter completeness after F6 draft |
| 3 | Section presence grep | Confirm all H04-H08 required sections exist |
| 4 | cex_score.py --apply | Run quality scoring in F7 GOVERN |
| 5 | cex_compile.py | Compile to YAML in F8 COLLABORATE |
| 6 | cex_doctor.py | System health check in F8 COLLABORATE |

## External References

| Resource | URL | Purpose |
|----------|-----|---------|
| GitHub CONTRIBUTING.md guide | https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions | Platform best practices for OSS contribution files |
| Conventional Commits spec | https://www.conventionalcommits.org/ | Commit message format standard |
| Developer Certificate of Origin | https://developercertificate.org/ | DCO text and sign-off requirements |
| Apache CLA | https://www.apache.org/licenses/contributor-agreements.html | Apache Foundation CLA templates (individual + corporate) |
| Markdownlint rules | https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md | Markdown style enforcement reference |
