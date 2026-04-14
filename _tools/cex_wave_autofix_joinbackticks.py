"""Join adjacent inline-code segments that sandwich a bare placeholder.

Input pattern:  `prefix_`{{placeholder}}`.suffix`
Output:         `prefix_{{placeholder}}.suffix`

Runs over archetypes/builders/ (excluding _builder-builder/ meta templates).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parents[1]
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# `A`{{X}}`B` -> `A{{X}}B`
SANDWICH_RE = re.compile(r"`([^`\n]*?)`(\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\})`([^`\n]*?)`")

# `A`{{X}} -> `A{{X}}`
HALF_LEFT_RE = re.compile(r"`([^`\n]*?)`(\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\})(?!`)")

# {{X}}`A` -> `{{X}}A`
HALF_RIGHT_RE = re.compile(r"(?<!`)(\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\})`([^`\n]*?)`")


def fix_text(text: str) -> tuple[str, int]:
    count = 0
    new = text
    for _ in range(3):
        prev = new
        new, n1 = SANDWICH_RE.subn(r"`\1\2\3`", new)
        count += n1
        new, n2 = HALF_LEFT_RE.subn(r"`\1\2`", new)
        count += n2
        new, n3 = HALF_RIGHT_RE.subn(r"`\1\2`", new)
        count += n3
        if new == prev:
            break
    return new, count


def main() -> int:
    fixed = 0
    for fp in sorted(BUILDER_DIR.rglob("bld_*.md")):
        if "_builder-builder" in str(fp).replace("\\", "/"):
            continue
        text = fp.read_text(encoding="utf-8", errors="replace")
        new, n = fix_text(text)
        if n:
            fp.write_text(new, encoding="utf-8", newline="\n")
            fixed += 1
            print(f"[JOIN] {fp.name}: {n} segment(s) merged")
    print(f"\nMerged backticks in {fixed} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
