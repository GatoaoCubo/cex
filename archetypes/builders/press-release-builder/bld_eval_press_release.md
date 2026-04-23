---
kind: quality_gate
id: p05_qg_press_release
pillar: P11
llm_function: GOVERN
purpose: Define hard gates and soft scoring dimensions for press_release quality enforcement
quality: 9.1
title: "Press Release Quality Gate"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, quality_gate]
tldr: "8 hard gates and 5 scored dimensions; minimum 8.0 to publish, 9.5 for golden status"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_press_release
  - bld_instruction_press_release
  - p11_qg_quality_gate
  - bld_schema_press_release
  - bld_output_template_press_release
  - p03_sp_press_release_builder
  - p11_qg_marketing_artifacts
  - p03_qg_webinar_script
  - p11_qg_response_format
  - bld_tools_press_release
---
## Quality Gate
## Definition
| Property | Value |
|---|---|
| Kind | press_release |
| Pillar | P05 |
| Scorer | cex_score.py |
| Quality floor | 8.0 (PUBLISH threshold) |
| Quality target | 9.0 |
| Golden threshold | 9.5 |
| Max retries | 2 (return to F6 PRODUCE) |
## HARD Gates (all must pass; one failure = REJECT)
| Gate | ID | Check | Pass condition | Failure action |
|---|---|---|---|---|
| YAML valid | H01 | Frontmatter parses without error | No YAML syntax errors | Fix frontmatter, re-run |
| ID pattern | H02 | ID matches regex | ^p05_pr_[a-z][a-z0-9_]+.md$ | Rename artifact |
| Kind correct | H03 | kind field value | kind == "press_release" | Correct kind |
| Headline | H04 | Headline present, character count | Present AND <= 80 chars | Shorten or add headline |
| Dateline | H05 | Dateline format | City in CAPS + AP state abbr + date | Fix dateline format |
| Lede 5Ws | H06 | Lede answers who/what/when/where/why | All 5 Ws detectable in lede | Rewrite lede |
| Boilerplate | H07 | "About [Company]:" section present | Section exists with content | Add boilerplate |
| Contact block | H08 | Media contact has email | Email field present and formatted | Add contact email |
## SOFT Scoring (5 dimensions, weighted to 1.0)
| Dimension | ID | Weight | What is scored | 10/10 example |
|---|---|---|---|---|
| AP style adherence | D01 | 0.25 | Style compliance: attribution verb, number rules, title format, date format, no Oxford comma | Zero AP violations; "said" used; titles before names |
| Headline quality | D02 | 0.25 | Hook strength, active voice, specificity, keyword relevance | Active verb, concrete number or name, no puffery |
| Quote authenticity | D03 | 0.20 | Attribution completeness, quote naturalness, avoidance of marketing-speak | Full name + title + "said"; quote sounds like a human said it |
| Boilerplate completeness | D04 | 0.15 | Company description, third person, present tense, 50-100 words | Covers: what company does, founded when, key differentiator |
| Contact block completeness | D05 | 0.15 | Name, title, email, phone all present | All four fields, phone with area code |

Score formula: (D01 x 0.25) + (D02 x 0.25) + (D03 x 0.20) + (D04 x 0.15) + (D05 x 0.15) = score out of 10.
## Actions by Score
| Score range | Status | Action |
|---|---|---|
| >= 9.5 | GOLDEN | Archive as exemplar in bld_examples_press_release.md |
| >= 8.0 | PUBLISH | Approved for wire service submission |
| >= 7.0 | REVIEW | Return to human editor for revision pass |
| < 7.0 | REJECT | Return to F6 PRODUCE (max 2 retries) |
## Bypass Table
| Bypass condition | Allowed | Notes |
|---|---|---|
| User waives embargo line | YES | User must explicitly confirm "FOR IMMEDIATE RELEASE" intent |
| User waives phone in contact | YES | Email-only contact acceptable if user confirms |
| Headline exceeds 80 chars | NO | Hard gate, no bypass permitted |
| Missing boilerplate | NO | Hard gate, no bypass permitted |
| Missing lede 5Ws | NO | Hard gate, no bypass permitted |
## Examples
## Golden Example
Score: 9.6/10. All H01-H08 gates pass. No AP style violations.

---

FOR IMMEDIATE RELEASE

DATALOOP LAUNCHES AI-POWERED PIPELINE THAT CUTS DATA PREP TIME BY 70%

SAN FRANCISCO, Calif., April 14, 2026 -- DataLoop Inc. today launched
DataLoop Accelerate, an AI-powered data preparation platform that reduces
the time data teams spend on pipeline configuration from hours to minutes,
available immediately to enterprise customers.

DataLoop Accelerate uses large language model inference to automatically
detect schema mismatches, resolve null values, and generate transformation
scripts from natural language descriptions. The platform integrates with
Snowflake, Databricks, and BigQuery out of the box, with no custom
connectors required. Pricing starts at $2,500 per month for teams of up to
20 data engineers.

Early access customers report a 70 percent reduction in data preparation
time across production pipelines. Meridian Analytics, a DataLoop customer
since 2024, reduced its weekly pipeline maintenance from 16 hours to fewer
than five after deploying Accelerate in January 2026.

"Data engineering teams spend more than half their time on undifferentiated
preparation work that adds no analytical value," said Priya Nair, Chief
Executive Officer at DataLoop Inc. "Accelerate changes that equation so
teams can focus on the insights, not the plumbing."

###

About DataLoop Inc.:
DataLoop Inc. builds AI-powered data infrastructure tools for enterprise
analytics teams. Founded in 2021 and headquartered in San Francisco,
DataLoop serves more than 300 enterprise customers across financial
services, healthcare, and technology verticals. The company has raised
$47 million in venture funding and employs 110 people.

Media Contact:
James Ortega
Head of Communications, DataLoop Inc.
james.ortega@dataloop.io
(415) 555-0182

---
### Why this is golden
| Element | Assessment |
|---|---|
| Headline | 63 chars, active voice, concrete "70%" hook, ALL CAPS |
| Dateline | CITY in caps, "Calif." abbreviation, correct date format |
| Lede | 35 words, answers who/what/when/where/why |
| Body | Two solid paragraphs, specific pricing and integration details |
| Quote | Human-sounding, attributed with full name and spelled-out title |
| ### mark | Present |
| Boilerplate | 75 words, third person, covers founding/HQ/customers/funding |
| Contact | Name, email (format valid), phone with area code |
## Anti-Example 1: Buried Lede
---

FOR IMMEDIATE RELEASE

THE EVOLVING LANDSCAPE OF ENTERPRISE DATA MANAGEMENT IN 2026

SAN FRANCISCO, Calif., April 14, 2026 -- As organizations continue to
grapple with the increasing volume and complexity of data flowing through
modern enterprise infrastructure, the demand for solutions that can
abstract away the complexity of data pipeline management has never been
higher. It is in this context that DataLoop Inc. is pleased to announce
the launch of DataLoop Accelerate.

---
### Why this fails
| Failure | Explanation |
|---|---|
| Buried lede | The product name does not appear until sentence three. Journalists who scan the first sentence will discard this release. |
| Headline is a topic, not news | "The Evolving Landscape..." tells journalists nothing happened. A news headline announces a fact. |
| Passive construction | "Is pleased to announce" is PR boilerplate that triggers journalist filters. |
| No 5 Ws in paragraph 1 | Who launched what for whom and why is not answered in the first paragraph. |
## Anti-Example 2: No Boilerplate
---

FOR IMMEDIATE RELEASE

DATALOOP LAUNCHES AI-POWERED PIPELINE THAT CUTS DATA PREP TIME BY 70%

SAN FRANCISCO, Calif., April 14, 2026 -- DataLoop Inc. today launched
DataLoop Accelerate, an AI-powered data preparation platform that reduces
pipeline configuration time by 70 percent.

"This changes how data teams work," said Priya Nair, CEO at DataLoop.

###

Media Contact:
james.ortega@dataloop.io

---
### Why this fails
| Failure | Explanation |
|---|---|
| No boilerplate | Journalists who cover the story need company background. Without it they must research the company separately -- many will not bother. Wire services flag releases without boilerplate. H07 hard gate fails. |
| CEO not spelled out | "CEO" must be "Chief Executive Officer" on first reference per AP style. D01 score deducted. |
| Quote uses marketing language | "This changes how data teams work" is vague. No specific claim. D03 score low. |
| Contact block incomplete | Email only. No name, no title, no phone. H08 hard gate fails on missing email format check. |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
