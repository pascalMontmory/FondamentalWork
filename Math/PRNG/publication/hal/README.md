# HAL Publications

## Current HAL Deposit

```text
hal-05633702v1
TACM / PRNG Structural Diagnostics
Pré-publication, Document de travail
Deposit date: 2026-05-26
```

Current submitted files are stored in:

```text
hal-05633702v1/
```

The current manuscript supersedes the earlier v1.0 draft as the repository's primary HAL-submitted PRNG document. It adds:

- empirical-measure formulation;
- null-calibrated seed-conditioned variance diagnostics;
- ECDF interpretation;
- exact rare-event binomial calibration;
- reproducible public CPU-only baseline;
- explicit separation between reproducible evidence and reported evidence requiring archival raw logs.

## Earlier Draft

The earlier v1.0 draft remains archived here:

```text
Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.pdf
Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.tex
```

Its original metadata are kept in `HAL_METADATA.md` for traceability.

## Build Current Submitted PDF

From `hal-05633702v1/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error tacm-prng-structural-diagnostics-hal-05633702v1.tex
pdflatex -interaction=nonstopmode -halt-on-error tacm-prng-structural-diagnostics-hal-05633702v1.tex
```
