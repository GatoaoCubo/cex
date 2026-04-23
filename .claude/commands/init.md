---
description: "Initialize CEX for your brand. First-time setup. Usage: /init [folder_path]"
quality: 9.0
title: "Init"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - brand_bootstrap
  - p03_sp_brand_nucleus
  - p01_kc_cex_as_digital_asset
  - p08_pat_brand_pipeline
  - p02_agent_commercial_nucleus
  - ctx_cex_new_dev_guide
  - spec_n06_brand_verticalization
  - p02_agent_brand_nucleus
  - skill_guided_decisions
  - p03_brand_discovery_interview
---

# /init — Bootstrap Your Brand

The X in CEX is YOUR brand. This command fills it.

## Phase 0: Environment Setup (ALWAYS runs first)

Before brand setup, verify API keys are configured:

```bash
python _tools/cex_env_wizard.py --check
```

If `ANTHROPIC_API_KEY` is missing, run the wizard:

```bash
python _tools/cex_env_wizard.py
```

This is the minimum required key to run CEX. All other keys are optional.
If the user types `/init --env`, run the wizard and stop (skip brand setup).

## Mode Detection

Check how the user invoked `/init`:

1. `/init` (no args) → **Conversational mode**: ask questions one by one
2. `/init C:\Users\...\my_brand_stuff` → **Ingest mode**: scan folder, then ask
3. `/init <url>` → **URL mode**: scrape website for brand signals
4. `/init https://github.com/...` → **Repo mode**: read GitHub repo for signals
5. `/init <file.pdf>` → **File mode**: ingest single file
6. `/init --reset` → Reset existing brand: `python _tools/cex_bootstrap.py --reset`
7. `/init --env` → Env wizard only (no brand setup)

## Step 0: Check Bootstrap Status

```bash
python _tools/cex_bootstrap.py --check
```

If already bootstrapped, show status and ask if they want to update or reset.

---

## PATH A — Conversational Mode (no folder)

Ask these questions ONE AT A TIME in natural language. Wait for each answer.
Use casual, friendly tone. The user might not know branding terminology.

**Round 1 — The basics**
1. "What's the name of your company or product?"
2. "If you had to describe what you do in one sentence — like an elevator pitch — what would it be?"
3. "What are 3 things your company would NEVER compromise on? Like core values."

**Round 2 — Personality**
- "How should your brand sound? More like a professor or a friend? More serious or fun?"
  - From their answer, map to 5D voice scores and suggest an archetype.
  - Present 3-4 archetype options in SIMPLE language:
    - "The Wise Guide (Sage) — educational, trustworthy"
    - "The Rebel (Outlaw) — bold, challenges the status quo"
    - "The Creator — innovative, original, artistic"
    - "The Caregiver — supportive, warm, protective"
    - etc. (only show 3-4 most likely matches)

**Round 3 — Your people**
1. "Describe your dream customer — not their age, but their daily frustrations and what they wish was different."
2. "After they use your product, what changes? Try: 'From ___ to ___ through ___'"

**Round 4 — Business**
1. "What category or market are you in?"
2. "How do you make money — subscriptions, one-time sales, courses, something else?"
3. "What currency — BRL, USD?"

After all answers: write YAML, bootstrap, confirm.

---

## PATH B — Ingest Mode (folder provided)

The user has a messy folder with brand materials. Process it:

### Step 1: Ingest

```bash
python _tools/brand_ingest.py "$ARGUMENTS" --for-llm
```

This scans the folder and extracts:
1. Color hex codes from CSS/HTML files
2. Font names
3. Potential brand names (by frequency)
4. Mission/vision/tagline (if found in text)
5. URLs, social handles, pricing
6. Source excerpts for context

### Step 2: Read documents (if any)

If `brand_ingest.py` reports documents (PDF, DOCX, PPTX):
1. Use the **markitdown** MCP tool to convert each to text
2. Extract brand signals from the converted text
3. Look for: pitch decks (positioning), brand guides (colors/fonts), proposals (ICP)

### Step 3: Read images (if any)

If images are found (logos, screenshots, Canva exports):
1. Describe what you see: colors, style, typography direction
2. Note potential logo files

### Step 4: Present findings to user

Show what you found:
> "I scanned your 23 files and found:
> - Brand name appears to be: **[name]** (appeared 14 times)
> - Colors used: **#FF5733**, **#1A1A2E**, **#50C878**
> - Font: **Inter** (in your CSS)
> - Mission fragment: '...'
> - Pricing: R$ 97, R$ 297 (subscription seems likely)
>
> Let me confirm a few things..."

### Step 5: Fill gaps conversationally

Ask ONLY about what wasn't found:
1. If no archetype signals → ask about personality
2. If no ICP found → ask about ideal customer
3. If no transformation → ask about before/after
4. If no values → ask about non-negotiables

### Step 6: Bootstrap

Write YAML from combined signals + answers:

```bash
python _tools/cex_bootstrap.py --from-file /tmp/brand_from_ingest.yaml
```

Verify:
```bash
python _tools/brand_validate.py
python _tools/brand_audit.py --json
```

---

## PATH C -- URL Mode

User provides a website URL (not a GitHub URL):

```bash
python _tools/brand_ingest.py --url "$ARGUMENTS" --for-llm
```

This scrapes homepage + /about + /pricing pages.
Uses Firecrawl if `FIRECRAWL_API_KEY` is set, otherwise plain HTTP.

Then follow PATH B Step 4 onwards (present findings, fill gaps conversationally).

---

## PATH D -- GitHub Repo Mode

User provides a GitHub URL (`https://github.com/{owner}/{repo}`):

```bash
python _tools/brand_ingest.py --repo "$ARGUMENTS" --for-llm
```

This reads README + key docs via the GitHub raw content API (no auth needed for public repos).
Also fetches the repo description from `api.github.com`.

Then follow PATH B Step 4 onwards.

---

## PATH E -- Single File Mode

User provides a path to a file (PDF, DOCX, MD, TXT):

```bash
python _tools/brand_ingest.py --file "$ARGUMENTS" --for-llm
```

If the file is a PDF/DOCX, attempts to use `markitdown` for conversion.
Then follow PATH B Step 4 onwards.

---

## Final Confirmation

Always end with:
> "Done! CEX is now the brain of **[BRAND_NAME]**.
> Everything I produce from now on will use your voice, colors, and identity.
>
> Want me to generate your full Brand Book? (32 sections, takes ~5 minutes)"

If they say yes → run the N06 Brand Book workflow.

---

## Edge Cases

**User has almost nothing**: Just a name and a vague idea.
→ That's fine. Fill what you can, use sensible defaults, mark gaps.
→ Suggest: "We can refine this later with `/init` again."

**User has TOO MUCH**: 500 files, multiple brands.
→ Ask: "Which brand should I focus on?" or "Which folder is the main one?"
→ Only ingest the subfolder they point to.

**User has an existing brand guide**: PDF with colors, fonts, voice.
→ Best case. Use markitdown to read it, extract everything.
→ This might fill 90% of brand_config.yaml automatically.

**User's materials are in a foreign language**:
→ brand_ingest.py detects language automatically.
→ Set BRAND_LANGUAGE accordingly.

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[brand_bootstrap]] | related | 0.42 |
| [[p03_sp_brand_nucleus]] | related | 0.36 |
| [[p01_kc_cex_as_digital_asset]] | related | 0.35 |
| [[p08_pat_brand_pipeline]] | related | 0.32 |
| [[p02_agent_commercial_nucleus]] | related | 0.30 |
| [[ctx_cex_new_dev_guide]] | related | 0.30 |
| [[spec_n06_brand_verticalization]] | related | 0.28 |
| [[p02_agent_brand_nucleus]] | related | 0.27 |
| [[skill_guided_decisions]] | related | 0.27 |
| [[p03_brand_discovery_interview]] | related | 0.26 |
