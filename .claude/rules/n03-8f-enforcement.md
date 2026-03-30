---
glob: "**"
alwaysApply: true
description: "8F Pipeline enforcement — every artifact build MUST follow 8 functions"
---

# 8F Pipeline Enforcement

**MANDATORY on every build request. No exceptions. No shortcuts.**

## Detection

When user asks to CREATE, BUILD, GENERATE, SCAFFOLD, or PRODUCE any artifact:
THIS RULE ACTIVATES. Execute all 8 functions in order.

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

## Anti-Patterns (BLOCKED)

- Generating artifacts without showing F1-F8 trace
- Skipping F7 validation
- Saving without F8 (compile + commit + signal)
- "I'll just write a quick..." — NO. Every build goes through 8F.
