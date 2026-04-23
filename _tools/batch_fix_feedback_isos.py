"""Batch fix bld_feedback_* ISOs: dedup quality, bullets->tables, fix density."""
import glob
import re
import sys

ANTI_PATTERNS_TABLE = """## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score to own output | H01 |
| No hallucination | Cite sources; no invented facts, metrics, refs | H03 |
| ASCII-only code | No emoji, no accented chars in .py/.ps1/.sh | H04 |
| No partial output | Complete artifact; no truncation, no "..." | H05 |
| No frontmatter omission | Every artifact starts with valid YAML frontmatter | H01 |
| No quality below 8.0 | Re-draft before publishing if self-assessment < 8.0 | H07 |"""

CORRECTION_TABLE = """## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify which H01-H07 gate failed | F7 |
| 2 | Return to F6 PRODUCE with explicit fix instruction | F6 |
| 3 | Re-run F7 GOVERN | F7 |
| 4 | Max 2 retries before escalating to N07 | F8 |"""


def build_failure_modes_table(kind_name):
    display = kind_name.replace("_", " ").title()
    return """## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Vague identity section | No concrete capabilities, tools, or constraints | Add specifics from builder ISOs |
| Missing frontmatter fields | id, kind, pillar absent or quality not null | Add all required fields per schema |
| Body prose only | density < 0.85, no tables | Convert lists to tables |
| Output schema mismatch | Output does not match output template | Re-read bld_output ISO |"""


def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    kind_match = re.search(r"domain:\s*(\S+)", content)
    kind_name = kind_match.group(1) if kind_match else "unknown"

    # 1. Fix duplicate quality: keep ONLY second occurrence (which is the heuristic score)
    new_lines = []
    quality_count = 0
    in_frontmatter = False
    fm_count = 0
    for line in lines:
        if line.strip() == "---":
            fm_count += 1
            if fm_count == 1:
                in_frontmatter = True
            elif fm_count == 2:
                in_frontmatter = False
        if in_frontmatter and re.match(r"^quality:\s", line):
            quality_count += 1
            if quality_count == 1:
                continue  # skip first (prepended by evolve)
        new_lines.append(line)

    content = "\n".join(new_lines)

    # 2. Fix density_score: 1.0 -> 0.88
    content = re.sub(r"density_score:\s*1\.0", "density_score: 0.88", content)

    # 3. Replace bullet-list Anti-Patterns with table
    anti_pattern = re.compile(
        r"## Anti-Patterns \(NEVER do\)\s*\n(?:\s*-\s+\*\*[^*]+\*\*:[^\n]+\n?)+",
        re.MULTILINE
    )
    if anti_pattern.search(content):
        content = anti_pattern.sub(ANTI_PATTERNS_TABLE + "\n", content)

    # 4. Replace bullet-list Common Failure Modes with table
    failure_pattern = re.compile(
        r"## Common Failure Modes[^\n]*\s*\n(?:\s*-\s+[^\n]+\n?)+",
        re.MULTILINE
    )
    if failure_pattern.search(content):
        content = failure_pattern.sub(
            build_failure_modes_table(kind_name) + "\n", content
        )

    # 5. Replace numbered Correction Protocol with table
    correction_pattern = re.compile(
        r"## Correction Protocol\s*\n(?:\s*\d+\.\s+[^\n]+\n?)+",
        re.MULTILINE
    )
    if correction_pattern.search(content):
        content = correction_pattern.sub(CORRECTION_TABLE + "\n", content)

    # 6. Fix kind from builder_default to knowledge_card
    content = content.replace("kind: builder_default", "kind: knowledge_card")

    # 7. Add tldr if missing
    if "tldr:" not in content:
        display = kind_name.replace("_", " ")
        tldr_line = f'tldr: "Anti-patterns and correction protocol for {display} builders. 6 NEVER rules + 4 failure modes + 3-step correction."'
        content = content.replace(
            "author: builder",
            f"{tldr_line}\nauthor: builder"
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    files = sorted(glob.glob("archetypes/builders/*/bld_feedback_*.md"))
    # Filter to only those with quality: 7.7 AND bullet-list body
    targets = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            c = fh.read()
        if "quality: 7.7" in c and ("- **No self-score**" in c or "- **No hallucination**" in c):
            targets.append(f)

    print(f"Found {len(targets)} feedback ISOs to fix")

    if "--dry-run" in sys.argv:
        for t in targets[:5]:
            print(f"  would fix: {t}")
        print(f"  ... and {len(targets) - 5} more")
        return

    fixed = 0
    for path in targets:
        try:
            fix_file(path)
            fixed += 1
        except Exception as e:
            print(f"  [FAIL] {path}: {e}")

    print(f"Fixed {fixed}/{len(targets)} feedback ISOs")


if __name__ == "__main__":
    main()
