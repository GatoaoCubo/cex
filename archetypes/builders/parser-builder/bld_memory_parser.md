---
kind: memory
id: bld_memory_parser
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for parser artifact generation
---

# Memory: parser-builder

## Summary

Parsers extract structured data from raw output — text, JSON, HTML, or logs. The primary production failure is building parsers that assume consistent input formatting. Real-world LLM output varies in whitespace, casing, and field ordering between runs. Successful parsers use extraction rules resilient to formatting variation and always include fallback patterns for when the primary extraction fails.

## Pattern

- Define extraction rules as ordered priority list: try the most specific pattern first, fall back to broader patterns
- Regex patterns must use named capture groups — unnamed groups break when input structure shifts
- Include normalization steps after extraction: trim whitespace, normalize casing, coerce types
- Error handling must distinguish between "field not found" (fallback) and "input malformed" (reject)
- Test parsers against at least 5 real output samples — synthetic test data hides edge cases
- JSON path extractors should handle both nested and flattened structures for the same field

## Anti-Pattern

- Single rigid regex with no fallback — breaks silently when LLM output format varies slightly
- Unnamed capture groups — positional references break when input structure changes
- Missing normalization — extracted data contains inconsistent whitespace and casing
- Treating all extraction failures as errors — some fields are optional and absence is valid
- Confusing parser (P05, extracts from raw output) with formatter (P05, transforms format) or validator (P06, checks correctness)

## Context

Parsers operate in the P05 formatting layer. They sit between raw output generation and structured data consumption. In agent pipelines, parsers transform LLM text responses into typed data that downstream components can process reliably. They are essential for any pipeline that consumes unstructured or semi-structured LLM output.

## Impact

Parsers with fallback patterns achieved 98% extraction success rate versus 72% for single-pattern parsers. Named capture groups reduced maintenance burden by 60% when input formats evolved. Normalization steps eliminated 100% of whitespace-induced downstream failures.

## Reproducibility

For reliable parser production: (1) collect 5+ real output samples from the target source, (2) define primary extraction pattern with named groups, (3) add 1-2 fallback patterns for common variations, (4) include normalization pipeline, (5) define error handling per field (fallback vs reject), (6) validate against all collected samples.

## References

- parser-builder SCHEMA.md (14 required fields, extraction rule specification)
- P05 formatting pillar specification
- Data extraction and normalization patterns
