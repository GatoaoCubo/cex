#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Kind Register -- Add a new kind to the taxonomy in one command."""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CEX_ROOT = Path(__file__).resolve().parent.parent
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"
TYPE_TO_TPL = CEX_ROOT / "archetypes" / "TYPE_TO_TEMPLATE.yaml"
MOTOR_PY = CEX_ROOT / "_tools" / "cex_8f_motor.py"
VALID_PILLARS = [f"P{i:02d}" for i in range(1, 13)]
VALID_FNS = ["BECOME","INJECT","REASON","CALL","PRODUCE","CONSTRAIN","GOVERN","COLLABORATE"]
PILLAR_DIRS = {}
for _d in sorted(CEX_ROOT.glob("P[0-9][0-9]_*")):
    if _d.is_dir(): PILLAR_DIRS[_d.name[:3]] = _d.name

def load_json(p: Path) -> Any:
    with open(p, encoding="utf-8") as f: return json.load(f)

def save_json(p: Path, data: dict[str, Any]) -> None:
    with open(p, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(data.items())), f, indent=2, ensure_ascii=False)
        f.write(chr(10))

def rd(p: Path) -> str: return Path(p).read_text(encoding="utf-8")
def wr(p: Path, s: str) -> None: Path(p).write_text(s, encoding="utf-8")

def reg_meta(
    kind: str,
    pillar: str,
    fn: str,
    desc: str,
    max_b: int,
    boundary: str,
    dry: bool,
) -> bool:
    meta = load_json(KINDS_META)
    if kind in meta: print("  [SKIP] kinds_meta: exists"); return False
    nm = pillar.lower() + "_" + kind + "_{{topic}}.md + .yaml"
    entry = {"boundary": boundary, "core": False, "description": desc,
             "llm_function": fn, "max_bytes": max_b, "naming": nm, "pillar": pillar}
    if dry: print("  [DRY] kinds_meta: would add"); return True
    meta[kind] = entry; save_json(KINDS_META, meta)
    print("  [OK]  kinds_meta: added"); return True

def reg_schema(
    kind: str,
    pillar: str,
    desc: str,
    max_b: int,
    boundary: str,
    dry: bool,
) -> bool:
    path = CEX_ROOT / PILLAR_DIRS[pillar] / "_schema.yaml"
    content = rd(path)
    pat = r"^\s+" + kind + ":"
    if re.search(pat, content, re.MULTILINE):
        print("  [SKIP] _schema: exists"); return False
    if dry: print("  [DRY] _schema: would add"); return True
    nm = pillar.lower() + "_" + kind + "_{{topic}}.md + .yaml"
    block_parts = [
        f"  {kind}:",
        f"    description: {desc}",
        f"    boundary: {boundary}",
        "    layer: content",
        "    core: false",
        "    machine_format: yaml",
        f"    naming: {nm}",
        "    constraints:",
        f"      max_bytes: {max_b}",
        "      density_min: 0.8",
        "      quality_min: 7.0",
        "    frontmatter_required:",
        "    - id", "    - kind", "    - pillar", "    - title",
        "    - version", "    - created", "    - updated", "    - author",
        "    - domain", "    - quality", "    - tags", "    - tldr",
    ]
    block = chr(10).join(block_parts)
    file_lines = content.split(chr(10))
    insert_at = len(file_lines)
    in_kinds = False
    for i, l in enumerate(file_lines):
        if l.strip() == "kinds:": in_kinds = True; continue
        if in_kinds and l and not l.startswith(" ") and ":" in l:
            insert_at = i; break
    file_lines.insert(insert_at, block)
    wr(path, chr(10).join(file_lines))

    print("  [OK]  _schema: added"); return True

def reg_ttt(kind: str, pillar: str, dry: bool) -> bool:
    content = rd(TYPE_TO_TPL)
    if re.search(rf"^{kind}:", content, re.MULTILINE):
        print("  [SKIP] TYPE_TO_TPL: exists"); return False
    tpl = PILLAR_DIRS[pillar] + "/templates/tpl_" + kind + ".md"
    val = tpl if (CEX_ROOT / tpl).exists() else "null"
    line = kind + ": " + val
    if dry: print("  [DRY] TYPE_TO_TPL: would add"); return True
    ll = content.split(chr(10))

    done = False
    for i, l in enumerate(ll):
        k = l.split(":")[0] if ":" in l else ""
        if k and k > kind: ll.insert(i, line); done = True; break
    if not done: ll.append(line)
    wr(TYPE_TO_TPL, chr(10).join(ll))
    print("  [OK]  TYPE_TO_TPL: added"); return True

def reg_motor(kind: str, pillar: str, fn: str, dry: bool) -> bool:
    content = rd(MOTOR_PY)
    check_str = '"' + kind + '": ['
    if check_str in content:
        print("  [SKIP] Motor: exists"); return False
    e1 = '    "' + kind + '": [("' + kind + '", "' + pillar + '", "' + fn + '")],'
    entries = [e1]
    if "_" in kind:
        h = kind.replace("_", "-")
        h_check = '"' + h + '":'
        if h_check not in content:
            entries.append('    "' + h + '": [("' + kind + '", "' + pillar + '", "' + fn + '")],')
    if dry: print(f"  [DRY] Motor: would add {len(entries)} entries"); return True
    ll = content.split(chr(10))

    insert_at = None; in_dict = False
    for i, l in enumerate(ll):
        if "OBJECT_TO_KINDS = {" in l: in_dict = True; continue
        if in_dict:
            if l.strip() == "}":
                if insert_at is None: insert_at = i
                break
            m = re.match(r'\s+"([^"]+)":', l)
            if m and m.group(1) > kind and insert_at is None: insert_at = i
    if insert_at is None: print("  [ERR] Motor: no insertion point"); return False
    for e in reversed(entries): ll.insert(insert_at, e)
    wr(MOTOR_PY, chr(10).join(ll))
    print(f"  [OK]  Motor: added {len(entries)} entries"); return True

def validate() -> int:
    meta = set(load_json(KINDS_META).keys())
    ttt = set()
    for l in rd(TYPE_TO_TPL).split(chr(10)):
        if ":" in l and not l.startswith("#"):
            k = l.split(":")[0].strip()
            if k: ttt.add(k)
    motor = set()
    for m in re.finditer(r'"(\w+)",\s*"P\d{2}"', rd(MOTOR_PY)):
        motor.add(m.group(1))
    print(f"  kinds_meta:  {len(meta)} kinds")
    print(f"  TYPE_TO_TPL: {len(ttt)} entries")
    print(f"  Motor:       {len(motor)} unique kinds")
    g1 = meta - ttt; g2 = meta - motor
    if g1: print(f"  [GAP] Missing in TYPE_TO_TPL: {sorted(g1)}")
    if g2: print(f"  [GAP] Missing in Motor: {sorted(g2)}")
    if not g1 and not g2: print("  [OK]  All registries in sync")
    return 0 if (not g1 and not g2) else 1

def list_kinds() -> None:
    meta = load_json(KINDS_META)
    print(f"{'Kind':<30} {'Pillar':<6} {'Fn':<12} {'MaxB':<6} Description")
    print("-" * 95)
    for k in sorted(meta):
        d = meta[k]
        desc = d.get("description", "")[:35]
        print(f"{k:<30} {d['pillar']:<6} {d['llm_function']:<12} {d['max_bytes']:<6} {desc}")
    print(f"Total: {len(meta)} kinds")

def main() -> None:
    ap = argparse.ArgumentParser(description="CEX Kind Register")
    ap.add_argument("--kind"); ap.add_argument("--pillar", choices=VALID_PILLARS)
    ap.add_argument("--function", choices=VALID_FNS)
    ap.add_argument("--description"); ap.add_argument("--max-bytes", type=int, default=4096)
    ap.add_argument("--boundary", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--validate", action="store_true")
    args = ap.parse_args()
    if args.list: list_kinds(); return
    if args.validate: sys.exit(validate())
    if not all([args.kind, args.pillar, args.function, args.description]):
        ap.error("--kind, --pillar, --function, --description required")
    if not re.match(r"^[a-z][a-z0-9_]+$", args.kind):
        ap.error("Invalid kind: must be lowercase snake_case.")
    boundary = args.boundary or f"Specifically a {args.kind}."
    print(f"Registering: {args.kind} ({args.pillar}, {args.function})")
    c = sum([
        reg_meta(args.kind, args.pillar, args.function, args.description, args.max_bytes, boundary, args.dry_run),
        reg_schema(args.kind, args.pillar, args.description, args.max_bytes, boundary, args.dry_run),
        reg_ttt(args.kind, args.pillar, args.dry_run),
        reg_motor(args.kind, args.pillar, args.function, args.dry_run),
    ])
    tag = "DRY-RUN" if args.dry_run else "DONE"
    print(f"{tag}: {c}/4 files updated")
    if not args.dry_run and c > 0:
        pd = PILLAR_DIRS[args.pillar]
        print(f"Next: tpl({pd}/templates/tpl_{args.kind}.md) + builder + KC + doctor")

if __name__ == "__main__": main()
