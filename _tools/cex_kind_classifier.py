#!/usr/bin/env python3
"""cex_kind_classifier.py -- show requires_external_context / requires_live_tools per kind.

Usage:
  python _tools/cex_kind_classifier.py             # summary stats
  python _tools/cex_kind_classifier.py --list ext  # all kinds needing external context
  python _tools/cex_kind_classifier.py --list live # all kinds needing live tools
  python _tools/cex_kind_classifier.py --kind landing_page  # single kind detail
  python _tools/cex_kind_classifier.py --pillar P05         # all kinds in P05
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
META_PATH = ROOT / ".cex" / "kinds_meta.json"


def load_meta():
    with open(META_PATH) as f:
        return json.load(f)


def summary(meta):
    total = len(meta)
    ext_true = [k for k, v in meta.items() if v.get("requires_external_context")]
    live_true = [k for k, v in meta.items() if v.get("requires_live_tools")]
    print("kinds_meta.json classification summary")
    print(f"  Total kinds           : {total}")
    print(f"  requires_external_context=true  : {len(ext_true)} ({100*len(ext_true)//total}%)")
    print(f"  requires_external_context=false : {total - len(ext_true)} ({100*(total-len(ext_true))//total}%)")
    print(f"  requires_live_tools=true        : {len(live_true)}")
    print()
    print(f"[OK] Live-tools kinds (route to Claude-only): {', '.join(sorted(live_true))}")


def list_kinds(meta, filter_type):
    if filter_type == "ext":
        field = "requires_external_context"
        label = "requires_external_context=true"
    elif filter_type == "live":
        field = "requires_live_tools"
        label = "requires_live_tools=true"
    else:
        print(f"[FAIL] Unknown filter: {filter_type}. Use 'ext' or 'live'.", file=sys.stderr)
        sys.exit(1)

    matches = sorted(k for k, v in meta.items() if v.get(field))
    print(f"{label} ({len(matches)} kinds):")
    for k in matches:
        pillar = meta[k].get("pillar", "?")
        desc = meta[k].get("description", "")[:60]
        print(f"  {k:<35} [{pillar}]  {desc}")


def show_kind(meta, kind_name):
    if kind_name not in meta:
        print(f"[FAIL] Kind '{kind_name}' not found.", file=sys.stderr)
        sys.exit(1)
    v = meta[kind_name]
    print(f"Kind: {kind_name}")
    print(f"  pillar                   : {v.get('pillar', '?')}")
    print(f"  description              : {v.get('description', '')}")
    print(f"  requires_external_context: {v.get('requires_external_context', False)}")
    print(f"  requires_live_tools      : {v.get('requires_live_tools', False)}")
    print(f"  llm_function             : {v.get('llm_function', '?')}")
    print(f"  status                   : {v.get('status', '?')}")
    routing = "claude-only (live tools required)"
    if v.get("requires_live_tools"):
        routing = "claude-only (live tools required)"
    elif v.get("requires_external_context"):
        routing = "any runtime (pre-flight MCP gather recommended)"
    else:
        routing = "any runtime (no external context needed)"
    print(f"  routing                  : {routing}")


def show_pillar(meta, pillar):
    matches = {k: v for k, v in meta.items() if v.get("pillar") == pillar}
    if not matches:
        print(f"[FAIL] No kinds found for pillar '{pillar}'.", file=sys.stderr)
        sys.exit(1)
    print(f"Pillar {pillar} -- {len(matches)} kinds:")
    print(f"  {'Kind':<35} {'ext':>5}  {'live':>5}  Description")
    print(f"  {'-'*35}  {'-'*5}  {'-'*5}  {'-'*40}")
    for k in sorted(matches):
        v = matches[k]
        ext = "YES" if v.get("requires_external_context") else "no"
        live = "YES" if v.get("requires_live_tools") else "no"
        desc = v.get("description", "")[:40]
        print(f"  {k:<35}  {ext:>5}  {live:>5}  {desc}")


def main():
    parser = argparse.ArgumentParser(
        description="Classify CEX kinds by external context and live tool requirements."
    )
    parser.add_argument("--list", choices=["ext", "live"], help="List kinds by type")
    parser.add_argument("--kind", help="Show classification for a single kind")
    parser.add_argument("--pillar", help="Show all kinds in a pillar (e.g. P05)")
    args = parser.parse_args()

    meta = load_meta()

    if args.kind:
        show_kind(meta, args.kind)
    elif args.list:
        list_kinds(meta, args.list)
    elif args.pillar:
        show_pillar(meta, args.pillar)
    else:
        summary(meta)


if __name__ == "__main__":
    main()
