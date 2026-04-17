---
glob: "**"
alwaysApply: true
description: "8F Universal Reasoning Protocol — every nucleus, every task, every time"
quality: 9.0
title: "8F-Reasoning"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# 8F Universal Reasoning Protocol

**MANDATORY for ALL nuclei (N01-N07). Every task. No exceptions.**

8F is not a "build checklist" — it's how CEX THINKS. Whether you're researching,
writing copy, building code, organizing knowledge, deploying, pricing, or orchestrating
— you follow the same 8 reasoning steps. This is what makes a 5-word user input
produce professional output: the 8F pipeline does the work the user can't.

## Detection

ANY task activates 8F. Not just "build" — also research, analyze, write, plan,
deploy, price, orchestrate. If a nucleus receives work, 8F runs.

## The 8 Functions (execute in sequence, show evidence)

### F1 CONSTRAIN
```
Read: .cex/kinds_meta.json → resolve kind
Read: P{xx}/_schema.yaml → load schema
Output: "F1: kind={kind}, pillar={pillar}, max_bytes={max}, naming={pattern}"
```

### F2 BECOME
```
Read: archetypes/builders/{kind}-builder/bld_manifest_{kind}.md
Read: archetypes/builders/{kind}-builder/bld_instruction_{kind}.md
Read: archetypes/builders/{kind}-builder/bld_system_prompt_{kind}.md
Output: "F2: Builder loaded ({N} ISOs). Identity: {role}"
```

### F3 INJECT
```
Read: P01_knowledge/library/kind/kc_{kind}.md
Search: examples/ and compiled/ for similar artifacts
Read: any relevant domain KCs
Output: "F3: Injected {N} knowledge sources. Template-First match: {score}%"
```

### F3b PERSIST (sub-step, optional)
```
After assembling context, declare what new knowledge should be persisted:
- New entities discovered -> entity_memory
- Updated facts -> knowledge_card update
- Session learnings -> learning_record
Output: "F3b: Persist {N} items (entities: {n1}, facts: {n2}, learnings: {n3})"
```

### F3c GROUND (sub-step, when sources cited)
```
For each injected source, record provenance:
- Source path/URL
- Retrieval confidence score
- Freshness (last updated timestamp)
Output: "F3c: Grounded {N} sources. Avg confidence: {X}%"
```

### F4 REASON
```
Plan: sections, approach, references, estimated density
Apply: Construction Triad (Template-First if match >= 60%)
Output: "F4: Plan — {N} sections, approach: {template|hybrid|fresh}"
```

### F5 CALL
```
List: available tools (compile, doctor, index, signal)
Scan: existing similar artifacts for reuse
Output: "F5: Tools ready. {N} similar artifacts found."
```

### F6 PRODUCE
```
Generate: complete artifact with frontmatter + body
Follow: builder instructions from F2
Apply: density target >= 0.85
Output: "F6: Draft generated ({bytes} bytes, {sections} sections)"
```

### F7 GOVERN
```
Validate: H01-H07 gates
Run: 12LP checklist (all 12 points)
Score: 5D dimensions (D1-D5 weighted)
Output: "F7: Score {X}/10. Gates: {pass}/{total}. 12LP: {pass}/12"
If FAIL: return to F6 (max 2 retries)
```

### F7b LEARN (sub-step, optional)
```
After scoring, capture feedback signals:
- What patterns led to high/low scores -> reward_signal
- Which gates commonly fail -> regression_check
- Quality trends over time -> quality metrics
Output: "F7b: Learn {N} signals (rewards: {n1}, regressions: {n2})"
```

### F8 COLLABORATE
```
Save: write .md file to correct pillar directory
Compile: python _tools/cex_compile.py {path}
Index: python _tools/cex_index.py (if available)
Commit: git add + git commit
Signal: python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', 'complete', {score})"
Output: "F8: Saved {path}. Compiled. Committed. Signal sent."
```

## Output Format

Every build MUST show the 8F trace:

```
=== 8F PIPELINE ===
F1 CONSTRAIN: kind=agent, pillar=P02, max=5120B
F2 BECOME: agent-builder loaded (13 ISOs)
F3 INJECT: kc_agent.md + 2 examples. Match: 72%
F4 REASON: 4 sections, approach=template (adapt from match)
F5 CALL: compile+doctor+index ready. 3 similar found.
F6 PRODUCE: 3,200 bytes, 4 sections, density=0.88
F7 GOVERN: 9.0/10. Gates: 7/7. 12LP: 12/12
F8 COLLABORATE: saved P02/agent_x.md. Compiled. Committed.
===================
```

## Why 8F Matters (The Leverage Principle)

The user will ALWAYS have a knowledge gap. Their input will be vague, incomplete,
non-technical. CEX compensates by running 8F on every input:

```
User: "make me a landing page"  (5 words, zero spec)
                │
  F1 CONSTRAIN  │→ kind=landing_page, pillar=P05, schema loaded, constraints set
  F2 BECOME     │→ landing-page-builder loaded (13 ISOs), sin lens injected
  F3 INJECT     │→ 10 context sources: KC, examples, memory, brand, similar artifacts
  F4 REASON     │→ plan: 12 sections, mobile-first, Tailwind, conversion-optimized
  F5 CALL       │→ tools executed, references fetched, sub-agents if needed
  F6 PRODUCE    │→ complete HTML page (responsive, dark mode, SEO, a11y)
  F7 GOVERN     │→ quality gate: 7 HARD gates, retry if < 8.0
  F8 COLLABORATE│→ saved, compiled, committed, signaled
                │
                ▼
Output: production-ready landing page (5 words in → professional artifact out)
```

This IS the product. The 8F pipeline is the force multiplier that makes CEX
outperform raw LLM calls. Every nucleus uses it. Every time.

## 8F by Nucleus

8F is the SAME protocol — the content changes per domain.

### N07 Orchestrator — "/mission build CRM"
```
F1 CONSTRAIN → scope: what kind of CRM? what nuclei needed? what wave structure?
F2 BECOME    → Ira Construtiva lens: ruthless quality, precise dispatch
F3 INJECT    → load mission plans, decision manifest, signal history
F4 REASON    → plan: 3 waves, 5 nuclei, dependency graph
F5 CALL      → provider discovery, agent spawn validation, PID tracking
F6 PRODUCE   → write handoffs + mission plan + wave schedule
F7 GOVERN    → validate: all handoffs have frontmatter? all nuclei have boot scripts?
F8 COLLABORATE → dispatch grid, monitor signals, consolidate on completion
```

### N01 Intelligence — "research competitor pricing in EdTech"
```
F1 CONSTRAIN → kind=knowledge_card, pillar=P01, domain=edtech pricing
F2 BECOME    → Avareza Investigativa lens: insatiable data hunger
F3 INJECT    → load KCs on pricing, EdTech market, existing competitor intel
F4 REASON    → plan: 6 competitors, 3 pricing dimensions, source map
F5 CALL      → retriever finds existing pricing KCs, query discovers related builders
F6 PRODUCE   → structured intelligence brief with pricing tables + sources
F7 GOVERN    → validate: sources cited? data density >= 0.85? no speculation?
F8 COLLABORATE → save to N01_intelligence/, compile, signal N07
```

### N02 Marketing — "write ad copy for Black Friday campaign"
```
F1 CONSTRAIN → kind=prompt_template, pillar=P03, domain=ad copy
F2 BECOME    → Luxúria Criativa lens: seductive, irresistible prose
F3 INJECT    → load brand voice, audience persona, past campaign KCs
F4 REASON    → plan: 3 ad variants (urgency, FOMO, value), A/B structure
F5 CALL      → brand config loaded, memory recalls past conversion data
F6 PRODUCE   → 3 ad copy variants with hooks, CTAs, and character limits
F7 GOVERN    → validate: brand voice match? CTA present? length within platform limits?
F8 COLLABORATE → save to N02_marketing/, compile, signal N07
```

### N06 Commercial — "design pricing tiers for SaaS product"
```
F1 CONSTRAIN → kind=content_monetization, pillar=P11, domain=SaaS pricing
F2 BECOME    → Gula Monetizadora lens: maximize every revenue stream
F3 INJECT    → load competitor pricing KC, market research, customer segments
F4 REASON    → plan: 3 tiers (free/pro/enterprise), feature gating, annual discount
F5 CALL      → retriever finds existing monetization artifacts, brand config loaded
F6 PRODUCE   → pricing model with tier table, feature matrix, revenue projections
F7 GOVERN    → validate: tiers differentiated? no cannibalization? margins positive?
F8 COLLABORATE → save to N06_commercial/, compile, signal N07
```

## Anti-Patterns (BLOCKED)

1. Processing a task without 8F trace — ANY task, not just builds
2. Skipping F7 validation
3. Saving without F8 (compile + commit + signal)
4. "I'll just do a quick..." — NO. Every task goes through 8F.
5. N07 dispatching without F1 (constraining scope) and F4 (planning approach)

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
