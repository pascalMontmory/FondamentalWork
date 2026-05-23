# Repository Structure

This repository is a research workspace for GUP, UV/IR, holography, cosmology,
public-data tests, twin-sector hypotheses and cold-atom sensor applications.

The goal of this document is to make the repository readable as a professional
research project rather than as a chronological collection of personal notes.

## Current organization

The repository is organized by research track. Each top-level directory is a
self-contained module with its own README, manuscript sources, notes, scripts
and reports when applicable.

```text
FondamentalWork/
  README.md
  docs/
  cellule-phase-deformee-gup/
  cellule-phase-vitesse-gup/
  relations-uv-ir-holographie-gup/
  contrainte-energie-noire-gup/
  conclusions-cosmologiques-gup-uvir/
  theorie-holographique-uvir-cellule-phase-deformee/
  constante-structure-fine-uvir/
  consequences-alpha-uvir-electromagnetisme/
  tests-donnees-publiques-gup-uvir/
  programmes-verification-publique-uvir/
  programme-tests-experimentaux-uvir/
  univers-jumeau-masse-negative-temps-inverse/
  synthese-travaux-confirmes-gup-uvir/
```

## Track types

Use these labels consistently in READMEs and publication summaries.

| Label | Meaning |
|---|---|
| `core` | Mathematical or theoretical foundation of the framework |
| `constraint` | No-go, exclusion or consistency constraint |
| `application` | Engineering or observational application of the framework |
| `test` | Public-data or reproducibility test program |
| `synthesis` | Curated synthesis of confirmed and rejected results |
| `speculative` | Conceptual extension that must not be mixed with confirmed results |

## Scientific status labels

Every track should state its status explicitly.

| Status | Meaning |
|---|---|
| `verified algebra` | Formula checked internally, but not an experimental claim |
| `numerically reproduced` | Recomputed with scripts and public constants/data |
| `observationally constrained` | Compared with public observational bounds |
| `candidate conjecture` | Coherent hypothesis, not yet established |
| `rejected as primary mechanism` | Useful negative result or no-go result |
| `engineering proposal` | Design framework or metrology protocol, not a built instrument |

## Standard module layout

A professional module should converge toward this layout:

```text
track-name/
  README.md                         # Scope, status, entry points
  main.tex                          # Main manuscript, if applicable
  PUBLICATION.md                    # Human-readable publication draft, if applicable
  notes/                            # Internal audits and derivations
  scripts/                          # Reproducible computations
  reports/                          # Generated or curated reports
  reports/data/                     # Generated CSV/data outputs, usually not committed
  reports/figures/                  # Generated figures, usually not committed
```

Existing tracks do not need to be moved immediately if that would break LaTeX or
script paths. Prefer first adding professional documentation, then migrate paths
track by track.

## Generated artifacts policy

Generated artifacts should be reproducible from source and are normally kept out
of Git:

- LaTeX products: `*.pdf`, `*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.out`
- generated CSV tables under `reports/data/`
- generated PNG figures under `reports/figures/`
- generated JSON summaries under `reports/*_summary.json`

Exceptions are allowed when a report is the primary review artifact. In that
case prefer Markdown reports over binary PDFs.

## Migration plan

Recommended non-breaking migration order:

1. Keep the current top-level track directories stable.
2. Add professional root documentation under `docs/`.
3. Normalize every track README with: purpose, status, entry points, commands,
   outputs, limitations.
4. Move obsolete scratch files into `notes/archive/` only after checking links.
5. Move generated artifacts out of Git or regenerate them in CI/local scripts.
6. Create release branches or tags for publication-ready states.

Avoid mass renames until scripts, LaTeX sources and relative links have been
updated and tested.
