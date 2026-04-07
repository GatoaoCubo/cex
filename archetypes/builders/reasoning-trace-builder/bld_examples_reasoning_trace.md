---
kind: examples
id: bld_examples_reasoning_trace
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of reasoning_trace artifacts
pattern: few-shot learning for structured decision audit records
---

# Examples: reasoning-trace-builder
## Golden Example
INPUT: "Record why research-agent selected ada-002 over cohere-embed-v3 for P01 retriever"
OUTPUT (`p03_rt_research_agent_20260406T143000.yaml`):
```yaml
agent: research-agent
intent: select embedding model for P01 retriever
steps:
  - step: 1
    thought: OpenAI ada-002 is the most widely deployed embedding model with extensive documentation
    evidence: "MTEB benchmark: 63.4% average, 8191 token limit, $0.0001/1K tokens, 1536 dimensions"
    confidence: 0.8
  - step: 2
    thought: Cohere embed-v3 offers higher benchmark scores and multilingual support
    evidence: "MTEB benchmark: 66.1% average, 512 token limit, requires API key rotation every 90 days"
    confidence: 0.7
  - step: 3
    thought: Our chunk size is 512 tokens — both models handle this, but ada-002 has 16x headroom
    evidence: "P01 embedding_config.yaml shows chunk_size=512, overlap=64"
    confidence: 0.9
  - step: 4
    thought: Cost comparison favors ada-002 for our projected volume of 50K documents/month
    evidence: "ada-002: ~$5/month at 50K docs; cohere-v3: ~$12/month at same volume (pricing page 2026-03)"
    confidence: 0.85
conclusion: "Selected ada-002 — 16x token headroom over chunk size, 58% lower cost at projected volume, and no API key rotation overhead. The 2.7% MTEB gap does not justify the operational complexity of cohere-v3."
alternatives_rejected:
  - alternative: Cohere embed-v3
    reason: "Higher MTEB score (+2.7%) but 512 token limit matches chunk size exactly (zero headroom), 2.4x higher cost, and API key rotation adds operational burden"
  - alternative: Local sentence-transformers (all-MiniLM-L6-v2)
    reason: "Zero API cost but 384 dimensions (vs 1536) reduces retrieval precision, and self-hosting adds infra maintenance"
confidence: 0.81
timestamp: "2026-04-06T14:30:00-03:00"
duration_ms: 4500
```
WHY THIS IS GOLDEN:
- filename follows `p03_rt_{agent}_{timestamp}.yaml`
- all required fields present: agent, intent, steps, conclusion, confidence, timestamp
- each step has thought + concrete evidence + calibrated confidence
- alternatives_rejected has evidence-based rejection reasons
- conclusion directly references step evidence (token headroom, cost, MTEB gap)
- overall confidence (0.81) is geometric mean of step confidences
- no execution instructions, no workflow logic
## Golden Low-Confidence Example
OUTPUT (`p03_rt_build_sat_20260406T160000.yaml`):
```yaml
agent: build-sat
intent: determine if kc_toolkit.md needs restructuring
steps:
  - step: 1
    thought: Current KC has 3 sections but toolkit kind has expanded to cover MCP mapping
    evidence: "kc_toolkit.md last updated 2026-02-15; toolkit-builder added MCP fields 2026-03-20"
    confidence: 0.7
  - step: 2
    thought: No user complaints about KC accuracy reported in feedback logs
    evidence: "grep of .cex/learning_records/ shows 0 entries mentioning kc_toolkit"
    confidence: 0.3
conclusion: "Insufficient evidence to justify restructuring — no user-reported issues, but KC is 5 weeks stale relative to builder updates. Recommend monitoring for 2 more weeks."
alternatives_rejected:
  - alternative: Immediate restructuring
    reason: "No concrete evidence of user impact; restructuring without cause wastes builder cycles"
confidence: 0.46
timestamp: "2026-04-06T16:00:00-03:00"
duration_ms: 2100
```
WHY THIS PASSES:
- low confidence (0.46) correctly reflects weak evidence at step 2
- conclusion honestly states insufficient evidence
- step 2 confidence capped at 0.3 due to absence-of-evidence reasoning
- would trigger memory feedback loop (confidence < 0.5)
## Anti-Example
BAD OUTPUT (`p03_rt_agent.md`):
```markdown
# Reasoning Trace
The agent decided to use ada-002 because it's a good model.
We considered other options but ada-002 seemed best.
Confidence: high.
```
FAILURES:
1. wrong format: markdown prose instead of structured YAML
2. wrong extension: `.md` instead of `.yaml`
3. no `agent` field — who reasoned?
4. no `steps` list — no chain-of-thought structure
5. no `evidence` — "it's a good model" is assertion, not reasoning
6. confidence is string "high" instead of numeric 0.0-1.0
7. no `alternatives_rejected` — what else was considered?
8. no `timestamp` — when was this decided?
9. includes no concrete data — completely unauditable
## Anti-Example: Instruction Drift
BAD OUTPUT (`p03_rt_build_sat_20260406.yaml`):
```yaml
agent: build-sat
intent: build landing page
steps:
  - step: 1
    thought: First, create the hero section with a CTA button
    evidence: "landing page best forctices document"
    confidence: 0.9
  - step: 2
    thought: Then add testimonials section below the fold
    evidence: "conversion rate optimization guide"
    confidence: 0.85
next_actions:
  - "Create hero section HTML"
  - "Add testimonials component"
  - "Deploy to staging"
```
FAILURES:
1. steps describe WHAT to do, not WHY a decision was made — this is an instruction
2. `next_actions` is an execution directive — belongs in instruction artifact
3. evidence is vague document references, not concrete data
4. no `conclusion`, no `alternatives_rejected`, no `timestamp`
5. this artifact is an instruction masquerading as a reasoning trace
