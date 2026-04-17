#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Prompt Layers -- load compiled artifacts from pillar directories.

Scans P{03,04,08,11}_*/compiled/ for YAML artifacts and provides them
as injectable prompt layers for cex_crew_runner.py.

Design: Each artifact is a YAML file with frontmatter. The body text
after the frontmatter '---' separator IS the prompt content. The
frontmatter provides metadata for filtering and routing.

Usage:
    from cex_prompt_layers import PromptLayers
    layers = PromptLayers()
    identity = layers.get("p03_sp_cex_core_identity")
    guardrails = layers.by_kind("guardrail")
    skills = layers.by_kind("skill")
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent

# Pillar directories that contain compiled artifacts
PILLAR_COMPILED_DIRS = [
    CEX_ROOT / "N00_genesis" / "P03_prompt" / "compiled",
    CEX_ROOT / "N00_genesis" / "P04_tools" / "compiled",
    CEX_ROOT / "N00_genesis" / "P08_architecture" / "compiled",
    CEX_ROOT / "N00_genesis" / "P11_feedback" / "compiled",
    CEX_ROOT / "N00_genesis" / "P12_orchestration" / "compiled",
]


def _parse_simple_meta(text: str) -> dict:
    """Parse simple key:value lines from text. Stops at complex values."""
    meta = {}
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, _, val = stripped.partition(":")
        key = key.strip()
        val = val.strip()
        # Skip multi-line or complex keys
        if key in ("body",):
            break
        # Strip quotes
        if val and val[0] in ('"', "'") and val[-1] == val[0]:
            val = val[1:-1]
        # Handle lists like [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip("'\"") for v in val[1:-1].split(",")]
        elif val.lower() == "null":
            val = None
        elif val.lower() == "true":
            val = True
        elif val.lower() == "false":
            val = False
        elif val.replace(".", "", 1).isdigit():
            val = float(val) if "." in val else int(val)
        meta[key] = val
    return meta


_META_KEYS = {
    "id", "kind", "pillar", "version", "created", "updated", "author",
    "title", "domain", "coverage", "languages", "quality", "tags",
    "tldr", "density_score", "severity", "enforcement",
}


def _try_yaml_safe_load(text: str) -> tuple:
    """Try parsing flat YAML with PyYAML. Returns (meta_dict, body_str) or None."""
    try:
        import yaml
        data = yaml.safe_load(text)
        if not isinstance(data, dict) or not data.get("id"):
            return None
        if data.get("body"):
            body = str(data.pop("body", ""))
            return data, body
        # Reconstruct body from non-metadata keys (compiled artifacts
        # without explicit 'body' key, e.g. prompt_compiler)
        if data.get("kind"):
            body_parts = []
            meta = {}
            for k, v in data.items():
                if k in _META_KEYS:
                    meta[k] = v
                else:
                    body_parts.append(f"## {k}\n{v}")
            if body_parts:
                return meta, "\n\n".join(body_parts)
    except Exception:
        pass
    return None


def _parse_yaml_frontmatter(text: str) -> tuple:
    """Parse YAML frontmatter from text. Returns (metadata_dict, body_text).

    Supports two formats:
    1. --- delimited frontmatter (markdown style)
    2. Flat YAML with a 'body' key containing prompt content (via PyYAML)
    """
    if text.startswith("---"):
        end = text.find("---", 3)
        if end >= 0:
            fm_text = text[3:end].strip()
            body = text[end + 3:].strip()
            meta = _parse_simple_meta(fm_text)
            return meta, body

    # Flat YAML format: use PyYAML for robust parsing
    result = _try_yaml_safe_load(text)
    if result:
        return result

    # Fallback: try simple metadata extraction
    meta = _parse_simple_meta(text)
    if meta.get("id") and meta.get("kind"):
        return meta, ""

    return {}, text


class PromptLayers:
    """Registry of compiled CEX artifacts loadable as prompt layers."""

    def __init__(self):
        self._artifacts = {}  # id -> {meta, body, path}
        self._by_kind = {}    # kind -> [id, ...]
        self._loaded = False

    def _ensure_loaded(self):
        if self._loaded:
            return
        self._loaded = True

        for d in PILLAR_COMPILED_DIRS:
            if not d.exists():
                continue
            for f in d.glob("*.yaml"):
                # Skip example files (ex_*)
                if f.name.startswith("ex_"):
                    continue
                try:
                    text = f.read_text(encoding="utf-8")
                    meta, body = _parse_yaml_frontmatter(text)
                    aid = meta.get("id", f.stem)
                    kind = meta.get("kind", "unknown")

                    self._artifacts[aid] = {
                        "meta": meta,
                        "body": body,
                        "path": str(f),
                    }

                    if kind not in self._by_kind:
                        self._by_kind[kind] = []
                    self._by_kind[kind].append(aid)
                except Exception:
                    continue

    def get(self, artifact_id: str) -> str:
        """Get artifact body text by ID. Returns empty string if not found."""
        self._ensure_loaded()
        entry = self._artifacts.get(artifact_id)
        return entry["body"] if entry else ""

    def get_meta(self, artifact_id: str) -> dict:
        """Get artifact metadata by ID."""
        self._ensure_loaded()
        entry = self._artifacts.get(artifact_id)
        return entry["meta"] if entry else {}

    def by_kind(self, kind: str) -> list:
        """Get all artifact IDs of a given kind."""
        self._ensure_loaded()
        return self._by_kind.get(kind, [])

    def get_all_of_kind(self, kind: str) -> str:
        """Get concatenated body text of all artifacts of a kind."""
        self._ensure_loaded()
        ids = self.by_kind(kind)
        parts = []
        for aid in ids:
            body = self.get(aid)
            if body:
                meta = self.get_meta(aid)
                title = meta.get("title", aid)
                parts.append(f"### {title}\n{body}")
        return "\n\n".join(parts)

    def list_all(self) -> dict:
        """Return {id: {kind, title, pillar}} for all loaded artifacts."""
        self._ensure_loaded()
        result = {}
        for aid, entry in self._artifacts.items():
            m = entry["meta"]
            result[aid] = {
                "kind": m.get("kind", "?"),
                "title": m.get("title", aid),
                "pillar": m.get("pillar", "?"),
            }
        return result

    def stats(self) -> dict:
        """Return summary statistics."""
        self._ensure_loaded()
        return {
            "total": len(self._artifacts),
            "by_kind": {k: len(v) for k, v in sorted(self._by_kind.items())},
        }


# Singleton for module-level use
_layers = None


def get_layers() -> PromptLayers:
    """Get singleton PromptLayers instance."""
    global _layers
    if _layers is None:
        _layers = PromptLayers()
    return _layers


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CEX Prompt Layers -- artifact loader")
    parser.add_argument("--list", action="store_true", help="List all loaded artifacts")
    parser.add_argument("--stats", action="store_true", help="Show summary statistics")
    parser.add_argument("--get", type=str, help="Get artifact body by ID")
    parser.add_argument("--kind", type=str, help="List artifacts of a kind")
    args = parser.parse_args()

    layers = get_layers()

    if args.stats:
        s = layers.stats()
        print(f"\n=== PromptLayers Stats ===\n")
        print(f"  Total artifacts: {s['total']}")
        print(f"  By kind:")
        for k, v in s["by_kind"].items():
            print(f"    {k:25s} : {v}")

    elif args.list:
        all_a = layers.list_all()
        print(f"\n=== {len(all_a)} Compiled Artifacts ===\n")
        for aid, info in sorted(all_a.items()):
            print(f"  {aid:45s} [{info['kind']:20s}] {info['pillar']}")

    elif args.get:
        body = layers.get(args.get)
        if body:
            print(body)
        else:
            print(f"Not found: {args.get}", file=sys.stderr)
            sys.exit(1)

    elif args.kind:
        ids = layers.by_kind(args.kind)
        if ids:
            print(f"\n=== {len(ids)} artifacts of kind '{args.kind}' ===\n")
            for aid in ids:
                meta = layers.get_meta(aid)
                print(f"  {aid}: {meta.get('title', '?')}")
        else:
            print(f"No artifacts of kind '{args.kind}'", file=sys.stderr)

    else:
        parser.print_help()
