# MathClass

MathClass is the verified-facing framework for arithmetic classes viewed through
terminal observation maps.

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

## Verified Content

The current theorem package proves structural facts, not prime-number
asymptotics:

- empirical terminal laws are probability measures on a finite state space;
- disjoint class unions give exact finite convex decompositions;
- terminal fibers are pure classes;
- terminal laws induce a pseudometric on classes by total variation distance;
- bound projection is exact at finite `N`;
- projection contracts total variation distance;
- if component limits exist, the same algebraic identities pass to limits;
- conditional Hardy-Littlewood terminal laws give conditional filtered
  coefficients.

## Not Proved

This framework does **not** prove:

- Collatz;
- Hardy-Littlewood;
- infinitely many twin primes;
- existence of terminal limits for primes, twins, cousins, or sexy primes;
- a special role for `B=89`.

## Files

- `mathclass-terminal-signatures.md`: readable summary of the demonstrated
  framework.
- `mathclass_terminal_signatures.tex`: full LaTeX report.
- `scripts/check_mathclass_identities.py`: finite verification script for
  mixture and projection identities.

## Reproduce

Compile the PDF locally:

```bash
latexmk -pdf -interaction=nonstopmode Math/MathClass/mathclass_terminal_signatures.tex
```

Run the finite checks:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 Math/MathClass/scripts/check_mathclass_identities.py
```
