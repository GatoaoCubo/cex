#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Claude Learn -- append a PR-comment lesson to CLAUDE.md.

Called by .github/workflows/claude_learn.yml when a PR comment starts with
"@.claude learn". Extracts the lesson, formats it, appends under a
"Lessons learned" section (creating the section if missing).

Usage:
  python _tools/cex_claude_learn.py \\
    --comment-body "@.claude learn always run cex_doctor before grid" \\
    --author jdoe --pr 42 --target CLAUDE.md

Design:
- Idempotent: duplicate lessons (same body) are deduped by hash.
- Safe: never rewrites CLAUDE.md wholesale, only appends.
- Ordered: lessons sorted newest-first within section.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TRIGGER = "@.claude learn"
SECTION_HEADER = "## Lessons learned (PR-sourced)"
SECTION_BODY_MARKER = "<!-- claude-learn:start -->"
SECTION_END_MARKER = "<!-- claude-learn:end -->"


def extract_lesson(body: str) -> str:
    body = body.strip()
    if body.lower().startswith(TRIGGER):
        body = body[len(TRIGGER):].strip(" :\n\t-")
    return body


def ensure_section(content: str) -> str:
    if SECTION_BODY_MARKER in content:
        return content
    block = (
        f"\n\n{SECTION_HEADER}\n\n"
        f"{SECTION_BODY_MARKER}\n"
        f"{SECTION_END_MARKER}\n"
    )
    return content.rstrip() + block


def lesson_hash(lesson: str) -> str:
    return hashlib.sha1(lesson.strip().lower().encode("utf-8")).hexdigest()[:10]


def append_lesson(content: str, lesson: str, author: str, pr: str) -> tuple[str, bool]:
    h = lesson_hash(lesson)
    if f"<!--lh:{h}-->" in content:
        return content, False
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = f"- <!--lh:{h}--> [{date}] (@{author}, PR #{pr}) {lesson}"
    pattern = re.compile(
        rf"({re.escape(SECTION_BODY_MARKER)}\n)",
        re.MULTILINE,
    )
    new_content, n = pattern.subn(rf"\1{entry}\n", content, count=1)
    if n == 0:
        new_content = content + f"\n{entry}\n"
    return new_content, True


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--comment-body", required=True)
    p.add_argument("--author", required=True)
    p.add_argument("--pr", required=True)
    p.add_argument("--target", default="CLAUDE.md")
    args = p.parse_args(argv)

    lesson = extract_lesson(args.comment_body)
    if not lesson:
        print("no lesson content after trigger -- skipping", file=sys.stderr)
        return 0

    target = Path(args.target)
    if not target.exists():
        print(f"target {target} not found", file=sys.stderr)
        return 1

    original = target.read_text(encoding="utf-8")
    with_section = ensure_section(original)
    updated, added = append_lesson(with_section, lesson, args.author, args.pr)

    if not added and updated == original:
        print("duplicate lesson -- no change", file=sys.stderr)
        return 0

    target.write_text(updated, encoding="utf-8")
    print(f"appended lesson {lesson_hash(lesson)} to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
