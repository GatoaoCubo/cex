#!/usr/bin/env python3
"""
cex_hooks.py — Pre/post build validation hooks for CEX artifacts.

Hooks:
  pre-save   FILE   — Validate artifact before saving (frontmatter, naming, size)
  post-save  FILE   — Compile + check after saving
  pre-commit        — Validate all staged .md files (git hook)
  validate   FILE+  — Full validation of one or more artifacts
  validate-all      — Check every nucleus artifact in repo
  install           — Install git pre-commit hook

Usage:
  python _tools/cex_hooks.py pre-save N07_admin/agents/agent_admin.md
  python _tools/cex_hooks.py post-save N01_intelligence/agents/agent_intelligence.md
  python _tools/cex_hooks.py pre-commit
  python _tools/cex_hooks.py validate N07_admin/agents/agent_admin.md
  python _tools/cex_hooks.py validate-all
  python _tools/cex_hooks.py install
"""

import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent

# Required frontmatter fields for all CEX artifacts
REQUIRED_FM = ["id", "kind", "pillar", "quality"]
DESIRED_FM = ["title", "version", "author", "tags", "tldr", "domain"]

# Pillar prefix pattern
PILLAR_PATTERN = re.compile(r"^P\d{2}$")

# Nucleus artifact directories
NUCLEUS_DIRS = [d for d in CEX_ROOT.iterdir()
                if d.is_dir() and re.match(r"N\d{2}_", d.name)]


def validate_artifact(path: str, content: str = None) -> list[dict]:
    """Validate a single artifact. Returns list of {level, code, msg}."""
    issues = []
    p = Path(path)

    if content is None:
        if not p.exists():
            return [{"level": "ERROR", "code": "E01", "msg": f"File not found: {path}"}]
        content = p.read_text(encoding="utf-8")

    size = len(content.encode("utf-8"))

    # E01: Has frontmatter
    fm = parse_frontmatter(content)
    if fm is None:
        issues.append({"level": "ERROR", "code": "E01", "msg": "No valid YAML frontmatter"})
        return issues  # Can't check more without FM

    # E02: Required fields
    for field in REQUIRED_FM:
        if field not in fm:
            issues.append({"level": "ERROR", "code": "E02", "msg": f"Missing required: {field}"})

    # E03: kind field is string
    kind = fm.get("kind")
    if kind and not isinstance(kind, str):
        issues.append({"level": "ERROR", "code": "E03", "msg": f"kind must be string, got {type(kind)}"})

    # E04: pillar matches P## pattern
    pillar = str(fm.get("pillar", ""))
    if pillar and not re.match(r"P\d{2}", pillar):
        issues.append({"level": "ERROR", "code": "E04", "msg": f"pillar '{pillar}' doesn't match P## pattern"})

    # W01: Desired fields
    for field in DESIRED_FM:
        if field not in fm:
            issues.append({"level": "WARN", "code": "W01", "msg": f"Missing recommended: {field}"})

    # W02: Size limits
    if size > 8192:
        issues.append({"level": "WARN", "code": "W02", "msg": f"Large artifact: {size}B (>8192B)"})
    if size < 200:
        issues.append({"level": "WARN", "code": "W03", "msg": f"Tiny artifact: {size}B (<200B)"})

    # W04: Empty body
    body_match = re.match(r'^---\n.*?\n---\s*', content, re.DOTALL)
    if body_match:
        body = content[body_match.end():]
        if len(body.strip()) < 50:
            issues.append({"level": "WARN", "code": "W04", "msg": "Body is nearly empty (<50 chars)"})

    # W05: Placeholder detection
    placeholders = re.findall(r'\b(TODO|TBD|FIXME|INSERT HERE|ADD LATER)\b', content, re.IGNORECASE)
    if placeholders:
        issues.append({"level": "WARN", "code": "W05", "msg": f"Placeholder text found: {', '.join(set(placeholders))}"})

    # I01: quality is null (info only)
    quality = fm.get("quality")
    if quality is None:
        issues.append({"level": "INFO", "code": "I01", "msg": "quality: null (awaiting peer review)"})

    return issues


def compile_artifact(path: str) -> tuple[bool, str]:
    """Run cex_compile.py on artifact. Returns (success, output)."""
    compile_script = CEX_ROOT / "_tools" / "cex_compile.py"
    if not compile_script.exists():
        return False, "cex_compile.py not found"
    try:
        result = subprocess.run(
            [sys.executable, str(compile_script), path],
            capture_output=True, text=True, timeout=30
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def run_pre_save(paths: list[str]) -> int:
    """Pre-save hook: validate before writing."""
    errors = 0
    for path in paths:
        issues = validate_artifact(path)
        error_count = sum(1 for i in issues if i["level"] == "ERROR")
        warn_count = sum(1 for i in issues if i["level"] == "WARN")

        if error_count:
            print(f"❌ {path}: {error_count} errors, {warn_count} warnings")
            errors += error_count
        elif warn_count:
            print(f"⚠️  {path}: {warn_count} warnings")
        else:
            print(f"✅ {path}: valid")

        for i in issues:
            if i["level"] in ("ERROR", "WARN"):
                symbol = "  ✗" if i["level"] == "ERROR" else "  !"
                print(f"{symbol} [{i['code']}] {i['msg']}")

    return errors


def run_post_save(paths: list[str]) -> int:
    """Post-save hook: validate + compile + report."""
    errors = 0
    for path in paths:
        # Validate
        issues = validate_artifact(path)
        error_count = sum(1 for i in issues if i["level"] == "ERROR")
        if error_count:
            print(f"❌ {path}: {error_count} validation errors — skipping compile")
            for i in issues:
                if i["level"] == "ERROR":
                    print(f"  ✗ [{i['code']}] {i['msg']}")
            errors += error_count
            continue

        # Compile
        ok, output = compile_artifact(path)
        if ok:
            print(f"✅ {path}: valid + compiled")
        else:
            print(f"⚠️  {path}: valid but compile failed: {output}")

    return errors


def run_pre_commit() -> int:
    """Pre-commit hook: validate all staged .md files in N0*/ directories."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True, timeout=10
        )
        staged = [f for f in result.stdout.strip().split("\n")
                  if f.strip() and f.endswith(".md") and re.match(r"N\d{2}_", f)]
    except Exception:
        staged = []

    if not staged:
        print("pre-commit: no nucleus .md files staged")
        return 0

    print(f"pre-commit: validating {len(staged)} staged artifact(s)...")
    errors = 0
    for path in staged:
        issues = validate_artifact(path)
        error_count = sum(1 for i in issues if i["level"] == "ERROR")
        if error_count:
            print(f"  ❌ {path}")
            for i in issues:
                if i["level"] == "ERROR":
                    print(f"    ✗ [{i['code']}] {i['msg']}")
            errors += error_count
        else:
            print(f"  ✅ {path}")

    if errors:
        print(f"\npre-commit: BLOCKED — {errors} error(s). Fix before committing.")
    else:
        print(f"\npre-commit: PASS — {len(staged)} artifact(s) valid.")
    return errors


def run_validate_all() -> int:
    """Validate all nucleus artifacts in the repo."""
    total = 0
    errors = 0
    warnings = 0
    clean = 0

    for ndir in sorted(NUCLEUS_DIRS):
        for md in sorted(ndir.rglob("*.md")):
            # Skip compiled/, README, non-artifact files
            if ("compiled" in str(md) or md.name.startswith("_")
                    or md.name.lower() == "readme.md"):
                continue
            total += 1
            issues = validate_artifact(str(md))
            e = sum(1 for i in issues if i["level"] == "ERROR")
            w = sum(1 for i in issues if i["level"] == "WARN")
            if e:
                errors += e
                rel = md.relative_to(CEX_ROOT)
                print(f"  ❌ {rel}")
                for i in issues:
                    if i["level"] == "ERROR":
                        print(f"    ✗ [{i['code']}] {i['msg']}")
            elif w:
                warnings += w
            else:
                clean += 1

    print(f"\n{'='*60}")
    print(f"  Validated: {total} artifacts")
    print(f"  Clean:     {clean}")
    print(f"  Warnings:  {warnings}")
    print(f"  Errors:    {errors}")
    print(f"{'='*60}")
    return errors


def install_git_hook():
    """Install git pre-commit hook."""
    hooks_dir = CEX_ROOT / ".git" / "hooks"
    if not hooks_dir.exists():
        print("ERROR: .git/hooks/ not found. Is this a git repo?")
        return 1

    hook_path = hooks_dir / "pre-commit"
    hook_content = """#!/bin/sh
# CEX pre-commit hook — validates staged nucleus artifacts
python _tools/cex_hooks.py pre-commit
exit $?
"""
    hook_path.write_text(hook_content, encoding="utf-8")
    # Make executable on Unix
    try:
        os.chmod(str(hook_path), 0o755)
    except Exception:
        pass
    print(f"✅ Git pre-commit hook installed at {hook_path}")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "pre-save":
        if not args:
            print("Usage: cex_hooks.py pre-save FILE [FILE...]")
            sys.exit(1)
        sys.exit(run_pre_save(args))

    elif cmd == "post-save":
        if not args:
            print("Usage: cex_hooks.py post-save FILE [FILE...]")
            sys.exit(1)
        sys.exit(run_post_save(args))

    elif cmd == "pre-commit":
        sys.exit(run_pre_commit())

    elif cmd == "validate":
        if not args:
            print("Usage: cex_hooks.py validate FILE [FILE...]")
            sys.exit(1)
        sys.exit(run_pre_save(args))

    elif cmd == "validate-all":
        sys.exit(run_validate_all())

    elif cmd == "install":
        sys.exit(install_git_hook())

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
