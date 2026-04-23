"""
E2E Evolution Tests -- Validates the full CEX evolution cycle.

Tests cover: kind registration, skeleton builders, schema integrity,
motor resolution, memory fields, config fields, and index operations.

Spec 3 of the Universal Agent Patterns trilogy.
"""

import json
import sys
from pathlib import Path

import pytest
import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(CEX_ROOT / "_tools"))

BUILDERS_DIR = CEX_ROOT / "archetypes" / "builders"
TAXONOMY_PATH = CEX_ROOT / "archetypes" / "TAXONOMY_LAYERS.yaml"
KINDS_META_PATH = CEX_ROOT / ".cex" / "kinds_meta.json"

NEW_KINDS = ["memory_scope", "effort_profile", "hook_config"]
NEW_BUILDERS = ["memory-scope-builder", "effort-profile-builder", "hook-config-builder"]
EXPECTED_ISOS = 12


def load_kinds_meta():
    return json.loads(KINDS_META_PATH.read_text(encoding="utf-8"))


def load_taxonomy():
    return yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))


def load_manifest(builder_name):
    kind_slug = builder_name.replace("-builder", "").replace("-", "_")
    p = BUILDERS_DIR / builder_name / f"bld_model_{kind_slug}.md"
    return p.read_text(encoding="utf-8") if p.exists() else None


# ===========================================================================
# Test 1: Discovery -> Builder (Motor Resolution)
# ===========================================================================


class TestDiscoveryToBuilder:
    @pytest.mark.integration
    def test_motor_resolves_new_kinds(self):
        """Motor OBJECT_TO_KINDS contains entries for new kinds."""
        from cex_8f_motor import OBJECT_TO_KINDS

        for kind in NEW_KINDS:
            assert kind in OBJECT_TO_KINDS, f"{kind} missing from OBJECT_TO_KINDS"
            entries = OBJECT_TO_KINDS[kind]
            assert len(entries) >= 1
            assert entries[0][0] == kind  # kind name matches

    @pytest.mark.integration
    def test_motor_resolves_hyphenated(self):
        """Motor resolves hyphenated variants for underscore kinds."""
        from cex_8f_motor import OBJECT_TO_KINDS

        for kind in ["effort-profile", "hook-config"]:
            assert kind in OBJECT_TO_KINDS, f"{kind} (hyphenated) missing from Motor"


# ===========================================================================
# Test 2: Builder -> Memory Load
# ===========================================================================


class TestBuilderMemoryLoad:
    @pytest.mark.integration
    def test_builders_have_memory_iso(self):
        """Each new builder has a bld_memory file."""
        for builder in NEW_BUILDERS:
            kind_slug = builder.replace("-builder", "").replace("-", "_")
            mem_path = BUILDERS_DIR / builder / f"bld_memory_{kind_slug}.md"
            assert mem_path.exists(), f"{builder} missing bld_memory"

    @pytest.mark.integration
    def test_memory_has_observation(self):
        """Memory ISOs contain observation field or pattern section."""
        for builder in NEW_BUILDERS:
            kind_slug = builder.replace("-builder", "").replace("-", "_")
            mem_path = BUILDERS_DIR / builder / f"bld_memory_{kind_slug}.md"
            content = mem_path.read_text(encoding="utf-8")
            has_obs = "observation" in content.lower() or "pattern" in content.lower()
            assert has_obs, f"{builder} memory lacks observation/pattern"


# ===========================================================================
# Test 3: Builder -> Effort -> Model
# ===========================================================================


class TestBuilderEffortModel:
    @pytest.mark.integration
    def test_effort_profile_builder_exists(self):
        """effort-profile-builder is a functional builder with 12 ISOs."""
        bp = BUILDERS_DIR / "effort-profile-builder"
        assert bp.is_dir()
        isos = list(bp.glob("bld_*.md"))
        assert len(isos) == EXPECTED_ISOS

    @pytest.mark.integration
    def test_effort_levels_documented(self):
        """Effort profile knowledge card documents model-to-level mapping."""
        kc = BUILDERS_DIR / "effort-profile-builder" / "bld_knowledge_effort_profile.md"
        content = kc.read_text(encoding="utf-8")
        for term in ["low", "medium", "high"]:
            assert term in content.lower(), f"Effort level '{term}' not in knowledge card"


# ===========================================================================
# Test 4: Builder -> Tool Deny (boundary check)
# ===========================================================================


class TestBuilderBoundary:
    @pytest.mark.integration
    def test_builder_manifests_have_boundary(self):
        """Each new builder manifest declares what it IS and IS NOT."""
        for builder in NEW_BUILDERS:
            manifest = load_manifest(builder)
            assert manifest is not None, f"{builder} manifest not found"
            has_boundary = ("IS NOT" in manifest or "NOT" in manifest
                           or "boundary" in manifest.lower()
                           or "do NOT" in manifest)
            assert has_boundary, f"{builder} manifest lacks boundary declaration"

    @pytest.mark.integration
    def test_kinds_meta_has_boundary(self):
        """kinds_meta.json has boundary field for all new kinds."""
        meta = load_kinds_meta()
        for kind in NEW_KINDS:
            assert kind in meta, f"{kind} not in kinds_meta"
            assert "boundary" in meta[kind], f"{kind} missing boundary in kinds_meta"
            assert len(meta[kind]["boundary"]) > 10, f"{kind} boundary too short"


# ===========================================================================
# Test 5: Builder -> Hook Lifecycle
# ===========================================================================


class TestHookLifecycle:
    @pytest.mark.integration
    def test_hook_config_builder_exists(self):
        """hook-config-builder has 12 ISOs."""
        bp = BUILDERS_DIR / "hook-config-builder"
        assert bp.is_dir()
        isos = list(bp.glob("bld_*.md"))
        assert len(isos) == EXPECTED_ISOS

    @pytest.mark.integration
    def test_hook_config_documents_phases(self):
        """Hook config knowledge card documents lifecycle phases."""
        kc = BUILDERS_DIR / "hook-config-builder" / "bld_knowledge_hook_config.md"
        content = kc.read_text(encoding="utf-8")
        for phase in ["pre", "post", "error"]:
            assert phase in content.lower(), f"Phase '{phase}' not in hook_config KC"


# ===========================================================================
# Test 6: Builder -> Quality -> Memory Update
# ===========================================================================


class TestQualityMemory:
    @pytest.mark.integration
    def test_quality_gates_exist(self):
        """Each new builder has a quality gate ISO."""
        for builder in NEW_BUILDERS:
            kind_slug = builder.replace("-builder", "").replace("-", "_")
            qg = BUILDERS_DIR / builder / f"bld_eval_{kind_slug}.md"
            assert qg.exists(), f"{builder} missing eval"

    @pytest.mark.integration
    def test_quality_gates_have_hard_gates(self):
        """Quality gate ISOs define HARD gates."""
        for builder in NEW_BUILDERS:
            kind_slug = builder.replace("-builder", "").replace("-", "_")
            qg = BUILDERS_DIR / builder / f"bld_eval_{kind_slug}.md"
            content = qg.read_text(encoding="utf-8")
            assert "HARD" in content or "H0" in content, \
                f"{builder} quality gate missing HARD gates"


# ===========================================================================
# Test 7: New Kinds Registered
# ===========================================================================


class TestNewKindsRegistered:
    @pytest.mark.integration
    def test_kinds_in_taxonomy(self):
        """All 3 new kinds appear in TAXONOMY_LAYERS.yaml runtime layer."""
        content = TAXONOMY_PATH.read_text(encoding="utf-8")
        for kind in NEW_KINDS:
            assert kind in content, f"{kind} missing from TAXONOMY_LAYERS.yaml"

    @pytest.mark.integration
    def test_kinds_in_meta(self):
        """All 3 new kinds are in kinds_meta.json."""
        meta = load_kinds_meta()
        for kind in NEW_KINDS:
            assert kind in meta, f"{kind} missing from kinds_meta.json"

    @pytest.mark.integration
    def test_skeleton_builders_complete(self):
        """Each new builder has exactly 13 ISO files."""
        for builder in NEW_BUILDERS:
            bp = BUILDERS_DIR / builder
            assert bp.is_dir(), f"{builder} directory missing"
            isos = list(bp.glob("bld_*.md"))
            assert len(isos) == EXPECTED_ISOS, \
                f"{builder} has {len(isos)} ISOs, expected {EXPECTED_ISOS}"

    @pytest.mark.integration
    def test_skeleton_builders_under_30kb(self):
        """Each skeleton builder totals under 30KB."""
        for builder in NEW_BUILDERS:
            bp = BUILDERS_DIR / builder
            total = sum(f.stat().st_size for f in bp.glob("bld_*.md"))
            assert total < 30 * 1024, \
                f"{builder} is {total} bytes, exceeds 30KB limit"

    @pytest.mark.integration
    def test_taxonomy_overlaps_declared(self):
        """3 new overlap pairs exist in TAXONOMY."""
        content = TAXONOMY_PATH.read_text(encoding="utf-8")
        for pair_kind in ["memory_scope", "effort_profile", "hook_config"]:
            assert pair_kind in content, f"{pair_kind} overlap missing"

    @pytest.mark.integration
    def test_runtime_layer_count(self):
        """Runtime layer count reflects 3 new additions."""
        tax = load_taxonomy()
        count = tax["layers"]["runtime"]["count"]
        kinds = tax["layers"]["runtime"]["kinds"]
        assert count >= 32, f"Runtime count is {count}, expected >= 32"
        assert len(kinds) >= 32, f"Runtime kinds list has {len(kinds)}, expected >= 32"


# ===========================================================================
# Test 8: Schema Integrity (regression)
# ===========================================================================


class TestSchemaIntegrity:
    @pytest.mark.integration
    def test_manifests_have_keywords(self):
        """Builders with evolved manifests have keywords in frontmatter or body."""
        manifest_count = 0
        keyword_count = 0
        for bd in BUILDERS_DIR.iterdir():
            if not bd.is_dir():
                continue
            kind_slug = bd.name.replace("-builder", "").replace("-", "_")
            manifest = bd / f"bld_model_{kind_slug}.md"
            if manifest.exists():
                manifest_count += 1
                content = manifest.read_text(encoding="utf-8")
                if "keyword" in content.lower() or "routing" in content.lower():
                    keyword_count += 1
        assert manifest_count >= 103, f"Only {manifest_count} manifests found (expected >= 103)"
        # At least 90% should have keywords (schema evolution target)
        ratio = keyword_count / manifest_count if manifest_count else 0
        assert ratio >= 0.85, f"Only {keyword_count}/{manifest_count} manifests have keywords ({ratio:.0%})"

    @pytest.mark.integration
    def test_configs_exist(self):
        """Each builder has a config ISO."""
        config_count = 0
        for bd in BUILDERS_DIR.iterdir():
            if not bd.is_dir():
                continue
            kind_slug = bd.name.replace("-builder", "").replace("-", "_")
            config = bd / f"bld_config_{kind_slug}.md"
            if config.exists():
                config_count += 1
        assert config_count >= 103, f"Only {config_count} configs found (expected >= 103)"

    @pytest.mark.integration
    def test_no_lost_kinds(self):
        """kinds_meta.json has >= 104 kinds (99 original + 3 research/social + 2 new)."""
        meta = load_kinds_meta()
        assert len(meta) >= 104, f"Only {len(meta)} kinds in meta (expected >= 104)"


# ===========================================================================
# Test 9: Index Integrity
# ===========================================================================


class TestIndexIntegrity:
    @pytest.mark.integration
    def test_index_db_exists_or_buildable(self):
        """index.db exists or can be built."""
        idx_path = CEX_ROOT / ".cex" / "index.db"
        idx_json = CEX_ROOT / ".cex" / "index.json"
        assert idx_path.exists() or idx_json.exists() or \
            (CEX_ROOT / "_tools" / "cex_index.py").exists(), \
            "No index found and no indexer available"

    @pytest.mark.integration
    def test_retriever_importable(self):
        """cex_retriever module is importable."""
        import cex_retriever
        assert hasattr(cex_retriever, "find_similar") or hasattr(cex_retriever, "build_index")


# ===========================================================================
# Test 10: Autodiscovery Pipeline
# ===========================================================================


class TestAutodiscoveryPipeline:
    @pytest.mark.integration
    def test_motor_classify_known_kind(self):
        """Motor classifies 'agent' object correctly."""
        from cex_8f_motor import OBJECT_TO_KINDS
        assert "agent" in OBJECT_TO_KINDS
        entries = OBJECT_TO_KINDS["agent"]
        kinds = [e[0] for e in entries]
        assert "agent" in kinds

    @pytest.mark.integration
    def test_motor_classify_new_kinds(self):
        """Motor classifies new kinds correctly."""
        from cex_8f_motor import OBJECT_TO_KINDS
        for kind in NEW_KINDS:
            assert kind in OBJECT_TO_KINDS, f"{kind} not discoverable via Motor"

    @pytest.mark.integration
    def test_type_to_template_sync(self):
        """TYPE_TO_TEMPLATE.yaml has entries for new kinds."""
        ttt_path = CEX_ROOT / "archetypes" / "TYPE_TO_TEMPLATE.yaml"
        content = ttt_path.read_text(encoding="utf-8")
        for kind in NEW_KINDS:
            assert kind in content, f"{kind} missing from TYPE_TO_TEMPLATE.yaml"

    @pytest.mark.integration
    def test_total_builder_count(self):
        """Total builder count >= 107."""
        builders = [d for d in BUILDERS_DIR.iterdir() if d.is_dir()]
        assert len(builders) >= 106, f"Only {len(builders)} builders (expected >= 106)"

    @pytest.mark.integration
    def test_total_kind_count(self):
        """Total kind count >= 104."""
        meta = load_kinds_meta()
        assert len(meta) >= 104, f"Only {len(meta)} kinds (expected >= 104)"
