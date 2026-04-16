---
kind: tools
id: bld_tools_press_release
pillar: P04
llm_function: CALL
purpose: Production, validation, and distribution tools for the press_release builder
quality: 9.2
title: "Press Release Builder Tools"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, tools]
tldr: "CEX production tools plus AP style checker, embargo validator, word counter, and wire service references"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools

| Tool | Command | Purpose | When to use |
|---|---|---|---|
| cex_compile.py | python _tools/cex_compile.py {path} | Compile .md artifact to .yaml | After F8 save |
| cex_score.py | python _tools/cex_score.py --apply {path} | Run 3-layer quality scoring | After F6 draft |
| cex_retriever.py | python _tools/cex_retriever.py --query "press release {topic}" | Find similar press releases for context | F3 INJECT phase |
| cex_doctor.py | python _tools/cex_doctor.py | Full builder health check | Post-build verification |

## Validation Tools

| Tool | Validation type | Check | Pass condition |
|---|---|---|---|
| AP Style Checker | Style compliance | Attribution verbs, number rules, title format | Zero AP violations |
| Embargo date validator | Temporal validity | Embargo date is in the future, formatted correctly | Date > today, ISO format |
| Word count validator | Length constraint | Body word count 300-500 | 300 <= count <= 500 |
| Headline length validator | Character constraint | Headline under 80 characters | len(headline) <= 80 |
| Contact format validator | Field completeness | Email matches regex, phone has area code | Both fields present and formatted |
| Lede word counter | Lede constraint | Lede sentence under 35 words | len(lede.split()) <= 35 |

### AP Style Checker invocation (integrated into cex_score.py)

The AP style checks run automatically as part of D01 soft scoring. The scorer
inspects the following in sequence:

1. Attribution verbs: scan all quote blocks for "said" -- flag any other verb
2. Number rules: digits 1-9 must be spelled out; 10+ use numerals
3. Title format: titles before names (not after) in attribution lines
4. Date format: "Month DD, YYYY" -- no "st/nd/rd/th" suffixes
5. Time format: "10 a.m. EDT" -- not "10:00 AM" or "10AM"
6. State abbreviations: verify AP abbreviations, not postal codes

### Embargo date validator logic

```
embargo_check(artifact):
  if embargo_date is null:
    confirm "FOR IMMEDIATE RELEASE" on line 1
    return PASS
  if embargo_date <= today:
    return FAIL -- embargo date is in the past
  if embargo_date not on line 1 of document body:
    return FAIL -- embargo not on line 1
  return PASS
```

## External References

| Resource | URL | Purpose |
|---|---|---|
| AP Stylebook Online | https://www.apstylebook.com | Primary style authority; subscription required |
| PR Newswire submission | https://www.prnewswire.com/news-releases/ | Wire distribution portal |
| BusinessWire submission | https://services.businesswire.com | Alternative wire distribution |
| GlobeNewswire submission | https://www.globenewswire.com | Third wire option; strong European reach |
| PR Newswire formatting guide | https://www.prnewswire.com/resources/ | Formatting requirements for submissions |

## Tool Execution Order (F5 CALL phase)

Run tools in this order during F5:

1. cex_retriever.py -- find similar artifacts (inject as F3 context)
2. embargo_validator -- check embargo date before composing
3. [compose artifact -- F6 PRODUCE]
4. word_count_validator -- verify 300-500 word target
5. headline_length_validator -- verify <= 80 chars
6. lede_word_counter -- verify <= 35 words
7. contact_format_validator -- verify email and phone
8. cex_score.py --apply -- full 3-layer scoring
9. cex_compile.py -- compile to YAML
10. cex_doctor.py -- final health check
