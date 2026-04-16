#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Setup Validator -- Validates a fresh PC is ready for CEX.

Usage:
  python _tools/cex_setup_validator.py              # full check, human-readable
  python _tools/cex_setup_validator.py --json        # machine-readable output
  python _tools/cex_setup_validator.py --fix         # attempt auto-fix for FAIL items
  python _tools/cex_setup_validator.py --category runtime  # check only one category
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Status constants
# ---------------------------------------------------------------------------
OK = "OK"
FAIL = "FAIL"
INFO = "INFO"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_cmd(cmd: list[str], timeout: int = 30) -> tuple[int, str, str]:
    """Run a command, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, shell=False
        )
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except FileNotFoundError:
        return -1, "", "command not found"
    except subprocess.TimeoutExpired:
        return -2, "", "timeout"
    except Exception as e:
        return -3, "", str(e)


def run_shell(cmd_str: str, timeout: int = 30) -> tuple[int, str, str]:
    """Run a command via shell, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(
            cmd_str, capture_output=True, text=True, timeout=timeout, shell=True
        )
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -2, "", "timeout"
    except Exception as e:
        return -3, "", str(e)


def parse_version(text: str) -> tuple[tuple[int, int, int] | None, str]:
    """Extract first version-like string (x.y.z or x.y) from text."""
    m = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text)
    if m:
        major, minor = int(m.group(1)), int(m.group(2))
        patch = int(m.group(3)) if m.group(3) else 0
        return (major, minor, patch), m.group(0)
    return None, ""


def version_gte(
    ver_tuple: tuple[int, int, int] | None, min_tuple: tuple[int, int, int]
) -> bool:
    """True if ver_tuple >= min_tuple."""
    if ver_tuple is None:
        return False
    return ver_tuple >= min_tuple


# ---------------------------------------------------------------------------
# Check result accumulator
# ---------------------------------------------------------------------------

class CheckResult:
    def __init__(
        self,
        category: str,
        name: str,
        status: str,
        detail: str = "",
        fix_cmd: str | None = None,
    ) -> None:
        self.category = category
        self.name = name
        self.status = status   # OK, FAIL, INFO
        self.detail = detail
        self.fix_cmd = fix_cmd  # shell command string if auto-fixable

    def to_dict(self) -> dict[str, str]:
        """Serialize the check result for machine-readable output."""
        d = {
            "category": self.category,
            "name": self.name,
            "status": self.status,
            "detail": self.detail,
        }
        if self.fix_cmd:
            d["fix_cmd"] = self.fix_cmd
        return d

    def display(self) -> str:
        """Format the check result for human-readable output."""
        tag = {"OK": "[OK]", "FAIL": "[FAIL]", "INFO": "[--]"}[self.status]
        line = "  %s %s" % (tag, self.detail if self.detail else self.name)
        return line


# ---------------------------------------------------------------------------
# Category: RUNTIME
# ---------------------------------------------------------------------------

def check_runtime() -> list[CheckResult]:
    """Validate core runtime binaries and minimum supported versions."""
    results = []

    # Python >= 3.12
    rc, out, err = run_cmd([sys.executable, "--version"])
    combined = out or err
    ver, ver_str = parse_version(combined)
    if version_gte(ver, (3, 12, 0)):
        results.append(CheckResult("RUNTIME", "python", OK,
                                   "Python %s (>= 3.12)" % ver_str))
    else:
        results.append(CheckResult("RUNTIME", "python", FAIL,
                                   "Python %s (need >= 3.12)" % (ver_str or "not found")))

    # Node >= 18
    rc, out, err = run_cmd(["node", "--version"])
    ver, ver_str = parse_version(out or err)
    if version_gte(ver, (18, 0, 0)):
        results.append(CheckResult("RUNTIME", "node", OK,
                                   "Node %s (>= 18)" % ver_str))
    else:
        results.append(CheckResult("RUNTIME", "node", FAIL,
                                   "Node %s (need >= 18)" % (ver_str or "not found")))

    # Git >= 2.40
    rc, out, err = run_cmd(["git", "--version"])
    ver, ver_str = parse_version(out or err)
    if version_gte(ver, (2, 40, 0)):
        results.append(CheckResult("RUNTIME", "git", OK,
                                   "Git %s (>= 2.40)" % ver_str))
    else:
        results.append(CheckResult("RUNTIME", "git", FAIL,
                                   "Git %s (need >= 2.40)" % (ver_str or "not found")))

    # uv/uvx
    rc, out, err = run_cmd(["uvx", "--version"])
    combined = out or err
    ver, ver_str = parse_version(combined)
    if rc == 0 and ver:
        results.append(CheckResult("RUNTIME", "uvx", OK,
                                   "uvx %s" % ver_str))
    else:
        results.append(CheckResult("RUNTIME", "uvx", FAIL,
                                   "uvx not found"))

    return results


# ---------------------------------------------------------------------------
# Category: PACKAGES
# ---------------------------------------------------------------------------

def check_packages(fix_mode: bool = False) -> list[CheckResult]:
    """Validate required Python packages and the Claude CLI."""
    results = []
    pip_pkgs = [
        ("pyyaml", "yaml", "pyyaml"),
        ("tiktoken", "tiktoken", "tiktoken"),
        ("numpy", "numpy", "numpy"),
        ("scikit-learn", "sklearn", "scikit-learn"),
    ]

    for label, import_name, pip_name in pip_pkgs:
        rc, out, err = run_cmd(
            [sys.executable, "-c",
             "import %s; print(getattr(%s, '__version__', 'ok'))" % (import_name, import_name)]
        )
        if rc == 0:
            ver_str = out.strip().split("\n")[-1] if out.strip() else "ok"
            results.append(CheckResult("PACKAGES", label, OK,
                                       "%s %s" % (label, ver_str)))
        else:
            fix = "pip install %s" % pip_name
            results.append(CheckResult("PACKAGES", label, FAIL,
                                       "%s not installed (run: %s)" % (label, fix),
                                       fix_cmd=fix))

    # Claude Code CLI
    rc, out, err = run_cmd(["claude", "--version"])
    combined = out or err
    ver, ver_str = parse_version(combined)
    if rc == 0:
        results.append(CheckResult("PACKAGES", "claude-cli", OK,
                                   "Claude Code %s" % (ver_str or "ok")))
    else:
        results.append(CheckResult("PACKAGES", "claude-cli", FAIL,
                                   "Claude Code CLI not found"))

    return results


# ---------------------------------------------------------------------------
# Category: MCP_SERVERS
# ---------------------------------------------------------------------------

def check_mcp_servers() -> list[CheckResult]:
    """Validate MCP server configs and probe their backing packages."""
    results = []
    mcp_files = sorted(ROOT.glob(".mcp-n0*.json"))

    for mcp_path in mcp_files:
        nucleus = mcp_path.stem.replace(".mcp-", "").upper()  # n01 -> N01
        try:
            data = json.loads(mcp_path.read_text(encoding="utf-8"))
        except Exception as e:
            results.append(CheckResult("MCP_SERVERS", nucleus, FAIL,
                                       "%s: parse error -- %s" % (nucleus, str(e))))
            continue

        servers = data.get("mcpServers", {})
        for name, cfg in servers.items():
            cmd = cfg.get("command", "")
            args = cfg.get("args", [])
            # Extract the package name from args
            pkg = ""
            for a in args:
                if a == "-y" or a == "-c" or a.startswith("--"):
                    continue
                if a in ("npx", "uvx", "cmd", "/c"):
                    continue
                pkg = a
                break

            if not pkg:
                results.append(CheckResult("MCP_SERVERS", name, INFO,
                                           "%s: %s -- could not determine package" % (nucleus, name)))
                continue

            # Check if the underlying tool (npx/uvx) exists
            base_cmd = cmd if cmd not in ("cmd",) else "npx"
            if not shutil.which(base_cmd):
                results.append(CheckResult("MCP_SERVERS", name, FAIL,
                                           "%s: %s -- %s not found" % (nucleus, name, base_cmd)))
                continue

            # For npx packages, check with `npx -y <pkg> --help` (quick probe)
            # For uvx packages, check with `uvx <pkg> --version`
            if base_cmd == "npx":
                # Check if npm can resolve the package (npm is a .cmd on Windows)
                clean_pkg = pkg.split("@latest")[0] if pkg.endswith("@latest") else pkg
                probe_rc, probe_out, probe_err = run_shell(
                    "npm view %s version" % clean_pkg, timeout=15
                )
                if probe_rc == 0 and probe_out.strip():
                    ver_str = probe_out.strip().split("\n")[-1]
                    results.append(CheckResult("MCP_SERVERS", name, OK,
                                               "%s: %s %s" % (nucleus, name, ver_str)))
                else:
                    results.append(CheckResult("MCP_SERVERS", name, FAIL,
                                               "%s: %s -- npm cannot resolve '%s'" % (
                                                   nucleus, name, clean_pkg)))
            elif base_cmd == "uvx":
                # Use pip index to check if the pypi package exists
                clean_pkg = pkg.split("@")[0]
                probe_rc, probe_out, _ = run_cmd(
                    [sys.executable, "-m", "pip", "index", "versions", clean_pkg],
                    timeout=15
                )
                if probe_rc == 0:
                    results.append(CheckResult("MCP_SERVERS", name, OK,
                                               "%s: %s (pypi ok)" % (nucleus, name)))
                else:
                    results.append(CheckResult("MCP_SERVERS", name, INFO,
                                               "%s: %s -- cannot verify '%s'" % (
                                                   nucleus, name, clean_pkg)))
            else:
                results.append(CheckResult("MCP_SERVERS", name, INFO,
                                           "%s: %s -- unknown runner '%s'" % (
                                               nucleus, name, base_cmd)))

    return results


# ---------------------------------------------------------------------------
# Category: ENV_VARS
# ---------------------------------------------------------------------------

ENV_VARS_SPEC = [
    ("ANTHROPIC_API_KEY", "Anthropic API (all nuclei)", False),
    ("GITHUB_TOKEN", "GitHub (N03, N05)", True),
    ("FIRECRAWL_API_KEY", "Firecrawl (N01, N04)", False),
    ("BRAVE_API_KEY", "Brave Search (N01)", False),
    ("SUPABASE_ACCESS_TOKEN", "Supabase (N04)", False),
    ("CANVA_CLIENT_ID", "Canva (N02, N03, N06)", False),
    ("CANVA_CLIENT_SECRET", "Canva (N02, N03, N06)", False),
    ("STRIPE_SECRET_KEY", "Stripe (N06)", False),
]


def check_env_vars() -> list[CheckResult]:
    """Inspect expected environment variables and classify missing ones."""
    results = []
    for var_name, desc, required in ENV_VARS_SPEC:
        val = os.environ.get(var_name)
        if val:
            results.append(CheckResult("ENV_VARS", var_name, OK,
                                       "%s (set)" % var_name))
        else:
            status = FAIL if required else INFO
            results.append(CheckResult("ENV_VARS", var_name, status,
                                       "%s (not set -- %s)" % (var_name, desc)))
    return results


# ---------------------------------------------------------------------------
# Category: STRUCTURE
# ---------------------------------------------------------------------------

def check_structure(fix_mode: bool = False) -> list[CheckResult]:
    """Validate expected repository directories and boot scripts."""
    results = []

    # Nucleus dirs
    for i in range(1, 8):
        ndir = ROOT / ("N%02d_%s" % (i, _nucleus_name(i)))
        # Just check N0x_* pattern
        matches = list(ROOT.glob("N%02d_*" % i))
        if matches:
            results.append(CheckResult("STRUCTURE", "N%02d" % i, OK,
                                       "N%02d dir exists" % i))
        else:
            results.append(CheckResult("STRUCTURE", "N%02d" % i, FAIL,
                                       "N%02d_* directory missing" % i))

    # Runtime dirs
    runtime_base = ROOT / ".cex" / "runtime"
    runtime_subdirs = [
        "handoffs", "signals", "pids", "proposals", "plans",
        "decisions", "locks", "outputs", "archive"
    ]
    for sd in runtime_subdirs:
        p = runtime_base / sd
        if p.is_dir():
            results.append(CheckResult("STRUCTURE", "runtime/%s" % sd, OK,
                                       ".cex/runtime/%s exists" % sd))
        else:
            fix = None
            if fix_mode:
                fix = "mkdir"
            results.append(CheckResult("STRUCTURE", "runtime/%s" % sd, FAIL,
                                       ".cex/runtime/%s missing" % sd, fix_cmd=fix))

    # Boot scripts
    for i in range(1, 7):
        bp = ROOT / "boot" / ("n%02d.ps1" % i)
        if bp.exists():
            results.append(CheckResult("STRUCTURE", "boot/n%02d.ps1" % i, OK,
                                       "boot/n%02d.ps1 exists" % i))
        else:
            results.append(CheckResult("STRUCTURE", "boot/n%02d.ps1" % i, FAIL,
                                       "boot/n%02d.ps1 missing" % i))

    # .claude dirs
    for subdir in ["rules", "commands", "agents"]:
        p = ROOT / ".claude" / subdir
        if p.is_dir():
            results.append(CheckResult("STRUCTURE", ".claude/%s" % subdir, OK,
                                       ".claude/%s/ exists" % subdir))
        else:
            results.append(CheckResult("STRUCTURE", ".claude/%s" % subdir, FAIL,
                                       ".claude/%s/ missing" % subdir))

    return results


def _nucleus_name(i: int) -> str:
    names = {
        1: "intelligence", 2: "marketing", 3: "engineering",
        4: "knowledge", 5: "operations", 6: "commercial", 7: "admin"
    }
    return names.get(i, "unknown")


# ---------------------------------------------------------------------------
# Category: GIT_HOOKS
# ---------------------------------------------------------------------------

def check_git_hooks(fix_mode: bool = False) -> list[CheckResult]:
    """Validate that the repository pre-commit hook is installed."""
    results = []
    hook_path = ROOT / ".git" / "hooks" / "pre-commit"
    if hook_path.exists():
        results.append(CheckResult("GIT_HOOKS", "pre-commit", OK,
                                   "pre-commit hook installed"))
    else:
        fix = "python _tools/cex_hooks.py install"
        results.append(CheckResult("GIT_HOOKS", "pre-commit", FAIL,
                                   "pre-commit hook not installed (run: %s)" % fix,
                                   fix_cmd=fix))
    return results


# ---------------------------------------------------------------------------
# Category: SYSTEM
# ---------------------------------------------------------------------------

def check_system() -> list[CheckResult]:
    """Validate host-level prerequisites such as disk space and ASCII hygiene."""
    results = []

    # Disk space > 1GB free
    try:
        usage = shutil.disk_usage(str(ROOT))
        free_gb = usage.free / (1024 ** 3)
        if free_gb > 1.0:
            results.append(CheckResult("SYSTEM", "disk_space", OK,
                                       "%.1f GB free (> 1 GB)" % free_gb))
        else:
            results.append(CheckResult("SYSTEM", "disk_space", FAIL,
                                       "%.2f GB free (need > 1 GB)" % free_gb))
    except Exception:
        results.append(CheckResult("SYSTEM", "disk_space", INFO,
                                   "could not check disk space"))

    # Power plan (Windows only)
    if sys.platform == "win32":
        rc, out, err = run_shell(
            "powercfg /query SCHEME_CURRENT SUB_SLEEP STANDBYIDLE", timeout=10
        )
        if rc == 0 and out:
            # Look for "Current AC Power Setting Index" line
            # 0x00000000 means never sleep
            m = re.search(r"Current AC Power Setting Index:\s*0x([0-9a-fA-F]+)", out)
            if m:
                val = int(m.group(1), 16)
                if val == 0:
                    results.append(CheckResult("SYSTEM", "sleep_ac", OK,
                                               "AC sleep: disabled (never)"))
                else:
                    minutes = val // 60 if val > 0 else val
                    results.append(CheckResult("SYSTEM", "sleep_ac", INFO,
                                               "AC sleep: %d seconds (%d min) -- consider disabling" % (
                                                   val, minutes)))
            else:
                results.append(CheckResult("SYSTEM", "sleep_ac", INFO,
                                           "could not parse sleep setting"))
        else:
            results.append(CheckResult("SYSTEM", "sleep_ac", INFO,
                                       "powercfg query failed"))

    # ASCII compliance
    sanitize_path = ROOT / "_tools" / "cex_sanitize.py"
    if sanitize_path.exists():
        rc, out, err = run_cmd(
            [sys.executable, str(sanitize_path), "--check", "--scope", "_tools/"],
            timeout=30
        )
        if rc == 0:
            results.append(CheckResult("SYSTEM", "ascii_compliance", OK,
                                       "ASCII compliance: _tools/ clean"))
        else:
            combined = (out + " " + err).strip()
            # Truncate for display
            if len(combined) > 100:
                combined = combined[:100] + "..."
            results.append(CheckResult("SYSTEM", "ascii_compliance", FAIL,
                                       "ASCII violations in _tools/ (%s)" % combined))
    else:
        results.append(CheckResult("SYSTEM", "ascii_compliance", INFO,
                                   "cex_sanitize.py not found -- cannot check"))

    return results


# ---------------------------------------------------------------------------
# Category: OLLAMA
# ---------------------------------------------------------------------------

OLLAMA_BINARY_PATHS = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Ollama" / "ollama.exe",
    Path("C:/Users") / os.environ.get("USERNAME", "user") / "AppData" / "Local" / "Programs" / "Ollama" / "ollama.exe",
]


def check_ollama() -> list[CheckResult]:
    """Validate Ollama installation, service health, models, and GPU access."""
    results = []

    # 1. Binary exists
    binary_found = None
    # Try shutil.which first (if ollama is on PATH)
    which_path = shutil.which("ollama")
    if which_path:
        binary_found = which_path
    else:
        for bp in OLLAMA_BINARY_PATHS:
            if bp.exists():
                binary_found = str(bp)
                break

    if binary_found:
        results.append(CheckResult("OLLAMA", "binary", OK,
                                   "Ollama binary: %s" % binary_found))
    else:
        results.append(CheckResult("OLLAMA", "binary", FAIL,
                                   "Ollama binary not found (checked PATH + AppData)"))
        # If no binary, remaining checks will also fail
        results.append(CheckResult("OLLAMA", "service", FAIL,
                                   "Ollama service: skipped (no binary)"))
        results.append(CheckResult("OLLAMA", "models", FAIL,
                                   "Ollama models: skipped (no binary)"))
        results.append(CheckResult("OLLAMA", "gpu", INFO,
                                   "GPU check: skipped (no binary)"))
        return results

    # 2. Service responding
    try:
        import urllib.request
        req = urllib.request.Request("http://localhost:11434/api/tags",
                                    method="GET")
        resp = urllib.request.urlopen(req, timeout=5)
        body = resp.read().decode("utf-8", errors="replace")
        tag_data = json.loads(body)
        models = tag_data.get("models", [])
        results.append(CheckResult("OLLAMA", "service", OK,
                                   "Ollama service responding (port 11434)"))
    except Exception as e:
        err_str = str(e)[:80]
        results.append(CheckResult("OLLAMA", "service", FAIL,
                                   "Ollama service not responding: %s" % err_str))
        results.append(CheckResult("OLLAMA", "models", FAIL,
                                   "Ollama models: skipped (service down)"))
        results.append(CheckResult("OLLAMA", "gpu", INFO,
                                   "GPU check: independent of service"))
        # Still check GPU
        results.extend(_check_gpu())
        return results

    # 3. At least 1 model pulled
    if models:
        model_names = [m.get("name", "?") for m in models]
        display = ", ".join(model_names[:5])
        if len(model_names) > 5:
            display += " (+%d more)" % (len(model_names) - 5)
        results.append(CheckResult("OLLAMA", "models", OK,
                                   "Ollama models: %d pulled (%s)" % (
                                       len(model_names), display)))
    else:
        results.append(CheckResult("OLLAMA", "models", FAIL,
                                   "Ollama: no models pulled (run: ollama pull qwen3:8b)"))

    # 4. GPU available
    results.extend(_check_gpu())

    return results


def _check_gpu() -> list[CheckResult]:
    """Check nvidia-smi for GPU availability."""
    results = []
    rc, out, err = run_cmd(["nvidia-smi", "--query-gpu=name,memory.total",
                            "--format=csv,noheader,nounits"], timeout=10)
    if rc == 0 and out.strip():
        # Parse first line: "NVIDIA GeForce RTX 5070 Ti, 16384"
        line = out.strip().split("\n")[0]
        results.append(CheckResult("OLLAMA", "gpu", OK,
                                   "GPU: %s" % line.strip()))
    elif rc == -1:
        results.append(CheckResult("OLLAMA", "gpu", INFO,
                                   "nvidia-smi not found (CPU-only inference)"))
    else:
        results.append(CheckResult("OLLAMA", "gpu", INFO,
                                   "GPU query failed: %s" % (err[:60] or "unknown")))
    return results


# ---------------------------------------------------------------------------
# Fix mode
# ---------------------------------------------------------------------------

def apply_fixes(all_results: list[CheckResult]) -> int:
    """Apply supported automatic fixes for failed checks."""
    fixed = 0
    for r in all_results:
        if r.status != FAIL or not r.fix_cmd:
            continue

        if r.fix_cmd == "mkdir":
            # Reconstruct path
            if "runtime/" in r.name:
                subdir = r.name.split("runtime/")[1]
                p = ROOT / ".cex" / "runtime" / subdir
                p.mkdir(parents=True, exist_ok=True)
                print("  [FIXED] created %s" % p.relative_to(ROOT))
                fixed += 1
        elif r.fix_cmd.startswith("pip install"):
            rc, out, err = run_cmd(
                [sys.executable, "-m", "pip", "install", r.fix_cmd.split()[-1]],
                timeout=120
            )
            if rc == 0:
                print("  [FIXED] %s" % r.fix_cmd)
                fixed += 1
            else:
                print("  [SKIP] %s failed: %s" % (r.fix_cmd, err[:80]))
        elif "cex_hooks.py" in r.fix_cmd:
            hooks_path = ROOT / "_tools" / "cex_hooks.py"
            if hooks_path.exists():
                rc, out, err = run_cmd(
                    [sys.executable, str(hooks_path), "install"], timeout=30
                )
                if rc == 0:
                    print("  [FIXED] git hooks installed")
                    fixed += 1
                else:
                    print("  [SKIP] hook install failed: %s" % err[:80])
        else:
            print("  [SKIP] manual fix needed: %s" % r.fix_cmd)

    return fixed


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

CATEGORIES_ORDER = [
    "RUNTIME", "PACKAGES", "MCP_SERVERS", "ENV_VARS",
    "STRUCTURE", "GIT_HOOKS", "SYSTEM", "OLLAMA"
]


def print_human(all_results: list[CheckResult]) -> None:
    """Print grouped validator results in a human-readable format."""
    print("=== CEX Setup Validator ===")
    print()

    for cat in CATEGORIES_ORDER:
        cat_results = [r for r in all_results if r.category == cat]
        if not cat_results:
            continue

        ok_count = sum(1 for r in cat_results if r.status == OK)
        fail_count = sum(1 for r in cat_results if r.status == FAIL)
        info_count = sum(1 for r in cat_results if r.status == INFO)
        total = len(cat_results)

        if fail_count == 0 and info_count == 0:
            header = "%s (%d/%d PASS)" % (cat, ok_count, total)
        elif fail_count > 0:
            header = "%s (%d/%d PASS, %d FAIL)" % (cat, ok_count, total, fail_count)
        else:
            header = "%s (%d/%d PASS, %d INFO)" % (cat, ok_count, total, info_count)

        print(header)
        for r in cat_results:
            print(r.display())
        print()

    # Summary
    total = len(all_results)
    ok_total = sum(1 for r in all_results if r.status == OK)
    fail_total = sum(1 for r in all_results if r.status == FAIL)
    info_total = sum(1 for r in all_results if r.status == INFO)
    print("SUMMARY: %d/%d checks PASS | %d FAIL | %d INFO" % (
        ok_total, total, fail_total, info_total))


def print_json(all_results: list[CheckResult]) -> None:
    """Print validator results as a JSON document."""
    checks = [r.to_dict() for r in all_results]
    ok_total = sum(1 for r in all_results if r.status == OK)
    fail_total = sum(1 for r in all_results if r.status == FAIL)
    info_total = sum(1 for r in all_results if r.status == INFO)
    output = {
        "checks": checks,
        "summary": {
            "total": len(all_results),
            "pass": ok_total,
            "fail": fail_total,
            "info": info_total,
        }
    }
    print(json.dumps(output, indent=2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Run the requested validator categories and emit the selected output format."""
    parser = argparse.ArgumentParser(description="CEX Setup Validator")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    parser.add_argument("--fix", action="store_true", help="Attempt auto-fix for FAIL items")
    parser.add_argument("--category", type=str, default=None,
                        help="Check only one category (runtime, packages, mcp_servers, env_vars, structure, git_hooks, system)")
    args = parser.parse_args()

    category_filter = args.category.upper() if args.category else None
    if category_filter and category_filter not in CATEGORIES_ORDER:
        print("Unknown category: %s" % args.category)
        print("Valid: %s" % ", ".join(c.lower() for c in CATEGORIES_ORDER))
        sys.exit(2)

    all_results: list[CheckResult] = []

    runners: dict[str, Any] = {
        "RUNTIME": check_runtime,
        "PACKAGES": lambda: check_packages(fix_mode=args.fix),
        "MCP_SERVERS": check_mcp_servers,
        "ENV_VARS": check_env_vars,
        "STRUCTURE": lambda: check_structure(fix_mode=args.fix),
        "GIT_HOOKS": lambda: check_git_hooks(fix_mode=args.fix),
        "SYSTEM": check_system,
        "OLLAMA": check_ollama,
    }

    for cat in CATEGORIES_ORDER:
        if category_filter and cat != category_filter:
            continue
        all_results.extend(runners[cat]())

    if args.fix:
        if not args.json:
            print("=== CEX Setup Validator (FIX MODE) ===")
            print()
        fixed = apply_fixes(all_results)
        if not args.json:
            print()
            print("Fixed %d items. Re-run without --fix to verify." % fixed)
            print()

    if args.json:
        print_json(all_results)
    else:
        if not args.fix:
            print_human(all_results)

    fail_count = sum(1 for r in all_results if r.status == FAIL)
    sys.exit(1 if fail_count > 0 else 0)


if __name__ == "__main__":
    main()
