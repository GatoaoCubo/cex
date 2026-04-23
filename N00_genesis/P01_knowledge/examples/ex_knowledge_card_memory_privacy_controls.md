---
id: p01_kc_memory_privacy_controls
kind: knowledge_card
pillar: P01
title: "Edge-Layer Privacy Controls for LLM Agent Memory Systems"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: llm_memory
quality: 9.1
tags: [privacy, guardrails, tag-stripping, hook-layer, memory-systems]
tldr: "Privacy guardrails at hook layer strip <private> tags before storage; worker strips auto-context tags to prevent re-storage loops"
when_to_use: "Building agents that capture user context and need user-controlled privacy exclusion at the edge"
keywords: [privacy-controls, tag-stripping, edge-layer, hook-privacy, memory-guardrails]
long_tails:
  - "How to implement privacy controls in LLM agent memory"
  - "How to prevent sensitive data from being stored in agent memory"
axioms:
  - "SEMPRE enforce privacy at edge (hook layer), never at storage layer"
  - "NUNCA filter after storage — prevention only, no post-hoc deletion"
linked_artifacts:
  primary: p01_kc_memory_session_compression
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p10_ax_privacy_controls
  - p01_kc_memory_lifecycle_hooks
  - p01_kc_memory_worker_service
  - p01_kc_memory_cross_ide
  - bld_architecture_hook
  - p03_sp_hook_builder
  - p12_wf_advisory_hooks
  - hook-builder
  - p10_ax_lifecycle_hooks
  - hook-config-builder
---

## Summary

Privacy in LLM memory systems requires enforcement at the edge (hook layer) before data reaches storage. Users wrap sensitive content in `<private>` tags; hooks strip them before any HTTP call to the worker service.

The worker independently strips auto-injected `<claude-mem-context>` tags to prevent re-storage loops where injected context gets stored as a new observation. This two-layer approach separates concerns: user-controlled exclusion at edge, system-controlled dedup at worker.

Tag stripping uses a shared utility (`tag-stripping.ts`) ensuring identical logic across Claude Code and Cursor integrations. Hooks are fire-and-forget (exit 0 on error) so privacy failures never block the user workflow. The worker signals rejection via `skipped: true` with a `reason` field, and the hook checks both before proceeding with observation storage.

No server-side filtering exists after storage. The architecture enforces prevention-only: if data passes the edge, it persists. This design eliminates the need for deletion workflows and guarantees sensitive content never touches the database.

## Spec

| Component | Layer | Tag | Purpose |
|-----------|-------|-----|---------|
| `<private>content</private>` | Hook (edge) | User-applied | Excludes sensitive content from storage |
| `<claude-mem-context>...</claude-mem-context>` | Worker | Auto-injected | Prevents re-storage of injected context |
| Exit 0 | Hook | N/A | Non-blocking: graceful error or success |
| Exit 2 | Hook | N/A | Blocking: stderr fed to LLM for decision |
| `skipped` + `reason` | Worker response | N/A | Signals hook to abort observation storage |
| `tag-stripping.ts` | Shared utility | Both | Single implementation for all hooks |

## Patterns

| Trigger | Action |
|---------|--------|
| User wraps text in `<private>` | Hook strips before forwarding to worker |
| Worker returns `skipped: true` | Hook aborts observation storage (exit 0) |
| Worker receives auto-context tags | Strip `<claude-mem-context>` before processing |
| Multiple IDE integrations | Centralize stripping logic in shared utility |
| Hook encounters error | Fire-and-forget: curl -s, errors to /dev/null, exit 0 |

## Anti-Patterns

- Filtering after storage (data already persisted, deletion unreliable)
- Privacy at worker instead of edge (data travels over network)
- Skipping `skipped` flag check (stores observations worker already rejected)
- Duplicating tag-stripping logic per hook (drift between implementations)
- Using exit 1 for privacy errors (blocks user workflow unnecessarily)

## Code

<!-- lang: typescript | purpose: hook-layer privacy check -->
```typescript
// Hook layer: check worker response before storing observation
const response = await fetch('/api/sessions/init', { body: payload });
const result = await response.json();

if (result.skipped && result.reason) {
  // Privacy check failed — abort without storing
  process.exit(0);
}

// Worker layer: strip auto-context before processing
function stripContextTags(text: string): string {
  return text.replace(/<claude-mem-context>[\s\S]*?<\/claude-mem-context>/g, '');
}
```

## References

- source: https://github.com/thedotmack/claude-mem
- source: https://arxiv.org/abs/2303.11366
- related: p01_kc_memory_session_compression
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_ax_privacy_controls]] | downstream | 0.50 |
| [[p01_kc_memory_lifecycle_hooks]] | sibling | 0.38 |
| [[p01_kc_memory_worker_service]] | sibling | 0.33 |
| [[p01_kc_memory_cross_ide]] | sibling | 0.30 |
| [[bld_architecture_hook]] | downstream | 0.28 |
| [[p03_sp_hook_builder]] | downstream | 0.28 |
| [[p12_wf_advisory_hooks]] | downstream | 0.26 |
| [[hook-builder]] | downstream | 0.24 |
| [[p10_ax_lifecycle_hooks]] | downstream | 0.24 |
| [[hook-config-builder]] | downstream | 0.24 |
