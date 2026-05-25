# HAL Publication Draft

Upload this PDF to HAL:

```text
Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.pdf
```

The LaTeX source is:

```text
Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.tex
```

HAL upload metadata are prepared in:

```text
HAL_METADATA.md
```

Build command:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.tex
pdflatex -interaction=nonstopmode -halt-on-error Montmory_Structural_Diagnostic_Framework_for_PRNGs_v1.0.tex
```

Current PDF status:

- 13 pages, A4;
- English abstract and French summary;
- HAL title: `Structural Stability Diagnostics for Pseudo-Random Number Generators: Seed Sensitivity and Functional Variance Dispersion`;
- no confidential correspondence;
- no proprietary recurrence details;
- includes BigCrush ARM/Metal/CUDA summary and SHA-256 manifest;
- includes GSQI and epsilon(T) public definitions;
- includes a numeric inter-seed dispersion table with min/max variances and ratios;
- labels missing SmallCrush, x86, stream hashes, adapter source, and benchmark artifacts explicitly.
