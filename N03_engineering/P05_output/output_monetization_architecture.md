---
id: n03_output_monetization_architecture
kind: output
pillar: P05
title: "Monetization Technical Architecture — CEX Public + Paid Course + FT Model"
version: 1.0.0
created: 2026-04-02
author: n03_builder
domain: engineering
quality: 9.2
tags: [monetization, architecture, distribution, ci-cd, security, public-repo, course, fine-tune]
tldr: "End-to-end technical blueprint: MIT repo prep, cex-brain GGUF distribution, hybrid course platform, CI/CD, security, and effort estimates."
density_score: 0.93
---

# Monetization Technical Architecture

## Executive Summary

Three revenue pillars:

| Pillar | Asset | Price | Delivery |
|--------|-------|-------|----------|
| **Open** | CEX repo (MIT) | Free | GitHub public |
| **Builder** | Curso track 2 | R$497 | Lemon Squeezy + content site |
| **Master** | Curso track 3 + cex-brain:14b | R$997 | Lemon Squeezy + gated download |

---

## 1. Repo Preparation for Public Release

### 1.1 What Must Be Cleaned

| Category | Current State | Action |
|----------|--------------|--------|
| **Secrets** | `.env` in `.gitignore` ✅ | Verify `git log -- .env` shows no real keys. Run `git filter-repo` if ANY key was ever committed with real values |
| **.env.example** | 87 keys, all blank ✅ | Keep as-is — documents the ecosystem |
| **Hardcoded paths** | `C:\Users\PC` scanned — **0 hits** in `_tools/`, `boot/`, `.claude/` | ✅ Clean |
| **Personal data** | Git author "Gato³ ao Cubo" | Decide: keep (personal brand) or anonymize before public |
| **API key refs in code** | `cex_boot_gen.py`, `cex_kc_index.py` reference env vars | ✅ They read from `os.environ`, not hardcoded — safe |
| **Runtime dirs** | `.cex/runtime/`, `.cex/learning_records/`, `.cex/temp/` | Already in `.gitignore` ✅ |
| **_config/** | Currently empty (deleted) | `.gitignore` has `_config/*.credentials` — keep the rule |
| **_archive/** | In `.gitignore` ✅ | Will not leak |
| **Proof artifacts** | `_tools/proof/` (8.5MB) | Already in `.gitignore` ✅ |

### 1.2 .gitignore Audit

Current `.gitignore` is **solid**. Add these before going public:

```gitignore
# === Additional for public release ===

# User brand config (private by default)
.cex/brand/brand_config.yaml

# User experiment data
.cex/experiments/results.tsv
.cex/overnight/

# IDE settings (already have .vscode/)
.idea/

# OS files (already have Thumbs.db, .DS_Store)
*.swp
*~

# Python venv
.venv/
venv/
```

### 1.3 README.md vs CLAUDE.md

| File | Audience | Content |
|------|----------|---------|
| `README.md` (NEW) | GitHub visitors, students, contributors | What CEX is, quickstart, architecture diagram, course link |
| `CLAUDE.md` | LLM agents working inside the repo | Internal rules, nucleus routing, 8F pipeline — stays as-is |

**README.md structure:**

```
# CEX — Typed Knowledge System for LLM Agents
> 114 kinds · 12 pillars · 8 nuclei · 8F pipeline

## What is CEX?
[2 paragraphs + architecture diagram]

## Quickstart
git clone → python cex_setup.py → /init

## Course
[3 tiers table + Lemon Squeezy link]

## Architecture
[Mermaid diagram of pillars + nuclei]

## Contributing
[link to CONTRIBUTING.md]

## License
MIT
```

### 1.4 First-Run Onboarding

Current flow: user clones → runs `python _tools/cex_init.py` → answers 5 questions → scaffolds.

**Improvement: `cex_setup.py` (new, root-level)**

```python
#!/usr/bin/env python3
"""CEX Setup — One command to get started.

Usage:
    python cex_setup.py          # Interactive
    python cex_setup.py --check  # Verify deps only
"""
import subprocess, sys, shutil
from pathlib import Path

DEPS = {
    "python": ("python --version", "3.10+"),
    "pyyaml": ("python -c 'import yaml'", "pip install pyyaml"),
    "git": ("git --version", "https://git-scm.com"),
}

OPTIONAL = {
    "ollama": ("ollama --version", "https://ollama.ai"),
    "ruff": ("ruff --version", "pip install ruff"),
}

def check(name, cmd, fix):
    try:
        subprocess.run(cmd.split(), capture_output=True, check=True)
        print(f"  ✓ {name}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"  ✗ {name} — {fix}")
        return False

def main():
    print("CEX Setup\n")
    print("Required:")
    ok = all(check(n, c, f) for n, (c, f) in DEPS.items())
    print("\nOptional:")
    for n, (c, f) in OPTIONAL.items():
        check(n, c, f)

    if not ok:
        print("\n✗ Fix required deps above, then re-run.")
        sys.exit(1)

    print("\n✓ All required deps OK.")
    print("\nNext: python _tools/cex_init.py")
    print("  or: type /init in Claude Code\n")

if __name__ == "__main__":
    main()
```

---

## 2. cex-brain Distribution Architecture

### 2.1 GGUF Generation Pipeline

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌──────────┐    ┌─────────┐
│ Export Data  │───▶│ Train QLoRA  │───▶│   Merge    │───▶│ Quantize │───▶│  GGUF   │
│ (cex corpus) │    │ (Unsloth)    │    │ (base+LoRA)│    │ (Q5_K_M) │    │ (upload) │
└─────────────┘    └──────────────┘    └────────────┘    └──────────┘    └─────────┘
       │                  │                   │                │              │
  cex_finetune.py    unsloth/trl         merge_lora.py    llama.cpp     upload.py
  → JSONL              4-bit             → full model      → GGUF         → HF Hub
  ~50K examples        A100/H100         ~28GB fp16        ~10GB Q5       + Ollama
```

**Step-by-step:**

| Step | Tool | Input | Output | Time (est.) |
|------|------|-------|--------|-------------|
| 1. Export training data | `cex_finetune_export.py` (NEW) | All .md + .yaml in repo | `train.jsonl` (~50K pairs) | 5 min |
| 2. QLoRA fine-tune | Unsloth + TRL | `train.jsonl` + Qwen3-14B base | LoRA adapter (~200MB) | 2-4h (A100) |
| 3. Merge | `merge_lora_to_base.py` | Base + adapter | Full fp16 (~28GB) | 10 min |
| 4. Quantize | `llama-cpp-python` / `llama.cpp` | fp16 model | GGUF Q5_K_M (~10GB) | 15 min |
| 5. Upload | `huggingface_hub` Python | GGUF file | HF Hub gated repo | 20 min |

### 2.2 Hosting Options

| Option | Pros | Cons | Cost | Recommendation |
|--------|------|------|------|---------------|
| **HuggingFace Hub (gated)** | Free hosting, CDN, versioning, gating API | Manual approval OR webhook | Free | ★ Primary |
| Ollama Registry | Native `ollama pull`, seamless UX | No gating — anyone can pull | Free | Public models only |
| S3 + CloudFront | Full control, temp links | Infra cost, maintenance | ~$5/mo | Backup |

### 2.3 License Key Verification — Recommended: Option A

```
┌──────────┐    ┌─────────────────┐    ┌──────────────┐    ┌──────────────┐
│  Student  │───▶│  Lemon Squeezy  │───▶│   Webhook    │───▶│  Verify API  │
│  buys     │    │  checkout       │    │  (Railway)   │    │  (FastAPI)   │
└──────────┘    └─────────────────┘    └──────────────┘    └──────────────┘
                                              │                     │
                                              ▼                     ▼
                                       Store license_key     GET /download?key=xxx
                                       in Supabase           → verify key
                                                             → return temp S3 URL
                                                             → expire in 24h
```

**Option A: Lemon Squeezy webhook → temp download link**

```python
# verify_api.py — FastAPI endpoint on Railway
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import boto3, hashlib

app = FastAPI()

@app.get("/download")
async def download(key: str):
    # 1. Verify license with Lemon Squeezy API
    license = await verify_lemon_squeezy(key)
    if not license or not license["valid"]:
        raise HTTPException(403, "Invalid license key")

    # 2. Generate presigned S3 URL (24h TTL)
    s3 = boto3.client("s3")
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": "cex-models", "Key": "cex-brain-14b-q5.gguf"},
        ExpiresIn=86400,
    )
    return {"download_url": url, "expires_in": "24h", "size_gb": 10.2}
```

**Why Option A over B and C:**

| Criterion | A (webhook+temp) | B (Modelfile key) | C (HF gated) |
|-----------|:-:|:-:|:-:|
| Automation | ✓ Fully automatic | ✗ Manual header hack | ✗ Manual approval |
| UX | ✓ Click → download | ✗ Edit Modelfile | ✗ Wait for approval |
| Piracy resistance | ✓ Temp link expires | ✗ Key visible in file | ✗ Once approved, forever |
| Implementation | Medium | Complex | Easy |

### 2.4 Size Feasibility

| Model | Quantization | Size | Download @ 50Mbps | Viable? |
|-------|-------------|------|-------------------|---------|
| Qwen3-14B | Q5_K_M | ~10.2 GB | ~28 min | ✓ Yes |
| Qwen3-14B | Q4_K_M | ~8.4 GB | ~23 min | ✓ Yes (faster) |
| Qwen3-14B | Q8_0 | ~14.8 GB | ~40 min | ⚠ Borderline |

**Recommendation:** Ship Q5_K_M as default. Offer Q4_K_M as "lite" variant for users with slower connections.

---

## 3. Course Platform Architecture

### 3.1 Tech Stack Decision

```
┌─────────────────────────────────────────────────────────┐
│                    COURSE DELIVERY                       │
│                                                          │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────┐ │
│  │   Lemon     │   │   Content    │   │   Video      │ │
│  │   Squeezy   │   │   Site       │   │   Host       │ │
│  │             │   │              │   │              │ │
│  │  Checkout   │   │  Astro SSG   │   │  YouTube     │ │
│  │  Licenses   │   │  + MDX       │   │  Unlisted    │ │
│  │  Webhooks   │   │  on Vercel   │   │              │ │
│  │  5% fee     │   │  Free tier   │   │  Free        │ │
│  └──────┬──────┘   └──────┬───────┘   └──────┬───────┘ │
│         │                 │                   │          │
│         ▼                 ▼                   ▼          │
│    license_key      gated routes         embed links     │
│    verification     (middleware)         (no listing)     │
└─────────────────────────────────────────────────────────┘
```

### 3.2 Content Delivery Comparison

| Component | Option A (★ Recommended) | Option B | Option C |
|-----------|-------------------------|----------|----------|
| **Checkout** | Lemon Squeezy | Stripe + custom | Hotmart |
| **Text content** | Astro SSG + MDX on Vercel | GitHub Wiki | Notion |
| **Video** | YouTube unlisted | Vimeo OTT ($20/mo) | Self-hosted |
| **Exercises** | CEX checkpoint files | Google Forms | Custom app |
| **Cost** | ~$0/mo (LS fee on sales) | ~$20/mo minimum | 20% of sales |

**Why Astro + MDX:**
- Markdown-native (write course in the same format as CEX artifacts)
- Static site = zero server cost (Vercel free tier)
- Gated routes via middleware checking Lemon Squeezy license
- MDX allows interactive code blocks, live CEX artifact previews

### 3.3 Video Delivery

| Platform | Cost | DRM? | Embed? | Recommendation |
|----------|------|------|--------|---------------|
| YouTube unlisted | Free | No | Yes | ★ MVP (launch fast) |
| Vimeo OTT | $20/mo | Yes | Yes | V2 (if piracy is a concern) |
| Bunny Stream | $5/mo | Token auth | Yes | V2 alternative |
| Self-hosted (S3) | ~$3/mo | Signed URLs | Custom | Overkill |

**MVP decision:** YouTube unlisted. Piracy risk is low for niche educational content. Migrate to Vimeo/Bunny only if leaks become a measurable problem.

### 3.4 Exercise Verification

Students verify completion by running CEX itself:

```bash
# Student completes Module 3 exercise → builds a knowledge_card
python _tools/cex_8f_runner.py --kind knowledge_card --execute

# Checkpoint: student exports their artifact hash
python _tools/cex_checkpoint.py --module 3 --export
# Output: checkpoint_m03_a1b2c3d4.json

# Upload checkpoint to course site for verification
# (Site verifies: correct kind, valid frontmatter, quality >= 7.0)
```

**`cex_checkpoint.py` (NEW — ~100 lines):**
- Reads student's built artifact
- Validates frontmatter + quality gates
- Generates signed hash (module_id + artifact_id + student_key)
- Exports JSON that the course site can verify

---

## 4. CI/CD for the Product

### 4.1 Public Repo Pipeline

```yaml
# .github/workflows/ci.yaml
name: CEX CI
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install ruff
      - run: ruff check _tools/
      - run: ruff format --check _tools/

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -e ".[dev]"
      - run: pytest _tools/tests/ -m "not slow"

  doctor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install pyyaml
      - run: python _tools/cex_doctor.py --ci
      # Fails if any builder is broken

  system-test:
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install pyyaml
      - run: python _tools/cex_system_test.py
```

### 4.2 Versioning Strategy

```
v1.0.0        ← Course "Builder Track" launches, references this tag
v1.1.0        ← New kinds added, course Module 7 references this
v1.1.1        ← Bug fix, no course impact
v2.0.0        ← Breaking change (schema migration), Course V2

Tags: git tag -a v1.0.0 -m "Builder Track launch"
```

| Rule | Implementation |
|------|---------------|
| Course references pinned tags, not `main` | `git clone --branch v1.0.0` in course instructions |
| New features land on `main` first | Students on older tags still work |
| Breaking changes bump major version | Course updates reference new tag |
| `CHANGELOG.md` auto-generated | `python _tools/changelog_gen.py` before each release |

### 4.3 Course Content Updates

```
course-content/           # Separate repo (private)
├── modules/
│   ├── m01-foundations/   # Track 1 (free)
│   ├── m02-first-build/
│   ├── m03-8f-deep/      # Track 2 (Builder, R$497)
│   └── ...
├── astro.config.mjs
├── src/
│   ├── middleware.ts      # Lemon Squeezy license check
│   └── pages/
└── package.json
```

Course content lives in a **separate private repo** — never mixed with the MIT-licensed CEX repo.

---

## 5. Security and Compliance

### 5.1 MIT License Implications

| Permits | Does NOT Protect |
|---------|------------------|
| Commercial use | Your brand name (trademark it separately) |
| Modification | Your course content (separate repo, not MIT) |
| Distribution | Your fine-tuned model (separate license) |
| Private use | Against someone reselling the course (but they can fork the repo) |

**Action items:**
- ✅ MIT license already present (`LICENSE` file)
- Register "CEX" as trademark (optional, low priority)
- Course content in private repo with "All Rights Reserved" header
- cex-brain model: dual license — GGUF file under "CEX Model License" (derivative OK, redistribution NO)

### 5.2 Data Privacy (LGPD/GDPR)

| Data Point | Where | Risk | Mitigation |
|------------|-------|------|------------|
| Brand config from `/init` | Local only (`.cex/brand/`) | None — never leaves user's machine | ✅ Already safe |
| Student email | Lemon Squeezy | Medium — LS is data processor | Add DPA link, privacy policy on checkout |
| Course progress | Checkpoint files (local) | None — local JSON | ✅ Already safe |
| License keys | Supabase (verify API) | Low — keys are not PII | Store hashed, TTL 1 year |

**Required documents:**
1. Privacy Policy (course site footer)
2. Terms of Service (Lemon Squeezy checkout)
3. Data Processing Agreement reference (Lemon Squeezy provides this)

### 5.3 Base Model License Audit

| Model | License | Commercial Use? | Redistribution? | FT Derivative? |
|-------|---------|:---:|:---:|:---:|
| Qwen3-14B | Apache 2.0 | ✓ Yes | ✓ Yes | ✓ Yes |
| Llama 3.1-8B | Meta Community | ✓ Yes (under 700M MAU) | ✓ Yes | ✓ Yes |
| Mistral-7B | Apache 2.0 | ✓ Yes | ✓ Yes | ✓ Yes |

**Qwen3 is the safest choice** — Apache 2.0 has no MAU limits, no special clauses. Fine-tuning and selling the derivative is explicitly permitted. Must include Apache 2.0 notice in the GGUF distribution.

---

## 6. Effort Estimate

### 6.1 Task Breakdown

| # | Task | Category | Hours | Automated? | Depends On |
|---|------|----------|:-----:|:----------:|:----------:|
| 1 | `.gitignore` additions | Repo prep | 0.5 | — | — |
| 2 | `git filter-repo` audit (verify no leaked keys) | Repo prep | 1 | Partial | — |
| 3 | `README.md` public | Repo prep | 3 | — | — |
| 4 | `cex_setup.py` (installer) | Repo prep | 2 | — | — |
| 5 | `CONTRIBUTING.md` | Repo prep | 1 | — | — |
| 6 | `cex_finetune_export.py` (training data export) | Model | 4 | — | — |
| 7 | QLoRA fine-tune run | Model | 6 | Script | 6 |
| 8 | GGUF quantization + upload | Model | 2 | Script | 7 |
| 9 | Verify API (FastAPI + S3 presigned) | Model | 6 | — | — |
| 10 | Lemon Squeezy integration (checkout + webhook) | Platform | 4 | — | — |
| 11 | Astro course site scaffold | Platform | 8 | — | — |
| 12 | License middleware (gated routes) | Platform | 3 | — | 10 |
| 13 | Module 1-3 content (Foundations — free) | Content | 12 | — | 11 |
| 14 | Module 4-7 content (Builder — R$497) | Content | 20 | — | 11 |
| 15 | Module 8-10 content (Master — R$997) | Content | 16 | — | 14 |
| 16 | Video recording + editing (10 modules) | Content | 30 | — | 13-15 |
| 17 | `cex_checkpoint.py` (exercise verification) | Platform | 3 | — | — |
| 18 | GitHub Actions CI/CD | Repo prep | 2 | — | — |
| 19 | Privacy Policy + ToS | Legal | 2 | Template | — |
| 20 | Launch landing page | Marketing | 4 | — | 10 |
| | **TOTAL** | | **122.5h** | | |

### 6.2 MVP — Builder Track Launch (Minimum Viable)

| Task | Hours | Priority |
|------|:-----:|:--------:|
| `.gitignore` + `git filter-repo` audit | 1.5 | P0 |
| `README.md` + `cex_setup.py` | 5 | P0 |
| GitHub Actions CI | 2 | P0 |
| Lemon Squeezy checkout | 4 | P0 |
| Astro site + license middleware | 11 | P0 |
| Modules 1-7 text content | 32 | P0 |
| Video (modules 1-7) | 21 | P1 |
| `cex_finetune_export.py` + FT run + GGUF | 12 | P1 |
| Verify API | 6 | P1 |
| Privacy/ToS | 2 | P0 |
| **MVP TOTAL** | **96.5h** | |

**Timeline estimate at 4h/day: ~24 working days (~5 weeks)**

### 6.3 What Can Be Automated (via CEX itself)

| Task | How |
|------|-----|
| README.md generation | `/build output readme_public` → N03 builds from CLAUDE.md |
| CONTRIBUTING.md | `/build output contributing_guide` |
| Training data export | `cex_finetune_export.py` scans all artifacts programmatically |
| CI workflow | Template from N05 operations |
| Changelog | `python _tools/changelog_gen.py` (already exists) |
| Landing page copy | `/dispatch n02 "landing page for CEX course"` |

---

## Architecture Diagram

```
                         ┌─────────────────────────┐
                         │      STUDENT FLOW        │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                  ▼
            ┌──────────────┐  ┌────────────┐  ┌───────────────┐
            │  GitHub      │  │  Course    │  │  cex-brain    │
            │  (public)    │  │  Site      │  │  Download     │
            │              │  │  (Astro)   │  │  (FastAPI)    │
            │  MIT repo    │  │  Vercel    │  │  Railway      │
            │  /init free  │  │  gated     │  │  gated        │
            └──────┬───────┘  └─────┬──────┘  └──────┬────────┘
                   │                │                 │
                   │         ┌──────┴──────┐          │
                   │         │   Lemon     │          │
                   │         │   Squeezy   │──────────┘
                   │         │   (payment) │  webhook → license verify
                   │         └─────────────┘
                   │
        ┌──────────┴──────────┐
        │  Student's machine  │
        │                     │
        │  CEX repo (cloned)  │
        │  + cex-brain GGUF   │
        │  + Ollama runtime   │
        │  + /init → branded  │
        └─────────────────────┘
```
