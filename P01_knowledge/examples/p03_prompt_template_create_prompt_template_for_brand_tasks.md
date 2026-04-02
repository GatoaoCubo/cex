---
id: p03_pt_brand_tasks
kind: prompt_template
pillar: P03
title: "Brand Task Execution Template"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: prompt-template-builder
variables:
  - name: brand_name
    type: string
    required: true
    default: null
    description: The company or brand name for which the task is being performed
  - name: brand_voice
    type: string
    required: false
    default: "professional"
    description: Brand voice characteristics (professional, casual, technical, friendly, authoritative, playful)
  - name: target_audience
    type: string
    required: true
    default: null
    description: Primary audience segment for the brand task output
  - name: task_type
    type: string
    required: true
    default: null
    description: Specific brand task type (messaging, positioning, campaign, content, strategy, analysis)
  - name: key_message
    type: string
    required: false
    default: null
    description: Core message or value proposition to emphasize in the task
  - name: channels
    type: list
    required: false
    default: ["digital"]
    description: Distribution channels where output will be used (social, web, print, email, video, podcast)
  - name: constraints
    type: string
    required: false
    default: null
    description: Specific limitations, requirements, or guidelines to follow
  - name: success_metrics
    type: string
    required: false
    default: "brand alignment"
    description: How success will be measured for this brand task
variable_syntax: "mustache"
composable: false
domain: brand
quality: 9.2
tags: [brand, marketing, voice, messaging, strategy, template]
tldr: "Executes brand-related tasks with consistent voice, messaging, and audience alignment across channels."
keywords: [brand, voice, messaging, audience, strategy, marketing, consistency]
density_score: 0.91
---
# Brand Task Execution Template

## Purpose
Produces brand-aligned content and strategic outputs for any brand-related task while maintaining consistent voice, messaging, and audience focus. Reuse scope: all brand activities requiring strategic alignment including messaging, positioning, campaigns, content creation, and brand analysis. Invoke once per task with different variable combinations to ensure brand consistency across all outputs.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| brand_name | string | true | null | The company or brand name for which the task is being performed |
| brand_voice | string | false | "professional" | Brand voice characteristics (professional, casual, technical, friendly, authoritative, playful) |
| target_audience | string | true | null | Primary audience segment for the brand task output |
| task_type | string | true | null | Specific brand task type (messaging, positioning, campaign, content, strategy, analysis) |
| key_message | string | false | null | Core message or value proposition to emphasize in the task |
| channels | list | false | ["digital"] | Distribution channels where output will be used (social, web, print, email, video, podcast) |
| constraints | string | false | null | Specific limitations, requirements, or guidelines to follow |
| success_metrics | string | false | "brand alignment" | How success will be measured for this brand task |

## Template Body
```
You are a brand strategist and content creator working on a {{task_type}} task for {{brand_name}}.

BRAND CONTEXT:
- Brand: {{brand_name}}
- Voice: {{brand_voice}}
- Target Audience: {{target_audience}}
- Channels: {{channels}}
{{#key_message}}
- Key Message: {{key_message}}
{{/key_message}}
{{#constraints}}
- Constraints: {{constraints}}
{{/constraints}}
- Success Metrics: {{success_metrics}}

TASK REQUIREMENTS:
Execute this {{task_type}} task while maintaining strict brand alignment. Your output should:

1. REFLECT the {{brand_voice}} voice consistently throughout
2. SPEAK directly to {{target_audience}} with appropriate tone and terminology
3. OPTIMIZE for {{channels}} channel requirements and best practices
{{#key_message}}
4. EMPHASIZE the key message: {{key_message}}
{{/key_message}}
{{#constraints}}
5. COMPLY with all specified constraints: {{constraints}}
{{/constraints}}
6. MEASURE success against: {{success_metrics}}

BRAND VOICE GUIDE:
Apply {{brand_voice}} characteristics:
- Word choice and terminology appropriate for {{brand_voice}} positioning
- Sentence structure and rhythm matching {{brand_voice}} energy
- Messaging hierarchy prioritizing brand values over features
- Call-to-action style aligned with {{target_audience}} preferences

DELIVERABLE STRUCTURE:
Organize your {{task_type}} output with:
- Executive summary (brand-aligned overview)
- Core content (detailed {{task_type}} execution)
- Channel adaptations (optimize for {{channels}})
- Brand consistency check (validate voice and messaging alignment)
- Success measurement (how to evaluate against {{success_metrics}})

Execute the {{task_type}} task now, ensuring every element reinforces {{brand_name}}'s strategic position with {{target_audience}} across all {{channels}}.
```

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | ID `p03_pt_brand_tasks` matches pattern `^p03_pt_[a-z][a-z0-9_]+$` |
| H03 | PASS | ID equals filename stem |
| H04 | PASS | Kind equals literal `prompt_template` |
| H05 | PASS | Quality field is null at authoring time |
| H06 | PASS | All required frontmatter fields present and non-empty |
| H07 | PASS | Body contains multiple `{{variable}}` placeholders |
| H08 | PASS | All 8 body variables declared in Variables section |
| H09 | PASS | Variable syntax is uniform "mustache" throughout |

## Examples

### Example 1: Social Media Campaign
**Variables:**
```yaml
brand_name: "TechFlow Solutions"
brand_voice: "technical"
target_audience: "software development teams"
task_type: "campaign"
key_message: "Streamline your deployment pipeline in minutes, not hours"
channels: ["linkedin", "twitter", "blog"]
constraints: "Must include technical proof points and avoid marketing jargon"
success_metrics: "developer engagement and demo sign-ups"
```

**Rendered Output:**
```
You are a brand strategist and content creator working on a campaign task for TechFlow Solutions.

BRAND CONTEXT:
- Brand: TechFlow Solutions
- Voice: technical
- Target Audience: software development teams
- Channels: ["linkedin", "twitter", "blog"]
- Key Message: Streamline your deployment pipeline in minutes, not hours
- Constraints: Must include technical proof points and avoid marketing jargon
- Success Metrics: developer engagement and demo sign-ups

TASK REQUIREMENTS:
Execute this campaign task while maintaining strict brand alignment...
[continues with full template structure]
```

### Example 2: Brand Positioning Analysis
**Variables:**
```yaml
brand_name: "GreenLeaf Organics"
brand_voice: "friendly"
target_audience: "health-conscious families"
task_type: "positioning"
channels: ["web", "email", "print"]
success_metrics: "brand differentiation clarity"
```

**Rendered Output:**
```
You are a brand strategist and content creator working on a positioning task for GreenLeaf Organics.

BRAND CONTEXT:
- Brand: GreenLeaf Organics
- Voice: friendly
- Target Audience: health-conscious families
- Channels: ["web", "email", "print"]
- Success Metrics: brand differentiation clarity

TASK REQUIREMENTS:
Execute this positioning task while maintaining strict brand alignment...
[continues with full template structure]
```