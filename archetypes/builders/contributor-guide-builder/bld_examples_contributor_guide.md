---
kind: examples
id: bld_examples_contributor_guide
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of contributor_guide artifacts
quality: 8.9
title: "Examples Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, examples]
tldr: "Golden and anti-examples of contributor_guide artifacts"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Golden Example
**Contributing to Kubernetes**
**Developer Setup**  
1. Install [Go 1.20+](https://golang.org/dl/)  
2. Clone repo: `git clone https://github.com/kubernetes/kubernetes.git`  
3. Run: `make generate && make test`  
**PR Flow**  
1. Fork repo on GitHub  
2. Create branch: `git checkout -b feature/your-fix`  
3. Commit with [Conventional Commits](https://www.conventionalcommits.org/)  
4. Submit PR to `main` with title prefix: `kind/`  
**Coding Standards**  
- Use GoFmt and [golint](https://github.com/golang/lint)  
- 100% test coverage required  
- No unreviewed dependencies  

**Review Process**  
- Requires 2 LGTMs from maintainers  
- Code owners must approve  
- Merge via GitHub squash  

**CLA**  
All contributors must sign [Apache 2.0 CLA](https://cla.apache.org/)  

## Anti-Example 1: Missing CLA Section
**Contributing to ExampleProject**  
**Developer Setup**  
Install Node.js and run `npm install`.  

**PR Flow**  
Submit PRs to `develop` branch.  

**Coding Standards**  
Use ESLint and write tests.  

**Review Process**  
Maintainers will review within 7 days.  

**Why it fails**  
No CLA requirement specified. Contributors may submit code without legal agreement, risking project liability.  

## Anti-Example 2: Vague Setup Instructions
**Contributing to SampleApp**  
**Developer Setup**  
"Set up your environment."  

**PR Flow**  
"Follow standard process."  

**Coding Standards**  
"Follow best practices."  

**Review Process**  
"Get feedback from team."  

**Why it fails**  
Instructions are too vague. Contributors cannot reproduce the environment or follow workflow, leading to failed contributions and wasted time.