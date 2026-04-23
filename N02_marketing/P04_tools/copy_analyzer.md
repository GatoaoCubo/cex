---
id: n02_tool_copy_analyzer
kind: cli_tool
pillar: P04
title: "Copy Analyzer — N02 Marketing Quality Tool"
version: 1.0.0
created: 2026-04-07
author: n02_marketing
domain: copy_analysis
nucleus: N02
quality: 9.0
tags: [cli-tool, copy-analyzer, N02, marketing, quality, readability]
tldr: "Automated copy analysis pipeline: readability scoring, persuasion pattern detection, CTA quality grading, brand voice compliance, and funnel-stage alignment. The ruthless editor that catches what humans miss."
density_score: 0.91
related:
  - p08_ac_n02
  - p03_sp_marketing_nucleus
  - p02_agent_brand_nucleus
  - p07_sr_visual_frontend_marketing
  - p07_sr_5d_marketing
  - n02_self_review_2026-04-02
  - p03_ap_visual_frontend_marketing
  - p03_sp_brand_nucleus
  - p03_sp_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
---

# Copy Analyzer — Marketing Quality Tool

## Purpose

Automated quality analysis for all N02 marketing copy. Reads any copy artifact (email, ad, landing page, social post) and produces a multi-dimensional quality report. Catches readability failures, weak CTAs, missing psychological triggers, brand voice drift, and funnel misalignment — before the copy ships.

## Pipeline

```
INPUT ─► PARSE structure ─► READABILITY score
              │
              ▼
         PERSUASION scan (formula detection)
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
   CTA      BRAND    FUNNEL
  grade     voice    align
      │       │       │
      └───────┼───────┘
              ▼
         REPORT (scores + fixes)
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
   JSON    SUMMARY  MEMORY
  detail    human   update
```

## Usage

```bash
# Analyze a single copy file
python copy_analyzer.py --input N02_marketing/artifacts/email_sequence_template.md

# Analyze all copy in a directory
python copy_analyzer.py --input N02_marketing/P05_output/ --recursive

# Analyze with specific audience target
python copy_analyzer.py --input copy.md --audience b2c --funnel tofu

# Output JSON report
python copy_analyzer.py --input copy.md --format json --output report.json

# Quick score (no detailed report)
python copy_analyzer.py --input copy.md --quick

# Compare two versions (A/B analysis)
python copy_analyzer.py --compare v1.md v2.md
```

## Analysis Dimensions

### 1. Readability Score
```yaml
metrics:
  flesch_reading_ease:
    b2c_target: ">= 65"
    b2b_target: ">= 50"
    executive_target: ">= 40"
  
  avg_sentence_length:
    target: "<= 16 words"
    flag: "> 22 words"
  
  avg_word_length:
    target: "<= 5 chars"
    flag: "> 7 chars"
  
  passive_voice_pct:
    target: "< 10%"
    flag: "> 15%"
  
  paragraph_length:
    target: "<= 3 sentences"
    flag: "> 5 sentences"
```

### 2. Persuasion Pattern Detection
```yaml
formula_detection:
  AIDA:
    attention: "hook/headline present?"
    interest: "problem/opportunity developed?"
    desire: "benefits/transformation shown?"
    action: "clear CTA present?"
  
  PAS:
    problem: "pain point named?"
    agitate: "consequences deepened?"
    solution: "relief presented?"
  
  BAB:
    before: "current state described?"
    after: "desired state described?"
    bridge: "mechanism explained?"
  
  score: "formula_coverage_pct"
  fix: "missing elements listed"
```

### 3. CTA Quality Grade
```yaml
cta_analysis:
  specificity:
    fail: ["click here", "learn more", "submit", "buy now"]
    pass: ["Get my free audit", "Start 14-day trial", "See pricing"]
    grade: "A (specific benefit + action) / B (action only) / C (generic) / F (missing)"
  
  count_check:
    ideal: "1 primary CTA per section"
    warning: "> 2 CTAs per section (decision fatigue)"
    fail: "0 CTAs in conversion-focused copy"
  
  first_person:
    preferred: "'Get MY guide' > 'Get YOUR guide'"
    score: "first_person_pct"
  
  urgency_check:
    present: "deadline, scarcity, or consequence of inaction"
    authentic: "is the urgency real or fabricated?"
```

### 4. Brand Voice Compliance
```yaml
voice_check:
  tone_score:
    source: "brand_config.yaml → tone_spectrum"
    method: "compare copy tone vs configured brand tone"
    tolerance: "+/- 1 point on 1-5 scale"
  
  vocabulary_check:
    banned_words: "loaded from brand_config.yaml"
    signature_phrases: "present/absent check"
    jargon_level: "appropriate for target audience?"
  
  person_consistency:
    check: "consistent use of we/you/they throughout"
    flag: "mixed person references"
  
  energy_match:
    check: "copy energy matches brand energy setting"
    flag: "calm brand + hyperbolic copy, or bold brand + flat copy"
```

### 5. Funnel Stage Alignment
```yaml
funnel_check:
  detected_stage: "TOFU / MOFU / BOFU (auto-detected from signals)"
  intended_stage: "from --funnel flag or frontmatter"
  alignment_score: "match / mismatch / ambiguous"
  
  stage_signals:
    tofu: ["awareness", "discover", "introduction", "free", "learn"]
    mofu: ["compare", "consider", "evaluate", "demo", "trial"]
    bofu: ["buy", "start", "subscribe", "limited", "guarantee"]
  
  misalignment_examples:
    - "TOFU copy with aggressive pricing → warn: audience not ready"
    - "BOFU copy without objection handling → warn: missing FAQ/guarantee"
    - "MOFU copy without social proof → warn: trust not built"
```

## Report Format

### Summary Report (default)
```
╔══════════════════════════════════════════════╗
║  COPY ANALYSIS REPORT                       ║
║  File: email_sequence_template.md           ║
║  Analyzed: 2026-04-07 19:55:00              ║
╠══════════════════════════════════════════════╣
║                                              ║
║  📖 Readability:     8.2/10  (Flesch: 68)   ║
║  🎯 Persuasion:      7.5/10  (PAS detected) ║
║  🔘 CTA Quality:     A  (specific + benefit) ║
║  🎨 Brand Voice:     9.0/10  (on-brand)     ║
║  📊 Funnel Align:    ✅ MOFU  (correct)      ║
║                                              ║
║  OVERALL:  8.2/10                            ║
║                                              ║
║  ⚠️  Issues Found: 3                         ║
║  1. Sentence too long (line 42): 28 words    ║
║  2. Passive voice (line 67): "was achieved"  ║
║  3. Missing urgency element in final CTA     ║
║                                              ║
║  ✅ Fixes Applied: 0 (use --fix to auto-fix) ║
╚══════════════════════════════════════════════╝
```

### JSON Report (--format json)
```json
{
  "file": "email_sequence_template.md",
  "timestamp": "2026-04-07T19:55:00-03:00",
  "scores": {
    "readability": 8.2,
    "persuasion": 7.5,
    "cta_grade": "A",
    "brand_voice": 9.0,
    "funnel_alignment": "correct",
    "overall": 8.2
  },
  "issues": [...],
  "suggestions": [...],
  "formula_detected": "PAS",
  "word_count": 342,
  "reading_time_seconds": 82
}
```

## Integration

| Direction | Target | Data |
|-----------|--------|------|
| Input ← | Any N02 copy artifact | .md files with copy content |
| Input ← | `brand_config.yaml` | Brand voice settings |
| Output → | `copy_optimization_insights.md` | Analysis patterns feed memory |
| Output → | `cex_score.py` | Scores compatible with peer review |
| Output → | `cex_feedback.py` | Quality tracking integration |
| Trigger | `cex_hooks.py` | Auto-run on pre-commit for copy files |

## Quality Gates

```yaml
pass_criteria:
  - readability_score >= 7.0
  - persuasion_score >= 6.0
  - cta_grade in [A, B]  # C and F = fail
  - brand_voice_score >= 7.0
  - funnel_alignment = correct or ambiguous  # mismatch = fail
  - no_critical_issues  # (0 F-grade CTAs, 0 brand violations)

auto_fix_capable:
  - passive_voice → active_voice suggestion
  - long_sentences → split recommendation
  - generic_CTA → specific_CTA variants
  - missing_urgency → urgency element suggestions
```

## Nucleus Dependencies

| Dependency | What | Why |
|------------|------|-----|
| `brand_config.yaml` | Brand voice settings | Voice compliance requires brand context |
| `scoring_rubric_marketing.md` | Evaluation criteria | Aligns scores with N02 quality standards |
| `kc_email_sequence.md` | Email patterns | Validates sequence copy against KC rules |
| `kc_campaign.md` | Campaign patterns | Validates campaign copy against KC rules |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_n02]] | downstream | 0.35 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.35 |
| [[p02_agent_brand_nucleus]] | upstream | 0.32 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.31 |
| [[p07_sr_5d_marketing]] | downstream | 0.31 |
| [[n02_self_review_2026-04-02]] | downstream | 0.31 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.30 |
| [[p03_sp_brand_nucleus]] | upstream | 0.30 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.28 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.28 |
