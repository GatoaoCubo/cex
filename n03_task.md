---
mission: WAVE7
nucleus: n03
wave: dev-manifests
created: 2026-04-14
model: claude-opus-4-6
---

# N03 -- Build 3 dev-manifest kinds (39 ISOs): AGENTS.md + MCP-Apps + K8s-AI

## Your kinds (developer-facing manifests)

1. **agents_md** (P02/CONSTRAIN, max 3072B) -- AAIF/OpenAI AGENTS.md project-root manifest (60K+ projects adoption). Instructs coding agents: setup commands, test/lint commands, conventions, PR format, deploy rules. Think CLAUDE.md standardized.

2. **mcp_app_extension** (P04/CALL, max 4096B) -- MCP SEP-1865 Apps Extension (Anthropic+OpenAI active draft 2026). App lifecycle (install/launch/terminate), app manifest schema, capability declarations, permission grants, sandbox boundaries.

3. **kubernetes_ai_requirement** (P09/CONSTRAIN, max 4096B) -- CNCF KAR v1.35 (GA Nov 2025). K8s AI workload requirements: GPU topology, InfiniBand, MIG partitioning, DRA scheduling, checkpoint PVCs, multi-node training constraints.

## Gold template to clone

Read ALL 13 files in `archetypes/builders/partner-listing-builder/`. Clone SHAPE.

## Required ISOs per kind (13 each = 39 total)

Same 13-ISO structure in `archetypes/builders/{kind}-builder/`.

## Domain keywords (validator check)

- **agents_md**: AGENTS.md, coding-agent, setup-command, test-command, lint-command, pr-format, deploy-rule, project-root, 60K-projects, AAIF
- **mcp_app_extension**: MCP, SEP-1865, app-manifest, install, launch, terminate, capability, sandbox, permission-grant, Anthropic, OpenAI
- **kubernetes_ai_requirement**: K8s, KAR, CNCF, GPU-topology, InfiniBand, MIG, DRA, checkpoint-PVC, multi-node, v1.35

## 8F protocol

1. Read partner-listing-builder/ (gold)
2. Read kinds_meta.json (add 3 new kinds if missing)
3. Read N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md (spec citations)
4. For each kind x 13 ISOs: clone gold, inject manifest-specific content
5. Compile + Validate + Fix FAILs
6. Commit: `git add archetypes/builders/{agents-md,mcp-app-extension,kubernetes-ai-requirement}-builder/ && git commit -m "[N03] WAVE7: 3 dev-manifest kinds (39 ISOs) -- AGENTS.md+MCP-Apps+KAR"`

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
```
