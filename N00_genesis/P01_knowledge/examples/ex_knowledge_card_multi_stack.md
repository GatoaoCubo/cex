---
id: p01_kc_multi_stack
kind: knowledge_card
pillar: P01
title: "Multi-Stack Design Knowledge Architecture — 13 Stacks, Zero Duplication"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cross_platform_development
quality: 9.1
tags: [multi-stack, design-system, cross-platform, csv-schema, adapter-pattern]
tldr: "Unified design knowledge serves 13 tech stacks via shared core CSVs + per-stack guideline CSVs with identical schema"
when_to_use: "Building systems that generate code or design recommendations across multiple frontend and mobile stacks"
keywords: [multi-stack, design-tokens, cross-platform, adapter-pattern, csv-schema]
long_tails:
  - "How to share design knowledge across React Vue SwiftUI and Flutter"
  - "What architecture prevents knowledge duplication in multi-stack systems"
axioms:
  - "SEMPRE manter conhecimento core stack-agnostico"
  - "NUNCA duplicar regras de design por stack"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://design-tokens.github.io/community-group/format/"
related:
  - bld_instruction_landing_page
  - p01_kc_csv_as_knowledge
  - kc_landing_page
  - bld_memory_landing_page
  - bld_knowledge_card_landing_page
  - p04_browser_design_extractor
---

## Summary

Architecture pattern where unified design knowledge — styles, colors, typography,
guidelines — serves 13 frontend and mobile stacks without data duplication.
Stack-agnostic core lives in shared CSV files with universal rules.
Stack-specific guidelines (API idioms, component patterns, pitfalls) live in
per-stack CSVs with identical schema enabling a single reusable search engine.
Default stack is html-tailwind when user does not specify one.

## Spec

| Category | Stacks | Count |
|----------|--------|-------|
| Web HTML | html-tailwind (default) | 1 |
| React Ecosystem | react, nextjs, shadcn | 3 |
| Vue Ecosystem | vue, nuxtjs, nuxt-ui | 3 |
| Other Web | svelte, astro | 2 |
| iOS | swiftui | 1 |
| Android | jetpack-compose | 1 |
| Cross-Platform | react-native, flutter | 2 |

### Data Architecture

Core knowledge (styles, colors, typography) lives in shared CSVs loaded for every stack.
Per-stack CSVs contain only platform-specific idioms and API patterns.
Source of truth is the main data directory; CLI and symlinks are derived copies.

### CSV Schema (uniform across all stacks)

```
Category, Guideline, Description, Do, Don't, Code Good, Code Bad, Severity, Docs URL
```

### CLI Distribution Targets

| Flag | Target Platform |
|------|-----------------|
| --ai claude | Claude Code skills directory |
| --ai cursor | Cursor AI skills directory |
| --ai windsurf | Windsurf AI skills directory |
| --ai copilot | GitHub Copilot workflow |
| --ai all | All platforms simultaneously |

## Patterns

| Trigger | Action |
|---------|--------|
| User mentions stack in prompt | Activate matching stack CSV |
| No stack specified | Default to html-tailwind |
| Same design token, different stack | Adapter translates to platform idiom |
| New stack to support | Add CSV with standard schema, done |
| Pre-publish CLI update | Sync source directory to cli/assets/ |

## Anti-Patterns

- Duplicating design knowledge per stack (N copies diverge fast)
- Hardcoding stack in core recommendations (breaks extensibility)
- Stack guidelines without separate CSV (pollutes shared core)
- Assuming HTML when stack is ambiguous (default + ask user)
- Different CSV schemas per stack (breaks reusable search)

## Code

<!-- lang: bash | purpose: stack-specific search commands -->
```bash
python search.py "form validation" --stack react
python search.py "navigation" --stack swiftui
python search.py "state management" --stack flutter
```

<!-- lang: tsx | purpose: React adapter output for shared design token -->
```tsx
<button className="bg-primary hover:bg-primary/90 text-white px-4 py-2">
  Click me
</button>
```

<!-- lang: swift | purpose: SwiftUI adapter output for same design token -->
```swift
Button("Click me") { }
    .background(Color.primary)
    .foregroundColor(.white)
    .padding(.horizontal, 16)
    .cornerRadius(8)
```

## References

- source: https://design-tokens.github.io/community-group/format/
- source: https://tailwindcss.com/docs/configuration
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_landing_page]] | downstream | 0.20 |
| [[p01_kc_csv_as_knowledge]] | sibling | 0.17 |
| [[kc_landing_page]] | sibling | 0.17 |
| [[bld_memory_landing_page]] | downstream | 0.17 |
| [[bld_knowledge_card_landing_page]] | sibling | 0.16 |
| [[p04_browser_design_extractor]] | downstream | 0.15 |
