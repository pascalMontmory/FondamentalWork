# Math Formula Audit

This file defines how mathematical formulas should be audited before being presented as verified.

## Audit Levels

| Level | Meaning |
| --- | --- |
| `A0 inventory` | Formula identified, source file and context recorded. |
| `A1 syntax` | Notation, dimensions, and domain assumptions checked. |
| `A2 derivation` | Algebraic derivation checked line by line. |
| `A3 computation` | Numerical or symbolic check is reproducible locally. |
| `A4 theorem` | Full proof is written with hypotheses and conclusion. |

## Rule For Publication

Only `A3` bounded computational claims and `A4` mathematical claims should be described as verified. `A1` and `A2` are useful review stages but are not enough to advertise a result as established.

## Current Branch Status

This restructuring branch creates the audit framework and namespaces. It does not claim that every formula in the repository has already passed a full mathematical audit.