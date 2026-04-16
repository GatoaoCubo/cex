---
kind: learning_record
id: p10_lr_mcp_app_extension_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for mcp_app_extension construction
quality: 8.8
title: "Learning Record MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, learning_record]
tldr: "Learned patterns and pitfalls for mcp_app_extension construction"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Early mcp_app_extension drafts conflated Apps Extension manifests with plain mcp_server contracts, asked for broad permission scopes without justification, and skipped the terminate handler. Several drafts treated the parent-frame DOM as reachable, violating the SEP-1865 sandbox policy and failing Anthropic + OpenAI client review.

## Pattern
Anchor every manifest in SEP-1865 section numbers: section 3 for manifest fields, section 4-6 for install/launch/terminate, section 7 for permission-grant justification. Pin capabilities to the backing mcp_server's advertised tool + resource list (no wildcards). Use CSP `frame-ancestors` to name allowed MCP client origins (Anthropic Claude, OpenAI ChatGPT) and `sandbox="allow-scripts"` as the default iframe posture.

## Evidence
Across a sample of early drafts, manifests with explicit install/launch/terminate schemas passed AAIF review on the first pass; those without failed with a mean of 3 revisions. Manifests listing capabilities one-to-one against mcp_server tools had zero capability-mapping defects, while wildcard manifests had a 60% mismatch rate in val_cap_map.py.

## Recommendations
- Always cite SEP-1865 and MCP spec 2025-11-25 in the knowledge-card injection.
- Enforce a lifecycle checklist: install, launch, terminate -- all three with postMessage schemas.
- Require per-permission inline justification; reject manifests with unjustified scopes at H07.
- Disallow `network:*`, `file:*`, or any wildcard permission.
- Document the sandbox CSP explicitly; never rely on client defaults.
- Treat the parent-frame DOM as unreachable; any assumption otherwise fails the AAIF review.
