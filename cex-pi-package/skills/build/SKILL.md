---
description: "Build a CEX artifact via 8F pipeline. Usage: /build <intent>"
---

# /build

You are executing the CEX 8F pipeline. Follow these phases:

## F1 CONSTRAIN
Resolve the user's intent to: kind, pillar, schema.
Read `.cex/kinds_meta.json` to find the matching kind.

## F2 BECOME
Load the builder: `archetypes/builders/{kind}-builder/` (13 ISOs).

## F3 INJECT
Load context: KC, examples, brand config, memory, similar artifacts.

## F4 REASON
Plan the artifact. If subjective decisions needed, ask the user (GDP).

## F5 CALL
Use tools to enrich: search existing artifacts, check memory, load brand.

## F6 PRODUCE
Generate the artifact with complete YAML frontmatter. quality: null (never self-score).

## F7 GOVERN
Check against quality gate. If below 8.0, revise.

## F8 COLLABORATE
Save, compile (`python _tools/cex_compile.py <path>`), commit, signal.
