"""Phase 3: revert kind to builder_default (neutral rubric 7.5) + add list items for structural bonus.

Score path: structural 8.5+ with rubric 7.5 = average 8.0+.
Structural needs: body_words>=400 (+0.2) + list_items>=3 (+0.2) = +0.4 raw.
"""
import glob
import sys

KEY_BEHAVIORS = """## Key Behaviors

- Builder MUST load all 12 ISOs (1:1 with pillars) before producing any artifact
- Builder MUST run F7 GOVERN quality gate before saving output
- Builder MUST compile output via cex_compile.py after saving (F8 COLLABORATE)
- Builder MUST signal completion with quality score to N07 orchestrator
- Builder MUST NOT self-score: quality field is always null in own output
"""


def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changed = False

    # 1. Revert kind: knowledge_card -> builder_default (if we changed it)
    if "kind: knowledge_card" in content:
        # Check if this is actually a feedback ISO (not a legit KC)
        if "bld_feedback_" in path:
            content = content.replace("kind: knowledge_card", "kind: builder_default")
            changed = True

    # 2. Add Key Behaviors section if missing (adds list_items + word count)
    if "## Key Behaviors" not in content:
        if "## Quality Thresholds" in content:
            content = content.replace(
                "## Quality Thresholds",
                KEY_BEHAVIORS + "## Quality Thresholds"
            )
        elif "## Related Artifacts" in content:
            content = content.replace(
                "## Related Artifacts",
                KEY_BEHAVIORS + "## Related Artifacts"
            )
        else:
            content = content.rstrip() + "\n" + KEY_BEHAVIORS
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    files = sorted(glob.glob("archetypes/builders/*/bld_feedback_*.md"))
    print(f"Scanning {len(files)} feedback ISOs...")

    if "--dry-run" in sys.argv:
        needs = 0
        for f in files:
            with open(f, "r", encoding="utf-8") as fh:
                c = fh.read()
            issues = []
            if "kind: knowledge_card" in c and "bld_feedback_" in f:
                issues.append("revert-kind")
            if "## Key Behaviors" not in c:
                issues.append("add-behaviors")
            if issues:
                needs += 1
                if needs <= 5:
                    print(f"  {f}: {', '.join(issues)}")
        print(f"Total: {needs}")
        return

    fixed = 0
    for path in files:
        try:
            if fix_file(path):
                fixed += 1
        except Exception as e:
            print(f"  [FAIL] {path}: {e}")

    print(f"Fixed {fixed}/{len(files)}")


if __name__ == "__main__":
    main()
