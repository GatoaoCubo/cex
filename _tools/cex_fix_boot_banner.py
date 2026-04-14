"""Strip colored-bg init block and decorative banner from boot scripts.

Boot scripts used to:
  1. Set DarkBlue background + White foreground
  2. Resize buffer + window
  3. Clear-Host
  4. Write banner
  5. Run [CEX_TUI_HYGIENE] block (already present) -- reset colors + Clear-Host

Steps 1-4 are wiped by step 5 anyway, but steps 1-3 race with
_spawn/spawn_grid.ps1 MoveWindow(). When MoveWindow fires AFTER step 5
and after Claude TUI enters alt-screen-buffer, the visible primary buffer
shows a flash of the old DarkBlue/banner content -- the "overlap" users
reported.

This tool:
  - Removes the colored-bg try/catch block (lines ~47-61 in n03.ps1)
  - Removes the decorative Write-Host banner (lines ~63-69)
  - Keeps Set-CexTitle + environment setup + HYGIENE block + CLI launch
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Match: try { ... $Host.UI.RawUI.BackgroundColor = "..." ... Clear-Host ... } catch {}
COLOR_BLOCK_RE = re.compile(
    r"^try \{\s*\n"
    r"(?:    \$Host\.UI\.RawUI\.(?:Background|Foreground)Color = \"\w+\"\s*\n)+"
    r"(?:    if \(-not \$env:CEX_GRID\) \{[\s\S]*?\n    \}\s*\n)?"
    r"    Clear-Host\s*\n"
    r"\} catch \{\}\s*\n",
    re.MULTILINE,
)

# Match: decorative banner (4-7 Write-Host lines with ForegroundColor, bracketed by blank Write-Host "")
BANNER_RE = re.compile(
    r"^Write-Host \"\"\s*\n"
    r"(?:Write-Host [\s\S]*?-ForegroundColor \w+\s*\n){2,8}"
    r"(?:if \(\$mission\) \{ Write-Host [\s\S]*?\}\s*\n)?"
    r"Write-Host \"\"\s*\n",
    re.MULTILINE,
)


def fix_file(path: Path, apply: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Remove colored-bg block
    text = COLOR_BLOCK_RE.sub("", text, count=1)
    # Remove decorative banner
    text = BANNER_RE.sub("", text, count=1)

    if text == original:
        return False

    if apply:
        path.write_text(text, encoding="utf-8")
        print(f"[FIX] {path.relative_to(ROOT)}")
    else:
        print(f"[DRY] {path.relative_to(ROOT)}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes")
    args = ap.parse_args()

    boot_dir = ROOT / "boot"
    targets = sorted(boot_dir.glob("n0*.ps1")) + sorted(boot_dir.glob("cex.ps1"))

    changed = 0
    for p in targets:
        if fix_file(p, args.apply):
            changed += 1

    mode = "applied" if args.apply else "dry-run"
    print(f"\n[{mode}] {changed}/{len(targets)} boot scripts modified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
