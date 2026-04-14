---
kind: examples
id: bld_examples_diff_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of diff_strategy artifacts
quality: null
title: "Examples Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, examples]
tldr: "Golden and anti-examples of diff_strategy artifacts"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
kind: diff_strategy
description: Transition from FIFO to Pro-Rata matching algorithm
---
def match_order(book, incoming):
    if book.mode == "FIFO":
        # Match against the oldest orders first (First-In-First-Out)
        return match_sequential(book.orders, incoming)
    elif book.mode == "PRO_RATA":
        # Match based on the proportion of size relative to total volume
        return match_pro_rata(book.orders, incoming)

## Anti-Example 1: edit_format
---
kind: edit_format
description: Update log message style
---
# BAD: This only changes the string output, not the matching logic.
print(f"Order {id} matched") -> print(f"MATCH_EVENT: {id}")

## Why it fails
This is a change to the presentation layer (string formatting) rather than a change to the underlying matching algorithm or application logic.

## Anti-Example 2: parser
---
kind: parser
description: Change CSV delimiter to Pipe
---
# BAD: This changes how input is tokenized, not how orders are processed.
parts = line.split(",") -> parts = line.split("|")

## Why it fails
This is a change to the data ingestion/parsing layer. The logic of how the parsed data is used to match orders remains identical.
