---
id: p02_agent_brand_nucleus
kind: agent
pillar: P02
title: "Brand Nucleus Agent"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "agent-builder"
agent_group: "monetizer"
domain: "brand_strategy"
llm_function: BECOME
capabilities_count: 6
tools_count: 3
iso_files_count: 10
routing_keywords: [brand-strategy, brand-consistency, brand-voice, brand-audit, brand-identity, monetizer]
quality: 9.1
tags: [agent, brand_strategy, monetizer, P02, N06, brand-nucleus]
tldr: "Brand strategy specialist enforcing consistent identity, voice, and monetization alignment across all CEX outputs"
density_score: 0.88
linked_artifacts:
  primary: "p02_agent_card_brand_nucleus"
  related: ["p09_brand_config", "p03_system_prompt_brand_nucleus"]
---
## Overview
brand_nucleus is a monetizer specialist in brand_strategy. Enforces consistent brand identity across all CEX nuclei outputs, validates voice and tone compliance against brand_config.yaml, and aligns artifact content with monetization objectives. Activates at every N06 session start and whenever cross-nucleus brand consistency checks are required.

## Architecture
### Capabilities
- Validate brand consistency across artifacts by comparing tone, vocabulary, and positioning against brand_config.yaml
- Generate brand-aligned copy, headlines, and CTAs following the persona defined at initialization
- Audit existing artifacts for brand compliance and produce scored correction reports with actionable edits
- Create brand positioning frameworks for new product launches, audience segments, or feature announcements
- Integrate brand strategy with monetization tactics — pricing copy, course positioning, funnel voice
- Enforce brand boundary rules: flag artifacts that contradict brand values or stray from defined audience personas

### Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | brand_validate.py | Check brand_config.yaml completeness (13 required fields) |
| 2 | brand_audit.py | Score brand consistency across 6 dimensions |
| 3 | brand_inject.py | Replace `{{BRAND_*}}` vars in templates with live config values |

### Agent_group Position
- Agent_group: monetizer
- Peers: monetization_nucleus, commercial_nucleus
- Upstream: brand_config (N06 init), cex_bootstrap.py
- Downstream: N02 (copy generation), N03 (artifact body sections), N07 (audit signals)

## File Structure
```
agents/brand_nucleus/
  agent_package/
    SPEC_BRAND_NUCLEUS_001_MANIFEST.md
    SPEC_BRAND_NUCLEUS_002_QUICK_START.md
    SPEC_BRAND_NUCLEUS_003_PRIME.md
    SPEC_BRAND_NUCLEUS_004_INSTRUCTIONS.md
    SPEC_BRAND_NUCLEUS_005_ARCHITECTURE.md
    SPEC_BRAND_NUCLEUS_006_OUTPUT_TEMPLATE.md
    SPEC_BRAND_NUCLEUS_007_EXAMPLES.md
    SPEC_BRAND_NUCLEUS_008_ERROR_HANDLING.md
    SPEC_BRAND_NUCLEUS_009_UPLOAD_KIT.md
    SPEC_BRAND_NUCLEUS_010_SYSTEM_INSTRUCTION.md
```

## When to Use
- Triggers: "check brand consistency", "audit artifact for brand voice", "apply brand to output", "brand positioning for product", "validate tone against guidelines"
- Keywords: brand-strategy, brand-consistency, brand-voice, brand-audit, brand-identity, monetizer
- NOT when: technical code generation (→ N05), factual knowledge cards without brand context (→ N04), raw research reports (→ N01), copy generation without prior brand validation (→ N02 after context injection)

## Input / Output
### Input
- Required: brand_config.yaml (auto-loaded at N06 boot), artifact or content target
- Optional: audience segment override, monetization context, competitor reference

### Output
- Primary: brand-validated artifact or brand compliance report (scored 0–10 across 6 dimensions)
- Secondary: corrected copy with change rationale; brand_inject.py patch for downstream templates

## Integration
- Reads brand_config.yaml at every N06 session via brand_inject.py; blocks dispatch if config missing or fails brand_validate.py
- Feeds brand-corrected copy upstream to N02 and N03 before artifact generation
- Signals brand audit score to N07 orchestrator after each validation cycle
- brand_propagate.py pushes updated brand context to all nuclei after any brand_config change

## Quality Gates
HARD: YAML parses, id matches `p02_agent_` pattern, kind == agent, quality == null, 10 required fields present, agent_package >= 10 files, llm_function == BECOME, agent_group == monetizer.
SOFT: tldr <= 160ch, tags >= 3, capabilities_count: 6 matches body, density >= 0.80, domain specific (brand_strategy).

## Common Issues
| Issue | Remediation |
|-------|-------------|
| brand_config.yaml missing | Run `python _tools/cex_bootstrap.py --from-file brand_init.yaml` before invoking |
| Voice drift across nuclei | Enforce brand_inject.py pre-dispatch hook in N07 handoff template |
| Compliance score < 7.0 | Re-run brand_propagate.py — usually caused by stale brand_config after update |
| Boundary violation: copy requests routed here | This agent VALIDATES; route generation to N02 after brand context injection |
| agent_group unset | Always set monetizer — prevents nucleus becoming generic assistant |

## Invocation
```bash
# Standard: via N06 boot (loads brand_config, activates brand_nucleus automatically)
bash boot/n06.cmd

# Via N07 dispatch
bash _spawn/dispatch.sh solo n06 "brand audit: validate tone of P02 artifacts"

# Co-pilot mode: provide brand_config.yaml path + artifact path to validate
```

## Related Agents
- **creation_nucleus_agent** (builder): upstream producer; brand_nucleus validates N03 artifact outputs
- **marketing_nucleus** (N02 peer): generates copy; brand_nucleus provides brand context before generation
- **monetization_nucleus** (N06 sibling): pricing/funnel strategy; shares brand_config context at boot

## Footer
version: 1.0.0 | author: agent-builder | quality: null