---
id: p01_kc_git_hooks_ci
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Git Hooks + Pre-Commit Validation"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [git-hooks, pre-commit, validation, quality-gates, ci]
tldr: "Git hooks as local quality gates: pre-commit validates artifacts before they reach CI. CEX uses cex_hooks.py (frontmatter check, compile, size). codexa-core uses 76 Python hooks (LLM validators, TTS, quality scoring)."
density_score: 1.0
when_to_use: "Apply when git hooks as local quality gates: pre-commit validates artifacts before they reach ci. cex uses c..."
keywords: [knowledge-card, software-engineering, githookspre-commit, hooks, pre-commit]
axioms:
  - "AVOID: ❌ No pre-commit hooks (bad artifacts reach CI)"
  - "AVOID: ❌ Hooks that take >10s (developers bypass with `--no-verify`)"
  - "AVOID: ❌ Hooks that modify files silently (confusing)"
linked_artifacts:
  primary: null
  related: []
related:
  - p04_hook_pre_commit_qa
  - bld_examples_hook_config
  - bld_tools_playground_config
  - bld_tools_integration_guide
  - validator-builder
  - p01_kc_hook_config
  - bld_tools_changelog
  - bld_tools_sandbox_spec
  - bld_tools_benchmark_suite
  - bld_knowledge_card_hook
---

# Git Hooks + Pre-Commit

## CEX Pre-Commit Hook

CEX validates every staged .md artifact before commit.

### .git/hooks/pre-commit

```bash
#!/bin/sh
python _tools/cex_hooks.py pre-commit
```

### What cex_hooks.py Checks

```python
def validate_artifact(path, content=None):
    issues = []
    fm = parse_frontmatter(content)
    if not fm:
        issues.append({"level": "ERROR", "msg": "Missing YAML frontmatter"})
        return issues
    for field in ["id", "kind", "pillar", "quality"]:
        if field not in fm:
            issues.append({"level": "ERROR", "msg": f"Missing field: {field}"})
    if fm.get("quality") is not None:
        try:
            q = float(fm["quality"])
            if q < 7.0:
                issues.append({"level": "WARN", "msg": f"Low quality: {q}"})
        except: pass
    return issues
```

### Hook Flow

```
git add artifact.md
git commit -m "..."
  └── pre-commit hook fires
      └── cex_hooks.py pre-commit
          ├── Find staged .md files (git diff --cached)
          ├── Skip README.md files
          ├── For each artifact:
          │   ├── Parse YAML frontmatter
          │   ├── Check required fields (id, kind, pillar, quality)
          │   ├── Check size limits
          │   └── Attempt compile (.md → .yaml)
          ├── If any ERROR → reject commit (exit 1)
          └── If all PASS → allow commit (exit 0)
```

## pre-commit Framework (Python)

For non-CEX projects, use the `pre-commit` framework.

### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: detect-private-key

  - repo: local
    hooks:
      - id: pytest-fast
        name: Fast tests
        entry: pytest -x -q --timeout=30 -m "not slow"
        language: system
        pass_filenames: false
        always_run: true
```

### Setup

```bash
pip install pre-commit
pre-commit install          # Install hooks
pre-commit run --all-files  # Run on all files
pre-commit autoupdate       # Update hook versions
```

## codexa-core Hooks (76 scripts)

codexa-core has advanced hooks under `.claude/hooks/`:

| Category | Files | Purpose |
|----------|-------|---------|
| validators/ | ~30 | 5D quality scoring, artifact validation |
| utils/llm/ | ~20 | LLM-powered review, summarization |
| utils/tts/ | ~10 | Text-to-speech for accessibility |
| quality/ | ~16 | Auto-scoring, density checks |

### Hook Pattern (Validator)

```python
# .claude/hooks/validators/validate_artifact.py
def validate_5d(content: str, kind: str, mode: str) -> ValidationResult:
    """5-Dimensional validation: structure, content, density, style, compliance."""
    scores = {
        "structure": check_structure(content, kind),
        "content": check_content_quality(content),
        "density": check_info_density(content),
        "style": check_writing_style(content),
        "compliance": check_compliance(content, kind),
    }
    total = sum(scores.values()) / len(scores)
    decision = "APPROVED" if total >= 7.0 else "REJECTED"
    return ValidationResult(scores=scores, total_score=total, decision=decision)
```

## Hook Categories

| Hook Type | When | Purpose |
|-----------|------|---------|
| pre-commit | Before commit | Validate syntax, frontmatter, secrets |
| pre-push | Before push | Run tests, lint |
| commit-msg | After message | Enforce conventional commits |
| post-merge | After merge | Run migrations, update deps |

## Anti-Patterns

- ❌ No pre-commit hooks (bad artifacts reach CI)
- ❌ Hooks that take >10s (developers bypass with `--no-verify`)
- ❌ Hooks that modify files silently (confusing)
- ❌ No way to skip hooks for emergency hotfixes
- ❌ Hooks duplicating full CI pipeline (keep hooks fast, CI thorough)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_hook_pre_commit_qa]] | downstream | 0.47 |
| [[bld_examples_hook_config]] | downstream | 0.32 |
| [[bld_tools_playground_config]] | downstream | 0.31 |
| [[bld_tools_integration_guide]] | downstream | 0.30 |
| [[validator-builder]] | downstream | 0.30 |
| [[p01_kc_hook_config]] | sibling | 0.29 |
| [[bld_tools_changelog]] | downstream | 0.28 |
| [[bld_tools_sandbox_spec]] | downstream | 0.28 |
| [[bld_tools_benchmark_suite]] | downstream | 0.28 |
| [[bld_knowledge_card_hook]] | sibling | 0.27 |
