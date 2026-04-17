"""Fix E02: add missing pillar: field to artifacts that have it in their path."""
import re, sys
from pathlib import Path

ROOT = Path(".")

def fix_file(fp: Path) -> bool:
    parts = fp.parts
    pillar = None
    for part in parts:
        pm = re.match(r"(P\d{2})_", part)
        if pm:
            pillar = pm.group(1)
            break
    if not pillar:
        return False

    content = fp.read_text(encoding="utf-8", errors="ignore")
    fm_end = content.find("\n---", 3)
    if fm_end == -1:
        return False

    fm = content[3:fm_end]
    if re.search(r"^pillar:", fm, re.MULTILINE):
        return False  # already has pillar

    # add after kind: line
    new_fm = re.sub(
        r"(^kind:\s*\S+)",
        r"\1\npillar: " + pillar,
        fm, count=1, flags=re.MULTILINE
    )
    if new_fm == fm:
        new_fm = fm + "\npillar: " + pillar

    new_content = "---" + new_fm + "\n---" + content[fm_end + 4:]
    fp.write_text(new_content, encoding="utf-8")
    return True


# Read target files from stdin
fixed = 0
for line in sys.stdin:
    m = re.search(r"\[FAIL\]\s+(.+)", line.strip())
    if not m:
        continue
    raw = m.group(1).strip()
    fp = Path(raw)
    if not fp.exists():
        print(f"MISSING: {fp}")
        continue
    if fix_file(fp):
        print(f"FIXED: {fp}")
        fixed += 1
    else:
        print(f"SKIP: {fp}")

print(f"Fixed: {fixed}")
