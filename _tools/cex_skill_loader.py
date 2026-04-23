#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Skill Loader -- Multi-source, cached, dedup'd builder ISO registry.

Pattern: OpenClaude loadSkillsDir.ts + bundledSkills.ts
Adapted for CEX builder ISOs with 5 priority-ordered sources.

Source priority (lower = overridden by higher):
  0. genesis   -- N00_genesis/archetypes/ (base templates)
  1. shared    -- archetypes/builders/_shared/ (cross-builder skills)
  2. builder   -- archetypes/builders/{kind}-builder/ (kind-specific)
  3. nucleus   -- N{xx}_*/builders/ (nucleus-specific overrides)
  4. brand     -- .cex/brand/overrides/ (brand-specific customization)

Usage:
    from cex_skill_loader import get_skill_loader

    loader = get_skill_loader()
    isos = loader.load_builder("agent")
    for iso in isos:
        print(iso.name, iso.source, iso.pillar)
"""

import fnmatch
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent

# Source priority (higher index = higher priority for override)
SOURCE_PRIORITY = {
    "genesis": 0,
    "shared": 1,
    "builder": 2,
    "nucleus": 3,
    "brand": 4,
}

# All 12 ISO file patterns per builder (1:1 with 12 pillars)
ISO_PATTERNS = [
    "bld_knowledge_{kind}.md",
    "bld_model_{kind}.md",
    "bld_prompt_{kind}.md",
    "bld_tools_{kind}.md",
    "bld_output_{kind}.md",
    "bld_schema_{kind}.md",
    "bld_eval_{kind}.md",
    "bld_architecture_{kind}.md",
    "bld_config_{kind}.md",
    "bld_memory_{kind}.md",
    "bld_feedback_{kind}.md",
    "bld_orchestration_{kind}.md",
]

# Stage-to-ISO mapping: which ISO prefixes are needed for each 8F stage.
# Enables selective loading -- load 3 ISOs instead of 12 for targeted work.
STAGE_ISO_MAP = {
    "model": ["model"],
    "constraint": ["schema", "model"],
    "prompt": ["prompt"],
    "memory": ["memory"],
    "knowledge": ["knowledge", "context"],
    "few_shot": ["eval"],
    "template": ["template", "output"],
    "format": ["style", "template", "output"],
    "eval": ["eval"],
    "tools": ["tools"],
    "hooks": ["hooks"],
    "context": ["context"],
    "schema": ["schema"],
    "orchestration": ["orchestration"],
    "architecture": ["architecture"],
    "config": ["config"],
    "feedback": ["feedback"],
}

# Convenience aliases mapping 8F function names to stage groups
F_STAGE_ALIASES = {
    "F1": ["model", "constraint"],
    "F2": ["model", "prompt"],
    "F3": ["memory", "knowledge", "few_shot"],
    "F6": ["prompt", "template", "format"],
    "F7": ["eval", "feedback"],
}


@dataclass
class BuilderISO:
    """A loaded builder instruction set (analogous to OpenClaude Skill)."""
    name: str                        # e.g., "bld_prompt_agent"
    kind: str                        # e.g., "agent"
    source: str                      # genesis | shared | builder | nucleus | brand
    path: Path                       # Filesystem path to ISO file
    content: str                     # Raw markdown content (body only)
    frontmatter: dict                # Parsed YAML frontmatter

    # Extracted from frontmatter
    pillar: str = ""
    allowed_tools: List[str] = field(default_factory=list)
    model_hint: str = ""             # "opus" | "sonnet" | "inherit"
    when_to_use: str = ""
    conditional_paths: List[str] = field(default_factory=list)

    @property
    def is_conditional(self) -> bool:
        return bool(self.conditional_paths)

    @property
    def priority(self) -> int:
        return SOURCE_PRIORITY.get(self.source, 0)

    def get_prompt(self, **substitutions) -> str:
        """Return content with substitutions applied.

        Supports: {{KIND}}, {{BRAND_NAME}}, {{BRAND_VOICE}}, etc.
        """
        result = self.content
        for key, value in substitutions.items():
            result = result.replace(f"{{{{{key}}}}}", str(value))
        return result


def parse_frontmatter(raw: str) -> Tuple[dict, str]:
    """Parse YAML frontmatter from markdown content.

    Returns (frontmatter_dict, body_content).
    """
    if not raw.startswith("---"):
        return {}, raw

    end = raw.find("---", 3)
    if end == -1:
        return {}, raw

    fm_str = raw[3:end].strip()
    content = raw[end + 3:].strip()

    try:
        fm = yaml.safe_load(fm_str) or {}
    except yaml.YAMLError:
        fm = {}

    return fm, content


class SkillLoader:
    """Registry for builder ISOs. Discovers, loads, caches, deduplicates."""

    def __init__(self):
        self._cache: Dict[str, List[BuilderISO]] = {}
        self._conditional: Dict[str, BuilderISO] = {}
        self._activated: Dict[str, BuilderISO] = {}

    def load_builder(self, kind: str, force: bool = False,
                     stages: Optional[List[str]] = None) -> List[BuilderISO]:
        """Load ISOs for a builder kind, optionally filtered by stage.

        Args:
            kind: Builder kind name (e.g., "agent").
            force: Bypass cache and reload from disk.
            stages: Optional list of stage/section names to load. When provided,
                only ISOs matching those stages are returned (saves ~60% context
                tokens for targeted operations). Accepts stage names from
                STAGE_ISO_MAP keys or 8F aliases (F1, F2, F3, F6, F7).
                None = load all ISOs (default, backward-compatible).

        Returns:
            List of BuilderISO objects, sorted by source priority.
        """
        # Full load (cached)
        if kind in self._cache and not force:
            all_isos = self._cache[kind]
        else:
            all_isos = self._load_all_isos(kind)
            self._cache[kind] = all_isos

        # If no stage filter, return everything
        if stages is None:
            return all_isos

        # Resolve stage names to ISO prefix patterns
        prefixes = set()
        for stage in stages:
            # Check 8F aliases first (F1, F2, etc.)
            if stage.upper() in F_STAGE_ALIASES:
                for sub_stage in F_STAGE_ALIASES[stage.upper()]:
                    for prefix in STAGE_ISO_MAP.get(sub_stage, [sub_stage]):
                        prefixes.add(prefix)
            elif stage in STAGE_ISO_MAP:
                for prefix in STAGE_ISO_MAP[stage]:
                    prefixes.add(prefix)
            else:
                # Treat as a direct ISO prefix
                prefixes.add(stage)

        # Filter ISOs: match if any prefix appears in the ISO filename
        # Also always include shared skills (skill_* files)
        filtered = []
        for iso in all_isos:
            if iso.source == "shared":
                filtered.append(iso)
                continue
            name_lower = iso.name.lower()
            for prefix in prefixes:
                if f"_{prefix}_" in name_lower or name_lower.endswith(f"_{prefix}"):
                    filtered.append(iso)
                    break

        return filtered

    def _load_all_isos(self, kind: str) -> List[BuilderISO]:
        """Internal: load all ISOs for a kind from all sources."""
        isos: List[BuilderISO] = []
        seen_canonical: set = set()

        for source, paths in self._discover_sources(kind).items():
            for path in sorted(paths):
                try:
                    canonical = path.resolve()
                except OSError:
                    continue

                if canonical in seen_canonical:
                    continue
                seen_canonical.add(canonical)

                iso = self._load_iso(kind, source, path)
                if iso:
                    isos.append(iso)

        # Sort by source priority (lower first, so higher overrides later)
        isos.sort(key=lambda i: i.priority)
        return isos

    def _discover_sources(self, kind: str) -> Dict[str, List[Path]]:
        """Discover ISO files from all sources, priority-ordered."""
        sources: Dict[str, List[Path]] = {}

        # Genesis (base templates)
        genesis_dir = CEX_ROOT / "N00_genesis" / "archetypes" / "builders" / f"{kind}-builder"
        if genesis_dir.exists():
            sources["genesis"] = list(genesis_dir.glob("bld_*.md"))

        # Shared (cross-builder skills)
        shared_dir = CEX_ROOT / "archetypes" / "builders" / "_shared"
        if shared_dir.exists():
            sources["shared"] = list(shared_dir.glob("skill_*.md"))

        # Builder (kind-specific -- primary source)
        builder_dir = CEX_ROOT / "archetypes" / "builders" / f"{kind}-builder"
        if builder_dir.exists():
            sources["builder"] = list(builder_dir.glob("bld_*.md"))

        # Nucleus overrides (any N{xx}_* that has builders/)
        for ndir in sorted(CEX_ROOT.glob("N[0-9][0-9]_*")):
            kind_dir = ndir / "builders" / f"{kind}-builder"
            if kind_dir.exists():
                existing = sources.get("nucleus", [])
                existing.extend(kind_dir.glob("bld_*.md"))
                sources["nucleus"] = existing

        # Brand overrides (highest priority)
        brand_dir = CEX_ROOT / ".cex" / "brand" / "overrides" / f"{kind}-builder"
        if brand_dir.exists():
            sources["brand"] = list(brand_dir.glob("bld_*.md"))

        return sources

    def _load_iso(self, kind: str, source: str, path: Path) -> Optional[BuilderISO]:
        """Load and parse a single ISO file."""
        try:
            raw = path.read_text(encoding="utf-8")
            fm, content = parse_frontmatter(raw)

            return BuilderISO(
                name=path.stem,
                kind=kind,
                source=source,
                path=path,
                content=content,
                frontmatter=fm,
                pillar=str(fm.get("pillar", "")),
                allowed_tools=fm.get("allowed_tools", []) or [],
                model_hint=str(fm.get("model", "inherit")),
                when_to_use=str(fm.get("when_to_use", "")),
                conditional_paths=fm.get("paths", []) or [],
            )
        except Exception as e:
            print(f"[SkillLoader] Failed to load {path}: {e}", file=sys.stderr)
            return None

    def activate_for_paths(self, file_paths: List[str]) -> List[str]:
        """Activate conditional ISOs when matching files are touched.

        Pattern: OpenClaude activateConditionalSkillsForPaths
        """
        activated = []

        for name, iso in list(self._conditional.items()):
            for fp in file_paths:
                if any(fnmatch.fnmatch(fp, pat) for pat in iso.conditional_paths):
                    self._activated[name] = iso
                    del self._conditional[name]
                    activated.append(name)
                    break

        return activated

    def get_active_isos(self, kind: str) -> List[BuilderISO]:
        """Get all ISOs for a kind: cached + dynamically activated."""
        base = self.load_builder(kind)
        dynamic = [
            iso for iso in self._activated.values()
            if iso.kind == kind
        ]
        return base + dynamic

    def get_iso_by_name(self, kind: str, iso_name: str) -> Optional[BuilderISO]:
        """Get a specific ISO by name. Returns highest-priority match."""
        isos = self.load_builder(kind)
        matches = [i for i in isos if i.name == iso_name]
        if matches:
            return matches[-1]  # Last = highest priority
        return None

    def list_kinds(self) -> List[str]:
        """List all available builder kinds."""
        builder_dir = CEX_ROOT / "archetypes" / "builders"
        if not builder_dir.exists():
            return []
        kinds = []
        for d in sorted(builder_dir.iterdir()):
            if d.is_dir() and d.name.endswith("-builder") and d.name != "_shared":
                kinds.append(d.name.replace("-builder", ""))
        return kinds

    def clear_cache(self):
        """Clear all caches (call after file changes)."""
        self._cache.clear()

    def stats(self) -> dict:
        """Loader statistics for diagnostics."""
        all_kinds = self.list_kinds()
        total_isos = 0
        by_source = {s: 0 for s in SOURCE_PRIORITY}

        for kind in all_kinds:
            isos = self.load_builder(kind)
            total_isos += len(isos)
            for iso in isos:
                by_source[iso.source] = by_source.get(iso.source, 0) + 1

        return {
            "kinds": len(all_kinds),
            "total_isos": total_isos,
            "by_source": by_source,
            "conditional": len(self._conditional),
            "activated": len(self._activated),
        }


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_loader: Optional[SkillLoader] = None


def get_skill_loader() -> SkillLoader:
    """Get the singleton skill loader."""
    global _loader
    if _loader is None:
        _loader = SkillLoader()
    return _loader


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CEX Skill Loader -- Builder ISO registry")
    parser.add_argument("--list", action="store_true", help="List all builder kinds")
    parser.add_argument("--load", metavar="KIND", help="Load ISOs for a builder kind")
    parser.add_argument("--stats", action="store_true", help="Show loader statistics")
    args = parser.parse_args()

    loader = get_skill_loader()

    if args.list:
        kinds = loader.list_kinds()
        print(f"\n=== {len(kinds)} Builder Kinds ===\n")
        for k in kinds:
            isos = loader.load_builder(k)
            print(f"  {k:25s} ({len(isos)} ISOs)")

    elif args.load:
        isos = loader.load_builder(args.load)
        print(f"\n=== {args.load}-builder ({len(isos)} ISOs) ===\n")
        for iso in isos:
            size = len(iso.content)
            print(f"  [{iso.source:8s}] {iso.name:40s} ({size:,} bytes)")
            if iso.pillar:
                print(f"             pillar={iso.pillar}")

    elif args.stats:
        s = loader.stats()
        print("\n=== SkillLoader Stats ===\n")
        print(f"  Kinds:         {s['kinds']}")
        print(f"  Total ISOs:    {s['total_isos']}")
        print(f"  Conditional:   {s['conditional']}")
        print(f"  Activated:     {s['activated']}")
        print("  By source:")
        for src, count in s['by_source'].items():
            print(f"    {src:10s}: {count}")

    else:
        parser.print_help()
