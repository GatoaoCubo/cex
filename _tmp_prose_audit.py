import re, os, sys
from pathlib import Path
from collections import Counter

root = Path(".")
prose_heavy = []
total_with_fm = 0

for f in root.rglob("*.md"):
    s = str(f)
    if ".git" in s or "_archive" in s or "node_modules" in s or "cex-pi-package" in s:
        continue
    try:
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        total_with_fm += 1
        body = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
        lines = body.strip().split("\n")
        if not lines:
            continue
        structured = 0
        prose = 0
        for line in lines:
            l = line.strip()
            if not l:
                continue
            if (l.startswith("#") or l.startswith("|") or l.startswith("-") or
                l.startswith("*") or l.startswith("> ") or l.startswith("```")):
                structured += 1
            else:
                prose += 1
        total_lines = structured + prose
        if total_lines > 5 and prose / total_lines > 0.5:
            prose_heavy.append((str(f), prose, total_lines, round(prose / total_lines, 2)))
    except:
        pass

print(f"Total artifacts with frontmatter: {total_with_fm}")
pct = round(len(prose_heavy) / total_with_fm * 100) if total_with_fm else 0
print(f"Prose-heavy (>50% prose lines): {len(prose_heavy)} ({pct}%)")
print()

dirs = Counter()
for p, _, _, _ in prose_heavy:
    d = p.split(os.sep)[0]
    dirs[d] += 1

print("By top directory:")
for d, c in dirs.most_common(15):
    print(f"  {c:4d}  {d}")

print()
print("Worst offenders (>70% prose):")
worst = sorted([x for x in prose_heavy if x[3] > 0.70], key=lambda x: -x[3])[:20]
for p, pr, tot, ratio in worst:
    print(f"  {int(ratio*100)}%  ({pr}/{tot} lines)  {p}")
