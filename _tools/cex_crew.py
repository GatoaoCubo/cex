"""cex_crew.py -- discover, list, and run composable crews.

A composable crew is a crew_template.md + N role_assignment.md files + an
optional team_charter.md. This tool:

  1. Scans the repo for crew_template.md files (by kind frontmatter).
  2. Resolves role_assignment refs declared in the template's `## Roles` table.
  3. Optionally attaches a team_charter (mission/budget/deadline/gate).
  4. Delegates to cex_crew_runner.CrewRunner.load_from_crew_template(...)
     to build a plan dict, then CrewRunner.run(...) to execute.

Usage:
  python _tools/cex_crew.py list                         # list known crews
  python _tools/cex_crew.py show product_launch          # print resolved plan
  python _tools/cex_crew.py run product_launch \
      --charter N02_marketing/P12_orchestration/team_charter_launch_demo.md
  python _tools/cex_crew.py run product_launch --execute # real LLM calls

The crew NAME matches `crew_name` in the template frontmatter (or the file
stem without the `p12_ct_` prefix).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))

from cex_crew_runner import CrewRunner, _parse_md_frontmatter  # noqa: E402


def find_crews() -> list[dict]:
    """Scan the repo for crew_template artifacts. Look in N0*/crews and P12_*.

    Returns a list of {name, path, process, roles, purpose} dicts.
    """
    found: list[dict] = []
    seen: set[str] = set()
    patterns = ["N0*/P12_orchestration/p12_ct_*.md", "P12_*/**/p12_ct_*.md"]
    for pat in patterns:
        for p in ROOT.glob(pat):
            if p.name in seen:
                continue
            seen.add(p.name)
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            fm = _parse_md_frontmatter(text)
            if fm.get("kind") and fm["kind"] != "crew_template":
                continue
            name = fm.get("crew_name") or re.sub(r"^p12_ct_", "", p.stem)
            # count roles by parsing the Roles table
            roles = _count_roles(text)
            found.append(
                {
                    "name": name,
                    "path": str(p.resolve().relative_to(ROOT.resolve())).replace("\\", "/"),
                    "process": fm.get("process", "sequential"),
                    "roles": roles,
                    "purpose": fm.get("purpose", ""),
                }
            )
    return sorted(found, key=lambda x: x["name"])


def _count_roles(text: str) -> int:
    in_section = False
    count = 0
    for line in text.splitlines():
        low = line.strip().lower()
        if low.startswith("## "):
            in_section = low.startswith("## roles")
            continue
        if not in_section:
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].lower() in ("role", "---", ":---"):
            continue
        if re.match(r"^[-: ]+$", cells[0]):
            continue
        count += 1
    return count


def resolve_crew(name: str) -> Path:
    """Map a crew NAME (or path) to a crew_template file path."""
    p = Path(name)
    if p.suffix == ".md" and p.exists():
        return p
    # Known convention: p12_ct_{name}.md
    for candidate in [
        ROOT / f"N02_marketing/P12_orchestration/p12_ct_{name}.md",
        *sorted(ROOT.glob(f"N0*/P12_orchestration/p12_ct_{name}.md")),
        *sorted(ROOT.glob(f"P12_*/**/p12_ct_{name}.md")),
    ]:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"No crew_template found for '{name}'. "
        "Run `python _tools/cex_crew.py list` to see available crews."
    )


def cmd_list(_args) -> int:
    crews = find_crews()
    if not crews:
        print("No crews found. Expected pattern: N0*/P12_orchestration/p12_ct_*.md")
        return 0
    print(f"[{len(crews)}] composable crews discovered:\n")
    for c in crews:
        print(
            f"  {c['name']:28s} [{c['process']:13s}] roles={c['roles']:2d}  "
            f"{c['path']}"
        )
        if c["purpose"]:
            purpose = c["purpose"][:100]
            print(f"    -> {purpose}")
    return 0


def cmd_show(args) -> int:
    crew_path = resolve_crew(args.name)
    charter_path = Path(args.charter) if args.charter else None
    plan = CrewRunner.load_from_crew_template(
        crew_path, charter_path=charter_path
    )
    print(json.dumps(plan, indent=2, ensure_ascii=True, default=str))
    return 0


def cmd_run(args) -> int:
    crew_path = resolve_crew(args.name)
    charter_path = Path(args.charter) if args.charter else None
    plan = CrewRunner.load_from_crew_template(
        crew_path, charter_path=charter_path
    )
    print(
        f"[CREW] {plan['crew_meta']['crew_name']} "
        f"(process={plan['crew_meta']['process']}, roles={len(plan['crew_meta']['roles'])})"
    )

    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else ROOT / ".cex" / "runtime" / "crews" / plan["crew_meta"]["crew_name"]
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    runner = CrewRunner(plan)
    state = runner.run(
        dry_run=not args.execute,
        output_dir=output_dir,
    )
    failed = sum(1 for o in state.outputs.values() if o.status == "failed")
    print(f"[CREW] done. output={output_dir}, failed={failed}")
    return 1 if failed > 0 else 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="CEX composable-crew runner (discover + instantiate + execute)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp_list = sub.add_parser("list", help="List all available crews")
    sp_list.set_defaults(func=cmd_list)

    sp_show = sub.add_parser("show", help="Print the resolved plan JSON")
    sp_show.add_argument("name", help="Crew name or path")
    sp_show.add_argument("--charter", help="Optional team_charter path")
    sp_show.set_defaults(func=cmd_show)

    sp_run = sub.add_parser("run", help="Execute the crew (dry-run by default)")
    sp_run.add_argument("name", help="Crew name or path")
    sp_run.add_argument("--charter", help="Optional team_charter path")
    sp_run.add_argument("--output-dir", help="Output directory (default: .cex/runtime/crews/{name})")
    sp_run.add_argument(
        "--execute",
        action="store_true",
        help="Real LLM execution (default: dry-run generates prompts only)",
    )
    sp_run.set_defaults(func=cmd_run)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
