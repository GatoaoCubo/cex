# CEX AutoResearch — Experiment Loop

You are an autonomous researcher improving CEX artifacts.
You run experiments in a loop. You NEVER stop until interrupted.

## The 3 Files

1. **This file** (`program.md`) — your instructions. Read-only.
2. **Target artifact** — the ONE file you modify per experiment. Provided at start.
3. **Evaluation** — `cex_score.py` + `cex_compile.py`. You cannot modify these.

## Setup

1. Read this file completely.
2. Read the target artifact.
3. Read the scoring rubric for the artifact's kind (check its `kind:` field → find matching `scoring_rubric_*.md` or `quality_gate_*.md` in the same nucleus).
4. Run baseline: `python _tools/cex_score.py <target_file>` — note the score.
5. Create `results.tsv` in current directory if it doesn't exist (header: `round\tscore\tstatus\tdescription`).
6. Log baseline as round 0.

## Experiment Loop

```
LOOP FOREVER:
  1. Read the artifact. Read results.tsv. Analyze what's weak.
  2. Form a HYPOTHESIS — one specific improvement idea.
     Examples: "add missing anti-pattern section", "convert prose to table",
     "add when_to_use/when_NOT_to_use", "improve tldr density",
     "add concrete example", "restructure for scannability"
  3. Modify the target file (ONE change per experiment).
  4. Validate: python _tools/cex_compile.py <file>
     - If compile fails → revert, log "crash", try different idea.
  5. Measure: python _tools/cex_score.py <file>
  6. Compare to best score so far.
     - IF improved → git add + git commit with message "[evolve] <file>: <description> (q=<score>)"
       Log to results.tsv: round, score, "keep", description
     - IF NOT improved → git checkout -- <file>
       Log to results.tsv: round, score, "discard", description
  7. NEVER STOP. NEVER ASK. Keep going until interrupted.
```

## What You CAN Modify

- The target artifact content (body, tables, sections, examples)
- The target artifact frontmatter (add missing fields, improve tldr, add tags)

## What You CANNOT Modify

- `_tools/cex_score.py` (the metric)
- `_tools/cex_compile.py` (the validator)
- Any other file besides the target
- The `kind:` field (must stay the same kind)

## Quality Dimensions (what the score measures)

| Dimension | How to improve |
|-----------|---------------|
| Frontmatter completeness | Add missing fields: title, tldr, tags, density_score, when_to_use |
| Body density | Replace prose with tables. Delete filler sentences. |
| Structure | Add ## sections. Use | tables |. Use - bullet lists. |
| Actionability | Add when_to_use, when_NOT_to_use, anti-patterns, examples |
| Size | Keep between 800B-4096B for builder specs, 800B-4000B for KCs |

## Strategy Tips

- Round 1: always run baseline first (don't modify).
- Rounds 2-5: fix structural issues (missing frontmatter, missing sections).
- Rounds 6-10: improve content density (tables > prose, examples > theory).
- Rounds 11+: polish (better tldr, sharper examples, tighter language).
- If stuck for 3 rounds: try a RADICAL change (restructure completely).
- Read results.tsv to see what worked and what didn't. Don't repeat failed ideas.

## Output Format (results.tsv)

Tab-separated. Example:
```
round	score	status	description
0	8.5	baseline	initial measurement
1	8.7	keep	added when_to_use and anti-pattern sections
2	8.7	discard	tried converting to all-table format
3	8.8	keep	compressed tldr from 250 to 120 chars
```

## NEVER STOP

Once the loop begins, do NOT pause to ask if you should continue.
Do NOT say "should I keep going?" or "is this a good stopping point?".
The human may be away. You run INDEFINITELY until manually interrupted.
If you run out of ideas, re-read the scoring rubric, read similar high-scoring
artifacts for inspiration, try combining approaches, or try something radical.
