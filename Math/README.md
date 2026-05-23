# Math

This namespace is for mathematical foundations shared across projects.

It is deliberately separate from `COSMO/`: the goal is to keep reusable
mathematics, formalisms, algorithms and proof scaffolding independent from a
specific physics or software repository.

## Initial workstreams

| Track | Purpose | Status |
|---|---|---|
| `Math/VDF/` | Formalize the VDF mathematical framework shared across projects | definitions pending |
| `Math/PRNG/` | Formalize the mathematical and algorithmic structure of your PRNG | definitions pending |

VDF should capture reusable mathematical structure. PRNG should capture the
state transition, output function, period/statistical/security claims and test
vectors of the pseudo-random generator.

## Intended contents

Use `Math/` for:

- definitions and axioms;
- reusable notation;
- lemmas and proofs;
- algebraic identities;
- geometric or variational formalisms;
- algorithm definitions such as PRNG state transitions;
- links between mathematical workstreams and applied repositories;
- minimal test scripts for symbolic, numerical or statistical sanity checks.

Do not use `Math/` for:

- repo-specific implementation details;
- generated plots or reports from applications;
- speculative physics claims without a mathematical statement;
- operational documentation for unrelated software;
- security claims without a stated model and reproducible tests.

## Standard layout

Each mathematical track should converge toward:

```text
Math/topic-name/
  README.md
  definitions.md
  notation.md
  lemmas.md
  examples.md
  links-to-repos.md
  scripts/
  tests/
```

Algorithmic tracks such as PRNG may add:

```text
period.md
statistical-tests.md
security-model.md
reference-vectors.md
```

## Review rule

A mathematical note should state:

- the objects being defined;
- the assumptions;
- the theorem, lemma, identity or algorithmic claim being made;
- whether it is proved, conjectural, empirical or only a working definition;
- where it is used in other repositories.
