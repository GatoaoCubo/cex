---
id: p06_is_builder_specification
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "builder specification format for CEX agent construction"
fields:
  - name: "builder_id"
    type: "string"
    required: true
    default: null
    description: "Unique identifier for the builder (kebab-case)"
    error_message: "builder_id is required - provide kebab-case identifier"
  - name: "kind"
    type: "string"
    required: true
    default: null
    description: "Type of builder (e.g., type_builder, content_builder)"
    error_message: "kind is required - specify builder type"
  - name: "pillar"
    type: "string"
    required: true
    default: null
    description: "Target pillar for output artifacts (P01-P12)"
    error_message: "pillar is required - specify target pillar P01-P12"
  - name: "domain"
    type: "string"
    required: true
    default: null
    description: "Specialized domain or focus area"
    error_message: "domain is required - specify builder's domain"
  - name: "capabilities"
    type: "list"
    required: true
    default: null
    description: "List of builder capabilities and specializations"
    error_message: "capabilities is required - list what this builder can do"
  - name: "keywords"
    type: "list"
    required: true
    default: null
    description: "Keywords for routing and discovery"
    error_message: "keywords is required - provide routing keywords"
  - name: "triggers"
    type: "list"
    required: false
    default: []
    description: "Natural language patterns that trigger this builder"
    error_message: null
  - name: "crew_role"
    type: "string"
    required: true
    default: null
    description: "Role when working in crews (specialist, generalist, coordinator)"
    error_message: "crew_role is required - define crew collaboration role"
  - name: "geo_description"
    type: "string"
    required: false
    default: "Multi-level description for global routing"
    description: "L1/L2/L3 tiered description for geographic routing"
    error_message: null
  - name: "version"
    type: "string"
    required: false
    default: "1.0.0"
    description: "Semantic version of the builder specification"
    error_message: null
  - name: "parent"
    type: "string"
    required: false
    default: null
    description: "Parent builder if this inherits from another"
    error_message: null
  - name: "llm_function"
    type: "string"
    required: false
    default: "BECOME"
    description: "Primary LLM function (BECOME, REASON, INJECT, etc.)"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Convert comma-separated string to list of strings"
  - from: "string"
    to: "string"
    rule: "Trim whitespace and normalize case for identifiers"
examples:
  - {
      builder_id: "knowledge-card-builder",
      kind: "content_builder",
      pillar: "P01",
      domain: "knowledge_management",
      capabilities: ["create knowledge cards", "structure domain expertise", "generate reference materials"],
      keywords: ["knowledge", "card", "reference", "domain"],
      triggers: ["create knowledge card about", "document expertise in"],
      crew_role: "specialist",
      geo_description: "L1: Knowledge card specialist. L2: Creates structured reference materials. L3: Documents domain expertise.",
      version: "1.0.0"
    }
  - {
      builder_id: "system-prompt-builder",
      kind: "prompt_builder", 
      pillar: "P03",
      domain: "prompt_engineering",
      capabilities: ["craft system prompts", "define agent behavior", "set operational constraints"],
      keywords: ["system", "prompt", "behavior", "constraints"],
      crew_role: "specialist"
    }
domain: "builder-specification"
quality: 8.9
tags: [input-schema, builder-specification, cex-agents, P06]
tldr: "Input contract for builder specs: requires identity, capabilities, routing, crew role for CEX agent construction"
density_score: 0.91
---
# Contract Definition
Builder specifications define the structure and behavior of CEX agent builders. This input schema specifies what data must be provided to create a valid builder specification that can be used for agent construction and routing within the CEX system.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | builder_id | string | YES | - | Unique identifier for the builder (kebab-case) |
| 2 | kind | string | YES | - | Type of builder (e.g., type_builder, content_builder) |
| 3 | pillar | string | YES | - | Target pillar for output artifacts (P01-P12) |
| 4 | domain | string | YES | - | Specialized domain or focus area |
| 5 | capabilities | list | YES | - | List of builder capabilities and specializations |
| 6 | keywords | list | YES | - | Keywords for routing and discovery |
| 7 | triggers | list | NO | [] | Natural language patterns that trigger this builder |
| 8 | crew_role | string | YES | - | Role when working in crews (specialist, generalist, coordinator) |
| 9 | geo_description | string | NO | "Multi-level description for global routing" | L1/L2/L3 tiered description for geographic routing |
| 10 | version | string | NO | "1.0.0" | Semantic version of the builder specification |
| 11 | parent | string | NO | null | Parent builder if this inherits from another |
| 12 | llm_function | string | NO | "BECOME" | Primary LLM function (BECOME, REASON, INJECT, etc.) |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Convert comma-separated string to list of strings |
| string | string | Trim whitespace and normalize case for identifiers |

## Examples
```json
{
  "builder_id": "knowledge-card-builder",
  "kind": "content_builder",
  "pillar": "P01", 
  "domain": "knowledge_management",
  "capabilities": ["create knowledge cards", "structure domain expertise", "generate reference materials"],
  "keywords": ["knowledge", "card", "reference", "domain"],
  "triggers": ["create knowledge card about", "document expertise in"],
  "crew_role": "specialist",
  "geo_description": "L1: Knowledge card specialist. L2: Creates structured reference materials. L3: Documents domain expertise.",
  "version": "1.0.0"
}
```

## References
- CEX Builder Architecture: `archetypes/builders/` directory structure
- Pillar System: P01-P12 classification schema
- Crew Collaboration: `.claude/rules/` collaboration patterns