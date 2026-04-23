---
kind: tools
id: bld_tools_sandbox_spec
pillar: P04
llm_function: CALL
purpose: Tools available for sandbox_spec production
quality: 8.9
title: "Tools Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, tools]
tldr: "Tools available for sandbox_spec production"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_playground_config
  - bld_tools_integration_guide
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_github_issue_template
  - bld_tools_changelog
  - p01_kc_git_hooks_ci
  - bld_tools_white_label_config
  - bld_tools_api_reference
  - bld_tools_competitive_matrix
---

## Production Tools
| Tool | Purpose | When |
|---|---|---|
| cex_compile.py | Compile .md artifact to .yaml | Post-write (F8) |
| cex_retriever.py | TF-IDF similarity over 2184 docs | Find prior sandbox_spec artifacts (F3) |
| cex_score.py | 3-layer scoring (structural + rubric + semantic) | Quality gate (F7) |
| cex_doctor.py | Builder health check across 13 ISOs | Pre-dispatch validation |
| cex_hygiene.py | Frontmatter + ASCII + naming enforcement | Pre-commit (F7) |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_wave_validator.py | D01-D15 defect checks across ISOs | After bulk generation |
| cex_sanitize.py --check | ASCII-only enforcement on .py/.ps1 | Pre-commit hook |
| cex_hooks.py pre-commit | YAML frontmatter + schema compliance | Git pre-commit |

## External References
- PCI-DSS v4.0 sandbox isolation requirements (test/cardholder env separation)
- gVisor (Google user-space kernel sandbox)
- Firecracker (AWS micro-VM, <125ms boot, KVM-based)
- Stripe test mode (dual-key pattern: test_ vs live_ prefixes)
- HIPAA 164.312 technical safeguards (sandbox audit controls)
- NIST SP 800-190 container security guide
- ISO/IEC 27001:2022 A.8.31 separation of development, test, production

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_playground_config]] | sibling | 0.55 |
| [[bld_tools_integration_guide]] | sibling | 0.54 |
| [[bld_tools_rbac_policy]] | sibling | 0.41 |
| [[bld_tools_usage_quota]] | sibling | 0.40 |
| [[bld_tools_github_issue_template]] | sibling | 0.38 |
| [[bld_tools_changelog]] | sibling | 0.36 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.35 |
| [[bld_tools_white_label_config]] | sibling | 0.35 |
| [[bld_tools_api_reference]] | sibling | 0.34 |
| [[bld_tools_competitive_matrix]] | sibling | 0.34 |
