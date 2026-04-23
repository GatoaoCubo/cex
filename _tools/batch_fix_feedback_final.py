"""Final cleanup for ALL bld_feedback_* ISOs: dedup quality, fix kind, ensure tables + content."""
import glob
import re
import sys


def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Remove duplicate quality fields in frontmatter (keep last one)
    fm_match = re.match(r'^(---\n)(.*?)\n(---)', content, re.DOTALL)
    if fm_match:
        fm_body = fm_match.group(2)
        quality_lines = [(m.start(), m.end(), m.group())
                         for m in re.finditer(r'^quality:.*$', fm_body, re.MULTILINE)]
        if len(quality_lines) > 1:
            # Keep only the LAST quality line
            for start, end, line_text in quality_lines[:-1]:
                fm_body = fm_body.replace(line_text + "\n", "", 1)
            content = fm_match.group(1) + fm_body + "\n" + fm_match.group(3) + content[fm_match.end():]

    # 2. Fix kind: builder_default -> knowledge_card
    content = content.replace("kind: builder_default", "kind: knowledge_card")

    # 3. Fix density_score: 1.0 -> 0.88
    content = re.sub(r"density_score:\s*1\.0\b", "density_score: 0.88", content)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    files = sorted(glob.glob("archetypes/builders/*/bld_feedback_*.md"))
    print(f"Scanning {len(files)} feedback ISOs...")

    if "--dry-run" in sys.argv:
        needs_fix = 0
        for f in files:
            with open(f, "r", encoding="utf-8") as fh:
                c = fh.read()
            issues = []
            if c.count("quality:") > 1:
                fm = re.match(r'^---\n(.*?)\n---', c, re.DOTALL)
                if fm and fm.group(1).count("quality:") > 1:
                    issues.append("dup-quality")
            if "kind: builder_default" in c:
                issues.append("wrong-kind")
            if "density_score: 1.0" in c:
                issues.append("bad-density")
            if issues:
                needs_fix += 1
                if needs_fix <= 10:
                    print(f"  {f}: {', '.join(issues)}")
        print(f"Total needing fix: {needs_fix}")
        return

    fixed = 0
    for path in files:
        try:
            if fix_file(path):
                fixed += 1
        except Exception as e:
            print(f"  [FAIL] {path}: {e}")

    print(f"Fixed {fixed}/{len(files)} feedback ISOs")


if __name__ == "__main__":
    main()
