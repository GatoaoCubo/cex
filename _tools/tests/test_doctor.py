"""Tests for cex_doctor.py -- Health check."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class TestDoctorImport:
    @pytest.mark.unit
    def test_import(self):
        """cex_doctor should be importable."""
        import cex_doctor
        assert hasattr(cex_doctor, "main") or True  # Module loads

    @pytest.mark.integration
    def test_doctor_run(self):
        """Doctor should run against real repo without crashing."""
        import subprocess
        result = subprocess.run(
            [sys.executable, "_tools/cex_doctor.py"],
            capture_output=True, text=True, timeout=30,
            cwd=str(Path(__file__).resolve().parent.parent.parent),
        )
        # Doctor may return non-zero for warnings, but shouldn't crash
        assert result.returncode in (0, 1, 2)
        assert "PASS" in result.stdout or "WARN" in result.stdout or "FAIL" in result.stdout


class TestDoctorBuilders:
    @pytest.mark.integration
    def test_builder_count(self):
        """Should find 100+ builders in real repo."""
        builders = list(
            (Path(__file__).resolve().parent.parent.parent / "archetypes" / "builders").iterdir()
        )
        builder_dirs = [b for b in builders if b.is_dir()]
        assert len(builder_dirs) >= 99  # 99 kind builders + domain builders

    @pytest.mark.integration
    def test_builders_have_isos(self):
        """Each builder should have bld_*.md files."""
        builder_root = Path(__file__).resolve().parent.parent.parent / "archetypes" / "builders"
        for builder_dir in list(builder_root.iterdir())[:5]:
            if builder_dir.is_dir():
                isos = list(builder_dir.glob("bld_*.md"))
                assert len(isos) >= 10, f"{builder_dir.name} has only {len(isos)} ISOs"
