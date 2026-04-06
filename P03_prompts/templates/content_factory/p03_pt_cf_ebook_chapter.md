---
id: p03_pt_cf_ebook_chapter
kind: prompt_template
pillar: P03
title: "Content Factory — eBook Chapter Template"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
variables:
  - name: BRAND_NAME
    type: string
    required: true
    default: null
    description: "Company or brand name"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Brand tone descriptor"
  - name: CONTENT_TOPIC
    type: string
    required: true
    default: null
    description: "Chapter subject"
  - name: CONTENT_CHAPTER_TITLE
    type: string
    required: true
    default: null
    description: "Title of this chapter"
  - name: CONTENT_CHAPTER_NUMBER
    type: integer
    required: true
    default: null
    description: "Chapter number in the book sequence"
  - name: CONTENT_BOOK_TITLE
    type: string
    required: true
    default: null
    description: "Title of the full book for consistency"
  - name: CONTENT_KEY_POINTS
    type: list
    required: true
    default: null
    description: "3-6 key points this chapter must cover"
  - name: CONTENT_WORD_COUNT
    type: integer
    required: false
    default: 3000
    description: "Target word count for the chapter"
  - name: TARGET_AUDIENCE
    type: string
    required: true
    default: null
    description: "Reader persona and knowledge level"
variable_syntax: mustache
composable: true
domain: content_factory
quality: null
tags: [prompt_template, ebook, chapter, writing, content_factory, P03]
tldr: "Reusable mold for generating ebook chapters with intro-body-examples-summary-exercises structure"
keywords: [ebook chapter, livro, escrita, book, content factory, writing]
density_score: 0.90
---

# eBook Chapter Template

## Purpose
Generates a complete ebook chapter from a content brief. The output follows a pedagogical writing structure: intro-body-examples-summary-exercises optimized for digital reading. Designed to feed into Pandoc compilation (md to EPUB/PDF) in the Content Factory pipeline.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | — | Company or brand name |
| BRAND_VOICE | string | yes | — | Tone descriptor |
| CONTENT_TOPIC | string | yes | — | Chapter subject |
| CONTENT_CHAPTER_TITLE | string | yes | — | Chapter title |
| CONTENT_CHAPTER_NUMBER | integer | yes | — | Sequence number |
| CONTENT_BOOK_TITLE | string | yes | — | Book title |
| CONTENT_KEY_POINTS | list | yes | — | 3-6 key points |
| CONTENT_WORD_COUNT | integer | no | 3000 | Target words |
| TARGET_AUDIENCE | string | yes | — | Reader persona |

## Template Body

```
You are a technical writer for {{BRAND_NAME}}. Write in a {{BRAND_VOICE}} tone.

BOOK: {{CONTENT_BOOK_TITLE}}
CHAPTER {{CONTENT_CHAPTER_NUMBER}}: {{CONTENT_CHAPTER_TITLE}}
AUDIENCE: {{TARGET_AUDIENCE}}
WORD COUNT: {{CONTENT_WORD_COUNT}} words

Write a chapter covering:
{{CONTENT_KEY_POINTS}}

## OUTPUT FORMAT

# Chapter {{CONTENT_CHAPTER_NUMBER}}: {{CONTENT_CHAPTER_TITLE}}

## Introduction (10% of word count)
- Opening hook: Connect {{CONTENT_TOPIC}} to a real-world problem or scenario
- Chapter promise: "In this chapter, you will learn..."
- Connection: How this builds on previous chapters in {{CONTENT_BOOK_TITLE}}

## [Section per key point] (65% of word count total)
For EACH item in {{CONTENT_KEY_POINTS}}:

### [Key Point as Section Title]
- **Explanation**: Core concept in accessible language (2-3 paragraphs)
- **Example**: Concrete, relatable example with enough detail to be actionable
- **Code/Data** (if applicable): Formatted code block or table
- **Callout Box**: One "Pro Tip" or "Common Mistake" per section

## Summary (10% of word count)
- Bullet-point recap of each key point (one sentence each)
- Key takeaway: The single most important idea from this chapter

## Exercises (15% of word count)
- 3-5 exercises ranging from comprehension to application
- Each exercise: question + expected difficulty + estimated time
- At least one exercise requires the reader to produce something (not just answer)

## CONSTRAINTS
- Total word count MUST be {{CONTENT_WORD_COUNT}} (+/- 10%)
- Paragraphs max 4 sentences for digital readability
- One concept per subsection — no information overload
- Include transition sentences between sections
- Match {{BRAND_VOICE}} tone — consistent with other chapters
- Use Markdown formatting (headers, bold, code blocks, callouts)
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^p03_pt_[a-z][a-z0-9_]+$ |
| H02 | PASS | All required frontmatter fields present |
| H03 | PASS | All {{vars}} in body exist in variables list |
| H04 | PASS | All variables in list appear in template body |
| H05 | PASS | File size < 8192 bytes |
| H06 | PASS | variable_syntax is mustache consistently |

## Examples

### Example 1: Chapter on vector databases
Variables:
```yaml
BRAND_NAME: "DataCraft"
BRAND_VOICE: "technical-approachable"
CONTENT_TOPIC: "Vector databases for semantic search"
CONTENT_CHAPTER_TITLE: "Storing and Searching Embeddings"
CONTENT_CHAPTER_NUMBER: 4
CONTENT_BOOK_TITLE: "Building RAG Systems — A Practical Guide"
CONTENT_KEY_POINTS:
  - "What vector databases are and why they matter"
  - "Choosing between Pinecone, Weaviate, and Chroma"
  - "Indexing strategies: HNSW vs IVF"
  - "Hybrid search: combining vectors with keyword filters"
CONTENT_WORD_COUNT: 3000
TARGET_AUDIENCE: "Backend developers building their first RAG pipeline"
```
