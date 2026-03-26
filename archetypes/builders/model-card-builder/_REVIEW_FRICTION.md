# Production Friction Report - model-card-builder
## Date: 2026-03-26
## Reviewer: CODEX
## Artifact produced: p02_mc_google_gemini_2_5_pro.md
## Production time: ~25 min
## Quality self-assessment: DO NOT SCORE (quality: null rule)

## FRICTION LOG (chronological)
1. [10:05 -03] Reading the 13 builder files - the builder is consistent on structure, but `OUTPUT_TEMPLATE.md`, `SCHEMA.md`, and `QUALITY_GATES.md` are not fully aligned on what must exist in the body versus frontmatter.
2. [10:08 -03] Running Phase 1 research - `TOOLS.md` says to use `brain_query`, but no direct workflow or command example is provided, so I used a repository search to confirm there was no existing Gemini 2.5 Pro card.
3. [10:11 -03] Reading `OUTPUT_TEMPLATE.md` - the template forces a `Provider` row with source `-`, which conflicts with the system rule that every data point must cite a source URL.
4. [10:13 -03] Researching Google docs - the model page provides exact token limits and capabilities, but not a formal `release_date`; I had to infer `2025-06-17` from the release notes entry where stable `gemini-2.5-pro` was announced.
5. [10:15 -03] Filling pricing - Google pricing is split by prompt size (`<= 200K` and `> 200K`) and has separate cache/storage concepts, while the schema wants one `input`, one `output`, one `cache_read`, and one `cache_write`.
6. [10:17 -03] Filling `cache_write` - Google context caching docs do not expose an Anthropic-style cache write price in `per_1M_tokens`; I set `cache_write: null` instead of inventing a number with the wrong unit.
7. [10:19 -03] Filling `fine_tunable` - the schema requires a boolean, but the feature is absent from the model page; I had to use the changelog plus the fine-tuning shutdown notice to justify `false`.
8. [10:21 -03] Validating quality gates - `QUALITY_GATES.md` says to "run checks mentally", and `validate_kc.py` is for `knowledge_card`, not `model_card`, so there is no matching automated validator for this builder.
9. [10:23 -03] Final pass - the body size limit in `SCHEMA.md`/`CONFIG.md` is tight for a card that also requires a Source URL in every row, so I compressed explanations aggressively to stay spec-dense.

## TEMPLATE vs SCHEMA MISMATCHES
| Template field | Schema field | Issue |
|---|---|---|
| `## Specifications` includes `Architecture` row | No frontmatter/body schema field named `architecture` | Template demands content the schema never defines formally. |
| `Provider` spec row source is `-` | System prompt says every data point needs a source URL | Template example conflicts with source-citation rule. |
| `pricing.cache_write` | Google pricing exposes cache usage plus storage, not a write-token price | Schema assumes a provider-neutral caching model that does not match Google docs. |
| `provider` enum in template | `provider` enum in `CONFIG.md` | Template lists fewer valid providers than config (`alibaba`, `ai21`, `other` missing). |
| `tldr` pattern uses one price pair | `pricing` object is singular and exact | Template cannot represent tiered pricing cleanly for providers like Google. |

## AMBIGUOUS INSTRUCTIONS
| Instruction | What I did | What I think was intended |
|---|---|---|
| "Read OUTPUT_TEMPLATE.md - follow exactly" | I followed the section layout exactly but replaced `-` with URLs where the builder also requires citation for every data point. | Follow the structure exactly, not every literal placeholder/example token. |
| "If data unavailable: mark field as null, add comment" | I used `null` for `cache_write` and documented the reason in this report because YAML frontmatter comments inside the template would be awkward and no comment field exists. | Allow nulls plus an external friction note when the schema has no place to store the explanation. |
| "Pricing has concrete numbers" | I used the official `<= 200K` tier as the canonical frontmatter value and documented the `> 200K` tier in the body. | The builder probably wants a normalized "base case" price, but it should say how to handle tiered pricing. |
| "Verify each data point against official source" | I used the model page, pricing page, and changelog together because no single Google page holds all required fields. | Multiple official sources are acceptable when one page is incomplete. |

## RECOMMENDATIONS
1. Add a dedicated `validate_model_card.py` so Phase 3 is not "mental only" and does not rely on a KC validator with incompatible gates.
2. Define an explicit policy for tiered pricing: base tier, max tier, min tier, or allow arrays/ranges.
3. Clarify how to map provider-specific caching models into `cache_read` and `cache_write`, or loosen the schema for providers without symmetric cache prices.
4. Add `release_date_source` guidance or allow `release_date: null` without penalty when the model page omits it.
5. Align the provider enum across `OUTPUT_TEMPLATE.md` and `CONFIG.md`.
6. Either formalize `Architecture` in the schema or remove it from the required template.
