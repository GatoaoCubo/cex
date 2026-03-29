---
kind: tools
id: bld_tools_checkpoint
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for checkpoint production
---

# Tools: checkpoint-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing checkpoint artifacts and workflow refs in pool | Phase 1 (check duplicates, find workflow_ref) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, checkpoint kind |
| CEX Examples | P12_orchestration/examples/ | Real checkpoint artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_checkpoint |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Workflow artifacts | P12_orchestration/examples/p12_wf_*.md | workflow_ref lookup |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `p12_ck_`, workflow_ref non-empty,
step non-empty, tags includes "checkpoint", body has 4 sections, body <= 2048 bytes, quality == null.
## workflow_ref Lookup
Before composing, verify the workflow_ref exists:
1. Search pool: `brain_query("workflow {domain_keyword}")`
2. Check: `cex/P12_orchestration/examples/p12_wf_{slug}.md`
3. If workflow artifact does not exist yet: use provisional id and add comment noting dependency
