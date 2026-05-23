# COSMO Non-Validated Area

This directory is the canonical place for COSMO hypotheses, draft articles, speculative derivations, negative diagnostics, and analyzed but **not verified** claims.

## Status Rule

Files in this directory may contain useful scientific ideas, candidate formulas, numerical clues, or publication drafts. They must not be cited as established results.

A file may leave this directory only if one of the following is true:

1. the derivation is complete and internally checked;
2. the result is explicitly conditional and all assumptions are visible;
3. a numerical/observational claim has a reproducible script, stated data source, stated parameter range, and uncertainty estimate;
4. the file has been rewritten as an executive summary that separates verified, conditional, and conjectural claims.

## Difference From `COSMO/work/`

- `non-validated/`: hypotheses, draft manuscripts, speculative claims, rejected or weakened claims, and research programs.
- `work/`: scripts, reproducibility notes, generated local outputs, and temporary analysis products.
- `COSMO/` track roots: only polished track entry points, verified or explicitly conditional summaries, and stable papers.

## Current COSMO Non-Validated Families

## Migrated Tracks

The first migration pass moved these full tracks here:

| Track | Reason for non-validated status |
|---|---|
| `constante-structure-fine-uvir/` | The README explicitly presents an `alpha--UV/IR` conjecture. |
| `consequences-alpha-uvir-electromagnetisme/` | Consequences depend on the non-validated alpha/UVIR conjecture. |
| `programme-tests-experimentaux-uvir/` | This is a test plan and decision matrix, not a validated result. |
| `conclusions-cosmologiques-gup-uvir/` | Interpretive/open cosmological conclusions, including theoretical blocks still to prove. |

These tracks can be promoted later file by file if a proof, a bounded reproducible computation, or a precise conditional theorem is added.

### GUP / UVIR Master Framework

- candidate GUP deformation laws;
- dynamic UV/IR relations;
- holographic scaling assumptions;
- vacuum regularization mechanisms not yet derived from a complete theory.

### Dark-Energy Constraint

- claims linking a GUP-regulated vacuum density to the observed cosmological constant;
- parameter choices or beta constraints that rely on unproven assumptions;
- no-go or compatibility statements not yet cross-checked against literature.

### Fine-Structure Constant and Electromagnetism

- conjectural links between UV/IR structure and `alpha`;
- electromagnetic consequences not yet derived from a complete model;
- numerology or fitted constants pending out-of-sample tests.

### Public-Data and Observational Tests

- Planck/BAO/SNe/FIRAS/SPARC/BBN/neutron-star comparisons that are not yet packaged with scripts, data sources, and uncertainty propagation;
- exploratory fits and plots.

### Quantum Sensor Applications

- sensor-noise-budget extensions that are reproducible but not yet tied to a validated physical derivation;
- benchmark comparisons needing clear assumptions and data provenance.

## Promotion Checklist

Before moving material out of this directory, add:

- exact claim statement;
- assumptions separated from conclusions;
- derivation or reproducible computation;
- comparison to known literature;
- numerical values with units and uncertainty where applicable;
- data/source provenance for observational checks;
- explicit statement of what is not proven.

## Current Policy

When in doubt, put a COSMO claim here first. Promote only after review.
