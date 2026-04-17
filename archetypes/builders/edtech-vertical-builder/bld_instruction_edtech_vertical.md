---
kind: instruction
id: bld_instruction_edtech_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for edtech_vertical
quality: 8.9
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
1. Define artifact structure per bld_schema_edtech_vertical.md (focus_area, target_demographic, compliance fields).  
2. Write FERPA/COPPA compliance section: name records type, data minimization approach, and parental consent flow.  
3. Draft LTI 1.3 integration specs: OAuth 2.0 + IMS Security Framework v1.0, resource links, tool configuration per Canvas/Moodle/Blackboard.  
4. Outline student data privacy protocols: AES-256 encryption, pseudonymization approach, access control model.  
5. Develop use case scenarios (e.g., secure grade sync via xAPI, COPPA-compliant onboarding for K-12).  
6. Reference bld_output_template_edtech_vertical.md for formatting (headers, tables, regulatory sections).  
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
