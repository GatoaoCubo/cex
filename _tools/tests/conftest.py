"""
Shared fixtures for CEX tool tests.

Provides isolated test environments with minimal CEX directory structures,
sample artifacts, and builder setups. All fixtures use tmp_path for isolation.
"""

import json
import sys
from pathlib import Path

import pytest

# Ensure _tools is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


# =============================================================================
# Valid Artifact Fixtures
# =============================================================================


VALID_FRONTMATTER = """\
---
id: test_artifact_001
kind: knowledge_card
pillar: P01
title: "Test Knowledge Card"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: test
domain: testing
quality: 8.5
tags: [test, fixture]
tldr: "A test artifact for pytest fixtures."
density_score: 0.85
---

# Test Knowledge Card

## Section One

This is test content with enough substance to pass validation.

| Column A | Column B |
|----------|----------|
| data 1   | data 2   |

## Section Two

More content to ensure density thresholds are met.

```python
def example():
    return "hello"
```
"""

VALID_FRONTMATTER_NO_QUALITY = """\
---
id: test_no_quality
kind: knowledge_card
pillar: P01
title: "Test No Quality"
version: 1.0.0
created: 2026-03-31
author: test
quality: null
---

# Test Card

Content here.
"""

INVALID_NO_FRONTMATTER = """\
# Just a markdown file

No frontmatter here.
"""

INVALID_MISSING_FIELDS = """\
---
id: test_missing
title: "Missing kind and pillar"
---

# Incomplete

Missing required fields.
"""


@pytest.fixture
def valid_artifact(tmp_path):
    """Create a valid CEX artifact file with frontmatter."""
    f = tmp_path / "kc_test.md"
    f.write_text(VALID_FRONTMATTER, encoding="utf-8")
    return f


@pytest.fixture
def valid_artifact_null_quality(tmp_path):
    """Create an artifact with quality: null."""
    f = tmp_path / "kc_null_quality.md"
    f.write_text(VALID_FRONTMATTER_NO_QUALITY, encoding="utf-8")
    return f


@pytest.fixture
def invalid_artifact_no_fm(tmp_path):
    """Create an artifact without frontmatter."""
    f = tmp_path / "no_frontmatter.md"
    f.write_text(INVALID_NO_FRONTMATTER, encoding="utf-8")
    return f


@pytest.fixture
def invalid_artifact_missing_fields(tmp_path):
    """Create an artifact with incomplete frontmatter."""
    f = tmp_path / "missing_fields.md"
    f.write_text(INVALID_MISSING_FIELDS, encoding="utf-8")
    return f


# =============================================================================
# CEX Root Fixture (Isolated)
# =============================================================================


@pytest.fixture
def cex_root(tmp_path):
    """Create a minimal isolated CEX directory structure."""
    # Core dirs
    (tmp_path / ".cex").mkdir()
    (tmp_path / ".cex" / "runtime" / "signals").mkdir(parents=True)
    (tmp_path / ".cex" / "runtime" / "handoffs").mkdir(parents=True)
    (tmp_path / "_tools").mkdir()
    (tmp_path / "archetypes" / "builders").mkdir(parents=True)

    # Pillar dirs
    for i in range(1, 13):
        p = tmp_path / f"P{i:02d}_test"
        p.mkdir()

    # Nucleus dirs
    for i in range(1, 8):
        n = tmp_path / f"N{i:02d}_test"
        n.mkdir()

    # Minimal kinds_meta.json
    kinds = {
        "knowledge_card": {
            "pillar": "P01",
            "function": "store",
            "description": "Typed knowledge unit",
            "max_bytes": 5120,
            "boundary": "context",
        },
        "agent": {
            "pillar": "P03",
            "function": "act",
            "description": "Agent definition",
            "max_bytes": 4096,
            "boundary": "context",
        },
    }
    (tmp_path / ".cex" / "kinds_meta.json").write_text(
        json.dumps(kinds, indent=2), encoding="utf-8"
    )

    return tmp_path


# =============================================================================
# Builder Fixture
# =============================================================================


@pytest.fixture
def sample_builder(tmp_path):
    """Create a minimal builder directory with ISOs."""
    builder_dir = tmp_path / "archetypes" / "builders" / "knowledge-card-builder"
    builder_dir.mkdir(parents=True)

    isos = {
        "bld_model_knowledge_card.md": "---\nid: sp\nkind: model\npillar: P02\nquality: null\n---\n# Model\nYou build KCs.",
        "bld_prompt_knowledge_card.md": "---\nid: inst\nkind: prompt\npillar: P03\nquality: null\n---\n# Prompt\nStep 1: Read. Step 2: Write.",
        "bld_schema_knowledge_card.md": "---\nid: sch\nkind: schema\npillar: P02\nquality: null\n---\n# Schema\nmax_bytes: 5120",
    }

    for name, content in isos.items():
        (builder_dir / name).write_text(content, encoding="utf-8")

    return builder_dir
