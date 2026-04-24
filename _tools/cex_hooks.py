#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_hooks.py -- Pre/post build validation hooks for CEX artifacts.

Hooks:
  pre-save   FILE   -- Validate artifact before saving (frontmatter, naming, size)
  post-save  FILE   -- Compile + check after saving
  pre-commit        -- Validate all staged .md files (git hook)
  validate   FILE+  -- Full validation of one or more artifacts
  validate-all      -- Check every nucleus artifact in repo
  install           -- Install git pre-commit hook

Usage:
  python _tools/cex_hooks.py pre-save N07_admin/P02_model/agent_admin.md
  python _tools/cex_hooks.py post-save N01_intelligence/P02_model/agent_intelligence.md
  python _tools/cex_hooks.py pre-commit
  python _tools/cex_hooks.py validate N07_admin/P02_model/agent_admin.md
  python _tools/cex_hooks.py validate-all
  python _tools/cex_hooks.py install
"""

import argparse
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

# Valid 8f frontmatter pattern: F[1-8]_lowercase (e.g. F3_inject, F1_constrain)
VALID_8F_PATTERN = re.compile(r"^F[1-8]_[a-z]+$")

# Pillar prefix pattern
PILLAR_PATTERN = re.compile(r"^P\d{2}$")

# Nucleus artifact directories
NUCLEUS_DIRS = [d for d in CEX_ROOT.iterdir()
                if d.is_dir() and re.match(r"N\d{2}_", d.name)]


# ---------------------------------------------------------------------------
# Builder Lifecycle Hooks (Phase 2C -- Runtime Evolution)
# ---------------------------------------------------------------------------


def hook_validate_inputs(builder_id: str, input_data: dict) -> dict:
    """Built-in pre_build hook: validate required frontmatter fields exist."""
    issues = []
    fm = input_data.get("frontmatter", {})
    for field in REQUIRED_FM:
        if field not in fm:
            issues.append(f"Missing required field: {field}")
    return {
        "proceed": len(issues) == 0,
        "modified_input": input_data,
        "issues": issues,
    }


def hook_compile_and_index(builder_id: str, output_data: dict) -> dict:
    """Built-in post_build hook: compile artifact + rebuild index."""
    path = output_data.get("path", "")
    if not path:
        return {"accept": True, "modified_output": output_data}

    ok, msg = compile_artifact(path)
    output_data["compiled"] = ok
    output_data["compile_msg"] = msg

    # Try index rebuild
    index_script = CEX_ROOT / "_tools" / "cex_index.py"
    if index_script.exists():
        try:
            subprocess.run(
                [sys.executable, str(index_script)],
                capture_output=True, text=True, timeout=30
            )
            output_data["indexed"] = True
        except Exception:
            output_data["indexed"] = False

    return {"accept": True, "modified_output": output_data}


def hook_log_quality_failure(builder_id: str, score: float, gates_failed: list[str]) -> dict:
    """Built-in on_quality_fail hook: log failure to learning records."""
    import json as _json
    import time as _time

    lr_dir = CEX_ROOT / ".cex" / "learning_records"
    lr_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": _time.strftime("%Y-%m-%dT%H:%M:%S"),
        "builder_id": builder_id,
        "event": "quality_failure",
        "score": score,
        "gates_failed": gates_failed,
    }
    fname = f"qf_{builder_id}_{_time.strftime('%Y%m%d_%H%M%S')}.json"
    try:
        (lr_dir / fname).write_text(
            _json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except OSError:
        pass

    return {"retry": score >= 5.0, "feedback": f"Score {score:.1f}, failed: {', '.join(gates_failed)}"}


def hook_retry_with_feedback(builder_id: str, score: float, gates_failed: list[str]) -> dict:
    """Built-in on_quality_fail hook: retry with structured feedback."""
    feedback_lines = [
        f"Quality score {score:.1f} is below threshold.",
        f"Failed gates: {', '.join(gates_failed)}" if gates_failed else "",
        "Focus on:",
    ]
    for gate in gates_failed[:3]:
        if gate.startswith("H01"):
            feedback_lines.append("  - Fix YAML frontmatter (must parse cleanly)")
        elif gate.startswith("H02"):
            feedback_lines.append("  - Fix id field (must match pattern)")
        elif gate.startswith("H03"):
            feedback_lines.append("  - Fix kind field (must match target)")
        elif gate.startswith("H04"):
            feedback_lines.append("  - Set quality: null (never self-score)")
        else:
            feedback_lines.append(f"  - Address {gate}")

    return {
        "retry": True,
        "feedback": "\n".join(line for line in feedback_lines if line),
    }


# Registry of built-in hook functions
BUILTIN_HOOKS = {
    "validate_inputs": hook_validate_inputs,
    "compile_and_index": hook_compile_and_index,
    "log_quality_failure": hook_log_quality_failure,
    "retry_with_feedback": hook_retry_with_feedback,
}


def execute_hook(hook_name: str | None, hook_type: str, **kwargs) -> dict | None:
    """Execute a named hook function.

    Args:
        hook_name: Name of the hook function (from bld_config.hooks), or None to skip.
        hook_type: One of pre_build, post_build, on_error, on_quality_fail.
        **kwargs: Arguments passed to the hook function.

    Returns:
        Hook result dict, or None if hook is null/skipped.
    """
    if not hook_name:
        return None

    func = BUILTIN_HOOKS.get(hook_name)
    if not func:
        return {"error": f"Unknown hook: {hook_name}"}

    try:
        return func(**kwargs)
    except Exception as e:
        return {"error": f"Hook '{hook_name}' failed: {e}"}


def run_builder_hooks(hooks_config: dict | None, hook_type: str, **kwargs) -> dict | None:
    """Run the appropriate hook from a builder's hooks config.

    Args:
        hooks_config: The hooks dict from bld_config (pre_build, post_build, etc.)
        hook_type: Which hook to run.
        **kwargs: Arguments for the hook.

    Returns:
        Hook result, or None if no hook configured.
    """
    if not hooks_config or not isinstance(hooks_config, dict):
        return None

    hook_name = hooks_config.get(hook_type)
    return execute_hook(hook_name, hook_type, **kwargs)


# ---------------------------------------------------------------------------
# Artifact Validation
# ---------------------------------------------------------------------------


def validate_artifact(path: str, content: str = None) -> list[dict]:
    """Validate a single artifact. Returns list of {level, code, msg}."""
    issues = []
    p = Path(path)

    if content is None:
        if not p.exists():
            return [{"level": "ERROR", "code": "E01", "msg": f"File not found: {path}"}]
        content = p.read_text(encoding="utf-8")

    size = len(content.encode("utf-8"))

    # E01: Has frontmatter (skip tpl_* files -- intentional mustache placeholders)
    if p.name.startswith("tpl_"):
        return issues
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

    # W06: 8f field presence and format
    if "8f" not in fm:
        issues.append({"level": "WARN", "code": "W06", "msg": "Missing recommended: 8f (primary 8F function)"})
    else:
        val_8f = str(fm.get("8f", ""))
        if val_8f and not VALID_8F_PATTERN.match(val_8f):
            issues.append({"level": "WARN", "code": "W06",
                           "msg": "8f value '%s' does not match F[1-8]_[a-z]+ pattern" % val_8f})

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
            print(f"[FAIL] {path}: {error_count} errors, {warn_count} warnings")
            errors += error_count
        elif warn_count:
            print(f"[WARN]  {path}: {warn_count} warnings")
        else:
            print(f"[OK] {path}: valid")

        for i in issues:
            if i["level"] in ("ERROR", "WARN"):
                symbol = "  [X]" if i["level"] == "ERROR" else "  !"
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
            print(f"[FAIL] {path}: {error_count} validation errors -- skipping compile")
            for i in issues:
                if i["level"] == "ERROR":
                    print(f"  [X] [{i['code']}] {i['msg']}")
            errors += error_count
            continue

        # Compile
        ok, output = compile_artifact(path)
        if ok:
            print(f"[OK] {path}: valid + compiled")
        else:
            print(f"[WARN]  {path}: valid but compile failed: {output}")

    return errors


def check_encoding(staged_files: list[str]) -> int:
    """Check staged .py/.ps1 files for non-ASCII in executable output lines.

    Rejects any .py file with non-ASCII in print()/logging calls,
    and any .ps1 file with non-ASCII in Write-Host/Write-Output calls.
    Returns error count.
    """
    CODE_EXTENSIONS = {".py", ".ps1", ".sh", ".cmd", ".bat"}
    errors = 0
    code_files = [f for f in staged_files
                  if any(f.endswith(ext) for ext in CODE_EXTENSIONS)]

    if not code_files:
        return 0

    print("  encoding_check: scanning %d code file(s)..." % len(code_files))
    for path in code_files:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                for line_num, line in enumerate(fh, 1):
                    for ch in line:
                        cp = ord(ch)
                        if cp > 127:
                            # Allow BOM at start of .ps1
                            if cp == 0xFEFF and line_num == 1:
                                continue
                            errors += 1
                            if errors <= 5:
                                print(f"    [FAIL] {path}:{line_num} "
                                      f"U+{cp:04X} (non-ASCII)")
        except (UnicodeDecodeError, OSError):
            errors += 1
            print(f"    [FAIL] {path}: cannot read as UTF-8")

    if errors > 5:
        print(f"    ... and {errors - 5} more encoding issues")
    if errors == 0:
        print("  encoding_check: PASS")
    return errors


def check_ps_parse(staged_files: list[str]) -> int:
    """Validate PowerShell syntax for staged .ps1 files.

    Uses PowerShell's parser to check for syntax errors.
    Returns error count.
    """
    ps1_files = [f for f in staged_files if f.endswith(".ps1")]
    if not ps1_files:
        return 0

    print("  ps_parse_check: validating %d .ps1 file(s)..." % len(ps1_files))
    errors = 0
    for path in ps1_files:
        try:
            # Use PowerShell AST parser for syntax validation.
            # Path is embedded in the script (quoted) and piped
            # via stdin to avoid -Command argument mangling.
            abs_path = str(Path(path).resolve()).replace("'", "''")
            ps_script = (
                "$errors = $null; "
                "$null = [System.Management.Automation.Language.Parser]"
                "::ParseFile('%s', [ref]$null, [ref]$errors); "
                "if ($errors.Count -gt 0) { "
                "$errors | ForEach-Object { Write-Output $_.Message }; "
                "exit 1 } else { exit 0 }"
            ) % abs_path
            result = subprocess.run(
                ["powershell", "-NoProfile", "-Command", "-"],
                input=ps_script,
                capture_output=True, text=True, timeout=15
            )
            if result.returncode != 0:
                errors += 1
                msg = result.stdout.strip() or result.stderr.strip()
                print(f"    [FAIL] {path}: {msg[:200]}")
        except Exception as e:
            # PowerShell not available -- skip gracefully
            print(f"    [SKIP] {path}: PowerShell not available ({e})")

    if errors == 0:
        print("  ps_parse_check: PASS")
    return errors


def check_sanitize(staged_files: list[str]) -> int:
    """Run cex_sanitize.py --check on _tools/ when staged .py files exist there.

    This catches non-ASCII that check_encoding also flags, but provides
    actionable replacement suggestions (em-dash -> --, smart quotes -> straight, etc.).
    Returns error count (0 = clean, 1 = issues found).
    """
    py_in_tools = [f for f in staged_files
                   if f.endswith(".py") and f.replace("\\", "/").startswith("_tools/")]
    if not py_in_tools:
        return 0

    sanitize_script = CEX_ROOT / "_tools" / "cex_sanitize.py"
    if not sanitize_script.exists():
        print("  sanitize_check: SKIP (cex_sanitize.py not found)")
        return 0

    print("  sanitize_check: running cex_sanitize.py --check --scope _tools/ ...")
    try:
        result = subprocess.run(
            [sys.executable, str(sanitize_script), "--check", "--scope", "_tools/"],
            capture_output=True, text=True, timeout=30
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.returncode != 0:
            print("    [FAIL] cex_sanitize found non-ASCII in _tools/")
            print("    Fix with: python _tools/cex_sanitize.py --fix --scope _tools/")
            return 1
        else:
            print("  sanitize_check: PASS")
            return 0
    except Exception as e:
        print("  sanitize_check: SKIP (%s)" % e)
        return 0


def check_yaml_valid(staged_files: list[str]) -> int:
    """Validate YAML syntax for staged .yaml/.yml files.

    Checks that all staged YAML files parse without errors.
    Returns error count.
    """
    yaml_files = [f for f in staged_files
                  if f.endswith(".yaml") or f.endswith(".yml")]
    if not yaml_files:
        return 0

    print("  yaml_valid_check: validating %d YAML file(s)..." % len(yaml_files))
    errors = 0

    try:
        import yaml as _yaml
    except ImportError:
        print("  yaml_valid_check: SKIP (pyyaml not installed)")
        return 0

    for path in yaml_files:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                _yaml.safe_load(fh)
        except _yaml.YAMLError as e:
            errors += 1
            # Extract just the problem description
            msg = str(e).split("\n")[0][:200]
            print(f"    [FAIL] {path}: {msg}")
        except OSError as e:
            errors += 1
            print(f"    [FAIL] {path}: {e}")

    if errors == 0:
        print("  yaml_valid_check: PASS")
    return errors


def check_wave_validator(staged_files: list[str]) -> int:
    """Run cex_wave_validator.py on staged builder ISOs.

    Catches 7 systemic defects (llm_function mismatch, self-scored quality,
    id pattern issues, missing domain keywords, foreign-domain leakage,
    unresolved placeholders, incomplete frontmatter).
    Returns error count (0 = clean, 1 = any failures).
    """
    iso_staged = [f for f in staged_files
                  if f.endswith(".md")
                  and "archetypes/builders/" in f.replace("\\", "/")
                  and Path(f).name.startswith("bld_")]
    if not iso_staged:
        return 0

    validator = CEX_ROOT / "_tools" / "cex_wave_validator.py"
    if not validator.exists():
        print("  wave_validator_check: SKIP (cex_wave_validator.py not found)")
        return 0

    print("  wave_validator_check: validating %d staged ISO(s)..." % len(iso_staged))
    try:
        result = subprocess.run(
            [sys.executable, str(validator), "--staged"],
            capture_output=True, text=True, timeout=60,
        )
        out = result.stdout.strip()
        if out:
            for line in out.split("\n"):
                print("    " + line)
        if result.returncode != 0:
            print("    [FAIL] cex_wave_validator found ISO defects")
            return 1
        print("  wave_validator_check: PASS")
        return 0
    except Exception as e:
        print("  wave_validator_check: SKIP (%s)" % e)
        return 0


def check_kinds_meta_ascii(staged_files: list) -> int:
    """Auto-sanitize .cex/kinds_meta.json to pure ASCII if staged.

    Python 3.14 on Windows defaults to cp1252 for open() without encoding=.
    Non-ASCII bytes in kinds_meta.json crash any code that reads it without
    encoding='utf-8' kwarg. Re-serialize with ensure_ascii=True (escapes
    non-ASCII to \\uXXXX) to make the file cp1252-safe.
    """
    import json as _json
    target = ".cex/kinds_meta.json"
    if target not in staged_files and target.replace("/", "\\") not in staged_files:
        return 0
    path = CEX_ROOT / ".cex" / "kinds_meta.json"
    if not path.exists():
        return 0
    try:
        raw = path.read_bytes()
    except Exception:
        return 0
    # Detect non-ASCII bytes
    if all(b < 128 for b in raw):
        return 0  # Already clean
    # Decode + re-serialize
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            s = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        print("  [FAIL] kinds_meta.json: unable to decode")
        return 1
    try:
        d = _json.loads(s)
    except _json.JSONDecodeError as e:
        print(f"  [FAIL] kinds_meta.json: invalid JSON ({e})")
        return 1
    out = _json.dumps(d, ensure_ascii=True, indent=2, sort_keys=False)
    path.write_text(out, encoding="utf-8")
    # Re-stage the sanitized file
    try:
        subprocess.run(["git", "add", target], check=True, timeout=10,
                       capture_output=True)
        print(f"  [AUTO-FIX] kinds_meta.json sanitized to ASCII ({len(d)} kinds)")
    except Exception as e:
        print(f"  [WARN] kinds_meta.json sanitized but re-stage failed: {e}")
    return 0


# Repo root whitelist -- any NEW file at repo root must match one of these.
# Generator misfires (no pillar path resolution) and git add -A sweeps in cex_auto*.py
# created orphan root files like `core`, `phases`, `quality_gate`, and
# `- Keep and complete YAML frontmatter` (LLM prompt echoed as filename).
# See _reports/polish/w2_consolidation.md for the cleanup that motivated this gate.
ROOT_WHITELIST = {
    "CLAUDE.md", "README.md", "QUICKSTART.md", "CONTRIBUTING.md",
    "CHANGELOG.md", "LICENSE", "MIT_LICENSE", "CODE_OF_CONDUCT.md", "SECURITY.md",
    ".gitignore", ".gitattributes", ".editorconfig", ".env.example",
    "requirements.txt", "requirements-llm.txt", "pyproject.toml",
    "setup.py", "setup.cfg", "Makefile", "package.json", "package-lock.json",
    "tsconfig.json", ".mcp.json", ".mcp-n07.json",
    "n01_task.md", "n02_task.md", "n03_task.md", "n04_task.md",
    "n05_task.md", "n06_task.md", "n07_task.md",
}


def check_root_writes(staged_files: list[str]) -> int:
    """Block NEW files being committed at repo root unless whitelisted.

    Motivation: generators (mostly LLM writers without pillar-path resolution)
    kept dropping artifacts at the repo root. cex_auto_research.py and
    cex_auto.py do `git add -A` in their yolo cycle, sweeping those strays
    into `[AUTO] cycle N` commits. Result: files like `core`, `phases`,
    `quality_gate`, or even `- Keep and complete YAML frontmatter` (LLM
    echoing a prompt instruction as filename) accumulated at front-page.

    This gate only fires on ADDITIONS (A). Modifying an existing whitelisted
    root file is fine. Nested paths (anything with `/` or `\\`) are ignored --
    pillar dirs, _tools/, _reports/, etc. are pillar-owned and safe.
    """
    try:
        result = subprocess.run(
            ["git", "dif", "--cached", "--name-only", "--diff-filter=A"],
            capture_output=True, text=True, timeout=10
        )
        added = [f.strip() for f in result.stdout.strip().split("\n")
                 if f.strip()]
    except Exception:
        return 0

    errors = 0
    for f in added:
        # Normalize separators (git on Windows may emit either)
        norm = f.replace("\\", "/")
        # Skip nested paths -- this check only guards the REPO ROOT
        if "/" in norm:
            continue
        if norm in ROOT_WHITELIST:
            continue
        print(f"  [FAIL] root-write: '{norm}' is not in ROOT_WHITELIST")
        print(f"         Generator misfire? Move to a pillar dir (P{{01-12}}_*/, N{{00-07}}_*/, _tools/, _docs/).")
        print(f"         If intentional, add '{norm}' to ROOT_WHITELIST in _tools/cex_hooks.py.")
        errors += 1
    return errors


def run_pre_commit() -> int:
    """Pre-commit hook: validate staged files.

    Checks:
    1. Artifact validation (frontmatter, naming) for staged .md in N0*/
    2. Encoding check: reject non-ASCII in staged .py/.ps1/.sh/.cmd
    3. PowerShell parse: AST validation for staged .ps1
    4. YAML validation: syntax check for staged .yaml/.yml
    5. Sanitize check: cex_sanitize.py --check on staged _tools/*.py
    6. Wave validator: 7 systemic checks on staged builder ISOs
    7. kinds_meta.json ASCII sanitation
    8. Root-write gate: block orphan files at repo root (whitelist-based)
    """
    try:
        result = subprocess.run(
            ["git", "dif", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True, timeout=10
        )
        all_staged = [f.strip() for f in result.stdout.strip().split("\n")
                      if f.strip()]
    except Exception:
        all_staged = []

    if not all_staged:
        print("pre-commit: no files staged")
        return 0

    errors = 0

    # 1. Artifact validation (existing behavior)
    # Exclude README.md (fractal nav docs, not typed artifacts) and agent_card_*.md
    # that live at nucleus root (they're configured to allow bare frontmatter).
    md_staged = [f for f in all_staged
                 if f.endswith(".md") and re.match(r"N\d{2}_", f)
                 and not f.endswith("/README.md")
                 and not f.endswith("\\README.md")]
    if md_staged:
        print(f"pre-commit: validating {len(md_staged)} staged artifact(s)...")
        for path in md_staged:
            issues = validate_artifact(path)
            error_count = sum(1 for i in issues if i["level"] == "ERROR")
            if error_count:
                print(f"  [FAIL] {path}")
                for i in issues:
                    if i["level"] == "ERROR":
                        print(f"    [X] [{i['code']}] {i['msg']}")
                errors += error_count
            else:
                print(f"  [OK] {path}")

    # 2. Encoding check -- non-ASCII in executable code
    errors += check_encoding(all_staged)

    # 3. PowerShell parse check
    errors += check_ps_parse(all_staged)

    # 4. YAML validation
    errors += check_yaml_valid(all_staged)

    # 5. Sanitize check -- cex_sanitize.py on staged _tools/*.py
    errors += check_sanitize(all_staged)

    # 6. Wave validator -- 7 systemic checks on staged builder ISOs
    errors += check_wave_validator(all_staged)

    # 7. Auto-sanitize kinds_meta.json (cp1252-safe via ensure_ascii=True)
    errors += check_kinds_meta_ascii(all_staged)

    # 8. Root-write gate -- block generator-misfire orphans at repo root
    errors += check_root_writes(all_staged)

    # 9. Secret scan -- block live API keys / tokens in staged files
    errors += check_secret_scan(all_staged)

    if errors:
        print(f"\npre-commit: BLOCKED -- {errors} error(s). Fix before committing.")
    else:
        total = len(all_staged)
        print(f"\npre-commit: PASS -- {total} file(s) checked.")
    return errors


SECRET_PATTERNS = [
    ("anthropic_key", re.compile(r"sk-ant-api\d{2}-[A-Za-z0-9_-]{60,}")),
    ("openai_key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{40,}")),
    ("github_token", re.compile(r"ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{82}")),
    ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("google_key", re.compile(r"AIzaSy[A-Za-z0-9_-]{33}")),
    ("cerebras_key", re.compile(r"csk-[a-z0-9]{40,}")),
    ("slack_token", re.compile(r"xox[bpa]-[A-Za-z0-9-]{50,}")),
    ("private_key", re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
]
SECRET_PLACEHOLDERS = {
    "ghp_1234567890abcdef1234567890abcdef1234",
    "AKIAXXXXXXXXXXXXXXXX",
}
SECRET_ALLOWLIST_MARKER = "allowlist-secret"
SECRET_SAFE_PATH_PREFIXES = (
    "archetypes/builders/",  # builder examples = documented placeholders
    "_reports/audit/",       # gitignored but defensive
    ".cex/retriever_index.json",
)


def check_secret_scan(staged: list[str]) -> int:
    """Scan staged files for live API keys / tokens. Returns error count.

    Allowlist:
    - Files inside builder ISO example dirs (placeholders only).
    - Lines containing the allowlist-secret marker.
    - Known placeholder strings (ghp_1234..., AKIAXXX...).
    """
    errors = 0
    for path in staged:
        norm = path.replace("\\", "/")
        if any(norm.startswith(p) or norm == p for p in SECRET_SAFE_PATH_PREFIXES):
            continue
        try:
            text = Path(path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if SECRET_ALLOWLIST_MARKER in line:
                continue
            for name, pat in SECRET_PATTERNS:
                m = pat.search(line)
                if not m:
                    continue
                if m.group(0) in SECRET_PLACEHOLDERS:
                    continue
                print(f"  [FAIL] secret-scan: {name} match in {path}:{line_no}")
                print("         Rotate the secret + remove from staged file.")
                print(f"         Allowlist with '# {SECRET_ALLOWLIST_MARKER}' on the line if intentional.")
                errors += 1
    return errors


def run_validate_all() -> int:
    """Validate all nucleus artifacts in the repo."""
    total = 0
    errors = 0
    warnings = 0
    clean = 0

    for ndir in sorted(NUCLEUS_DIRS):
        for md in sorted(ndir.rglob("*.md")):
            # Skip compiled/, README, non-artifact files, legacy library subdirs
            md_str = str(md)
            if ("compiled" in md_str or md.name.startswith("_")
                    or md.name.lower() == "readme.md"
                    or "library/infrastructure" in md_str.replace("\\", "/")
                    or "library/sources" in md_str.replace("\\", "/")
                    or "library/specs" in md_str.replace("\\", "/")):
                continue
            total += 1
            issues = validate_artifact(str(md))
            e = sum(1 for i in issues if i["level"] == "ERROR")
            w = sum(1 for i in issues if i["level"] == "WARN")
            if e:
                errors += e
                rel = md.relative_to(CEX_ROOT)
                print(f"  [FAIL] {rel}")
                for i in issues:
                    if i["level"] == "ERROR":
                        print(f"    [X] [{i['code']}] {i['msg']}")
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
# CEX pre-commit hook -- validates staged nucleus artifacts
python _tools/cex_hooks.py pre-commit
exit $?
"""
    hook_path.write_text(hook_content, encoding="utf-8")
    # Make executable on Unix
    try:
        os.chmod(str(hook_path), 0o755)
    except Exception:
        pass
    print(f"[OK] Git pre-commit hook installed at {hook_path}")
    return 0


def main():
    known_commands = {"pre-save", "post-save", "pre-commit", "validate", "validate-all", "install"}
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-") and sys.argv[1] not in known_commands:
        print(f"Unknown command: {sys.argv[1]}")
        print(__doc__)
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="cmd")

    for command in ("pre-save", "post-save", "validate"):
        subparser = subparsers.add_parser(command, help=f"Run the {command} hook.")
        subparser.add_argument("paths", nargs="*", help="One or more artifact paths.")

    subparsers.add_parser("pre-commit", help="Validate staged files.")
    subparsers.add_parser("validate-all", help="Validate all nucleus artifacts.")
    subparsers.add_parser("install", help="Install the git pre-commit hook.")

    parsed, _ = parser.parse_known_args()
    if not parsed.cmd:
        print(__doc__)
        sys.exit(1)

    cmd = parsed.cmd
    args = getattr(parsed, "paths", [])

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

if __name__ == "__main__":
    main()
