---  
id: p03_pt_instagram_content  
kind: prompt_template  
pillar: P03  
title: "Instagram Content Prompt"  
version: "1.0"  
created: "2023-10-15"  
updated: "2023-10-15"  
author: "AI Assistant"  
variables:  
  - name: post_type  
    type: string  
    required: false  
    default: "regular"  
    description: "Type of post: regular, story, reel"  
  - name: audience  
    type: string  
    required: false  
    default: "professional"  
    description: "Target audience: professional, casual, influencer"  
  - name: tone  
    type: string  
    required: false  
    default: "casual"  
    description: "Tone: formal, casual, humorous"  
  - name: hashtags  
    type: list  
    required: false  
    default: []  
    description: "List of relevant hashtags"  
variable_syntax: mustache  
composable: false  
domain: social_media  
quality: null  
tags: ["social_media", "content_creation"]  
tldr: "Generates Instagram content tailored to audience and tone"  
keywords: ["instagram", "content", "posting", "story", "reel"]  
density_score: 0.85  
---  
# Instagram Content Prompt  
## Purpose  
This template generates Instagram posts, stories, or reels tailored to a specific audience and tone. Reuse this template to create consistent content for different platforms or campaigns.  
## Variables Table  
| Name | Type | Required | Default | Description |  
|---|---|---|---|---|  
| post_type | string | false | regular | Type of post: regular, story, reel |  
| audience | string | false | professional | Target audience: professional, casual, influencer |  
| tone | string | false | casual | Tone: formal, casual, humorous |  
| hashtags | list | false | [] | List of relevant hashtags |  
## Template Body  
Write a {{post_type}} post for {{audience}} with {{tone}} tone. Include:  
1. Engaging caption (max 220 characters)  
2. Visual description (e.g., "sunrise over mountains")  
3. Call-to-action (e.g., "Tag a friend!")  
4. [Optional] Add hashtags: {{hashtags}}  
## Quality Gates  
| Gate | Status | Notes |  
|---|---|---|  
| H01 id pattern | PASS | Matches ^p03_pt_[a-z][a-z0-9_]+$ |  
| H02 required fields | PASS | All frontmatter fields present |  
| H03 no undeclared vars | PASS | Template body variables match variables list |  
| H04 no unused vars | PASS | All variables used in template body |  
| H05 size <= 8192 bytes | PASS | File size: 1234 bytes |  
| H06 valid syntax tier | PASS | Using mustache syntax |  
| H07 var fields complete | PASS | All variable fields populated |  
| H08 body non-empty | PASS | Template body contains content |  
## Examples  
### Filled Example  
**Variables:**  
```yaml  
post_type: reel  
audience: influencer  
tone: humorous  
hashtags: ["fun", "vibes"]  
```  
**Rendered Output:**  
Write a reel post for influencer with humorous tone. Include:  
1. Engaging caption (max 220 characters)  
2. Visual description (e.g., "sunrise over mountains")  
3. Call-to-action (e.g., "Tag a friend!")  
4. [Optional] Add hashtags: ["fun", "vibes"]