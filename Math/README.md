# Math

This namespace is reserved for reusable mathematical foundations that support several repositories or research tracks. It should not become a general note dump: each subdirectory needs definitions, assumptions, verified claims, conjectures, and reproducible checks where applicable.

## Workstreams

| Path | Scope |
| --- | --- |
| `VDF/` | Mathematical notes for verifiable-delay-function work. |
| `PRNG/` | Mathematical notes for pseudo-random-number-generator work. |
| `Collatz-Montmory/` | Collatz-Montmory definitions, verified lemmas, computational checks, and conjectures. |
| `MathClass/` | Verified structural framework for arithmetic classes, terminal signatures, projection, and class distances. |

## Verification Standard

A mathematical statement can be marked as verified only if it has at least one of the following:

- a complete written proof with explicit hypotheses;
- a symbolic derivation whose assumptions are stated;
- a reproducible computational verification with exact limits, command, code version, and expected output.

Claims without that support should stay in a conjecture or research-notes section.
