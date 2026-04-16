---
kind: examples
id: bld_examples_course_module
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of course_module artifacts
quality: 8.8
title: "Examples Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, examples]
tldr: "Golden and anti-examples of course_module artifacts"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
---
title: "Introduction to Data Science"
vendor: "edX"
version: "2.1"
type: course_module
---
**Learning Objectives**
- Understand fundamental statistical concepts
- Apply Python for data analysis
- Interpret machine learning model outputs

**Content**
Week 1: Statistics basics (mean, median, variance)
Week 2: Python libraries (Pandas, NumPy)
Week 3: Supervised learning algorithms

**Assessments**
- Weekly quizzes via [Quizizz](https://quizizz.com)
- Final project: Analyze a public dataset using Jupyter Notebooks
- Peer reviews on [Moodle](https://moodle.org)

**References**
- "Python for Data Analysis" by Wes McKinney
- edX course materials

## Anti-Example 1: Missing Core Elements
---
title: "Quick Python Guide"
vendor: "Udemy"
version: "1.0"
type: course_module
---
**Content**
- Basics of syntax
- Loops and functions

**Assessments**
- No assessments listed

## Why it fails
Lacks learning objectives and assessments, making the module incomplete and unmeasurable.

## Anti-Example 2: Boundary Violation
---
title: "Prompt Engineering Basics"
vendor: "Coursera"
version: "0.5"
type: course_module
---
**Learning Objectives**
- Create effective prompts for AI models

**Content**
- Prompt templates for different tasks
- Example: "Act as a {role} and {task}"

**Assessments**
- Self-assessment checklist

## Why it fails
Includes prompt templates, which are explicitly excluded from the course_module boundary.
