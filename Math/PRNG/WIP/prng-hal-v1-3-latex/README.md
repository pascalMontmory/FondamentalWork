# TACM / PRNG Diagnostics v1.3

This directory contains the LaTeX working version of TACM / PRNG Diagnostics v1.3.

Superseded for publication by:

```text
Math/PRNG/publication/hal/hal-05633702v1/
```

The v1.3 document focuses on interpretation of null-calibrated seed diagnostics:

- ECDF interpretation of `Z_s`;
- three-class verdicts: `compatible`, `calibration_drift`, `tail_anomaly`;
- exact binomial calibration for rare-event indicators;
- simple injected-defect power tests;
- synthesis tables for a publishable short revision.

Build:

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Main message:

```text
TACM does not replace TestU01. It adds a Monte Carlo workload-facing layer
that quantifies and classifies seed sensitivity in a statistically calibrated
and interpretable way.
```
