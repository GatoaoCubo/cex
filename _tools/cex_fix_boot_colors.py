"""
Auto-fix: PowerShell boot scripts leak RawUI.BackgroundColor/ForegroundColor
into the child CLI (Claude / Codex / Gemini / Ollama), causing color bleed
where sin-aware DarkGreen background bleeds into TUI output.

Fix: insert a console-reset block right before the CLI invocation line.
Idempotent - detects existing [CEX_COLOR_RESET] marker.

Usage:
    python _tools/cex_fix_boot_colors.py           # dry-run (report only)
    python _tools/cex_fix_boot_colors.py --apply   # write changes
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOT_DIR = ROOT / "boot"

RESET_BLOCK = """# [CEX_COLOR_RESET] Prevent RawUI color bleed into child CLI TUI
try {
    $Host.UI.RawUI.BackgroundColor = "Black"
    $Host.UI.RawUI.ForegroundColor = "Gray"
    [Console]::ResetColor()
} catch {}
"""

# Match lines like: `& claude @cliArgs`, `& codex @args`, `& gemini @a`, `& ollama ...`
CLI_LAUNCH_RE = re.compile(r"^(\s*)(& (?:claude|codex|gemini|ollama)\b.*)$", re.MULTILINE)


def patch(path: Path, apply: bool) -> tuple[bool, str]:
    txt = path.read_text(encoding="utf-8")
    if "[CEX_COLOR_RESET]" in txt:
        return False, "already patched"
    m = CLI_LAUNCH_RE.search(txt)
    if not m:
        return False, "no CLI launch line found"
    indent = m.group(1)
    block = "\n".join(indent + line for line in RESET_BLOCK.splitlines()) + "\n"
    new_txt = txt[: m.start()] + block + txt[m.start():]
    if apply:
        path.write_text(new_txt, encoding="utf-8")
    return True, f"patch inserted at line {txt[:m.start()].count(chr(10)) + 1}"


def main() -> int:
    apply = "--apply" in sys.argv
    if not BOOT_DIR.exists():
        print(f"[FAIL] boot dir not found: {BOOT_DIR}")
        return 1
    files = sorted(BOOT_DIR.glob("*.ps1"))
    changed = 0
    skipped = 0
    for f in files:
        ok, msg = patch(f, apply)
        tag = "[FIX]" if ok else "[--]"
        print(f"  {tag} {f.name:<30} {msg}")
        if ok:
            changed += 1
        else:
            skipped += 1
    verb = "patched" if apply else "would patch"
    print(f"\nSummary: {verb} {changed}, skipped {skipped}")
    if not apply and changed:
        print("Run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
