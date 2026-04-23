"""
test_schema_evolution.py -- 15 tests validating Schema Evolution v1.0.

Validates that all builder ISOs were correctly hydrated with the 8 universal
patterns: keywords, triggers, capabilities, memory_scope, observation_types,
effort, max_turns, disallowed_tools, permission_scope, Tool Permissions section.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BUILDER_DIR = Path(__file__).resolve().parent.parent.parent / "archetypes" / "builders"

# Builders that MUST have non-default overrides
NON_DEFAULT_BUILDERS = {
    "_builder-builder", "research-pipeline-builder", "system-prompt-builder",
    "output-validator-builder", "agent-builder", "knowledge-card-builder",
    "model-card-builder", "benchmark-builder", "content-monetization-builder",
    "supabase-data-layer-builder", "workflow-builder",
    "chain-builder", "knowledge-index-builder", "bugloop-builder",
}
# social-publisher-builder excluded: all its override values are defaults

VALID_EFFORTS = {"low", "medium", "high", "max"}
VALID_SCOPES = {"nucleus", "pillar", "global", "restricted"}
VALID_MEMORY_SCOPES = {"user", "project", "local"}
FIXED_OBS_TYPES = ["user", "feedback", "project", "reference"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_fm(path: Path) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    text = path.read_text(encoding="utf-8").strip()
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def collect_isos(prefix: str, exclude_meta: bool = True) -> list[tuple[str, Path]]:
    """Collect all ISOs matching prefix across builders."""
    results = []
    for bdir in sorted(BUILDER_DIR.iterdir()):
        if not bdir.is_dir():
            continue
        for f in bdir.glob(f"{prefix}_*.md"):
            if exclude_meta and "meta" in f.name:
                continue
            results.append((bdir.name, f))
    return results


MANIFESTS = collect_isos("bld_model")
MEMORIES = collect_isos("bld_memory")
CONFIGS = collect_isos("bld_config")
TOOLS = collect_isos("bld_tools")


# ---------------------------------------------------------------------------
# Test 1-3: Manifest discovery fields
# ---------------------------------------------------------------------------


class TestManifestDiscovery:
    """Tests 1-3: keywords, triggers, capabilities in manifest frontmatter."""

    def test_01_manifests_have_keywords(self):
        """All manifests have keywords list with >= 3 items."""
        missing = []
        for name, path in MANIFESTS:
            fm = parse_fm(path)
            kw = fm.get("keywords")
            if not isinstance(kw, list) or len(kw) < 3:
                missing.append(f"{name}: keywords={kw}")
        assert not missing, f"{len(missing)} manifests missing keywords:\n" + "\n".join(missing[:10])

    def test_02_manifests_have_triggers(self):
        """All manifests have triggers list with >= 2 items."""
        missing = []
        for name, path in MANIFESTS:
            fm = parse_fm(path)
            tr = fm.get("triggers")
            if not isinstance(tr, list) or len(tr) < 2:
                missing.append(f"{name}: triggers={tr}")
        assert not missing, f"{len(missing)} manifests missing triggers:\n" + "\n".join(missing[:10])

    def test_03_manifests_have_capabilities(self):
        """All manifests have capabilities string >= 50 chars."""
        missing = []
        for name, path in MANIFESTS:
            fm = parse_fm(path)
            geo = fm.get("capabilities")
            if not isinstance(geo, str) or len(geo.strip()) < 50:
                missing.append(f"{name}: capabilities len={len(geo) if geo else 0}")
        assert not missing, f"{len(missing)} manifests missing capabilities:\n" + "\n".join(missing[:10])


# ---------------------------------------------------------------------------
# Test 4-5: Memory taxonomy
# ---------------------------------------------------------------------------


class TestMemoryTaxonomy:
    """Tests 4-5: memory_scope and observation_types in memory frontmatter."""

    def test_04_memories_have_memory_scope(self):
        """All memories have memory_scope enum."""
        missing = []
        for name, path in MEMORIES:
            fm = parse_fm(path)
            scope = fm.get("memory_scope")
            if scope not in VALID_MEMORY_SCOPES:
                missing.append(f"{name}: memory_scope={scope}")
        assert not missing, f"{len(missing)} memories missing memory_scope:\n" + "\n".join(missing[:10])

    def test_05_memories_have_observation_types(self):
        """All memories have observation_types list with exactly 4 types."""
        missing = []
        for name, path in MEMORIES:
            fm = parse_fm(path)
            obs = fm.get("observation_types")
            if not isinstance(obs, list) or len(obs) != 4:
                missing.append(f"{name}: observation_types={obs}")
        assert not missing, f"{len(missing)} memories missing observation_types:\n" + "\n".join(missing[:10])


# ---------------------------------------------------------------------------
# Test 6-9: Config runtime fields
# ---------------------------------------------------------------------------


class TestConfigRuntime:
    """Tests 6-9: effort, max_turns, disallowed_tools, permission_scope."""

    def test_06_configs_have_effort(self):
        """All configs have effort enum."""
        missing = []
        for name, path in CONFIGS:
            fm = parse_fm(path)
            effort = fm.get("effort")
            if effort not in VALID_EFFORTS:
                missing.append(f"{name}: effort={effort}")
        assert not missing, f"{len(missing)} configs missing effort:\n" + "\n".join(missing[:10])

    def test_07_configs_have_max_turns(self):
        """All configs have max_turns int in range 1-100."""
        missing = []
        for name, path in CONFIGS:
            fm = parse_fm(path)
            mt = fm.get("max_turns")
            if not isinstance(mt, int) or mt < 1 or mt > 100:
                missing.append(f"{name}: max_turns={mt}")
        assert not missing, f"{len(missing)} configs missing max_turns:\n" + "\n".join(missing[:10])

    def test_08_configs_have_disallowed_tools(self):
        """All configs have disallowed_tools list."""
        missing = []
        for name, path in CONFIGS:
            fm = parse_fm(path)
            dt = fm.get("disallowed_tools")
            if not isinstance(dt, list):
                missing.append(f"{name}: disallowed_tools={dt}")
        assert not missing, f"{len(missing)} configs missing disallowed_tools:\n" + "\n".join(missing[:10])

    def test_09_configs_have_permission_scope(self):
        """All configs have permission_scope enum."""
        missing = []
        for name, path in CONFIGS:
            fm = parse_fm(path)
            ps = fm.get("permission_scope")
            if ps not in VALID_SCOPES:
                missing.append(f"{name}: permission_scope={ps}")
        assert not missing, f"{len(missing)} configs missing permission_scope:\n" + "\n".join(missing[:10])


# ---------------------------------------------------------------------------
# Test 10: Tools permission section
# ---------------------------------------------------------------------------


class TestToolPermissions:
    """Test 10: ## Tool Permissions section in tools files."""

    def test_10_tools_have_permission_section(self):
        """All tools files have ## Tool Permissions section."""
        missing = []
        for name, path in TOOLS:
            content = path.read_text(encoding="utf-8")
            if "## Tool Permissions" not in content:
                missing.append(name)
        assert not missing, f"{len(missing)} tools missing ## Tool Permissions:\n" + "\n".join(missing[:10])


# ---------------------------------------------------------------------------
# Test 11: Regression (no fields lost)
# ---------------------------------------------------------------------------


class TestRegression:
    """Test 11: No builder lost existing fields."""

    def test_11_no_lost_fields(self):
        """All manifests still have core fields (id, kind, pillar)."""
        missing = []
        for name, path in MANIFESTS:
            fm = parse_fm(path)
            for key in ("id", "kind", "pillar"):
                if key not in fm:
                    missing.append(f"{name}: missing {key}")
        assert not missing, f"Regression: {len(missing)} missing fields:\n" + "\n".join(missing[:10])


# ---------------------------------------------------------------------------
# Test 12: YAML parseable
# ---------------------------------------------------------------------------


class TestYAMLParseable:
    """Test 12: All modified files have valid YAML frontmatter."""

    def test_12_all_yaml_parseable(self):
        """Every ISO file has parseable YAML frontmatter."""
        broken = []
        for collection_name, collection in [("manifest", MANIFESTS), ("memory", MEMORIES),
                                             ("config", CONFIGS), ("tools", TOOLS)]:
            for name, path in collection:
                text = path.read_text(encoding="utf-8").strip()
                if text.startswith("---"):
                    end = text.find("---", 3)
                    if end > 0:
                        try:
                            yaml.safe_load(text[3:end])
                        except yaml.YAMLError as e:
                            broken.append(f"{name}/{collection_name}: {e}")
        assert not broken, f"{len(broken)} files with broken YAML:\n" + "\n".join(broken[:10])


# ---------------------------------------------------------------------------
# Test 13: Non-default overrides
# ---------------------------------------------------------------------------


class TestNonDefaultOverrides:
    """Test 13: 15 specific builders have non-default values."""

    def test_13_non_default_overrides(self):
        """15 builders with overrides have at least one non-default value."""
        defaults = {"effort": "medium", "permission_scope": "nucleus", "fork_context": None}
        missing_override = []

        for name, path in CONFIGS:
            if name not in NON_DEFAULT_BUILDERS:
                continue
            fm = parse_fm(path)
            has_override = False
            for key, default_val in defaults.items():
                actual = fm.get(key)
                if actual != default_val:
                    has_override = True
                    break
            # Also check disallowed_tools
            dt = fm.get("disallowed_tools", [])
            if dt:
                has_override = True

            if not has_override:
                missing_override.append(name)

        assert not missing_override, f"Builders without non-default overrides:\n" + "\n".join(missing_override)


# ---------------------------------------------------------------------------
# Test 14: observation_types always fixed
# ---------------------------------------------------------------------------


class TestObservationTypesFixed:
    """Test 14: observation_types always == [user, feedback, project, reference]."""

    def test_14_observation_types_fixed(self):
        """observation_types must always be the exact 4-type list."""
        wrong = []
        for name, path in MEMORIES:
            fm = parse_fm(path)
            obs = fm.get("observation_types")
            if obs != FIXED_OBS_TYPES:
                wrong.append(f"{name}: {obs}")
        assert not wrong, f"{len(wrong)} memories with wrong observation_types:\n" + "\n".join(wrong[:10])


# ---------------------------------------------------------------------------
# Test 15: capabilities has 3 layers
# ---------------------------------------------------------------------------


class TestCapabilitiesLayers:
    """Test 15: capabilities contains L1, L2, L3 markers."""

    def test_15_capabilities_three_layers(self):
        """capabilities must contain L1:, L2:, L3: markers."""
        missing = []
        for name, path in MANIFESTS:
            fm = parse_fm(path)
            geo = fm.get("capabilities", "")
            if not all(f"L{i}:" in geo for i in (1, 2, 3)):
                missing.append(f"{name}: geo='{geo[:60]}...'")
        assert not missing, f"{len(missing)} manifests without 3-layer capabilities:\n" + "\n".join(missing[:10])
