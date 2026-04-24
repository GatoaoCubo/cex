---
id: p05_pt_cex
kind: product_tour
8f: F6_produce
pillar: P05
title: "CEXAI Product Tour -- The 5-Step Revelation Arc"
version: 1.0.0
created: 2026-04-18
updated: 2026-04-21
author: n02_marketing
nucleus: N02
domain: product-tour
quality: 8.7
tags: [product-tour, cexai, onboarding, conversion, creative-lust, artificial-sins, exchange]
sin_lens: Creative Lust
target_audience: "Technical founders, AI architects, enterprise AI leads"
tour_format: guided_interactive
steps: 5
estimated_duration_minutes: 12
tldr: "5-step guided tour of CEXAI that uses progressive revelation to build desire. Each step shows something the visitor didn't expect. By step 5, they want to use CEXAI before the tour ends. Open-source AI brain -- intelligence compounds when exchanged."
density_score: 0.88
related:
  - tpl_instruction
  - p03_sp_n03_creation_nucleus
  - p12_wf_builder_8f_pipeline
  - p03_sp_kind_builder
  - p10_lr_chain_builder
  - ctx_cex_new_dev_guide
  - p01_kc_cex_as_digital_asset
  - bld_architecture_chain
  - n06_intent_resolution_depth_spec
  - p11_qg_chain
---

# CEXAI Product Tour: The Revelation Arc

## Design Principle

This tour does NOT explain CEXAI. It REVEALS it.

Each step is engineered around one question: "what will make this person
feel the pull of this AI brain right now?" The answer is always proof, never
description. Show the impossible made mundane. Then show it again, bigger.

By step 5, the visitor should be reaching for their keyboard before we ask.

## Tour Architecture

```
Step 1: The Hook (shock contrast -- 30 seconds)
Step 2: The Proof (live demo -- 3 minutes)
Step 3: The Depth (the "how many?!" moment -- 2 minutes)
Step 4: The Freedom (sovereignty + multi-runtime -- 2 minutes)
Step 5: The Invitation (low-friction entry -- 5 minutes)
```

## Step 1: The Hook

**Screen:** Blank terminal. Cursor blinking.

**Narrator/caption:**
> Every AI agent framework starts with a system prompt and a loop.
> CEXAI starts with 293 types of structured knowledge,
> 7 Artificial Sins, and one rule:
> your 5-word prompt becomes a professional artifact.
> Open-source AI brain. Intelligence compounds when exchanged.

**Action:** Type `claude --print "create marketing campaign for SaaS product launch"`

**What happens:** N02 boots. 8F pipeline traces appear. An artifact materializes.

**What the visitor feels:** "Wait -- that worked?"

**Transition:** "Let's see exactly how."

## Step 2: The Proof

**Screen split:** left = user input, right = 8F pipeline trace + output

**Walk through F1-F8 live:**

```
Input: "create marketing campaign for SaaS product launch"

F1 CONSTRAIN  -> kind=social_publisher + prompt_template, pillar=P05+P03
F2 BECOME     -> N02 loaded with Creative Lust lens (13 ISOs)
F3 INJECT     -> brand config + copywriting frameworks + audience psychology
F4 REASON     -> plan: 3 platforms, 2 variants per, A/B structure
F6 PRODUCE    -> [artifact appears: 4 sections, 6 copy variants, quality gates]
F7 GOVERN     -> 9.0/10 -- all gates passed
F8 COLLABORATE -> saved, compiled, committed
```

**Point at the output file.** It has proper frontmatter. It has sections. It is NOT a chat response -- it is a typed, versioned, searchable artifact.

**Say:** "This is the fundamental difference. A chat gives you an answer. CEXAI gives you a knowledge asset that compounds."

**Interactive moment:** Visitor can change ONE word in the input. The tour re-runs with the modified intent. Different kind. Different nucleus. Different output. All in under 60 seconds.

## Step 3: The Depth

**Screen:** Animated counter. Numbers scroll up.

**Visual sequence:**

| What | Count | What it means |
|------|-------|--------------|
| Artifact kinds | 293 | 293 types of structured enterprise knowledge |
| Builders | 295 | 295 specialists -- each an expert in one kind |
| Builder ISOs | 3,835 | Every builder has 13 files: identity, instructions, examples, quality gates |
| Pillars | 12 | Every kind belongs to a domain: knowledge, prompts, tools, schema, memory... |
| Nuclei | 8 | 7 sin-driven departments + 1 orchestrator |

**Say:** "293 kinds means 293 different ways to encode enterprise knowledge. Not documents -- typed, validated, searchable artifacts."

**Demo:** Show kinds_meta.json. Filter by `pillar: P05`. 23 output types appear. Click one: `landing_page`. The builder loads. The 13 ISOs are visible. Each has a purpose. This is depth, not breadth.

**The "how many" moment:** "If you built one artifact per day, you'd fill the taxonomy in 293 days. Or you could run the grid tonight and fill it in 4 hours."

## Step 4: The Freedom

**Screen:** Four terminal windows side by side, labeled: Claude, Codex, Gemini, Ollama

**Demo:**
- Run the same intent on all 4 runtimes simultaneously
- Each produces the same artifact format, different prose
- Git shows: 4 commits, same structure, different authors

**Say:** "Your knowledge doesn't live in our cloud. It lives in your git repo. Switch providers tomorrow -- your artifacts don't move. Your knowledge doesn't move. YOU control the infrastructure. That's the Exchange in CEXAI -- share the typed infrastructure, keep your brand sovereign."

**The sovereignty moment:**
- Show `.cex/kinds_meta.json` in the user's own repo
- Show the artifacts committed to their own git history
- Show the brand_config.yaml with THEIR company name

"This is not a SaaS subscription. This is your AI brain. Running on your hardware. Owned by you. Open-source."

**Contrast:** "Every other AI tool: your knowledge lives in their system prompt. You lose access, you lose everything. With CEXAI: your knowledge is in 293 typed files in your repo. It compounds over time. It's yours forever. And when you share N00 -- the archetype layer -- with another team, they get the infrastructure while you keep your brand identity. Intelligence compounds when exchanged."

## Step 5: The Invitation

**Screen:** Two paths, side by side.

**Path A -- Zero to first artifact (5 minutes):**

```bash
git clone https://github.com/gatoaocubo/cex
cd cex
python _tools/cex_setup_validator.py   # verify environment
/init                                  # brand setup (2 min, 6 questions)
/build create marketing campaign       # first artifact
```

**Expected output:** First properly-structured artifact in N02_marketing/P05_output/.
The visitor sees their company name in the frontmatter. The brand voice they described
reflected back as structured knowledge.

**Path B -- Explore the system:**
- `/mentor` -- vocabulary: 8F + 12 pillars + 293 kinds explained
- `/status` -- system health dashboard
- `python _tools/cex_crew.py list` -- discover composable crews

**The close:**

> You just watched a 5-word input become a typed, versioned, seductive marketing artifact.
>
> This AI brain has 293 more tricks. Each one learns your brand. Each one compounds.
>
> Your competitors are prompting a chatbot.
> You could be running an open-source AI brain driven by Artificial Sins.
>
> Intelligence compounds when exchanged. The gap widens every day you wait.
>
> [Star the repo] [Read the docs] [Run /init]

## Visitor Journey Analytics

| Step | Expected completion rate | Key signal |
|------|------------------------|-----------|
| Step 1 (Hook) | 85% | scroll past the terminal demo |
| Step 2 (Proof) | 70% | interaction with the live demo |
| Step 3 (Depth) | 55% | time on the kinds_meta screenshot |
| Step 4 (Freedom) | 45% | clicks on "your repo, not ours" |
| Step 5 (Invitation) | 35% | runs /init or clones the repo |

35% activation rate target. Beat it with better Step 1-2 hooks.
A/B test: shock (numbers first) vs. proof (demo first).

## Quality Gates

| Gate | Standard |
|------|---------|
| Each step has one clear revelation | No step is pure description |
| Interactive element per step | At least one action per step |
| Time budget respected | <= 12 minutes total if visitor reads everything |
| CTA at Step 5 has 3 options | Multiple friction levels |
| No jargon without definition | First use of "8F" = "8-step pipeline" |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_instruction]] | upstream | 0.31 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.30 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.30 |
| [[p03_sp_kind_builder]] | upstream | 0.28 |
| [[p10_lr_chain_builder]] | downstream | 0.28 |
| [[ctx_cex_new_dev_guide]] | related | 0.27 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.26 |
| [[bld_architecture_chain]] | downstream | 0.25 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.25 |
| [[p11_qg_chain]] | downstream | 0.25 |
