# Collatz-Montmory Definitions

No custom Collatz-Montmory definition is verified in this file yet. This file is the place to write the exact objects before any theorem is stated.

## Baseline Collatz Map

For reference, the classical Collatz map on positive integers is

```text
C(n) = n / 2        if n is even
C(n) = 3n + 1      if n is odd
```

The accelerated odd-only map, when used, must be defined separately with its domain and valuation convention.

## Required For Any Montmory Variant

A Montmory variant must state:

- the domain;
- the transition map;
- whether the map is classical, accelerated, modular, weighted, or symbolic;
- the invariant or descent quantity being studied;
- the exact meaning of convergence, cycle, stopping time, and exception.

Until those definitions are fixed, no Collatz-Montmory theorem should be marked as verified.