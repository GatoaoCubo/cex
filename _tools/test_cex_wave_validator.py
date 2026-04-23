#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_cex_wave_validator.py -- Unit + integration tests for the wave validator.

Runs without pytest (plain assertions + main runner). Exit 0 on pass, 1 on fail.

Usage:
  python _tools/test_cex_wave_validator.py
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cex_wave_validator as wv  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_iso(
    tmp: Path,
    filename: str,
    frontmatter: dict,
    body: str = "",
) -> Path:
    """Write a minimal ISO file with the given frontmatter + body."""
    lines = ["---"]
    for k, v in frontmatter.items():
        if v is None:
            lines.append(f"{k}: null")
        elif isinstance(v, list):
            lines.append(f"{k}: [{', '.join(str(x) for x in v)}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    path = tmp / filename
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def clean_fm(**overrides: Any) -> dict[str, Any]:
    """Return a valid complete frontmatter, with optional overrides."""
    fm = {
        "id": "bld_model_voice_pipeline",
        "kind": "model",
        "pillar": "P02",
        "llm_function": "BECOME",
        "title": "Test",
        "quality": None,
        "tags": "[voice_pipeline, test]",
    }
    fm.update(overrides)
    return fm


def assert_pass(errors: list[str], case: str) -> None:
    assert not errors, f"{case}: expected PASS, got errors: {errors}"


def assert_fail(errors: list[str], case: str, hint: str = "") -> None:
    assert errors, f"{case}: expected FAIL, got PASS"
    if hint:
        joined = " | ".join(errors).lower()
        assert hint.lower() in joined, \
            f"{case}: expected '{hint}' in errors, got: {errors}"


# ---------------------------------------------------------------------------
# 7 unit tests (one per check)
# ---------------------------------------------------------------------------


def test_c1_model_llm_function(tmp: Path) -> None:
    # FAIL: wrong llm_function for bld_model_*
    bad = make_iso(tmp, "bld_model_voice_pipeline.md",
                   clean_fm(llm_function="INJECT"),
                   body="STT and TTS pipeline.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C1 wrong llm_function", hint="llm_function")

    # PASS: correct BECOME
    good = make_iso(tmp, "bld_model_voice_pipeline.md",
                    clean_fm(llm_function="BECOME"),
                    body="STT and TTS pipeline.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C1 correct BECOME")


def test_c2_schema_quality_null(tmp: Path) -> None:
    # FAIL: out-of-range numeric
    bad = make_iso(tmp, "bld_schema_voice_pipeline.md",
                   clean_fm(id="bld_schema_voice_pipeline", kind="schema",
                            pillar="P06", llm_function="CONSTRAIN",
                            quality=99),
                   body="Schema fields and types for STT and TTS.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C2 quality out of range", hint="quality")

    # FAIL: non-numeric string
    bad2 = make_iso(tmp, "bld_schema_voice_pipeline.md",
                    clean_fm(id="bld_schema_voice_pipeline", kind="schema",
                             pillar="P06", llm_function="CONSTRAIN",
                             quality='"high"'),
                    body="Schema fields and types for STT and TTS.")
    errs = wv.validate_file(bad2)
    assert_fail(errs, "C2 non-numeric quality", hint="quality")

    # PASS: quality null (author convention)
    good = make_iso(tmp, "bld_schema_voice_pipeline.md",
                    clean_fm(id="bld_schema_voice_pipeline", kind="schema",
                             pillar="P06", llm_function="CONSTRAIN",
                             quality=None),
                    body="Schema fields and types for STT and TTS.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C2 quality null")

    # PASS: quality peer-reviewed in range
    good2 = make_iso(tmp, "bld_schema_voice_pipeline.md",
                     clean_fm(id="bld_schema_voice_pipeline", kind="schema",
                              pillar="P06", llm_function="CONSTRAIN",
                              quality=9.0),
                     body="Schema fields and types for STT and TTS.")
    errs = wv.validate_file(good2)
    assert_pass(errs, "C2 peer-reviewed quality 9.0")


def test_c3_h02_id_pattern(tmp: Path) -> None:
    # FAIL: id with unrecognized shape
    bad = make_iso(tmp, "bld_architecture_voice_pipeline.md",
                   clean_fm(id="random_name_no_prefix",
                            kind="architecture", pillar="P08",
                            llm_function="CONSTRAIN"),
                   body="Voice pipeline architecture with STT and TTS.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C3 bad id shape", hint="recognized prefix")

    # PASS: id with {slug}-builder suffix (model convention)
    good = make_iso(tmp, "bld_model_voice_pipeline.md",
                    clean_fm(id="voice-pipeline-builder",
                             kind="model", pillar="P02",
                             llm_function="BECOME"),
                    body="Voice pipeline builder model -- STT and TTS.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C3 {slug}-builder id")


def test_c4_domain_keywords_present(tmp: Path) -> None:
    # FAIL: no voice/audio/STT/TTS terms
    bad = make_iso(tmp, "bld_architecture_voice_pipeline.md",
                   clean_fm(id="bld_architecture_voice_pipeline",
                            kind="architecture", pillar="P08",
                            llm_function="CONSTRAIN"),
                   body="Some generic architecture. Nothing specific.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C4 missing domain keywords", hint="domain keyword")

    # PASS: has STT
    good = make_iso(tmp, "bld_architecture_voice_pipeline.md",
                    clean_fm(id="bld_architecture_voice_pipeline",
                             kind="architecture", pillar="P08",
                             llm_function="CONSTRAIN"),
                    body="STT stage feeds NLU; TTS synthesizes audio.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C4 has STT/TTS/audio")


def test_c5_no_wrong_domain_keywords(tmp: Path) -> None:
    # FAIL: crypto leakage in voice_pipeline
    bad = make_iso(tmp, "bld_prompt_voice_pipeline.md",
                   clean_fm(id="bld_prompt_voice_pipeline",
                            kind="prompt", pillar="P03",
                            llm_function="REASON"),
                   body="Stake your SOL on Solana. STT first, then TTS.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C5 solana leak", hint="foreign-domain")

    # PASS: no crypto terms (and "definitions" must NOT trigger DeFi match)
    good = make_iso(tmp, "bld_prompt_voice_pipeline.md",
                    clean_fm(id="bld_prompt_voice_pipeline",
                             kind="prompt", pillar="P03",
                             llm_function="REASON"),
                    body="See definitions in schema.md. STT config here.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C5 'definitions' does not match 'DeFi'")


def test_c6_placeholders_resolved(tmp: Path) -> None:
    # FAIL: unresolved placeholder in a prompt file (body)
    bad = make_iso(tmp, "bld_prompt_voice_pipeline.md",
                   clean_fm(id="bld_prompt_voice_pipeline",
                            kind="prompt", pillar="P03",
                            llm_function="REASON"),
                   body="Step 1: load the {{user_goal}} from STT output.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C6 unresolved placeholder", hint="placeholder")

    # PASS: same content in code fence is ignored
    good = make_iso(tmp, "bld_prompt_voice_pipeline.md",
                    clean_fm(id="bld_prompt_voice_pipeline",
                             kind="prompt", pillar="P03",
                             llm_function="REASON"),
                    body="Step 1: load STT audio.\n\n```\n{{user_goal}}\n```")
    errs = wv.validate_file(good)
    assert_pass(errs, "C6 placeholder in code fence ok")

    # PASS: output is exempt (placeholders are the point)
    exempt = make_iso(tmp, "bld_output_voice_pipeline.md",
                      clean_fm(id="bld_output_voice_pipeline",
                               kind="output", pillar="P05",
                               llm_function="PRODUCE"),
                      body="STT stage: {{stt_provider}}\nTTS: {{tts_provider}}")
    errs = wv.validate_file(exempt)
    assert_pass(errs, "C6 output exempt")


def test_c7_frontmatter_complete(tmp: Path) -> None:
    # FAIL: missing title
    fm = clean_fm()
    del fm["title"]
    bad = make_iso(tmp, "bld_architecture_voice_pipeline.md", fm,
                   body="Voice pipeline with STT and TTS.")
    errs = wv.validate_file(bad)
    assert_fail(errs, "C7 missing title", hint="title")

    # FAIL: pillar with wrong shape
    bad2 = make_iso(tmp, "bld_architecture_voice_pipeline.md",
                    clean_fm(pillar="P3"),
                    body="Voice pipeline with STT and TTS.")
    errs = wv.validate_file(bad2)
    assert_fail(errs, "C7 bad pillar shape", hint="pillar")

    # PASS: complete
    good = make_iso(tmp, "bld_architecture_voice_pipeline.md",
                    clean_fm(id="bld_architecture_voice_pipeline",
                             kind="architecture", pillar="P08",
                             llm_function="CONSTRAIN"),
                    body="Voice pipeline with STT and TTS.")
    errs = wv.validate_file(good)
    assert_pass(errs, "C7 complete frontmatter")


# ---------------------------------------------------------------------------
# Integration tests
# ---------------------------------------------------------------------------


def test_integration_clean_dir(tmp: Path) -> None:
    """Scan a known-good directory (voice-pipeline-builder) -- expect PASS."""
    target = wv.CEX_ROOT / "archetypes" / "builders" / "voice-pipeline-builder"
    if not target.exists():
        print("  SKIP: voice-pipeline-builder not present")
        return
    files = list(wv.iter_builder_files(target))
    assert files, "expected ISO files in voice-pipeline-builder"
    fail_count = sum(1 for f in files if wv.validate_file(f))
    assert fail_count == 0, \
        f"voice-pipeline-builder (known clean) had {fail_count} failures"


def test_integration_bad_dir(tmp: Path) -> None:
    """Build a directory with defects; expect >=1 fail per defect type."""
    bad_dir = tmp / "bad-builder"
    bad_dir.mkdir()

    # C1 defect
    make_iso(bad_dir, "bld_model_voice_pipeline.md",
             clean_fm(llm_function="INJECT"),
             body="STT and TTS pipeline.")
    # C2 defect: quality out of range
    make_iso(bad_dir, "bld_tools_voice_pipeline.md",
             clean_fm(id="bld_tools_voice_pipeline", kind="tools",
                      pillar="P04", llm_function="CALL", quality=99),
             body="STT and TTS tools.")

    files = list(wv.iter_builder_files(bad_dir))
    assert len(files) == 2
    failures = [f for f in files if wv.validate_file(f)]
    assert len(failures) == 2, \
        f"expected 2 failures in bad-builder, got {len(failures)}"


def test_runner_exit_codes(tmp: Path) -> None:
    """run_validation returns 0 on clean, 1 on dirty."""
    good_dir = tmp / "good"
    good_dir.mkdir()
    make_iso(good_dir, "bld_tools_voice_pipeline.md",
             clean_fm(id="bld_tools_voice_pipeline", kind="tools",
                      pillar="P04", llm_function="CALL"),
             body="STT and TTS tools for the voice pipeline.")
    rc = wv.run_validation(list(wv.iter_builder_files(good_dir)), label="good")
    assert rc == 0, f"good dir should return 0, got {rc}"

    bad_dir = tmp / "bad"
    bad_dir.mkdir()
    make_iso(bad_dir, "bld_tools_voice_pipeline.md",
             clean_fm(id="bld_tools_voice_pipeline", kind="tools",
                      pillar="P04", llm_function="BECOME"),
             body="STT and TTS tools.")
    rc = wv.run_validation(list(wv.iter_builder_files(bad_dir)), label="bad")
    assert rc == 1, f"bad dir should return 1, got {rc}"


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


TESTS = [
    test_c1_model_llm_function,
    test_c2_schema_quality_null,
    test_c3_h02_id_pattern,
    test_c4_domain_keywords_present,
    test_c5_no_wrong_domain_keywords,
    test_c6_placeholders_resolved,
    test_c7_frontmatter_complete,
    test_integration_clean_dir,
    test_integration_bad_dir,
    test_runner_exit_codes,
]


def main() -> int:
    tmp_root = Path(tempfile.mkdtemp(prefix="cex_wave_validator_test_"))
    passed = 0
    failed = 0
    try:
        for test in TESTS:
            tmp = tmp_root / test.__name__
            tmp.mkdir()
            try:
                test(tmp)
                passed += 1
                print(f"  [PASS] {test.__name__}")
            except AssertionError as e:
                failed += 1
                print(f"  [FAIL] {test.__name__}: {e}")
            except Exception as e:
                failed += 1
                print(f"  [ERROR] {test.__name__}: {type(e).__name__}: {e}")
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)

    total = passed + failed
    print(f"\nTests: {passed}/{total} passed, {failed}/{total} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
