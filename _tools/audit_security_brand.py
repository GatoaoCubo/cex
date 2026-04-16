"""Audit W3 SECURITY+BRAND: scan for secrets, brand coupling, personal info.

Patterns scanned:
- Brand strings: Gato3, gato3, gatoaocubo, cex-main
- Personal: financeiro@gatoaocubo3, GATO_TENANT, custom emails
- Hardcoded secrets: api keys, tokens (regex over common formats)
- Anthropic/OpenAI/etc keys
- Local-machine paths: C:\\Users\\CEX, /Users/cex
- Hostname leaks
- TODO/FIXME with sensitive markers (SECURITY, CREDENTIAL, PASSWORD)

Output: _reports/audit/security_brand.md
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT = ROOT / "_reports" / "audit" / "security_brand.md"

PATTERNS = {
    # BRAND COUPLING
    "brand_gato3": re.compile(r"\bGato3\b|\bgato3\b|\bGATO3\b", re.IGNORECASE),
    "brand_gatoaocubo": re.compile(r"gatoaocubo", re.IGNORECASE),
    "brand_cex_main": re.compile(r"\bcex-main\b", re.IGNORECASE),
    "brand_cex_user": re.compile(r"C:\\\\Users\\\\CEX|/Users/CEX|/Users/cex", re.IGNORECASE),

    # PERSONAL
    "email_personal": re.compile(r"financeiro@gatoaocubo3|cex@gatoaocubo", re.IGNORECASE),
    "email_other": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "tenant_id": re.compile(r"GATO_TENANT|gato_tenant_id"),

    # SECRETS (regex)
    "anthropic_key": re.compile(r"sk-ant-api\d{2}-[A-Za-z0-9_-]{40,}"),
    "openai_key": re.compile(r"sk-[A-Za-z0-9]{32,}"),
    "github_token": re.compile(r"ghp_[A-Za-z0-9]{36}|gho_[A-Za-z0-9]{36}"),
    "aws_key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "google_key": re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    "private_key": re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "bearer_token": re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}"),
    "generic_secret": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][A-Za-z0-9._\-]{16,}['\"]"),

    # SENSITIVE COMMENTS
    "todo_security": re.compile(r"(?i)#\s*(TODO|FIXME|XXX|HACK).*(security|password|credential|secret|key|auth)"),

    # HOSTNAME / NETWORK
    "ip_private": re.compile(r"\b(?:192\.168|10\.|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
    "localhost_port": re.compile(r"localhost:(\d{4,5})"),
}

SAFE_DIRS = {".git", ".venv_litellm", ".aider.tags.cache.v4", "node_modules",
             "__pycache__", ".pi", ".cex_signals", ".cex/runtime",
             ".cex/archive", "_reports/audit", ".cex/cache",
             ".cex/learning_records", ".cex/experiments",
             ".cex/overnight", ".cex/quality", ".cex/temp"}

# Prefix patterns: any path starting with one of these is excluded.
# Used for historical run-output dirs that capture absolute paths in traces.
SAFE_DIR_PREFIXES = ("_reports/leverage_map", "_reports/gridtest_")

# These files are EXPECTED to mention brand strings (they ARE the brand config)
BRAND_OWNERS = {
    ".cex/brand/brand_config.yaml",
    ".cex/instance/instance.yaml",
    "CLAUDE.md",
}

SAFE_PATTERNS = {
    # findings INSIDE these contexts get downgraded
    "email_other": [
        re.compile(r"noreply@anthropic\.com"),
        re.compile(r"@example\.com|@example\.org"),
        re.compile(r"@anthropic\.com"),
    ],
    "localhost_port": [
        re.compile(r"localhost:(80|443|3000|5432|8000|8080|11434|4000|6379)\b"),
    ],
}


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def in_safe_dir(rel_path: str) -> bool:
    """Check if path is in a dir we exclude from scan."""
    norm = rel_path.replace("\\", "/")
    if any(norm.startswith(d + "/") or norm == d for d in SAFE_DIRS):
        return True
    return any(norm.startswith(p) for p in SAFE_DIR_PREFIXES)


def is_safe_match(pattern_name: str, snippet: str) -> bool:
    """Downgrade matches that are noise (e.g. anthropic email)."""
    safelist = SAFE_PATTERNS.get(pattern_name, [])
    return any(s.search(snippet) for s in safelist)


def scan_text(rel_path: str, text: str) -> list[tuple[str, int, str]]:
    """Return list of (pattern_name, line_no, snippet)."""
    findings = []
    lines = text.splitlines()
    is_brand_owner = rel_path in BRAND_OWNERS
    for name, pat in PATTERNS.items():
        if is_brand_owner and name.startswith("brand_"):
            continue
        if is_brand_owner and name == "email_personal":
            continue
        for i, line in enumerate(lines, start=1):
            m = pat.search(line)
            if m:
                snippet = line.strip()[:140]
                if is_safe_match(name, snippet):
                    continue
                findings.append((name, i, snippet))
    return findings


def scan_files(records: list[dict]) -> dict:
    """Scan every text file."""
    findings: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    scanned = 0
    skipped_size = 0
    skipped_binary = 0
    for r in records:
        path = r["path"]
        if in_safe_dir(path):
            continue
        if path.endswith((".png", ".jpg", ".gif", ".svg", ".webp",
                          ".pdf", ".zip", ".gz", ".whl", ".pyc")):
            skipped_binary += 1
            continue
        if r["size_bytes"] > 500_000:
            skipped_size += 1
            continue
        try:
            text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        for finding in scan_text(path, text):
            findings[path].append(finding)
    print(f"[W3] scanned {scanned} files (skipped {skipped_size} large, "
          f"{skipped_binary} binary), {sum(len(v) for v in findings.values())} findings")
    return findings


def write_report(findings: dict) -> None:
    """Emit security_brand.md grouped by pattern."""
    by_pattern: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for path, items in findings.items():
        for name, line_no, snippet in items:
            by_pattern[name].append((path, line_no, snippet))

    severity = {
        "anthropic_key": ("CRITICAL", "ROTATE NOW + remove + use env var"),
        "openai_key": ("CRITICAL", "ROTATE NOW + remove + use env var"),
        "github_token": ("CRITICAL", "ROTATE NOW + remove"),
        "aws_key": ("CRITICAL", "ROTATE NOW + remove"),
        "google_key": ("CRITICAL", "ROTATE NOW + remove"),
        "private_key": ("CRITICAL", "ROTATE NOW + remove"),
        "bearer_token": ("HIGH", "Verify if real; remove if so"),
        "generic_secret": ("HIGH", "Verify; move to env or .env-not-tracked"),
        "brand_gato3": ("HIGH", "Replace with {{BRAND_NAME}} placeholder or move to brand_config"),
        "brand_gatoaocubo": ("HIGH", "Replace with {{BRAND_DOMAIN}} placeholder"),
        "brand_cex_main": ("MEDIUM", "Replace with config field or doc-only mention"),
        "brand_cex_user": ("HIGH", "Replace with Path.home() or {{USER_HOME}}"),
        "email_personal": ("HIGH", "Replace with {{BRAND_EMAIL}} or remove"),
        "email_other": ("LOW", "Inspect; whitelist if safe"),
        "tenant_id": ("MEDIUM", "Verify scope; consider env var"),
        "todo_security": ("MEDIUM", "Resolve before public push"),
        "ip_private": ("LOW", "Likely doc/example, verify"),
        "localhost_port": ("LOW", "Verify port is doc/example"),
    }

    lines = [
        "# W3 SECURITY + BRAND",
        "",
        f"Generated from `_reports/audit/inventory_full.jsonl`. "
        f"{sum(len(v) for v in findings.values())} findings across "
        f"{len(findings)} files.",
        "",
        "## Summary by pattern (sorted by severity)",
        "",
        "| Pattern | Hits | Severity | Fix |",
        "|---------|------|----------|-----|",
    ]
    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

    def sort_key(name: str) -> tuple:
        sev, _ = severity.get(name, ("LOW", ""))
        return (sev_order.get(sev, 99), -len(by_pattern[name]))

    for name in sorted(by_pattern.keys(), key=sort_key):
        sev, fix = severity.get(name, ("LOW", ""))
        lines.append(f"| {name} | {len(by_pattern[name])} | {sev} | {fix} |")
    lines.append("")
    lines.append("## Critical / High details")
    lines.append("")
    for name in sorted(by_pattern.keys(), key=sort_key):
        sev, _ = severity.get(name, ("LOW", ""))
        if sev not in ("CRITICAL", "HIGH"):
            continue
        items = by_pattern[name]
        lines.append(f"### {name} -- {sev} ({len(items)} hits)")
        lines.append("")
        lines.append("| File | Line | Snippet |")
        lines.append("|------|------|---------|")
        for path, line_no, snippet in items[:50]:
            snippet_safe = snippet.replace("|", "\\|").replace("`", "\\`")
            lines.append(f"| `{path}` | {line_no} | `{snippet_safe}` |")
        if len(items) > 50:
            lines.append(f"| ... | ... | (+{len(items) - 50} more) |")
        lines.append("")
    lines.append("## Medium / Low summary (counts by file)")
    lines.append("")
    medlow_files: dict[str, int] = defaultdict(int)
    for name in by_pattern:
        sev, _ = severity.get(name, ("LOW", ""))
        if sev in ("MEDIUM", "LOW"):
            for path, _line_no, _snippet in by_pattern[name]:
                medlow_files[path] += 1
    if medlow_files:
        lines.append("| File | Med/Low hits |")
        lines.append("|------|--------------|")
        for path, n in sorted(medlow_files.items(), key=lambda x: -x[1])[:50]:
            lines.append(f"| `{path}` | {n} |")
    else:
        lines.append("_None._")
    lines.append("")
    lines.append("## SECURITY_BRAND_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W3] report written: {OUT}")


def main() -> int:
    """Run W3 security+brand audit."""
    print("[W3] loading inventory...")
    records = load_inventory()
    print(f"[W3] {len(records)} records loaded")
    findings = scan_files(records)
    write_report(findings)
    print("[W3] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
