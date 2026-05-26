# PRNG Structural Diagnostics v1.2 LaTeX Draft

This directory contains a HAL-oriented LaTeX draft for PRNG Structural Diagnostics v1.2.

Build locally with:

```bash
pdflatex main.tex
pdflatex main.tex
```

The draft complements:

- `Math/PRNG/WIP/prng-structural-diagnostics-v1-2-hal-revision.md`
- `Math/PRNG/WIP/prng-ztest/`

Current WIP reference run:

```text
N=50000
R=8
seeds=1000 per generator
generators=MT19937, PCG64, Philox, SFC64
```

Local compiled artifact on the VPS:

```text
/home/pascal/prng-hal-v1-2-latex/main.pdf
```

The PDF is generated from this LaTeX source. The GitHub connector available in this session is reliable for UTF-8 source files; binary PDF upload should be done through GitHub UI, `gh api`, or a normal authenticated GitHub upload path when available.
