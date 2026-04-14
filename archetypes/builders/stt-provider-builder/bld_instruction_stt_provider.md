---
kind: instruction
id: bld_instruction_stt_provider
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for stt_provider
quality: 8.9
title: "Instruction Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, instruction]
tldr: "Step-by-step production process for stt_provider"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify STT API endpoints and authentication protocols (OAuth2, API keys).  
2. Evaluate provider latency, accuracy, and language support for target use cases.  
3. Align requirements with P04: CALL function constraints (e.g., real-time processing).  
4. Analyze audio input formats (WAV, FLAC) and required sampling rates.  
5. Review provider documentation for error codes and rate-limiting policies.  
6. Benchmark provider performance against industry standards (e.g., WER metrics).  

## Phase 2: COMPOSE  
1. Set up dev environment with Python 3.9+ and required libraries (requests, pydub).  
2. Define schema in SCHEMA.md: input (audio blob, metadata) → output (transcript, confidence).  
3. Implement core STT logic using provider’s API (e.g., `POST /v1/transcribe`).  
4. Handle audio preprocessing: normalize volume, split long files into 30s chunks.  
5. Integrate error handling for HTTP 4xx/5xx responses and retries (exponential backoff).  
6. Use OUTPUT_TEMPLATE.md for structured JSON output (transcript, timestamps, language).  
7. Add logging for audit trails (e.g., request ID, provider response time).  
8. Write unit tests for edge cases (silence, background noise, non-supported languages).  
9. Document API keys and endpoint URLs in a secure config file (not committed to repo).  

## Phase 3: VALIDATE  
[ ] [ ] Run unit tests: 100% coverage for all edge cases.  
[ ] [ ] Validate integration with provider’s sandbox environment.  
[ ] [ ] Confirm compliance with P04: CALL function SLAs (latency < 500ms).  
[ ] [ ] Test security: audio data encrypted in transit (TLS 1.2+), no plaintext logs.  
[ ] [ ] Perform load testing: 100 concurrent requests, 99.9% success rate.
