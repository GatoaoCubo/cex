"""
Auto-fix: PowerShell boot scripts leak RawUI colors + mismatched buffer/window
size + missing UTF-8 codepage into Claude/Codex/Gemini TUI. Symptoms:
  - Background color bleeds and gets overwritten mid-render
  - Unicode box-drawing renders as mojibake (cp1252 console + UTF-8 TUI)
  - Horizontal scroll-bar appears because BufferSize.Width > WindowSize.Width
  - TUI jumps / repaints wrong region when spawn_grid re-positions window

Fix: insert a TUI hygiene block right before the CLI invocation line.
Handles:
  1. chcp 65001 + UTF-8 console encoding (fixes mojibake)
  2. BufferSize.Width = WindowSize.Width (fixes horizontal scroll + clipping)
  3. Color reset (prevents DarkGreen bleed into child TUI)

Idempotent - marker [CEX_TUI_HYGIENE] supersedes old [CEX_COLOR_RESET].

Usage:
    python _tools/cex_fix_boot_tui.py           # dry-run
    python _tools/cex_fix_boot_tui.py --apply   # write changes
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOT_DIR = ROOT / "boot"

OLD_MARKER = "[CEX_COLOR_RESET]"
NEW_MARKER = "[CEX_TUI_HYGIENE]"

# The full hygiene block. Inserted right before `& claude|codex|gemini|ollama`.
HYGIENE_BLOCK = """# [CEX_TUI_HYGIENE] UTF-8 + buffer sync + color reset (prevents TUI bleed/mojibake)
try {
    # 1. UTF-8 codepage + encoding (Claude/Codex/Gemini emit unicode box-drawing)
    $null = (chcp 65001 2>$null)
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    [Console]::InputEncoding = [System.Text.Encoding]::UTF8
    $env:PYTHONIOENCODING = "utf-8"
    # 2. Sync BufferSize.Width to WindowSize.Width (no horizontal scroll, no clip)
    $win = $Host.UI.RawUI.WindowSize
    $buf = $Host.UI.RawUI.BufferSize
    if ($buf.Width -ne $win.Width) {
        $buf.Width = $win.Width
        $buf.Height = [Math]::Max($win.Height, 3000)
        $Host.UI.RawUI.BufferSize = $buf
    }
    # 3. Reset colors (prevents DarkGreen/RawUI bleed into child CLI TUI)
    $Host.UI.RawUI.BackgroundColor = "Black"
    $Host.UI.RawUI.ForegroundColor = "Gray"
    [Console]::ResetColor()
    Clear-Host
} catch {}
"""

# Match: `& claude @cliArgs`, `& codex @args`, `& gemini @a`, `& ollama ...`
CLI_LAUNCH_RE = re.compile(r"^(\s*)(& (?:claude|codex|gemini|ollama)\b.*)$", re.MULTILINE)

# Match the old color-only block (for removal/upgrade)
OLD_BLOCK_RE = re.compile(
    r"^# \[CEX_COLOR_RESET\].*?\n(?:try \{\s*\n"
    r"(?:\s+\$Host\.UI\.RawUI\.(?:Background|Foreground)Color = \"\w+\"\s*\n)+"
    r"(?:\s+\[Console\]::ResetColor\(\)\s*\n)"
    r"\} catch \{\}\s*\n)",
    re.MULTILINE,
)


def patch(path: Path, apply: bool) -> tuple[bool, str]:
    txt = path.read_text(encoding="utf-8")
    had_old = OLD_MARKER in txt and NEW_MARKER not in txt
    has_new = NEW_MARKER in txt

    # Case 1: already on new marker -> skip
    if has_new:
        return False, "already has TUI hygiene"

    # Find insertion point
    m = CLI_LAUNCH_RE.search(txt)
    if not m:
        return False, "no CLI launch line found"

    # Case 2: has OLD color-only block -> upgrade in place
    if had_old:
        new_txt = OLD_BLOCK_RE.sub("", txt, count=1)
        # re-find launch line after block removal (positions shifted)
        m2 = CLI_LAUNCH_RE.search(new_txt)
        if not m2:
            return False, "launch line vanished after old-block strip"
        indent = m2.group(1)
        block = "\n".join(indent + line for line in HYGIENE_BLOCK.splitlines()) + "\n"
        new_txt = new_txt[: m2.start()] + block + new_txt[m2.start():]
        action = "upgraded color-reset -> TUI hygiene"
    else:
        # Case 3: no marker at all -> fresh insert
        indent = m.group(1)
        block = "\n".join(indent + line for line in HYGIENE_BLOCK.splitlines()) + "\n"
        new_txt = txt[: m.start()] + block + txt[m.start():]
        action = f"inserted at line {txt[:m.start()].count(chr(10)) + 1}"

    if apply:
        path.write_text(new_txt, encoding="utf-8")
    return True, action


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
