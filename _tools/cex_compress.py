#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
kind: cli_tool
pillar: P04
nucleus: N05
quality: null
---
CEX Compress -- LLMLingua-2 wrapper for boot-time markdown compression.

Usage:
    python _tools/cex_compress.py --target boot
    python _tools/cex_compress.py --target file --dry-run .claude/rules/ascii-code-rule.md
    python _tools/cex_compress.py --target all --ratio 0.65 --in-place

Exit codes:
    0 = success
    1 = one or more files failed
"""

from __future__ import annotations

import argparse
import contextlib
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cex_shared import CEX_ROOT

MODEL_NAME = "microsoft/llmlingua-2-xlm-roberta-large-meetingbank"
MIN_BYTES = 500
FRONTMATTER_RE = re.compile(r"\A(---\r?\n.*?\r?\n---\r?\n?)(.*)\Z", re.DOTALL)


@dataclass
class FileResult:
    path: Path
    status: str
    before_bytes: int
    after_bytes: int
    ratio: float
    output_path: Path | None = None
    note: str = ""


_COMPRESSOR = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compress markdown with LLMLingua-2 while preserving repo layout."
    )
    parser.add_argument(
        "--target",
        choices=("boot", "file", "all"),
        required=True,
        help="boot = CLAUDE.md + .claude/rules/*.md; file = one path; all = all .md under .claude/",
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=0.7,
        help="Compression ratio passed to LLMLingua-2 (default: 0.7)",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite target files instead of writing .compressed.md siblings",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print byte savings without writing files",
    )
    parser.add_argument(
        "--skip-frontmatter",
        dest="skip_frontmatter",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Preserve YAML frontmatter and compress only the body (default: true)",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Required when --target file. Relative paths are resolved from repo root.",
    )
    args = parser.parse_args()

    if args.target == "file" and not args.path:
        parser.error("--target file requires a path")
    if args.target != "file" and args.path:
        parser.error("positional path is only valid with --target file")
    if args.ratio <= 0 or args.ratio > 1:
        parser.error("--ratio must be > 0 and <= 1")

    return args


def resolve_targets(target: str, path_arg: str | None) -> list[Path]:
    if target == "boot":
        paths = [CEX_ROOT / "CLAUDE.md"]
        paths.extend(sorted((CEX_ROOT / ".claude" / "rules").glob("*.md")))
        return [path for path in paths if path.exists()]

    if target == "all":
        return sorted(
            path for path in (CEX_ROOT / ".claude").rglob("*.md")
            if path.is_file() and not path.name.endswith(".compressed.md")
        )

    if path_arg is None:
        return []

    path = Path(path_arg)
    if not path.is_absolute():
        path = CEX_ROOT / path
    return [path.resolve()]


def split_frontmatter_exact(text: str) -> tuple[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), match.group(2)


def sibling_output_path(path: Path) -> Path:
    return path.with_name(path.stem + ".compressed" + path.suffix)


def get_compressor():
    global _COMPRESSOR
    if _COMPRESSOR is not None:
        return _COMPRESSOR

    try:
        from llmlingua import PromptCompressor
    except ImportError:
        print("[FAIL] Missing dependency: llmlingua")
        print("Install hint: python -m pip install llmlingua")
        return None

    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            _COMPRESSOR = PromptCompressor(
                model_name=MODEL_NAME,
                use_llmlingua2=True,
            )
    except Exception:
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                _COMPRESSOR = PromptCompressor(
                    model_name=MODEL_NAME,
                    use_llmlingua2=True,
                    device_map="cpu",
                )
        except Exception as exc:
            print("[FAIL] Could not initialize LLMLingua-2: %s" % exc)
            return None
    return _COMPRESSOR


def compress_text(text: str, ratio: float) -> str:
    compressor = get_compressor()
    if compressor is None:
        raise RuntimeError("compressor unavailable")
    chunks = split_for_compression(text)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        result = compressor.compress_prompt(chunks, rate=ratio)
    compressed_list = result.get("compressed_prompt_list") or []
    if compressed_list:
        compressed = "\n\n".join(part.strip() for part in compressed_list if part.strip())
    else:
        compressed = result.get("compressed_prompt", "").strip()
    if not compressed:
        raise RuntimeError("compressor returned empty output")
    return compressed


def split_for_compression(text: str, max_chars: int = 700) -> list[str]:
    parts = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    if not parts:
        return [text]

    chunks: list[str] = []
    current = ""
    for part in parts:
        candidate = part if not current else current + "\n\n" + part
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(part) <= max_chars:
            current = part
            continue

        lines = [line for line in part.splitlines() if line.strip()]
        current = ""
        for line in lines:
            candidate = line if not current else current + "\n" + line
            if len(candidate) <= max_chars:
                current = candidate
            else:
                if current:
                    chunks.append(current)
                current = line
        if current and len(current) > max_chars:
            chunks.append(current[:max_chars])
            current = current[max_chars:]

    if current:
        chunks.append(current)
    return chunks or [text]


def compress_file(path: Path, ratio: float, skip_frontmatter: bool,
                  dry_run: bool, in_place: bool) -> FileResult:
    if not path.exists():
        return FileResult(path, "fail", 0, 0, 1.0, note="file not found")

    text = path.read_text(encoding="utf-8")
    before_bytes = len(text.encode("utf-8"))

    if before_bytes < MIN_BYTES:
        return FileResult(path, "skip", before_bytes, before_bytes, 1.0, note="below 500 bytes")

    frontmatter = ""
    body = text
    if skip_frontmatter:
        frontmatter, body = split_frontmatter_exact(text)

    if not body.strip():
        return FileResult(path, "skip", before_bytes, before_bytes, 1.0, note="empty body")

    compressed_body = compress_text(body, ratio)
    final_text = frontmatter + compressed_body if skip_frontmatter else compressed_body
    after_bytes = len(final_text.encode("utf-8"))
    result_ratio = after_bytes / before_bytes if before_bytes else 1.0

    output_path = path if in_place else sibling_output_path(path)
    if not dry_run:
        output_path.write_text(final_text, encoding="utf-8")

    status = "ok"
    if dry_run:
        output_path = None

    return FileResult(
        path=path,
        status=status,
        before_bytes=before_bytes,
        after_bytes=after_bytes,
        ratio=result_ratio,
        output_path=output_path,
        note="compressed",
    )


def print_result(result: FileResult) -> None:
    print(
        "%s | BEFORE=%d | AFTER=%d | RATIO=%.3f | %s%s" % (
            result.status.upper(),
            result.before_bytes,
            result.after_bytes,
            result.ratio,
            result.path.as_posix(),
            "" if result.output_path is None else " -> " + result.output_path.as_posix(),
        )
    )
    if result.note:
        print("  note: %s" % result.note)


def print_summary(results: Iterable[FileResult]) -> None:
    rows = list(results)
    print("")
    print("SUMMARY")
    print("status | before | after | ratio | path")
    print("-" * 72)
    total_before = 0
    total_after = 0
    ok_count = 0
    fail_count = 0

    for row in rows:
        total_before += row.before_bytes
        total_after += row.after_bytes
        if row.status == "ok":
            ok_count += 1
        if row.status == "fail":
            fail_count += 1
        print(
            "%-6s | %6d | %5d | %0.3f | %s" % (
                row.status,
                row.before_bytes,
                row.after_bytes,
                row.ratio,
                row.path.as_posix(),
            )
        )

    total_ratio = total_after / total_before if total_before else 1.0
    print("-" * 72)
    print(
        "TOTAL  | %6d | %5d | %0.3f | ok=%d fail=%d files=%d" % (
            total_before,
            total_after,
            total_ratio,
            ok_count,
            fail_count,
            len(rows),
        )
    )


def main() -> int:
    args = parse_args()
    targets = resolve_targets(args.target, args.path)
    if not targets:
        print("[FAIL] No target files found")
        return 1

    results: list[FileResult] = []
    failed = False

    for path in targets:
        try:
            result = compress_file(
                path=path,
                ratio=args.ratio,
                skip_frontmatter=args.skip_frontmatter,
                dry_run=args.dry_run,
                in_place=args.in_place,
            )
        except Exception as exc:
            result = FileResult(path, "fail", 0, 0, 1.0, note=str(exc))

        print_result(result)
        results.append(result)
        if result.status == "fail":
            failed = True

    print_summary(results)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
