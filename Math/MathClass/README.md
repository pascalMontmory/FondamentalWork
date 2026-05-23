# MathClass

MathClass is a research area for arithmetic classes viewed through terminal
observation maps.

**Current status:** the class-signature research programme, reports, PDF and
large scans are kept in `non-validated/`. The exact finite identities are useful
and tested, but the broader interpretation as a theory of arithmetic classes is
not validated as an asymptotic result.

The current application is Collatz terminal entrance:

```math
\mathcal F \longmapsto \nu_{B,\mathcal F,N}.
```

Here `\mathcal F` may be:

- all integers;
- odd integers;
- a residue class `n = a mod q`;
- primes;
- prime patterns such as twins `{p:p,p+2 prime}`;
- cousins `{p:p,p+4 prime}`;
- sexy primes `{p:p,p+6 prime}`;
- any explicitly defined arithmetic class.

## Verified Finite Content

The scripts verify structural facts at finite `N`, not prime-number
asymptotics:

- empirical terminal laws are probability measures on a finite state space;
- disjoint class unions give exact finite convex decompositions;
- terminal fibers are pure classes;
- terminal laws induce a pseudometric on classes by total variation distance;
- bound projection is exact at finite `N`;
- projection contracts total variation distance;
- if component limits exist, the same algebraic identities pass to limits.

## Not Proved

This framework does **not** prove:

- Collatz;
- Hardy-Littlewood;
- infinitely many twin primes;
- existence of terminal limits for primes, twins, cousins, or sexy primes;
- a special role for `B=89`.

## Files

- `non-validated/mathclass-terminal-signatures.md`: readable research note for
  the class-signature framework.
- `non-validated/mathclass_terminal_signatures.tex`: full LaTeX report.
- `non-validated/mathclass_terminal_signatures.pdf`: compiled report.
- `non-validated/terminal-signature-verification-protocol.md`: verification
  protocol for exact identities and experimental convergence scans.
- `non-validated/reports/terminal-signature-tests-2026-05-23.md`: first
  diagnostic test report.
- `non-validated/reports/large-scan-2026-05-23/`: large scan at
  `N=300000,1000000,3000000` with CSV and SVG curves for prime-pattern
  distances and terminal filter mass.
- `scripts/check_mathclass_identities.py`: finite verification script for
  mixture and projection identities.

## Reproduce

Compile the PDF locally:

```bash
latexmk -pdf -interaction=nonstopmode Math/MathClass/non-validated/mathclass_terminal_signatures.tex
```

Run the finite checks:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/check_mathclass_identities.py
```

Run experimental scans:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_terminal_signature_convergence.py --limits 10000,30000,100000 --bounds 27,89,127
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/scan_prime_pattern_terminal_signatures.py --limits 10000,30000,100000 --bounds 27,89,127 --terminal-set 14,23,61,89
```

Generate the larger prime-pattern curves:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/generate_prime_pattern_curves.py --limits 300000,1000000,3000000 --bounds 27,89,127 --terminal-set 14,23,61,89
```
