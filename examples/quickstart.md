# Quickstart

This is the fastest verified path from a fresh clone to a healthy local CEX install. Run this first, confirm the repo is sane, then move to [build_one_artifact.md](build_one_artifact.md).

## Prerequisites

- Python 3.10+
- Git
- PowerShell on Windows or Bash for dispatch commands

## 1. Clone the repo

```bash
git clone https://github.com/<your-org>/cex.git
cd cex
```

Expected result: you are at the repo root and can see `_tools/`, `archetypes/`, `boot/`, and `P01_knowledge/`.

## 2. Install core dependencies

`requirements.txt` is the smallest reliable starting point:

```bash
python -m pip install -r requirements.txt
```

If you prefer the project metadata route, this repo also exposes the same core dependency in `pyproject.toml`:

```bash
python -m pip install .
```

Expected packages:

- `pyyaml>=6.0`
- `tiktoken>=0.7.0`

## 3. Run the health check

```bash
python _tools/cex_doctor.py
```

Expected output starts like this:

```text
========================================================================
CEX Doctor v2.0 -- Naming v2.0 + Density + 13-File Completeness
Root: <path-to-your-clone>
Mode: DIAGNOSE ONLY
========================================================================

Found 258 builder directories
```

Expected successful ending:

```text
========================================================================
Builders:       258
Total files:    3354 (expected 3354)
Total size:     9805.3 KB
Avg density:    0.90
Oversized:      40 files (>6144B std, >8192B instructions)
No frontmatter: 0 files
Result:         189 PASS | 69 WARN | 0 FAIL
========================================================================
```

If you get a Python import error instead, the install step is incomplete.

## 4. Optional: boot the orchestrator shell

Once `cex_doctor.py` runs, you can boot the N07 orchestrator entrypoint:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File boot/cex.ps1
```

Expected result: an interactive orchestrator session opens and reads the current handoff/mission context.

## Why this is the first example

It verifies the local toolchain without spending tokens, invoking a provider, or writing artifacts. If this step fails, every later example is noise.

## Next steps

Build one artifact with the 8F pipeline in [build_one_artifact.md](build_one_artifact.md).
