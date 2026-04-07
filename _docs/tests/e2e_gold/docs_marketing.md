---
id: e2e_gold_docs_marketing
kind: golden_test
type: marketing
pillar: P01
title: "Gold Standard — Project Documentation Marketing Artifacts"
version: 1.0.0
created: 2026-04-06
author: n02_marketing
scenario: S3
input: "documenta esse projeto"
quality: 9.1
tags: [e2e, gold-standard, docs, documentation, marketing, stress-test]
---

# Project Documentation — Marketing Gold Standard

> Scenario S3: "documenta esse projeto" — 3 words, maximum ambiguity.
> This gold standard defines what COMPELLING documentation looks like.
> Documentation IS marketing — bad docs kill adoption faster than bad features.

---

## 1. README Structure

A README that makes people WANT to use your project. Not just understand it — WANT it.

### Section Map

```
# Project Name
> One-line tagline that sells (not describes)

## The Problem
2-3 sentences. Paint the pain. Make the reader nod.

## The Solution
What this project does. 1 paragraph max. Concrete, not abstract.

## Quickstart
3-5 steps. Copy-paste ready. Time to first result: < 2 minutes.

## Features
Bullet list. Each feature = benefit, not spec.
- "Automatic retry with exponential backoff" → BAD (spec)
- "Never lose a request — auto-retries handle flaky APIs" → GOOD (benefit)

## Architecture (optional, for dev audience)
One diagram or ASCII art. Show how pieces connect.

## Installation
Full install instructions. Every OS. Every edge case.
If it can go wrong, document it.

## Usage
3 examples: basic, intermediate, advanced.
Each example: input → code → output.

## API Reference (if applicable)
Link to generated docs. Don't inline the full API.

## Contributing
How to contribute. What you accept. Code style. PR template.

## License
One line + link.
```

### Tone Rules for README

| Element | Tone | Example |
|---------|------|---------|
| Tagline | Bold, benefit-first | "Ship faster. Break nothing." |
| Problem section | Empathetic, specific | "You've been there: 3 AM, deployment failed..." |
| Solution section | Confident, concrete | "This tool does X, Y, Z. Period." |
| Quickstart | Imperative, minimal | "Run this. See that. Done." |
| Features | Benefit-driven | Each bullet answers "so what?" |
| Installation | Precise, paranoid | Assume nothing works first try |

### Anti-patterns (README fails)

- Wall of text with no headers
- "This is a project that..." (boring opener)
- Installation that assumes global deps are installed
- No quickstart (or quickstart > 10 steps)
- Features listed as specs, not benefits
- No example output (reader can't visualize result)

---

## 2. QUICKSTART Structure

The quickstart is the most important page in your docs. If it fails, nothing else matters.

### Template

```markdown
# Quickstart

> Time to first result: ~2 minutes

## Prerequisites

- [Runtime] version X+ (`command --version` to check)
- [Package manager] installed
- [Account/API key] if needed (link to get one)

## Step 1: Install

\```bash
[single command — prefer one-liner]
\```

## Step 2: Configure

\```bash
[minimal config — defaults should work for 80% of users]
\```

## Step 3: Run

\```bash
[the command that produces visible output]
\```

## Expected Output

\```
[exact output the user should see — copy-paste verifiable]
\```

## What Just Happened?

1-3 sentences explaining what the quickstart did.
Links to deeper docs for each concept.

## Next Steps

- [Common task 1](link) — "Add your first X"
- [Common task 2](link) — "Configure Y for production"
- [Troubleshooting](link) — "Something broke? Start here."
```

### Quickstart Rules

1. **Max 5 steps** — if you need more, your setup is too complex
2. **Copy-paste everything** — no "replace X with your value" without explanation
3. **Show expected output** — the reader needs to know it worked
4. **Prerequisites up front** — don't let them fail at step 3
5. **Time estimate** — "~2 minutes" sets expectations and builds confidence

---

## 3. Knowledge Card Template for Project Documentation

```markdown
---
id: kc_[project]_[topic]
kind: knowledge_card
type: technical
pillar: P01
title: "[Project] — [Topic]"
version: 1.0.0
created: [date]
author: [nucleus]
domain: [domain]
quality: null
tags: [project, topic, relevant-tags]
tldr: "One sentence: what this KC captures and why it matters"
when_to_use: "When [specific trigger or question this KC answers]"
keywords: [searchable, terms, for, retrieval]
linked_artifacts:
  - [path/to/related/artifact.md]
density_score: null
---

# [Topic Title]

## Executive Summary

3-5 sentences. What this is, why it exists, what it enables.
Dense. No filler. Every sentence carries information.

## Core Concepts

### [Concept 1]
Definition + why it matters + how it connects to other concepts.

### [Concept 2]
Same structure. Build understanding progressively.

## Architecture / How It Works

Diagram or structured explanation of the mechanism.
If code: annotated snippet (not full file dump).

## Usage Patterns

### Pattern 1: [Common Use Case]
```
[concrete example with input/output]
```

### Pattern 2: [Advanced Use Case]
```
[concrete example]
```

## Gotchas

- [Non-obvious thing 1] — why it catches people
- [Non-obvious thing 2] — how to avoid it

## References

- [Link 1](url) — what it contains
- [Link 2](url) — what it contains
```

### KC Quality Markers

| Marker | Threshold | Why |
|--------|-----------|-----|
| density_score | >= 0.85 | Every sentence must carry information |
| tldr | <= 150 chars | Forces clarity |
| when_to_use | present | Enables retrieval — KC without trigger = lost KC |
| linked_artifacts | >= 1 | No orphan knowledge |
| executive_summary | 3-5 sentences | Not 1 (too sparse), not 10 (too verbose) |

---

## Why Documentation IS Marketing

| Bad Docs | Good Docs |
|----------|-----------|
| "This module handles X" | "This module lets you X in 3 lines of code" |
| 50-page PDF nobody reads | Scannable sections with anchored links |
| "See source for details" | Annotated examples with expected output |
| Written for the author | Written for someone who has never seen this |
| Assumes knowledge | Builds knowledge progressively |
| No quickstart | 2-minute quickstart that actually works |

> The best documentation makes the reader feel smart, not stupid.
> Every friction point in your docs is a user you lost.

---

## Validation Criteria

- **DOC-01**: README structure has all required sections (Problem, Solution, Quickstart, Features, Install, Usage)
- **DOC-02**: README tagline exists and is under 80 characters
- **DOC-03**: Quickstart has max 5 steps
- **DOC-04**: Quickstart shows expected output
- **DOC-05**: Quickstart lists prerequisites before first command
- **DOC-06**: KC template includes all required frontmatter fields (id, kind, type, pillar, title, version, tldr, when_to_use)
- **DOC-07**: Features are written as benefits, not specs (at least 3 examples)
- **DOC-08**: Tone guidance exists with concrete examples (not just "be clear")
- **DOC-09**: Anti-patterns documented (what NOT to do)
- **DOC-10**: All content applicable to any project (not CEX-specific)
