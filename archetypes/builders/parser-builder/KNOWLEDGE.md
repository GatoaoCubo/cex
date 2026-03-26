---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for parser production
sources: CEX taxonomy, data extraction patterns, regex standards, structured output literature
---

# Domain Knowledge: parser

## Foundational Concept
A parser is a data extraction artifact that converts raw, semi-structured, or unstructured
output into typed structured data. In LLM-powered systems, parsers bridge the gap between
free-form model output and downstream systems that require structured input. The CEX parser
(P05) defines extraction rules (regex, JSON paths, selectors) with error handling and
normalization, producing consistent structured output from variable raw input.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| BeautifulSoup/lxml | HTML/XML parsing with selectors | css_selector and xpath methods |
| jq/JSONPath | JSON field extraction | json_path method |
| Regular expressions | Pattern-based text extraction | regex method |
| LangChain output parsers | LLM output to structured types | llm_extract method |
| Pydantic | Schema validation + parsing | output_format: typed_object |

## Key Patterns
- Method selection: use json_path for JSON, css_selector for HTML, regex for free text
- Required vs optional: at least one extraction must be required
- Error strategy hierarchy: fail (strict) > retry (resilient) > default (tolerant) > skip (lenient)
- Normalization pipeline: extract first, normalize second (trim, lowercase, type cast)
- Fallback extraction: if primary method fails, try simpler alternative
- Chunking: for large inputs, split into manageable chunks before parsing
- Streaming: for real-time inputs, parse incrementally without buffering entire input
- LLM extraction: use llm_extract only when pattern-based methods cannot work

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| extraction_count | Integrity check: frontmatter matches body | No direct equivalent |
| error_strategy | CEX mandates explicit error handling for every parser | LangChain retry_parser |
| normalization | Post-extraction transform pipeline | Pydantic validators |
| llm_extract method | CEX supports LLM-as-parser for complex extraction | LangChain structured output |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT parser |
|------|------------|---------------------|
| formatter (P05) | Output presentation (pretty print, template) | PRESENTS data, does not EXTRACT |
| validator (P06) | Content validation against rules | VALIDATES data, does not EXTRACT |
| naming_rule (P05) | Naming convention definition | NAMES things, does not EXTRACT data |
| scraper (P04) | Web data collection tool | COLLECTS from web, parser PROCESSES local data |

## References
- CEX TAXONOMY_LAYERS.yaml — parser in runtime layer
- CEX SEED_BANK.yaml — P05_parser seeds
- Regular expressions: PCRE2 syntax
- JSONPath specification: RFC 9535
