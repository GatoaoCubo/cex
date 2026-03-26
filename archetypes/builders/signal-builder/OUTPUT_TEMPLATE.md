---
lp: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a signal
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: signal

Naming pattern: `p12_sig_{event}.json`
Filename: `p12_sig_{{event}}.json`

```json
{
  "satellite": "{{satellite_slug}}",
  "status": "{{complete|error|progress}}",
  "quality_score": {{0.0_to_10.0}},
  "timestamp": "{{ISO_8601_timestamp}}",
  "task": "{{short_task_label_or_omit}}",
  "artifacts": ["{{artifact_path_1}}"],
  "artifacts_count": {{integer_or_omit}},
  "commit_hash": "{{git_hash_or_omit}}",
  "error_code": "{{short_error_code_or_omit}}",
  "message": "{{short_message_or_omit}}",
  "progress_pct": {{0_to_100_or_omit}}
}
```

## Derivation Notes
- The first four fields are the required minimum contract from SCHEMA.md
- All remaining fields are optional extensions from SCHEMA.md
- Omit absent optional fields instead of filling with placeholder strings
- Keep the payload atomic: no instructions, no routing logic, no nested plans
