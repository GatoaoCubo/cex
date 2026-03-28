# PESQUISA Agent - Error Handling & Recovery

**Version**: 1.0.0 | **Quality**: >= 8.0

---

## Top 5 Failure Modes

### 1. Insufficient Input Data (Confidence < 0.40)

**Symptoms**:
- Missing required fields (`product_query` or `target_marketplaces`)
- Query too vague ("pesquise chocolate" without category/audience)
- Confidence score < 0.40 threshold

**Root Causes**:
- User provided incomplete brief
- Agent received partial data from upstream
- Context lost in multi-step pipeline

**Detection**:
```python
if confidence_score < 0.40:
    raise InsufficientInputError("Missing critical fields")
```

**Recovery Steps**:
1. **Immediate**: Stop execution, don't proceed with incomplete research
2. **Clarification Request**: Ask user for missing fields
3. **Fallback**: If user unavailable, infer from context (mark as "ESTIMATED" in output)
4. **Logging**: Record insufficient input for pattern analysis

**Prevention**:
- Use input schema validation (`data/input_schema.yaml`) before execution
- Implement confidence calculation early in workflow
- Provide input templates with examples

---

### 2. Marketplace Search Failures (HTTP/Rate Limit/Blocked)

**Symptoms**:
- HTTP 429 (rate limit exceeded)
- HTTP 403 (IP blocked/bot detection)
- HTTP 503 (service unavailable)
- Timeout errors on marketplace searches

**Recovery Steps**:
1. **Rate Limit (429)**:
   - Immediate: Wait exponential backoff (5s -> 15s -> 45s)
   - Retry: Max 3 attempts per marketplace
   - Fallback: Skip marketplace, note in limitations section

2. **IP Block (403)**:
   - Immediate: Stop requests to that marketplace
   - Alternative: Use web_search tool with `site:marketplace.com.br` operator
   - Fallback: Mark marketplace as "unavailable" in output

3. **Service Down (503)**:
   - Immediate: Skip marketplace
   - Retry: Check again after completing other marketplaces
   - Fallback: Proceed with available data, note in confidence score

4. **Timeout**:
   - Immediate: Reduce search scope (fewer queries)
   - Retry: 2 attempts with increased timeout (30s -> 60s)
   - Fallback: Use cached/recent data if available

**Graceful Degradation**:
```markdown
## Inbound (Marketplaces)

NOTE: Mercado Livre temporariamente indisponivel (HTTP 429).
Dados baseados em Shopee e Amazon apenas.

| Source | URL | Preco | Rating |
|--------|-----|-------|--------|
| Shopee | [...] | R$ X | X.X |
| Amazon | [...] | R$ X | X.X |
```

---

### 3. Low Competitor Data (<3 Competitors Found)

**Symptoms**:
- Found < 3 competitors in all marketplaces combined
- No competitors match price range filter
- Category too niche with sparse results

**Recovery Steps**:
1. **Expand Search** (Automatic):
   - Remove price_range filter -> search again
   - Broaden category_filter (go up one level)
   - Add synonym queries
   - Expand to more marketplaces

2. **Alternative Data Sources**:
   - Google Shopping results
   - Social media product posts (Instagram/TikTok Shop)
   - B2B marketplaces (Alibaba/1688 for import research)

3. **Adjust Quality Gate**:
   - If still < 3 after expansion: proceed with 2 competitors
   - Mark output as "LIMITED_COMPETITION_DATA"
   - Lower confidence score proportionally

---

### 4. Compliance Data Unavailable (ANVISA/INMETRO)

**Recovery Steps**:
1. **Category Mapping Lookup**:
   - Common mappings:
     - Alimentos/Suplementos -> ANVISA
     - Eletronicos/Brinquedos -> INMETRO
     - Cosmeticos -> ANVISA
     - Texteis/Calcados -> INMETRO (alguns)

2. **Conservative Approach**:
   - If unsure: recommend consulting with compliance specialist
   - List potential requirements based on similar categories
   - Err on side of caution (assume stricter rules)

3. **Output Format**:
   ```markdown
   ## Compliance

   ALERTA: Classificacao regulatoria incerta. Recomendacoes abaixo sao preliminares.

   - **ANVISA**: POSSIVELMENTE aplicavel (categoria alimentos). Verificar RDC 27/2010.
   - **INMETRO**: Nao identificado requisito obrigatorio.
   - **Recomendacao**: Consultar advogado especializado antes do lancamento.
   ```

---

### 5. Output Format Errors (JSON Parsing Failures)

**Symptoms**:
- Downstream agent cannot parse research output
- JSON syntax errors in final output
- Missing required fields in handoff data
- Escape character issues with newlines in `report` field

**Detection**:
```python
import json
try:
    output = json.loads(agent_response)
    assert "productName" in output
    assert "report" in output
except (JSONDecodeError, AssertionError):
    raise OutputFormatError()
```

**Recovery Steps**:
1. **Escape Special Characters**:
   ```python
   def sanitize_output(text):
       text = text.replace('"', '\\"')
       text = text.replace('\n', '\\n')
       text = text.replace('\t', '\\t')
       return text
   ```

2. **Validate Before Output**:
   ```python
   output_dict = {
       "productName": sanitize_output(product_name),
       "report": sanitize_output(full_report_markdown)
   }
   json.dumps(output_dict)  # Will raise error if invalid
   ```

3. **Citation Stripping** (Critical):
   - Remove: `citeturn*`, `:OaiMdDirective_Annotations`
   - Remove: `[source0]`, `[source1]`
   - Clean output must be pure markdown text

---

## General Recovery Protocol

### Severity Levels

| Level | Criteria | Action |
|-------|----------|--------|
| **CRITICAL** | Cannot proceed, blocks all research | STOP execution, request user input |
| **HIGH** | Major data missing (>50% marketplaces fail) | Continue with reduced scope, warn user |
| **MEDIUM** | Partial data missing (1-2 marketplaces fail) | Graceful degradation, note in limitations |
| **LOW** | Minor issues (formatting, optional fields) | Auto-fix, log for monitoring |

### Recovery Decision Tree

```
ERROR DETECTED
    |
    v
Can we retry with different parameters?
    |
    +---> YES: Retry (max 3x)
    |
    +---> NO: Can we proceed with partial data?
              |
              +---> YES: Continue + warn user + reduce confidence
              |
              +---> NO: STOP + request clarification
```

### Error Logging Format

```yaml
error_log:
  timestamp: "2026-02-06T14:23:45Z"
  error_type: "MARKETPLACE_SEARCH_FAILURE"
  severity: "MEDIUM"
  marketplace: "mercado_livre"
  query: "whey protein isolado"
  http_status: 429
  recovery_action: "SKIP_MARKETPLACE"
  impact: "Data from 2 of 3 marketplaces only"
  confidence_penalty: -0.15
```

---

## Confidence Score Adjustments

| Issue | Confidence Penalty |
|-------|-------------------|
| Missing 1 marketplace | -0.05 |
| Missing 2+ marketplaces | -0.15 |
| < 3 competitors | -0.20 |
| No compliance data | -0.10 |
| < 10 queries logged | -0.15 |
| No Reclame Aqui data | -0.05 |
| Estimated (not verified) fields | -0.10 per field |

**Formula**:
```
Final Confidence = Base Confidence (0.80-1.00) - Sum(Penalties)
Minimum Output Confidence = 0.60 (below this = request clarification)
```

---

**Version**: 1.0.0 | **Created**: 2026-02-06 | **Quality**: 8.5/10
