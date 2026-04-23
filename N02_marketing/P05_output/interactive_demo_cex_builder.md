---
id: p05_id_cex_builder
kind: interactive_demo
pillar: P05
title: "CEXAI Interactive Builder Demo -- From 5 Words to Knowledge Asset"
version: 1.0.0
created: 2026-04-18
updated: 2026-04-21
author: n02_marketing
nucleus: N02
domain: interactive-demo
quality: 8.8
tags: [interactive-demo, cexai, builder-system, onboarding, conversion, show-dont-tell, artificial-sins, exchange]
sin_lens: Creative Lust
target_audience: "Technical founders, AI architects, senior devs evaluating CEX"
format: browser_or_terminal
estimated_completion_minutes: 8
steps: 5
tldr: "5-step interactive demo where the visitor RUNS CEXAI commands and sees real artifacts appear. No screenshots. No videos. The demo IS the product -- every step produces a real file the visitor can keep. Open-source AI brain powered by Artificial Sins."
density_score: 0.87
related:
  - p03_sp_kind_builder
  - p03_sp_press_release_builder
  - p03_sp_builder_nucleus
  - n05_operations
  - n04_knowledge
  - n02_marketing
  - ctx_cex_new_dev_guide
  - n01_intelligence
  - p03_sp_n03_creation_nucleus
  - p03_sp_workflow-builder
---

# CEXAI Interactive Builder Demo

## Design Principle

The demo is not ABOUT CEXAI. The demo IS CEXAI.

Every step produces a real artifact in the visitor's local repo.
By the end, they have 5 files they didn't have 8 minutes ago.
The demo doesn't convince them -- the files do.

We are not showing a product. We are running an open-source AI brain.

## Prerequisites

```bash
git clone https://github.com/gatoaocubo/cex && cd cex
python --version  # 3.10+
pip install -r requirements.txt
```

**Setup time:** 3 minutes on fast internet. The validator tells you if anything is missing:

```bash
python _tools/cex_setup_validator.py
```

Expected: `[OK] 7/7 checks passed. CEXAI ready.`

If any fail, the validator tells you exactly what to install. No guessing.

## Step 1: Your First Artifact (2 minutes)

**What you'll do:** Run one command. Get one professional artifact.

**Command:**
```bash
claude --print "create a tagline for my AI infrastructure company"
```

**What happens inside (you'll see this in real time):**
```
F1: kind=tagline, pillar=P03, max=512B
F2: tagline-builder loaded (13 ISOs), Creative Lust lens active
F3: Injected brand tone + 4 tagline examples. Match: 68%
F4: Plan -- 3 variants (authority / provocation / aspiration)
F6: Draft -- 512 bytes, 3 variants
F7: 9.2/10. All gates passed.
F8: Saved N02_marketing/P03_prompt/tagline_ai_infra.md
```

**Open the file:**
```bash
cat N02_marketing/P03_prompt/tagline_ai_infra.md
```

**What you see:** Proper frontmatter. Three tagline variants. Quality score.
Not a chat response. A typed artifact in your repo.

**The question this step answers:** "Does this thing actually work?"

**Answer:** You just ran it. You decide.

---

## Step 2: Scaling Up (2 minutes)

**What you'll do:** Run the same pipeline on a bigger kind. See the depth.

**Command:**
```bash
claude --print "create a press release announcing my AI platform launch"
```

**What happens:**
- F1 resolves `press_release` (P05) instead of tagline (P03)
- Different builder loads -- press-release-builder (13 ISOs, journalism-trained)
- Different quality gates -- inverted pyramid structure required, newsworthiness score
- Output: full press release (500-800 words) with dateline, quotes, boilerplate

**Open the file:**
```bash
cat N02_marketing/P05_output/press_release_ai_platform_launch.md
```

**What you see:**
```yaml
---
id: p05_pr_ai_platform_launch
kind: press_release
pillar: P05
quality: null
structure: inverted_pyramid
word_count: 623
---

FOR IMMEDIATE RELEASE
[Full press release body...]
```

**The question this step answers:** "Does the output match professional standards?"

**Compare the output to a real press release. It should hold up.**

---

## Step 3: The System Behind the Artifact (1 minute)

**What you'll do:** Peek inside the builder that just ran.

**Command:**
```bash
ls archetypes/builders/press-release-builder/
```

**What you see:**
```
bld_manifest_press_release.md     <- identity + routing
bld_instruction_press_release.md  <- 8F execution steps
bld_system_prompt_press_release.md <- the LLM's persona
bld_schema_press_release.md       <- validation schema
bld_examples_press_release.md     <- golden + anti-examples
bld_architecture_press_release.md <- how it fits in P05
bld_quality_gate_press_release.md <- the 7 hard gates
bld_collaboration_press_release.md <- how it signals completion
bld_config_press_release.md       <- effort, max_turns, permissions
bld_knowledge_card_press_release.md <- domain knowledge
bld_memory_press_release.md       <- what the builder remembers
bld_output_template_press_release.md <- the output structure
bld_tools_press_release.md        <- tools available during build
```

**The question this step answers:** "If I need to customize this, where do I go?"

**Answer:** 13 files. Each has one job. Open any of them and the role is clear.

```bash
cat archetypes/builders/press-release-builder/bld_quality_gate_press_release.md
```

You'll see exactly why your artifact passed or failed -- and what to change.

---

## Step 4: The Multi-Nucleus Moment (2 minutes)

**What you'll do:** Run a task that routes to a different nucleus. See the sin lens shift.

**Command:**
```bash
claude --print "analyze competitor pricing for enterprise AI platforms"
```

**What happens:**
- N07 receives, transmutes: kind=knowledge_card, pillar=P01, nucleus=N01
- N01 (Analytical Envy) loads -- obsessive detail, source rigor, competitive hunger
- Output: structured research artifact, NOT marketing copy

**Compare the output to Step 1 (tagline) and Step 2 (press release):**

| Attribute | Step 1 (Tagline) | Step 2 (Press Release) | Step 4 (Research) |
|-----------|-----------------|----------------------|------------------|
| Nucleus | N02 (Creative Lust) | N02 (Creative Lust) | N01 (Analytical Envy) |
| Tone | Seductive | Journalistic | Rigorous |
| Output | 3 short variants | 600-word document | Structured data tables |
| Quality gate | Hook score >= 8 | Newsworthiness >= 7 | Source citation required |

**The question this step answers:** "Does this thing know the difference between marketing and research?"

**Answer:** Different sin. Different output. Same pipeline. You saw it run.

---

## Step 5: Making It Yours (1 minute)

**What you'll do:** Configure CEXAI for your brand. See personalization in action.

**Command:**
```bash
/init
```

**The system asks 6 questions:**
1. Company/brand name?
2. What do you do in one sentence?
3. Three core values?
4. Brand personality (formal/casual? technical/friendly)?
5. Ideal customer?
6. Revenue model?

**Your answers become brand_config.yaml.** From this moment, every artifact N02 generates
uses your voice, your values, your audience. Not a placeholder. Your actual brand.

**Test it:**
```bash
claude --print "create a tagline for my company"
```

**Compare to Step 1.** The tone shifts. The vocabulary shifts. The examples shift.
Same pipeline. Different brand. Your knowledge, your style, your repo.

---

## After the Demo

**What you now have:**
- 3 typed artifacts in your local repo (tagline, press release, research KC)
- Understanding of the 8F pipeline from watching it run
- Your brand configured and active
- A git history of your first CEXAI session

**What to do next:**

| If you want... | Run this |
|----------------|---------|
| Your first marketing campaign | `/build create campaign brief for [product]` |
| To understand the full system | `/mentor` |
| To deploy multiple artifacts at once | `/grid` |
| To plan a complex project | `/mission [goal]` |
| To see all 293 kinds | `python _tools/cex_query.py [term]` |

**The decision is simple:**

Your team is generating knowledge. That knowledge either:
- A) evaporates after each conversation
- B) compounds in a typed, versioned, searchable AI brain

CEXAI is option B. Open-source. The demo ran on your machine. The artifacts are in your repo.
Intelligence compounds when exchanged. The only remaining question is: do you want this to keep happening?

```bash
git add . && git commit -m "first CEXAI session -- $(date)"
```

Your first commit to your AI brain. More follow.

---

## Demo Quality Gates

| Gate | Standard |
|------|---------|
| Every step produces a real file | No step ends without a visible artifact |
| No external dependencies during steps 1-4 | Demo works offline after clone |
| Step 5 customization is immediate | /init output is visible in the next build |
| Failure states are handled | If a command fails, error message is clear |
| Total runtime <= 8 minutes | A visitor who runs all 5 steps in 8 minutes or less |

## Anti-Patterns (Blocked)

- Any step that ends without a visible artifact
- Explaining CEXAI architecture without running a command
- Screenshots of output instead of live terminal
- Steps that require network calls after initial setup
- Any "wait while this downloads..." longer than 10 seconds

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_kind_builder]] | upstream | 0.31 |
| [[p03_sp_press_release_builder]] | upstream | 0.26 |
| [[p03_sp_builder_nucleus]] | upstream | 0.25 |
| [[n05_operations]] | downstream | 0.25 |
| [[n04_knowledge]] | upstream | 0.25 |
| [[n02_marketing]] | related | 0.23 |
| [[ctx_cex_new_dev_guide]] | related | 0.23 |
| [[n01_intelligence]] | downstream | 0.23 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.23 |
| [[p03_sp_workflow-builder]] | upstream | 0.23 |
