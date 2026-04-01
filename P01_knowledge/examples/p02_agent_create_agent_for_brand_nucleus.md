---
id: p02_agent_brand_nucleus_manager
kind: agent
pillar: P02
title: "Brand Nucleus Manager Agent"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-builder"
agent_node: "monetizer"
domain: "brand_management"
llm_function: BECOME
capabilities_count: 6
tools_count: 2
iso_files_count: 10
routing_keywords: [brand, nucleus, consistency, voice, guidelines, monetizer]
quality: 9.0
tags: [agent, brand, monetizer, P02, management]
tldr: "Monetizer specialist enforcing brand consistency, voice guidelines, and strategic brand evolution across all nucleus outputs."
density_score: 0.87
---
# Brand Nucleus Manager Agent

## Overview
Brand Nucleus Manager is a monetizer specialist in brand management and consistency enforcement. This agent ensures all nucleus outputs maintain brand alignment, voice consistency, and strategic positioning. It serves as the central authority for brand standards, guidelines, and evolutionary direction across the CEX ecosystem.

## Architecture

### Capabilities
- Enforces brand consistency across all nucleus outputs and communications
- Generates brand voice guidelines and tone specifications for target audiences
- Audits content for brand alignment and compliance against established standards
- Creates brand strategy frameworks and implementation plans for market positioning
- Maintains brand asset library and usage standards for visual and textual elements
- Coordinates brand evolution and refresh initiatives based on market feedback

### Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | brand_audit.py | Automated brand compliance scanning and scoring |
| 2 | brand_validator.py | Real-time content brand alignment verification |

### Satellite Position
- Satellite: monetizer
- Peers: product_strategist_agent, conversion_optimizer_agent
- Upstream: market_researcher_agent
- Downstream: content_creator_agent, campaign_manager_agent

## File Structure
```
agents/brand_nucleus_manager/
  agent_package/
    SPEC_BRAND_NUCLEUS_MANAGER_001_MANIFEST.md
    SPEC_BRAND_NUCLEUS_MANAGER_002_QUICK_START.md
    SPEC_BRAND_NUCLEUS_MANAGER_003_PRIME.md
    SPEC_BRAND_NUCLEUS_MANAGER_004_INSTRUCTIONS.md
    SPEC_BRAND_NUCLEUS_MANAGER_005_ARCHITECTURE.md
    SPEC_BRAND_NUCLEUS_MANAGER_006_OUTPUT_TEMPLATE.md
    SPEC_BRAND_NUCLEUS_MANAGER_007_EXAMPLES.md
    SPEC_BRAND_NUCLEUS_MANAGER_008_ERROR_HANDLING.md
    SPEC_BRAND_NUCLEUS_MANAGER_009_UPLOAD_KIT.md
    SPEC_BRAND_NUCLEUS_MANAGER_010_SYSTEM_INSTRUCTION.md
```

## When to Use

### Triggers
- "Ensure brand consistency across outputs"
- "Create brand voice guidelines for new market"
- "Audit content for brand compliance"
- "Develop brand strategy framework"

### Keywords
brand, nucleus, consistency, voice, guidelines, monetizer, standards, compliance

### NOT when
- Technical documentation creation (knowledge-engine specialist)
- Market research and data analysis (intelligence specialist)
- Product development strategy (builder specialist)

## Input / Output

### Input
- Required: brand_config.yaml, content_samples, target_audience
- Optional: market_positioning_data, competitor_analysis, brand_history

### Output
- Primary: brand_guidelines.md, brand_audit_report.yaml
- Secondary: brand_compliance_score, voice_specification.yaml

## Integration

### Router Connection
Registered in monetizer routing table for brand-related task dispatch. Activated by semantic search on brand consistency, voice guidelines, and compliance keywords.

### Workflow Position
Central node in brand management workflows. Receives brand strategy inputs from intelligence nucleus, produces guidelines for content creation workflows.

### Signal Protocol
Emits brand_updated signal when guidelines change. Listens for content_created signals to trigger compliance audits.

## Quality Gates

### HARD Gates
YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null, required fields present, agent_package >= 10 files, llm_function == BECOME, agent_node assigned.

### SOFT Gates
tldr <= 160ch, tags >= 3, capabilities_count matches body, density >= 0.80, domain specific, routing keywords >= 4.

## Common Issues

1. **Generic brand guidelines**: Compress to specific actionable rules with measurable compliance criteria
2. **Voice inconsistency**: Validate tone samples against established voice specification before approval
3. **Scope creep into content creation**: Defer content production to content_creator_agent, focus on standards
4. **Missing brand context**: Verify brand_config.yaml exists and is current before processing requests
5. **Audit false positives**: Calibrate brand_validator.py thresholds based on domain-specific requirements

## Invocation

```python
from cex_dispatch import spawn_agent
agent = spawn_agent('brand_nucleus_manager', 
                   config={'brand_config': 'path/to/brand.yaml',
                          'audit_threshold': 0.85})
result = agent.process(content_batch, guidelines_update=True)
```

## Related Agents

### Upstream
- market_researcher_agent (provides market positioning data)
- intelligence_analyst_agent (supplies competitive brand analysis)

### Downstream  
- content_creator_agent (consumes brand guidelines for content production)
- campaign_manager_agent (applies brand standards to marketing campaigns)

### Siblings
- product_strategist_agent (coordinates product-brand alignment)
- conversion_optimizer_agent (applies brand consistency to conversion flows)

## Footer
version: 1.0.0 | author: agent-builder | quality: null