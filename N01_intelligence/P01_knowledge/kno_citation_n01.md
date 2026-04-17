---
id: kno_citation_n01
kind: citation
pillar: P01
nucleus: N01
title: "N01 Citation"
version: "1.0.0"
quality: null
tags: [citation, n01, p01, analytical_envy, provenance]
---
<!-- 8F: F1=citation/P01 F2=citation-builder+kc_citation F3=nucleus_def_n01+citation_format_contract+source_quality_contract+kc_citation F4=structured provenance with reliability scoring
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_citation_n01.md -->

# N01 Citation

## Purpose
N01 citations are not decorative footnotes.
They are proof objects used to pressure every claim.
Analytical Envy means a citation must expose whether the source is good enough to beat the competing narrative.
If provenance is weak, the claim stays weak.

## Properties

| Property | Value |
|----------|-------|
| Kind | `citation` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Canonical contract | `citation_format_contract` |
| Reliability contract | `source_quality_contract` |
| Minimum required fields | source, title, url, accessed date, reliability |
| Citation style | APA-lite with operational metadata |
| Preferred source order | primary, official, analyst, media, community |
| Core use | research briefs, market snapshots, competitive matrices |

## Citation Thesis
A citation in N01 must let another analyst answer four questions fast:
1. Where did this come from.
2. When was it true.
3. Why should I trust it.
4. What exact claim does it support.

Any citation that cannot answer those four questions is incomplete.

## Required Field Set

| Field | Required | N01 expectation |
|-------|----------|-----------------|
| source_type | yes | official_doc, paper, filing, media, community, internal |
| title | yes | exact page or document title |
| author_org | yes | person or organization |
| url | yes | direct resolvable locator |
| published_date | yes when known | supports freshness scoring |
| date_accessed | yes | records temporal grounding |
| reliability_tier | yes | tier_1 to tier_3 |
| authority_score | yes | 1 to 5 |
| bias_level | yes | low, medium, high |
| excerpt | yes | short supporting passage |
| supports_claim | yes | explicit claim link |

## Reliability Model
N01 uses source quality as a ranking input, not a side note.

| Tier | Typical source | Why it matters |
|------|----------------|----------------|
| tier_1 | filings, official docs, peer reviewed papers, government sources | strongest for factual grounding |
| tier_2 | reputable analysts, major media, trusted industry databases | useful but not final authority |
| tier_3 | blogs, forums, social posts, vendor claims without corroboration | directional only |

Authority score and bias level refine the tier.
Freshness then decides whether a once-good source is still operationally usable.

## Citation Card Structure
Each citation should contain:
- source identity
- retrieval context
- evidence excerpt
- reliability evaluation
- intended usage scope
- invalidation trigger

This turns the citation into a durable research primitive instead of a link dump.

## Suggested Markdown Layout

| Section | Content |
|---------|---------|
| Summary | what the source is and why N01 keeps it |
| Provenance | URL, author, access time, publication time |
| Evidence | excerpt plus claim mapping |
| Reliability | authority, freshness, bias, conflict notes |
| Comparative use | where it can and cannot win in a source dispute |
| Refresh rule | when to revisit or replace it |

## Comparative Pressure Rules
1. A vendor claim should rarely stand alone in a competitor matrix.
2. A media summary should not outrank an official pricing page for current price facts.
3. A fresh forum report may beat a stale official doc for outage or sentiment observations, but only on that narrow claim.
4. A paper can anchor definitions and methods, not always market adoption.
5. If two sources conflict, cite both and record the conflict instead of averaging them away.

## Excerpt Discipline
The excerpt is the operational center of the citation.
It should be:
- short enough to inspect quickly
- specific enough to justify the linked claim
- preserved with date and source context

Avoid excerpts that are generic marketing copy.
Prefer excerpts with metrics, version references, dates, limits, pricing, or methodological definitions.

## Example Evaluation Grid

| Example source | Reliability view | Use |
|----------------|------------------|-----|
| vendor pricing page updated this month | high freshness, medium bias, high authority on price | use for list price |
| third-party review site from last year | medium authority, stale, medium bias | use for historical comparison only |
| conference paper on retrieval method | high authority, medium freshness, low bias | use for technical method claims |
| Reddit thread on customer pain points | low authority, high freshness, high bias variance | use only as sentiment signal |

## Invalidation And Refresh
N01 citations should expire by conditions, not intuition.

| Trigger | Action |
|---------|--------|
| pricing source older than 90 days | refresh before reuse |
| model spec source older than 30 days | verify before ranking competitors |
| page no longer resolves | replace or archive as historical only |
| conflicting newer official source appears | downgrade old citation |
| multiple low-tier sources echo same claim | seek one higher-tier confirmation |

## Anti-Patterns
- URL without excerpt
- excerpt without explicit supported claim
- publication date omitted on time-sensitive facts
- vendor blog treated as neutral evidence
- tier_3 source used as single proof for competitive positioning

## N01 Usage Pattern
In N01, citations should flow into:
- knowledge cards for reusable facts
- competitive matrices for procurement and sales pressure
- ontology notes for canonical definitions
- memory artifacts when stable entities or repeated source rules emerge

## N01 Decision
The N01 citation object exists to make every later synthesis defeasible and auditable.
That is the real analytical advantage.
Anyone can paste links.
N01 stores the reasons a source should win or lose in a conflict.
