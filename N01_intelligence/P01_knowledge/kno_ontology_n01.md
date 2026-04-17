---
id: kno_ontology_n01
kind: ontology
pillar: P01
nucleus: N01
title: "N01 Ontology"
version: "1.0.0"
quality: null
tags: [ontology, n01, p01, analytical_envy, taxonomy]
---
<!-- 8F: F1=ontology/P01 F2=ontology-builder+kc_ontology F3=nucleus_def_n01+kc_ontology+taxonomy_completeness_audit+source_quality_contract F4=formal taxonomy for comparative knowledge organization
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_ontology_n01.md -->

# N01 Ontology

## Purpose
The ontology gives N01 a durable map of what kinds of things exist in research work and how they relate.
Analytical Envy means taxonomy is not neutral filing.
It is a weapon against sloppy equivalence.
If two concepts are not the same, the ontology must stop them from being merged by convenience.

## Properties

| Property | Value |
|----------|-------|
| Kind | `ontology` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Standards family | OWL, SKOS, schema.org patterns |
| Main use | knowledge organization and semantic retrieval |
| Primary entities | source, vendor, product, claim, benchmark, segment |
| Inference goal | sharper comparison and traceability |
| Anti-goal | vague taxonomies that erase differences |
| Linked workloads | retrieval, citation, competitive analysis |

## Ontology Thesis
N01 needs explicit semantic boundaries for:
- who said something
- what artifact contains the claim
- what entity the claim is about
- which benchmark axis is being compared
- when the claim was valid
- how trustworthy the source is

Without those boundaries, retrieval and synthesis drift toward generic category blur.

## Core Class Set

| Class | Description |
|-------|-------------|
| Source | a document, page, filing, paper, or post |
| Citation | a grounded reference to a source |
| Claim | a proposition extracted from evidence |
| Entity | company, product, person, framework, market, region |
| ComparisonAxis | feature, price, latency, capability, distribution, trust |
| Benchmark | measured or stated value on an axis |
| EvidenceBundle | claim plus citations plus reliability metadata |
| ResearchArtifact | N01-produced note, matrix, or card |

## Key Relations

| Relation | Meaning |
|----------|---------|
| `supportsClaim` | citation or source backs a claim |
| `aboutEntity` | claim or benchmark concerns an entity |
| `comparesAgainst` | entity or benchmark is contrasted with another |
| `measuredOnAxis` | benchmark belongs to an axis |
| `publishedAt` | source or claim has temporal anchor |
| `hasReliabilityTier` | evidence quality marker |
| `containedIn` | excerpt or claim belongs to source or artifact |
| `invalidatedBy` | newer or stronger evidence defeats older claim |

## SKOS Layer
SKOS is useful for controlled labels and synonyms.

| SKOS pattern | N01 use |
|--------------|---------|
| prefLabel | canonical vendor or capability name |
| altLabel | synonyms, product aliases, renamed plans |
| broader | category hierarchy such as model provider to AI provider |
| narrower | more specific product lines or feature classes |
| related | adjacent concepts that often co-occur in research |

This reduces alias drift in retrieval and matrix assembly.

## OWL Layer
OWL matters where N01 needs stronger semantic constraints.

| OWL construct | N01 use |
|---------------|---------|
| class restrictions | benchmark must be tied to one comparison axis |
| disjoint classes | source is not the same as citation |
| domain and range | `supportsClaim` should connect evidence to claim |
| equivalence | map stable synonyms only after review |
| transitive relations | propagate broader market categories where useful |

## schema.org Alignment
schema.org patterns help N01 interoperate with external structured data.

| schema.org type | N01 mapping |
|-----------------|-------------|
| Organization | vendor or publisher entity |
| Product | product under analysis |
| CreativeWork | paper, report, article |
| Dataset | benchmark release or public evaluation set |
| Offer | pricing or plan artifact |
| Review | user or analyst evaluation source |

## Comparative Semantics
N01 must distinguish between:
- a claim and a benchmark
- a benchmark and a promise
- a source and a citation
- a product and a company
- a market segment and a geography

Those distinctions are where analytical advantage comes from.

## Retrieval Benefits

| Ontology feature | Retrieval effect |
|------------------|------------------|
| alias control | fewer missed hits on renamed products |
| typed claims | easier filtering by fact type |
| axis modeling | more accurate competitive comparisons |
| temporal typing | freshness-aware ranking |
| evidence bundles | better grounding for synthesis |

## Governance Rules
1. Do not create near-duplicate classes for stylistic preference.
2. Promote a term to canonical only when repeated across artifacts.
3. Treat vendor taxonomy and neutral taxonomy separately when needed.
4. Preserve contradictory claims as separate claim nodes until resolved.
5. Version ontology changes that affect retrieval or reporting.

## Anti-Patterns
- ontology that models everything and clarifies nothing
- tags masquerading as classes
- no relation for invalidated evidence
- mixing product plan names with generic capability labels
- flattening benchmark axes into free text

## N01 Decision
The N01 ontology exists to stop false sameness.
It gives every later artifact a stable semantic backbone so the nucleus can compare harder, retrieve cleaner, and challenge claims with precision instead of rhetoric.
