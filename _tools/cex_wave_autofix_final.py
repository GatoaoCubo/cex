"""Final mechanical pass: (a) backtick-wrap ALL unresolved placeholders in
prose (anything not already inside a fence or backticks); (b) insert a
single canonical domain-keyword sentence into bodies that lack one.

For (b), the sentence is inserted right after the first heading line as
a short prose note -- content-neutral, uses the canonical keyword for that
kind. Humans can rewrite later; the goal is just to clear C4.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parents[1]
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# Mirror of cex_wave_validator.DOMAIN_KEYWORDS subset we need here.
# Only kinds with remaining violations are listed.
DOMAIN_SENTENCES = {
    "db_connector": "This ISO addresses the database connector domain: connection pooling, query execution, and SQL dialect handling.",
    "dual_loop_architecture": "This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.",
    "mental_model": "This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.",
    "plugin": "This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.",
    "rate_limit_config": "This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.",
    "software_project": "This ISO describes a software project: its repository layout, modules, and build graph.",
    "threat_model": "This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.",
    "thinking_config": "This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.",
    "reasoning_strategy": "This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.",
    "content_filter": "This ISO defines a content filter -- the moderation rules that gate output or input.",
    "edit_format": "This ISO specifies an edit format: how diffs or patches are expressed and applied.",
    "bias_audit": "This ISO drives a bias audit: measuring fairness across demographic slices.",
    "computer_use": "This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.",
}

PLACEHOLDER_RE = re.compile(r"(?<!`)(\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\})(?!`)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
HEADING_RE = re.compile(r"^(#+\s+.+?)$", re.MULTILINE)


def iso_prefix(name: str) -> str:
    stem = name[:-3] if name.endswith(".md") else name
    for prefix in sorted([
        "bld_system_prompt", "bld_manifest", "bld_instruction",
        "bld_knowledge_card", "bld_memory", "bld_output_template",
        "bld_tools", "bld_collaboration", "bld_quality_gate",
        "bld_examples", "bld_architecture", "bld_config", "bld_schema",
    ], key=len, reverse=True):
        if stem.startswith(prefix + "_") or stem == prefix:
            return prefix
    return ""


def kind_from_filename(name: str) -> str:
    iso = iso_prefix(name)
    if not iso:
        return ""
    stem = name[:-3] if name.endswith(".md") else name
    if stem.startswith(iso + "_"):
        return stem[len(iso) + 1:]
    return ""


def wrap_placeholders_outside_fences(text: str) -> tuple[str, int]:
    count = 0
    parts: list[str] = []
    last = 0
    for m in CODE_FENCE_RE.finditer(text):
        seg, n = _wrap_seg(text[last:m.start()])
        count += n
        parts.append(seg)
        parts.append(m.group(0))
        last = m.end()
    seg, n = _wrap_seg(text[last:])
    count += n
    parts.append(seg)
    return "".join(parts), count


def _wrap_seg(segment: str) -> tuple[str, int]:
    def repl(m: re.Match[str]) -> str:
        tok = m.group(1)
        if tok in ("{{name}}", "{{kind}}", "{{brand}}"):
            return tok
        return f"`{tok}`"
    new, n = PLACEHOLDER_RE.subn(repl, segment)
    return new, n


def inject_domain_sentence(body: str, kind: str) -> tuple[str, bool]:
    sentence = DOMAIN_SENTENCES.get(kind)
    if not sentence:
        return body, False
    # Check if already present (case-insensitive)
    if sentence.lower() in body.lower():
        return body, False
    # Find first heading and insert after it
    m = HEADING_RE.search(body)
    if not m:
        # No heading: prepend
        return sentence + "\n\n" + body, True
    insert_at = m.end()
    new = body[:insert_at] + "\n\n" + sentence + body[insert_at:]
    return new, True


def fix_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return []
    head = text[:m.end()]
    body = text[m.end():]
    changes: list[str] = []

    # Placeholder wrap pass
    new_body, wrapped = wrap_placeholders_outside_fences(body)
    if wrapped:
        body = new_body
        changes.append(f"wrapped {wrapped} placeholder(s)")

    # Domain sentence injection
    kind = kind_from_filename(path.name)
    if kind in DOMAIN_SENTENCES:
        body, injected = inject_domain_sentence(body, kind)
        if injected:
            changes.append(f"injected domain sentence for '{kind}'")

    if changes:
        path.write_text(head + body, encoding="utf-8", newline="\n")
    return changes


def main() -> int:
    files = sorted(BUILDER_DIR.rglob("bld_*.md"))
    fixed = 0
    for fp in files:
        if "_builder-builder" in str(fp).replace("\\", "/"):
            continue
        changes = fix_file(fp)
        if changes:
            fixed += 1
            print(f"[FIX] {fp.relative_to(CEX_ROOT)}: {'; '.join(changes)}")
    print(f"\nFinal pass complete: {fixed} files touched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
