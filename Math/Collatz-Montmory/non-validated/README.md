# Collatz-Montmory Non-Validated Area

This directory is the canonical place for Collatz-Montmory hypotheses, draft articles, negative diagnostics, and research ideas that have been studied but are **not verified mathematical results**.

## Status Rule

Files in this directory may contain useful formulas, tests, conjectures, or publication drafts, but they must not be cited as established results.

A file may leave this directory only if one of the following is true:

1. it contains a complete proof;
2. it contains a clearly bounded computational theorem with reproducible code and stated limits;
3. it has been rewritten as an explicitly conditional theorem with all assumptions visible.

## Difference From `work/`

- `non-validated/`: hypotheses, draft articles, interpreted diagnostics, negative results, and open research programs.
- `work/scripts/`: executable exploratory scripts used to reproduce diagnostics.
- root `Math/Collatz-Montmory/`: verified-facing identities, definitions, and carefully conditional results only.

## Current Non-Validated Families

### Lambda_B and Bound Classes

- moving entrance laws `Lambda_B`;
- bound equivalence classes;
- terminal correction laws beyond the exact algebraic identities;
- claims involving the existence of a limit law.

### C_Montmory and Hardy-Littlewood Filtering

- candidate coefficient `C_Montmory`;
- filtered Hardy-Littlewood coefficient formulas;
- local bias products;
- threshold calibration by a target density.

### Resonance Centers

- interpretation of a bound as a passage or oscillation center;
- multiplicative windows around a center `B`;
- full passage law `(P_{B,eta}, U_{B,eta}, R_{B,eta})`;
- current negative diagnostics for a twin-prime-specific signal at `B=89`.

### Terminal Law Proof Programs

- proof program for terminal entrance measures `nu_{B,F,N}`;
- exact finite projectivity under bound projection;
- conditional terminal Hardy-Littlewood law for twins;
- open problem: existence of terminal limits for residue classes, positive-density families, primes, and twin-prime starts.
- direct application note for resonance testing, terminal filters, and artifact rejection.

### Collatz-Montmory Draft Articles

- draft publication notes;
- previously analyzed proposals;
- abandoned or weakened claims.

## Current Files

- `resonance-hypotheses-status.md`: current status of resonance claims and negative diagnostics around `B=89`.
- `terminal-measures-applications.md`: application note for terminal measure diagnostics, projection tests, and conditional Montmory filters.
- `terminal-laws-proof-program.md`: corrected non-validated proof program for terminal entrance laws; includes verified finite projectivity and explicitly conditional asymptotic statements.

## Current Hypothesis Status

- `89` is **not** validated as canonical.
- `89` is **not** currently supported as a twin-prime-specific passage resonance under the `eta=0.08` window test up to `10^7`.
- `89` may still be used as a terminal-bound representative inside the separate `Lambda_B` framework, but that framework remains conditional on existence of the limiting law.

## Promotion Checklist

Before moving a result out of this directory, add:

- exact definitions;
- proof or bounded computation;
- assumptions separated from conclusions;
- comparison to controls or known literature;
- reproducible script path if numerical;
- explicit statement of what is not proven.
