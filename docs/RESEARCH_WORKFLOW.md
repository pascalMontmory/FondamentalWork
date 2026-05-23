# Research Workflow

This document defines how new work should be added to the repository.

## Principle

A result should move through four stages:

```text
idea -> derivation -> reproducible test -> publication artifact
```

A folder can contain exploratory notes, but the README must make clear what is
confirmed, what is conditional and what is speculative.

## Stage 1 - Idea

Use notes for early exploration:

```text
track-name/notes/topic.md
```

A note should include:

- the question being tested;
- the assumptions;
- the equations used;
- a short verdict;
- links to scripts or publications if the idea matures.

## Stage 2 - Derivation

Move stable derivations into a manuscript or publication draft:

```text
track-name/main.tex
track-name/PUBLICATION.md
```

The derivation should identify:

- definitions;
- dimensional checks;
- limiting cases;
- known physics recovered;
- where the model adds an assumption.

## Stage 3 - Reproducible test

Every numerical claim should have a script when possible:

```text
track-name/scripts/test_or_simulate_topic.py
```

Scripts should write reproducible outputs under:

```text
track-name/reports/
track-name/reports/data/
track-name/reports/figures/
```

Keep source scripts and Markdown reports in Git. Keep generated binary outputs
out of Git unless they are intentionally part of a release.

## Stage 4 - Publication artifact

A publication-ready track should have:

- a clear title;
- an abstract or summary;
- a statement of novelty;
- a limitations section;
- a reproducibility section;
- a references section;
- a short status statement.

## Required README sections

Each top-level track README should converge toward this structure:

```text
# Track title

## Purpose
## Status
## Main result
## Files
## Reproducibility
## Outputs
## Limitations
## Next steps
```

## Quality gates

Before opening or updating a PR, run the relevant subset:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/test_*.py
latexmk -pdf -interaction=nonstopmode main.tex
```

For tracks with multiple publication files, compile the specific `.tex` files
listed in the track README.

## Claims policy

Use disciplined language:

- say `derives` only when the result follows from stated assumptions;
- say `reproduces` when a script recomputes a value from public constants/data;
- say `suggests` for conjectural numerical proximity;
- say `is excluded` only when the tested assumptions and public bound are clear;
- say `engineering proposal` for sensor or metrology designs not yet built.

## Speculative material

Speculative tracks are allowed, but they must be isolated. They should not be
mixed into confirmed synthesis documents unless clearly labeled.

The twin-sector / Moebius / zero-mode work is currently a speculative extension.
It can motivate tests and interpretations, but it should not be presented as a
confirmed derivation of local constants or laboratory measurements.

## Review checklist

Before a document is considered professional, check:

- the scope is explicit;
- the status label is explicit;
- assumptions are listed;
- equations have dimensions checked;
- generated results are reproducible;
- negative results are preserved;
- speculative claims are separated from verified claims;
- generated artifacts are not mixed with source unless intentional.
