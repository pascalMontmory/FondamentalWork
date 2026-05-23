# Conjectures

This file is for unproved statements only.

## Classical Collatz conjecture

Label: `conjecture`

For every positive integer `n`, repeated iteration of

```text
T(n) = n/2       if n is even
T(n) = 3n + 1   if n is odd
```

reaches `1`.

This repository does not currently contain a proof of this conjecture.

## Collatz-Montmory conjectures

Label: `open`

No Collatz-Montmory-specific conjecture is stated yet because the
Collatz-Montmory map is not defined in `definitions.md`.

When a conjecture is added, it must include:

```text
statement
map used
quantifier domain
known equivalence or non-equivalence to classical Collatz
verified finite range, if any
reason it is still unproved
```
