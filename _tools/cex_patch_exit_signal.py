"""Inject Emit-ExitSignal safety net into all non-claude boot wrappers.

Idempotent: skips files already patched.
Targets: boot/n0{1-6}_{gemini,codex,ollama,litellm}.ps1
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
BOOT_DIR = ROOT / "boot"

RUNTIMES = ["gemini", "codex", "ollama", "litellm"]
NUCLEI = ["n01", "n02", "n03", "n04", "n05", "n06"]

DOT_SOURCE = ". $PSScriptRoot/_shared/emit_exit_signal.ps1"
START_MARK = "$cex_start_time = Get-Date"

def patch_file(path: Path) -> str:
    txt = path.read_text(encoding="utf-8")
    if "Emit-ExitSignal" in txt:
        return "already-patched"

    lines = txt.splitlines(keepends=False)
    out = []
    inserted_dot = False
    # Insert dot-source after the first `. $PSScriptRoot/_shared/` line (vt_enable or theme)
    for i, line in enumerate(lines):
        out.append(line)
        if not inserted_dot and line.strip().startswith(". $PSScriptRoot/_shared/"):
            out.append(DOT_SOURCE)
            inserted_dot = True

    if not inserted_dot:
        # Fall back: insert after `$cexRoot = ...`
        for i, line in enumerate(out):
            if line.strip().startswith("$cexRoot ="):
                out.insert(i + 1, DOT_SOURCE)
                inserted_dot = True
                break

    # Insert $cex_start_time just before the main `& claude/gemini/codex/python` call,
    # and Emit-ExitSignal after `Set-CexTitle "DONE"` (or at end).
    new_lines = []
    ampersand_re = re.compile(r'^\s*&\s+(claude|gemini|codex|python)\b')
    started = False
    for line in out:
        if ampersand_re.match(line) and not started:
            new_lines.append(START_MARK)
            started = True
        new_lines.append(line)

    if not started:
        new_lines.append(START_MARK)

    # Append Emit-ExitSignal at end
    new_lines.append("Emit-ExitSignal -StartTime $cex_start_time")

    path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return "patched"

def main():
    results = {"patched": [], "already-patched": [], "missing": []}
    for nuc in NUCLEI:
        for rt in RUNTIMES:
            fp = BOOT_DIR / f"{nuc}_{rt}.ps1"
            if not fp.exists():
                results["missing"].append(fp.name)
                continue
            status = patch_file(fp)
            results[status].append(fp.name)

    print(f"PATCHED:        {len(results['patched'])}")
    for f in results['patched']: print(f"  + {f}")
    print(f"ALREADY-PATCHED: {len(results['already-patched'])}")
    for f in results['already-patched']: print(f"  = {f}")
    print(f"MISSING:        {len(results['missing'])}")
    for f in results['missing']: print(f"  - {f}")

if __name__ == "__main__":
    main()
