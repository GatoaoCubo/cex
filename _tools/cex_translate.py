#!/usr/bin/env python3
"""
cex_translate.py -- PT-BR to EN translation engine for CEX repo.

Uses Anthropic Haiku for batch translation of Portuguese content.
Handles .py (comments + strings), .md (prose), .ps1 (Write-Host + comments).

Usage:
    python _tools/cex_translate.py --check [path]      # count PT-BR lines
    python _tools/cex_translate.py --scope _tools/     # translate specific path
    python _tools/cex_translate.py --dry-run           # show changes without writing
    python _tools/cex_translate.py                     # translate all phases
"""

import argparse
import json
import re
import sys
from pathlib import Path

# -- PT-BR detection vocabulary (ASCII-only, no accented chars) -----------------

PT_WORDS = {
    "voce", "nao", "criar", "fazer", "usar", "arquivo", "pasta", "resultado",
    "erro", "aviso", "missao", "visao", "acao", "nucleo", "construcao", "execucao",
    "validacao", "gerenciar", "gerar", "gerador", "retorne", "preencha", "lista",
    "fonte", "fontes", "tarefa", "topico", "termos", "termo", "salvar", "formato",
    "saida", "entrada", "regras", "regra", "apenas", "denso", "densa", "densos",
    "denso", "frase", "conteudo", "contem", "conter", "novo", "nova", "todos",
    "todas", "cada", "sendo", "seja", "deve", "devem", "deve", "minimo", "maximo",
    "tamanho", "campo", "campos", "obrigatorio", "obrigatorios", "existe", "existem",
    "nenhum", "qualquer", "sempre", "nunca", "qualidade", "limite", "insumo",
    "artefato", "artefatos", "tipo", "tipos", "nome", "estrutura", "base",
    "contexto", "pilar", "pilares", "dominio", "variante", "palavras-chave",
    "palavras", "principal", "principio", "principios", "utilizar", "utiliza",
    "semente", "sementes", "use", "sua", "seu", "suas", "seus", "pelo", "pela",
    "pelos", "pelas", "alem", "seguindo", "seguir", "respeite", "respeitar",
    "crie", "criado", "criados", "especializado", "especializada", "valido",
    "valida", "secoes", "secao", "mensagem", "mensagens", "preenchidos",
    "preenchido", "verbatim", "busca", "consulta", "oficial", "documentacao",
    "invente", "inclua", "ordene", "minimo", "filler", "repeticao", "obviedades",
    "informacao", "unica", "unico", "classificar", "frase",
}

PT_SUFFIXES = ("-cao", "-coes", "-agem", "-agens", "cao", "coes")

# -- Files / ranges to NEVER translate ------------------------------------------

SKIP_FILES = {
    "translate_isos.py",
    "cex_translate.py",
    "cex_intent_resolver.py",   # multilingual intent maps are intentional
    "cex_handoff_composer.py",  # multilingual maps
    "cex_query.py",             # multilingual maps
}

# Line ranges to skip in specific files (0-indexed, inclusive)
SKIP_RANGES: dict[str, tuple[int, int]] = {
    "cex_8f_motor.py": (269, 549),   # intent resolution keyword maps (lines 270-550)
    "cex_intent_resolver.py": (0, 9999),  # entire file
}

# Directories to skip
SKIP_DIRS = {
    ".git", ".cex", "compiled", "__pycache__", ".venv", "node_modules",
    "_tests",
}

CEX_ROOT = Path(__file__).parent.parent
LOG_PATH = CEX_ROOT / ".cex" / "runtime" / "translate_log.jsonl"

# -- PT-BR detection ------------------------------------------------------------

def is_pt_line(text: str) -> bool:
    """Return True if the text contains Portuguese content."""
    lower = text.lower()
    words = re.findall(r"[a-z]+", lower)
    for w in words:
        if w in PT_WORDS:
            return True
        for suf in PT_SUFFIXES:
            if w.endswith(suf) and len(w) > len(suf) + 2:
                return True
    return False


def extract_translatable_py(lines: list[str]) -> list[tuple[int, str]]:
    """Extract (line_idx, content) from .py that should be translated.
    Only comments and string literals -- never variable names or imports.
    """
    results = []
    in_docstring = False
    docstring_char = None

    for i, raw in enumerate(lines):
        stripped = raw.strip()

        # Track triple-quoted docstrings
        if not in_docstring:
            for q in ('"""', "'''"):
                if stripped.startswith(q):
                    if stripped.count(q) >= 2 and len(stripped) > 3:
                        # single-line docstring
                        if is_pt_line(stripped):
                            results.append((i, raw))
                    else:
                        in_docstring = True
                        docstring_char = q
                        if is_pt_line(stripped):
                            results.append((i, raw))
                    break
            else:
                # Comment line
                if stripped.startswith("#") and is_pt_line(stripped):
                    results.append((i, raw))
                # Non-docstring string literals in assignments / function calls
                elif is_pt_line(stripped) and (
                    stripped.startswith(("sections.append(", "print(", "f\"", "'",
                                         '"', "'", "warnings.append("))
                    or "= f\"" in stripped or "= f'" in stripped
                    or "= \"" in stripped or "= '" in stripped
                ):
                    results.append((i, raw))
        else:
            if docstring_char and docstring_char in stripped:
                in_docstring = False
                docstring_char = None
            if is_pt_line(stripped):
                results.append((i, raw))

    return results


def extract_translatable_md(lines: list[str]) -> list[tuple[int, str]]:
    """Extract (line_idx, content) from .md that should be translated.
    Skip: frontmatter keys, code blocks, {{VARIABLES}}, kind/pillar names.
    """
    results = []
    in_frontmatter = False
    in_code_block = False
    fm_fence_count = 0

    for i, raw in enumerate(lines):
        stripped = raw.strip()

        # Frontmatter detection
        if i == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        # Code block
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Skip lines that are purely kind/pillar/nucleus references
        if re.match(r"^\s*\|?\s*[NP][0-9]+[_\s]", stripped):
            continue

        # Skip table rows that are PT/EN bilingual pairs (contain " / ")
        if " / " in stripped and "|" in stripped:
            continue

        if is_pt_line(stripped) and len(stripped) > 5:
            results.append((i, raw))

    return results


def extract_translatable_ps1(lines: list[str]) -> list[tuple[int, str]]:
    """Extract translatable lines from .ps1 files."""
    results = []
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if (stripped.startswith("#") or "Write-Host" in stripped) and is_pt_line(stripped):
            results.append((i, raw))
    return results


# -- Translation via Anthropic Haiku -------------------------------------------

def translate_batch(lines_content: list[str]) -> list[str]:
    """Translate a batch of lines PT-BR -> EN using Haiku. Returns same count."""
    try:
        from cex_sdk.models.chat import chat
    except ImportError:
        print("[WARN] cex_sdk not installed; skipping API translation")
        return lines_content

    joined = "\n".join(lines_content)

    prompt = (
        "Translate the following lines from Portuguese to English.\n"
        "Rules:\n"
        "- Preserve code syntax exactly (quotes, parentheses, f-strings, backslashes)\n"
        "- Preserve {{VARIABLES}}, {{{{PLACEHOLDERS}}}}, and {{MUSTACHE}} markers as-is\n"
        "- Preserve kind names (knowledge_card, agent, etc), pillar codes (P01-P12), "
        "nucleus IDs (N01-N07)\n"
        "- Preserve markdown formatting (##, **, -, |, `backticks`)\n"
        "- Output ONLY the translated lines, same count, same order\n"
        "- Use ASCII characters only (no accented letters, no em-dashes)\n"
        "- Do NOT add explanations or extra lines\n\n"
        "Lines to translate:\n"
        + joined
    )

    try:
        try:
            from _tools.cex_model_resolver import resolve_model_for_tool
            _model = resolve_model_for_tool("cex_translate", "light")["model"]
        except Exception:
            _model = "claude-haiku-4-5-20251001"
        translated = chat(prompt, model=_model, max_tokens=2048).strip()
        result_lines = translated.split("\n")
        # Pad or trim to match input count
        while len(result_lines) < len(lines_content):
            result_lines.append(lines_content[len(result_lines)])
        return result_lines[: len(lines_content)]
    except Exception as exc:
        print(f"[WARN] API error: {exc}")
        return lines_content


# -- File processing -----------------------------------------------------------

def should_skip_file(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return True
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    return False


def get_skip_range(path: Path) -> tuple[int, int] | None:
    return SKIP_RANGES.get(path.name)


def process_file(
    path: Path, dry_run: bool = False, verbose: bool = False
) -> dict:
    """Process one file. Returns stats dict."""
    if should_skip_file(path):
        return {"file": str(path), "skipped": True}

    suffix = path.suffix.lower()
    if suffix not in (".py", ".md", ".ps1", ".sh"):
        return {"file": str(path), "skipped": True}

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {"file": str(path), "skipped": True, "reason": "decode_error"}

    lines = content.splitlines(keepends=True)
    skip_range = get_skip_range(path)

    # Extract translatable lines
    stripped_lines = [l.rstrip("\r\n") for l in lines]
    if suffix == ".py":
        candidates = extract_translatable_py(stripped_lines)
    elif suffix in (".md",):
        candidates = extract_translatable_md(stripped_lines)
    elif suffix in (".ps1", ".sh"):
        candidates = extract_translatable_ps1(stripped_lines)
    else:
        candidates = []

    # Filter out skip ranges
    if skip_range:
        lo, hi = skip_range
        candidates = [(i, c) for (i, c) in candidates if not (lo <= i <= hi)]

    if not candidates:
        return {"file": str(path), "translated": 0}

    # Batch translate (40 lines at a time)
    BATCH = 40
    updates: dict[int, str] = {}
    for start in range(0, len(candidates), BATCH):
        batch = candidates[start: start + BATCH]
        raw_texts = [c for (_, c) in batch]
        translated = translate_batch(raw_texts)
        for (idx, orig), new_text in zip(batch, translated):
            if new_text.strip() != orig.strip():
                updates[idx] = new_text

    if not updates:
        return {"file": str(path), "translated": 0}

    if verbose:
        for idx, new_text in sorted(updates.items()):
            orig = stripped_lines[idx]
            print(f"  [{path}:{idx+1}]")
            print(f"  - {orig}")
            print(f"  + {new_text}")

    if not dry_run:
        new_lines = []
        for i, raw in enumerate(lines):
            if i in updates:
                # Preserve original line ending
                ending = "\r\n" if raw.endswith("\r\n") else "\n"
                new_lines.append(updates[i].rstrip("\r\n") + ending)
            else:
                new_lines.append(raw)
        path.write_text("".join(new_lines), encoding="utf-8")

    log_entry = {
        "file": str(path),
        "translated": len(updates),
        "dry_run": dry_run,
    }
    return log_entry


# -- Scanning / counting -------------------------------------------------------

def count_pt_lines(root: Path) -> dict[str, int]:
    """Count PT-BR lines per file without translating."""
    counts: dict[str, int] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if should_skip_file(path):
            continue
        if path.suffix.lower() not in (".py", ".md", ".ps1", ".sh"):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        stripped = content.splitlines()
        skip_range = get_skip_range(path)
        if path.suffix == ".py":
            cands = extract_translatable_py(stripped)
        elif path.suffix == ".md":
            cands = extract_translatable_md(stripped)
        else:
            cands = extract_translatable_ps1(stripped)
        if skip_range:
            lo, hi = skip_range
            cands = [(i, c) for (i, c) in cands if not (lo <= i <= hi)]
        if cands:
            counts[str(path.relative_to(CEX_ROOT))] = len(cands)
    return counts


# -- Phase definitions --------------------------------------------------------

PHASES = [
    {
        "name": "Phase 1: _tools Python files",
        "globs": ["_tools/*.py"],
        "suffixes": {".py"},
    },
    {
        "name": "Phase 2: boot ps1 + _spawn sh",
        "globs": ["boot/*.ps1", "_spawn/*.sh"],
        "suffixes": {".ps1", ".sh"},
    },
    {
        "name": "Phase 3: .claude rules/commands/skills",
        "globs": [".claude/rules/*.md", ".claude/commands/*.md", ".claude/skills/*.md"],
        "suffixes": {".md"},
    },
    {
        "name": "Phase 4: N00 knowledge cards + templates",
        "globs": [
            "N00_genesis/P*/library/kind/kc_*.md",
            "N00_genesis/P*/templates/tpl_*.md",
        ],
        "suffixes": {".md"},
    },
    {
        "name": "Phase 5: Nucleus content + specs",
        "globs": [
            "N0[1-7]_*/P01_knowledge/kc_*.md",
            "N0[1-7]_*/rules/*.md",
            "N0[1-7]_*/P08_architecture/*.md",
            "_docs/specs/*.md",
        ],
        "suffixes": {".md"},
    },
]


def run_phase(phase: dict, dry_run: bool, verbose: bool) -> int:
    """Run one translation phase. Returns total translated line count."""
    import glob as glob_mod

    total = 0
    print(f"\n=== {phase['name']} ===")
    for pattern in phase["globs"]:
        matched = sorted(glob_mod.glob(str(CEX_ROOT / pattern), recursive=True))
        for filepath in matched:
            p = Path(filepath)
            if p.suffix.lower() not in phase["suffixes"]:
                continue
            result = process_file(p, dry_run=dry_run, verbose=verbose)
            count = result.get("translated", 0)
            if count:
                marker = "[dry]" if dry_run else "[OK]"
                print(f"  {marker} {p.relative_to(CEX_ROOT)}: {count} lines translated")
                total += count

    if total == 0:
        print("  (nothing to translate)")
    return total


# -- Main ---------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="PT-BR -> EN translation engine")
    parser.add_argument("--check", nargs="?", const=".", metavar="PATH",
                        help="Count remaining PT-BR lines and exit")
    parser.add_argument("--scope", metavar="PATH",
                        help="Limit translation to a specific path")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show changes without writing files")
    parser.add_argument("--phase", type=int, choices=range(1, 6),
                        help="Execute only one phase (1-5)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show line-level diffs")
    args = parser.parse_args()

    # -- check mode
    if args.check is not None:
        scan_root = Path(args.check).resolve() if args.check != "." else CEX_ROOT
        print(f"Scanning PT-BR content under: {scan_root}")
        counts = count_pt_lines(scan_root)
        total = sum(counts.values())
        if counts:
            for f, n in sorted(counts.items(), key=lambda x: -x[1]):
                print(f"  {n:4d}  {f}")
        print(f"\nTotal PT-BR lines: {total}")
        return 0 if total < 50 else 1

    # -- scope mode (single path)
    if args.scope:
        scope_path = Path(args.scope).resolve()
        if scope_path.is_file():
            targets = [scope_path]
        else:
            targets = [p for p in scope_path.rglob("*") if p.is_file()]
        total = 0
        for p in targets:
            result = process_file(p, dry_run=args.dry_run, verbose=args.verbose)
            count = result.get("translated", 0)
            if count:
                marker = "[dry]" if args.dry_run else "[OK]"
                print(f"  {marker} {p}: {count} lines")
                total += count
        print(f"\nTotal: {total} lines translated")
        return 0

    # -- phase execution
    phases_to_run = PHASES if args.phase is None else [PHASES[args.phase - 1]]
    grand_total = 0
    for phase in phases_to_run:
        grand_total += run_phase(phase, dry_run=args.dry_run, verbose=args.verbose)

    print(f"\n=== Translation complete: {grand_total} lines translated ===")
    if args.dry_run:
        print("(dry-run -- no files were modified)")

    # Log results
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        import datetime
        f.write(json.dumps({
            "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "total": grand_total,
            "dry_run": args.dry_run,
            "phase": args.phase,
        }) + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
