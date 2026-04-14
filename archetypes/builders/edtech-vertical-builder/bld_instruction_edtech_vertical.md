---
kind: instruction
id: bld_instruction_edtech_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for edtech_vertical
quality: null
title: "Instruction Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, instruction]
tldr: "Step-by-step production process for edtech_vertical"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify FERPA and COPPA compliance requirements for student data handling.  
2. Analyze LMS integration standards (LTI 1.3, IMS Global).  
3. Map data privacy frameworks (GDPR, FERPA) to EdTech use cases.  
4. Survey common EdTech vertical use cases (e.g., adaptive learning, assessment tools).  
5. Document stakeholder needs: schools, parents, developers, regulators.  
6. Evaluate existing LMS APIs for compatibility and security features.  

## Phase 2: COMPOSE  
1. Define artifact structure per SCHEMA.md (sections: compliance, integration, privacy).  
2. Write FERPA/COPPA compliance section with data minimization examples.  
3. Draft LTI integration specs (OAuth 2.0, resource links, tool configuration).  
4. Outline student data privacy protocols (encryption, access controls).  
5. Develop use case scenarios (e.g., secure grade sync, third-party tool access).  
6. Reference OUTPUT_TEMPLATE.md for formatting (headers, bullet points, code blocks).  
7. Embed LTI code snippets (e.g., tool launch URL, placement options).  
8. Cross-reference schema elements with template placeholders.  
9. Finalize artifact with regulatory citations and LMS vendor examples.  

## Phase 3: VALIDATE  
- [ ] Verify FERPA data minimization: only collect student records necessary for stated purpose.
- [ ] Confirm COPPA parental consent mechanism is explicit for users under 13.
- [ ] Confirm LTI 1.3 OAuth 2.0 launch flow uses IMS Global Security Framework v1.0.
- [ ] Confirm 1EdTech xAPI or Caliper standard cited for learning analytics data.
- [ ] Verify district procurement path: state ed-tech approval list or ISTE certification noted.
- [ ] Confirm artifact adheres to bld_schema_edtech_vertical.md ID pattern and required fields.
