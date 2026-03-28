---
kind: collaboration
id: bld_collaboration_client
pillar: P12
llm_function: COLLABORATE
purpose: How client-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: client-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what endpoints does this client consume, and how does it authenticate?"
I do not build bidirectional connectors. I do not define MCP servers.
I specify unidirectional API consumers so agents can call external services reliably.

## Crew Compositions

### Crew: "External Integration"
```
  1. client-builder -> "API consumer with endpoints and auth"
  2. connector-builder -> "bidirectional sync if needed"
  3. env-config-builder -> "API keys and secret configuration"
```

### Crew: "Service Consumer Stack"
```
  1. interface-builder -> "formal contract with the service"
  2. client-builder -> "client implementation against the contract"
  3. fallback-chain-builder -> "degradation when service is unavailable"
```

## Handoff Protocol

### I Receive
- seeds: service name, base URL, auth strategy (API key, OAuth, bearer)
- optional: endpoint list, rate limits, pagination pattern, retry policy

### I Produce
- client artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_client_{service}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- interface-builder: provides formal contract that the client implements

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| connector-builder | May extend client into bidirectional integration |
| env-config-builder | Documents API keys and secrets the client requires |
| e2e-eval-builder | Tests full pipeline including external API calls |
