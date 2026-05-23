# Collatz-Montmory Work Area

This directory is now reserved mainly for executable work products, especially reproducible exploratory scripts.

For hypotheses, draft articles, analyzed but non-verified claims, and negative diagnostics, use:

```text
Math/Collatz-Montmory/non-validated/
```

## Current Role

- `scripts/`: exploratory and reproducibility scripts.
- legacy Markdown files still present here are non-validated unless promoted or migrated.
- new non-verified research notes should go to `../non-validated/`.

## Current Scripts

- `compute_terminal_measures.py`: computes finite terminal entrance laws and checks exact projection consistency between bounds.
- `evaluate_lambda_limit.py`: exploratory diagnostics for moving-depth entrance laws.
- `evaluate_local_dynamics.py`: local dynamics diagnostics.
- `evaluate_montmory_filter.py`: exploratory Montmory filter diagnostics.
- `evaluate_resonance_bounds.py`: candidate bound/window diagnostics.
- `evaluate_resonance_law_distance.py`: resonance-window law comparison between twins and controls.

## Rule

Do not cite files in this directory as verified results. Promote only after proof, bounded reproducible verification, or explicit conditional-theorem treatment.

## Migration Note

The repository is being split by status:

- verified-facing material: `Math/Collatz-Montmory/`
- non-validated hypotheses/articles: `Math/Collatz-Montmory/non-validated/`
- scripts and diagnostics: `Math/Collatz-Montmory/work/scripts/`
