# Collatz-Montmory

This directory is for the Collatz-Montmory mathematical workstream.

The rule for this track is strict:

```text
Only publish statements that are proved or reproducibly verified.
Everything else must be labeled conjecture, heuristic, observation or open question.
```

No claim of a proof of the Collatz conjecture should appear here unless the
proof has survived a line-by-line formal audit.

## Scope

This track may contain:

- definitions of the Collatz-Montmory map or reformulation;
- notation and normalization choices;
- proved lemmas;
- finite computational verification;
- invariants, variants or ranking functions;
- parity-vector or accelerated-map analysis;
- counterexample searches;
- links to other repositories where the work is implemented.

## Baseline classical map

The classical Collatz map is

```text
T(n) = n/2       if n is even
T(n) = 3n + 1   if n is odd
```

The standard accelerated odd map is

```text
A(n) = (3n + 1) / 2^v2(3n + 1), for odd n.
```

Any Collatz-Montmory variant must state exactly how it differs from these maps.

## Initial files

| File | Purpose |
|---|---|
| `definitions.md` | Canonical definitions of maps, domains and notation |
| `verified-lemmas.md` | Only proved lemmas or mechanically checked identities |
| `computational-verification.md` | Finite search methods, ranges, hashes and reproducibility |
| `conjectures.md` | Unproved statements, clearly separated from verified results |
| `audit-log.md` | Line-by-line mathematical audit status |
| `scripts/` | Reproducible verification scripts |
| `tests/` | Tests for scripts and identities |

## Verification standard

Every claim must include one of these labels:

| Label | Meaning |
|---|---|
| `proved` | A complete mathematical proof is written in this directory |
| `mechanically verified` | A finite identity or range was checked by script |
| `computational evidence` | Empirical evidence only; not a proof |
| `heuristic` | Plausible argument, not rigorous |
| `conjecture` | Explicitly unproved statement |
| `open` | Question with no current claim |

## First task

Before any result is added, write `definitions.md` with:

1. the exact Collatz-Montmory map;
2. its domain;
3. whether zero, negative integers or only positive integers are included;
4. whether the map is classical, accelerated, normalized or transformed;
5. the equivalence, if any, to the classical Collatz conjecture.
