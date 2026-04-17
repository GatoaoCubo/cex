---
kind: tools
id: bld_tools_agent_grounding_record
pillar: P04
llm_function: CALL
purpose: Tool inventory for grounding record production -- hash verification, OTel validation, compile pipeline, external references
quality: 9.2
title: "Agent Grounding Record Builder -- Tools"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, tools]
tldr: "Production: cex_compile + cex_score + cex_retriever. Validation: hash-verify + span-validator. External: OTel semconv + C2PA v2.3 spec."
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
# Agent Grounding Record Builder -- Tools

## Production Tools (CEX Core)

| Tool                   | Command                                                                 | 8F Stage | Purpose                                                  |
|------------------------|-------------------------------------------------------------------------|----------|----------------------------------------------------------|
| cex_compile.py         | `python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md` | F8     | Compile .md to .yaml, check frontmatter, validate size   |
| cex_score.py           | `python _tools/cex_score.py --apply P10_memory/grounding/p10_gr_{{prefix}}.md` | F7 | Run 3-layer scoring (structural + rubric + semantic) |
| cex_retriever.py       | `python _tools/cex_retriever.py --query "grounding provenance OTel"` | F3      | Find similar grounding records for context injection     |
| cex_doctor.py          | `python _tools/cex_doctor.py --pillar P10`                             | F8       | Health check on all P10 memory artifacts                 |
| cex_compile.py --all   | `python _tools/cex_compile.py --all`                                   | F8       | Recompile entire artifact library after batch production |

### cex_compile.py -- Grounding Record Specific Checks

When run against an agent_grounding_record artifact, cex_compile.py performs:
1. YAML frontmatter parse check
2. ID naming regex validation: ^p10_gr_[a-z0-9_]+\.md$
3. kind field = "agent_grounding_record" check
4. Byte size <= 4096 check
5. output_hash format check (64 hex chars)
6. otel_span_id format check (16 hex chars)

## Validation Tools

### Hash Verification Tool

Verifies that output_hash, content_hash, and tool I/O hashes are valid SHA-256 hex strings.

```bash
# Verify all hashes in a grounding record
python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md --verify-hash
# Compute output_hash from raw output file
python -c "
import hashlib
with open('raw_output.txt', 'rb') as f:
    raw = f.read()
print(hashlib.sha256(raw).hexdigest())
"
# Verify a specific hash value
python -c "
import hashlib, sys
data = sys.stdin.buffer.read()
print(hashlib.sha256(data).hexdigest())
" < raw_output.txt
```

Hash validation rules enforced:
- Length: exactly 64 characters
- Charset: lowercase hexadecimal [0-9a-f] only
- Algorithm: SHA-256 only (no MD5, no SHA-1, no SHA-512)
- Source: raw bytes before any post-processing

### OTel Span ID Validator

Validates that otel_span_id conforms to W3C Trace Context format.

```bash
# Validate span ID format (W3C: 16 lowercase hex chars)
python -c "
import re, sys
span_id = sys.argv[1]
pattern = re.compile(r'^[0-9a-f]{16}$')
if pattern.match(span_id):
    print('[OK] Valid W3C span ID: ' + span_id)
else:
    print('[FAIL] Invalid span ID format: ' + span_id)
    print('Expected: 16 lowercase hex characters')
    sys.exit(1)
" {{OTEL_SPAN_ID}}
```

Common span ID format errors:

| Error Pattern           | Example              | Fix                                      |
|-------------------------|----------------------|------------------------------------------|
| 32 chars (trace ID)     | 4bf92f3577b34da6...  | Use the span ID (16 chars), not trace ID |
| Uppercase letters       | 4BF92F3577B34DA6     | Convert to lowercase                     |
| Hyphens (UUID format)   | 4bf9-2f35-77b3-4da6  | Remove hyphens                           |
| Shorter than 16 chars   | 4bf92f35            | Retrieve correct span ID from OTel SDK   |

### UUID Validator (inference_id)

```bash
# Validate UUIDv4 format
python -c "
import re, sys
uuid = sys.argv[1]
pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
if pattern.match(uuid):
    print('[OK] Valid UUIDv4: ' + uuid)
else:
    print('[FAIL] Not a valid UUIDv4: ' + uuid)
    sys.exit(1)
" {{INFERENCE_ID}}
# Generate a new UUIDv4
python -c "import uuid; print(str(uuid.uuid4()))"
```

## External References

### OTel GenAI Semantic Conventions

| Resource                          | URL                                                                        | Use                                    |
|-----------------------------------|----------------------------------------------------------------------------|----------------------------------------|
| OTel GenAI semconv spec           | https://opentelemetry.io/docs/specs/semconv/gen-ai/                       | Canonical attribute names and values   |
| OTel Python SDK                   | https://github.com/open-telemetry/opentelemetry-python                    | SDK for span ID retrieval in Python    |
| OTel GenAI WG (active)            | https://github.com/open-telemetry/semantic-conventions/tree/main/docs/gen-ai | WG discussions and in-progress changes |
| W3C Trace Context Level 2         | https://www.w3.org/TR/trace-context-2/                                    | span ID format specification           |

Key OTel GenAI attributes for grounding record production:

| OTel Attribute           | Python Access                                     | Grounding Record Mapping |
|--------------------------|---------------------------------------------------|--------------------------|
| span.span_id             | span.get_span_context().span_id (as hex)         | otel_span_id             |
| gen_ai.response.model    | span.attributes.get("gen_ai.response.model")     | model.id                 |
| gen_ai.system            | span.attributes.get("gen_ai.system")             | model.provider           |
| gen_ai.tool.call.id      | event attributes on tool call span events        | tool_calls[*].tool_name  |

### C2PA v2.3 Specification

| Resource                          | URL                                                                        | Use                                    |
|-----------------------------------|----------------------------------------------------------------------------|----------------------------------------|
| C2PA v2.3 spec                    | https://c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html | Full spec for manifest format  |
| C2PA AI-ML guidance               | https://c2pa.org/specifications/specifications/2.3/ai-ml/                 | AI-specific assertions and guidance    |
| C2PA Python library               | https://github.com/contentauth/c2pa-python                                | Python SDK for manifest creation       |
| C2PA training-mining assertion    | Section 19.8 of C2PA v2.3 spec                                            | Training data disclosure assertion     |

C2PA manifest integration pattern:

```python
# Example: creating a C2PA manifest reference after output_hash is known
# (Using c2pa-python library -- install: pip install c2pa-python)
import c2pa
builder = c2pa.Builder({
    "claim_generator": "cex_grounding_record_builder/1.0",
    "assertions": [
        {"label": "c2pa.actions", "data": {
            "actions": [{"action": "c2pa.created", "softwareAgent": "{{MODEL_ID}}"}]
        }},
        {"label": "c2pa.hash.data", "data": {
            "name": "output", "alg": "sha256", "hash": "{{OUTPUT_HASH_BASE64}}"
        }}
    ]
})
# manifest_ref = builder.sign_file(output_path, signed_path, signer)
```

Note: Convert output_hash from hex to base64 for C2PA: `base64.b64encode(bytes.fromhex(output_hash)).decode()`

### SHA-256 Standard Reference

| Resource                | Reference                        | Notes                                     |
|-------------------------|----------------------------------|-------------------------------------------|
| FIPS 180-4              | NIST FIPS 180-4 (2015)           | SHA-256 standard; all hashes must comply  |
| Python hashlib          | stdlib hashlib.sha256()          | Use this; do not use md5() or sha1()      |
| Hash comparison         | `hmac.compare_digest(a, b)`      | Use constant-time comparison for security |

## Tool Call Sequence (F5 CALL)

Execute in this order during Phase 1 RESEARCH:

```bash
# Step 1: Retrieve similar grounding records for context
python _tools/cex_retriever.py --query "grounding provenance OTel per-inference" --limit 3
# Step 2: Load builder ISOs (if not already loaded via F2 BECOME)
# (ISOs are loaded as context, no shell command needed)
# Step 3: After Phase 2 COMPOSE -- validate artifact
python _tools/cex_compile.py P10_memory/grounding/p10_gr_{{prefix}}.md
# Step 4: Score artifact
python _tools/cex_score.py --apply P10_memory/grounding/p10_gr_{{prefix}}.md
# Step 5: Signal completion
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', {{SCORE}})"
# Step 6: Commit
git add P10_memory/grounding/p10_gr_{{prefix}}.md
git commit -m "[N04] add grounding record p10_gr_{{prefix}}: {{INFERENCE_DESCRIPTION}}"
```