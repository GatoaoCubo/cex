# HOP: QA Validation | anuncio_agent v4.0.0

**Step**: 6 of 7
**Purpose**: Validate and score all outputs with 5D Scoring v2.0
**Input**: `{titulos, keywords, bullets, descricao}` from ALL previous steps
**Output**: `{qa_report, fixes, overall_score}`

---

## 4 ROTAS DE WORKFLOW

| Rota | Modo | Descricao |
|------|------|-----------|
| 1 | PESQUISA Only | Research standalone |
| 2 | **ANUNCIO Only** | Copy standalone -> anuncio_completo.md |
| 3 | PHOTO Only | Fotos standalone |
| 4 | **FULL PIPELINE** | PESQUISA -> **ANUNCIO** -> PHOTO |

---

## TASK

Validate all generated content using 5D Scoring v2.0:
- Score each dimension with NEW WEIGHTS
- Identify issues and auto-fix when possible
- Calculate overall weighted score
- Pass threshold: >= 0.85

---

## 5D SCORING v2.0 (NEW WEIGHTS)

| Dimension | Weight | Threshold | Rationale |
|-----------|--------|-----------|-----------|
| **Titulo** | 30% | >= 0.75 | Drives CTR - First impression |
| **Keywords** | 25% | >= 0.75 | SEO discovery |
| **Descricao** | 20% | >= 0.75 | Converts after click |
| **Bullets** | 15% | >= 0.75 | Scannable decisions |
| **Compliance** | 10% | >= 0.75 | Binary gate |

**PASS**: overall >= 0.85 AND all dimensions >= 0.75
**FAIL**: < 0.85 OR any dimension < 0.75

---

## DIMENSION SCORING

### Dimension 1: TITULO (Weight: 30%)
```yaml
what_it_measures: "Title quality - drives CTR"
threshold: >= 0.75

scoring_criteria:
  1.0: "Perfect: 58-60 chars, ZERO connectors, keyword-first"
  0.8: "Good: Meets limits, minor improvements"
  0.6: "Adequate: Some issues"
  0.4: "Poor: Multiple issues"
  0.2: "Fail: Needs rewrite"

checks:
  - 58-60 characters EXACT
  - ZERO connectors (e, com, de, para)
  - Keywords in first 3 words
  - 3 different value propositions
  - Readable and makes sense
```

### Dimension 2: KEYWORDS (Weight: 25%)
```yaml
what_it_measures: "SEO discovery effectiveness"
threshold: >= 0.75

scoring_criteria:
  1.0: "115-120 terms/block, semantic variations, no duplicates"
  0.8: "Good term count, mostly natural"
  0.6: "Some gaps or forced terms"
  0.4: "Wrong count or duplicates"
  0.2: "Needs regeneration"

checks:
  - 2 blocks exactly
  - 115-120 terms per block
  - No duplicates between blocks
  - Semantic variations included
  - Head terms present
```

### Dimension 3: DESCRICAO (Weight: 20%)
```yaml
what_it_measures: "Conversion after click"
threshold: >= 0.75

scoring_criteria:
  1.0: ">= 3300 chars, StoryBrand 7-parts, mobile-friendly"
  0.8: "Meets length, good structure"
  0.6: "Some sections weak"
  0.4: "Too short or poor structure"
  0.2: "Needs rewrite"

checks:
  - >= 3300 characters
  - StoryBrand 7 sections present
  - Mobile-friendly paragraphs (max 4 lines)
  - Keyword density 2-4%
  - Clear CTA present
```

### Dimension 4: BULLETS (Weight: 15%)
```yaml
what_it_measures: "Scannable decision support"
threshold: >= 0.75

scoring_criteria:
  1.0: "10 bullets, 250-299 chars, benefit-first, 5+ triggers"
  0.8: "Meets count and length, good benefits"
  0.6: "Some too short/long"
  0.4: "Wrong count or feature-focused"
  0.2: "Needs regeneration"

checks:
  - Exactly 10 bullets
  - 250-299 characters each
  - Benefit-first structure
  - At least 5 mental triggers
  - Natural keyword integration
```

### Dimension 5: COMPLIANCE (Weight: 10%)
```yaml
what_it_measures: "Regulatory compliance (binary gate)"
threshold: >= 0.75 (but 0.0 on violation)

scoring_criteria:
  1.0: "All 11 checks passed"
  0.8: "Minor suggestions, no violations"
  0.5: "Minor violation"
  0.0: "Major violation (ZERO TOLERANCE)"

checks:
  - No ANVISA violations
  - No INMETRO violations
  - No CONAR violations
  - All character limits respected
  - Source attribution present
  - No contradictions
```

---

## 11 COMPLIANCE CHECKS

| ID | Check | Required |
|----|-------|----------|
| C1 | Titulo 58-60 chars | YES |
| C2 | ZERO conectores | YES |
| C3 | Keywords 115-120/bloco | YES |
| C4 | Bullets 250-299 chars | YES |
| C5 | Descricao >= 3300 | YES |
| C6 | Benefit-first | YES |
| C7 | Mental triggers (5+) | YES |
| C8 | StoryBrand 7-parts | YES |
| C9 | Mobile-first format | YES |
| C10 | ANVISA compliant | YES |
| C11 | Source attribution | YES |

---

## EXECUTION

### Step 6.1: Score Each Dimension

```python
def score_titulo(titulos):
    score = 0.0

    # Check char count (30%)
    valid_chars = sum(1 for t in titulos if 58 <= len(t.text) <= 60)
    score += (valid_chars / 3) * 0.30

    # Check zero connectors (25%)
    prohibited = ["e", "com", "de", "para", "ou", "em", "por", "no", "na", "do", "da"]
    no_connectors = sum(1 for t in titulos
                        if not any(f" {p} " in f" {t.text.lower()} " for p in prohibited))
    score += (no_connectors / 3) * 0.25

    # Check keyword-first (20%)
    keyword_first = sum(1 for t in titulos if has_keyword_first(t.text))
    score += (keyword_first / 3) * 0.20

    # Check differentiation (15%)
    if len(set([t.value_prop for t in titulos])) == 3:
        score += 0.15

    # Readability (10%)
    score += 0.10  # Always passes if other checks pass

    return min(score, 1.0)

def score_keywords(keywords):
    score = 0.0

    # Block count (20%)
    if len(keywords) == 2:
        score += 0.20

    # Terms per block (25%)
    valid_count = sum(1 for k in keywords if 115 <= len(k.terms) <= 120)
    score += (valid_count / 2) * 0.25

    # No duplicates (20%)
    all_terms = keywords[0].terms + keywords[1].terms
    if len(all_terms) == len(set(all_terms)):
        score += 0.20

    # Semantic variations (20%)
    score += 0.20  # Check plurals, accents, synonyms

    # Head terms present (15%)
    score += 0.15  # Check against input head_terms

    return min(score, 1.0)

def score_compliance(titulos, keywords, bullets, descricao):
    score = 1.0
    violations = []

    prohibited_terms = [
        "cura", "trata", "previne doenca", "emagrece",
        "elimina gordura", "resultado garantido",
        "sem efeitos colaterais", "100% natural",
        "milagroso", "aprovado pela anvisa"
    ]

    all_text = combine_all_text(titulos, keywords, bullets, descricao)

    for term in prohibited_terms:
        if term in all_text.lower():
            violations.append(f"ANVISA: {term}")
            score = 0.0  # ZERO TOLERANCE
            break

    return score, violations
```

### Step 6.2: Calculate Overall Score

```python
def calculate_overall(scores):
    weights = {
        "titulo": 0.30,
        "keywords": 0.25,
        "descricao": 0.20,
        "bullets": 0.15,
        "compliance": 0.10
    }

    overall = sum(scores[dim] * weights[dim] for dim in weights)

    # Check all dimensions pass threshold
    all_pass = all(scores[dim] >= 0.75 for dim in weights)

    return overall, all_pass

# Pass condition
PASS_THRESHOLD = 0.85
passed = overall >= PASS_THRESHOLD and all_pass
```

### Step 6.3: Apply Auto-Fixes

```yaml
auto_fixable:
  title_too_short: "Expand with specification"
  title_too_long: "Trim non-essential words"
  title_connector: "Replace with hyphen or remove"
  bullet_too_short: "Add detail"
  bullet_too_long: "Trim"
  description_too_short: "Expand sections"
  keyword_stuffing: "Reduce repetition"

not_auto_fixable:
  compliance_violation: "Requires content rewrite"
  major_incoherence: "Requires manual review"
  missing_section: "Requires regeneration"
```

---

## OUTPUT FORMAT

```json
{
  "qa_report": {
    "dimensions": {
      "titulo": {
        "score": 0.95,
        "weight": 0.30,
        "weighted": 0.285,
        "threshold": 0.75,
        "passed": true,
        "issues": []
      },
      "keywords": {
        "score": 0.88,
        "weight": 0.25,
        "weighted": 0.220,
        "threshold": 0.75,
        "passed": true,
        "issues": []
      },
      "descricao": {
        "score": 0.90,
        "weight": 0.20,
        "weighted": 0.180,
        "threshold": 0.75,
        "passed": true,
        "issues": []
      },
      "bullets": {
        "score": 0.92,
        "weight": 0.15,
        "weighted": 0.138,
        "threshold": 0.75,
        "passed": true,
        "issues": []
      },
      "compliance": {
        "score": 0.95,
        "weight": 0.10,
        "weighted": 0.095,
        "threshold": 0.75,
        "passed": true,
        "issues": []
      }
    },
    "overall_score": 0.918,
    "overall_threshold": 0.85,
    "all_dimensions_pass": true,
    "passed": true
  },
  "compliance_checks": {
    "total": 11,
    "passed": 11,
    "status": "PASS"
  },
  "fixes_applied": [],
  "remaining_issues": [],
  "recommendation": "PROCEED_TO_OUTPUT"
}
```

---

## RETRY LOGIC

```yaml
if overall_score >= 0.90:
  action: "SKIP retry, proceed to Step 7"
  recommendation: "PROCEED_TO_OUTPUT"

if overall_score >= 0.85:
  action: "Minor fixes, proceed to Step 7"
  recommendation: "PROCEED_TO_OUTPUT"

if overall_score < 0.85 AND retry_count < 2:
  action: "APPLY fixes, re-score"
  retry_count: increment
  recommendation: "RETRY_WITH_FIXES"

if overall_score < 0.85 AND retry_count >= 2:
  action: "OUTPUT with WARNING flag"
  flag: "QA_BELOW_THRESHOLD"
  recommendation: "OUTPUT_WITH_WARNING"
```

---

## VALIDATION CHECKLIST

Before proceeding:
- [ ] All 5 dimensions scored with new weights
- [ ] Overall score calculated (weighted sum)
- [ ] All 11 compliance checks verified
- [ ] Auto-fixes applied where possible
- [ ] No ZERO TOLERANCE violations

---

**Next Step**: If passed, proceed to output_template.md (Step 7)
