---
id: kc_multimodal_prompt
kind: knowledge_card
type: kind
pillar: P03
title: "Multimodal Prompt -- Deep Knowledge for multimodal_prompt"
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: n03_builder
domain: multimodal_prompt
quality: 9.1
tags: [multimodal_prompt, P03, INJECT, kind-kc, vision, audio]
tldr: "Cross-modal prompt pattern that interleaves text with vision, audio, or video inputs in a single structured request"
when_to_use: "Building, reviewing, or reasoning about multimodal_prompt artifacts"
keywords: [multimodal, vision, audio, image-prompt, content-blocks]
feeds_kinds: [multimodal_prompt]
density_score: 0.95
linked_artifacts:
  primary: null
  related: [action_prompt, prompt_template, multi_modal_config, vision_tool, audio_tool]
---

# Multimodal Prompt

## Spec
```yaml
kind: multimodal_prompt
pillar: P03
llm_function: INJECT
max_bytes: 4096
naming: p03_mmp_{{name}}.md
core: false
```

## What It Is
A multimodal_prompt is a prompt that interleaves text with non-text modalities (images, audio clips, video frames, PDFs) inside a single ordered request to a vision-language or omni model. Each input is a typed content block; order and positioning relative to text carry semantic weight. It is distinct from multi_modal_config (which selects model capabilities and codecs) and from vision_tool/audio_tool (which are runtime capabilities agents call). A multimodal_prompt is the message payload itself.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| OpenAI | `content: [{type:"text"}, {type:"image_url"}, {type:"input_audio"}]` | Typed content blocks array |
| Anthropic | `content: [{type:"text"}, {type:"image", source:{...}}]` | Base64 or URL image blocks, order-sensitive |
| Google Gemini | `Part.text`, `Part.inline_data(mime_type, data)`, `Part.file_data` | Parts list passed to `generate_content` |
| LangChain | `HumanMessage(content=[{"type":"text"...},{"type":"image_url"...}])` | Mirrors OpenAI schema |
| LlamaIndex | `ImageDocument` + `MultiModalLLM.complete(prompt, image_documents=...)` | Separate text + image doc channels |
| CrewAI | `Task` with attached files / vision tool outputs | Modality routed via tool, not task payload |
| Vertex AI | `Content(parts=[Part.from_text(...), Part.from_uri(...)])` | URI references for GCS-hosted media |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| modalities | list[str] | ["text"] | More modalities = richer grounding but higher cost and stricter model requirements |
| block_order | "text_first" \| "media_first" \| "interleaved" | "interleaved" | Media-first anchors attention on visual evidence; text-first biases toward instruction |
| media_encoding | "base64" \| "url" \| "file_id" | "base64" | Base64 inflates tokens ~33%; URL requires fetch cost; file_id best for reuse |
| detail_level | "low" \| "high" \| "auto" | "auto" | High = more vision tokens, better OCR; low = 85 tokens/image fixed |
| max_media_items | int | 10 | More items = better context; diminishing returns past ~20, context blowout past 100 |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Single-image grounding | OCR, chart reading, diagram Q&A | "Extract the table from this chart: [image]" |
| Before-and-after comparison | UI regression, medical imaging, diffs | "[image_a] [image_b] What changed?" |
| Visual chain-of-thought | Multi-step reasoning over images | "Step 1: identify objects. Step 2: [image]. Step 3: reason." |
| Audio transcription + analysis | Meeting notes, sentiment, speaker ID | "Transcribe and summarize: [audio]" |
| Frame sampling | Video understanding on non-video models | Sample N frames, send as image sequence |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Sending many high-detail images without need | Burns vision tokens, hits context cap | Use detail="low" when layout is simple |
| Putting text after all media blocks | Instruction lost to recency bias | Place instruction first, then evidence, then repeat instruction |
| Mixing modalities the model doesn't support | Silent downgrade or error | Gate on multi_modal_config capabilities before dispatch |
| Base64 inside prompt caching | Cache miss on every call | Use file_id / URL refs for reusable assets |

## Integration Graph
```
[multi_modal_config] --> [multimodal_prompt] --> [chain | action_prompt]
                                 |
                          [vision_tool | audio_tool]
```

## Decision Tree
- IF input is text-only THEN use action_prompt, not multimodal_prompt
- IF model lacks vision/audio capability THEN use a tool call (vision_tool) instead
- IF the same media is reused across calls THEN use file_id or URL to enable prompt_cache hits
- IF media count > 20 THEN chunk into multiple turns or preprocess with a retriever
- DEFAULT: interleaved blocks, detail="auto", instruction first and last

## Quality Criteria
- GOOD: Typed content blocks, explicit modality list, fits under 4096 bytes of prompt spec
- GREAT: Includes detail_level rationale, cache strategy, fallback for non-multimodal models
- FAIL: Raw base64 dumped in text; no modality declaration; exceeds model media cap; instruction buried between media blocks
