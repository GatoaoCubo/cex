---
glob: "**"
alwaysApply: true
description: "8F Universal Reasoning Protocol — every nucleus, every task, every time"
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

## Anti-Patterns (BLOCKED)

- Processing a task without 8F trace — ANY task, not just builds
- Skipping F7 validation
- Saving without F8 (compile + commit + signal)
- "I'll just do a quick..." — NO. Every task goes through 8F.
- N07 dispatching without F1 (constraining scope) and F4 (planning approach)
