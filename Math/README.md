# Math

This namespace is for mathematical foundations shared across projects.

It is deliberately separate from `COSMO/`: the goal is to keep reusable
mathematics, formalisms and proof scaffolding independent from a specific
physics or software repository.

## Initial focus

The first planned track is the VDF framework:

```text
Math/VDF/
```

The exact definition of VDF should be fixed in the first dedicated document. It
should capture the mathematical structure that supports several of the other
repositories, not only the cosmology work.

## Intended contents

Use `Math/` for:

- definitions and axioms;
- reusable notation;
- lemmas and proofs;
- algebraic identities;
- geometric or variational formalisms;
- links between VDF and applied repositories;
- minimal test scripts for symbolic or numerical sanity checks.

Do not use `Math/` for:

- repo-specific implementation details;
- generated plots or reports from applications;
- speculative physics claims without a mathematical statement;
- operational documentation for unrelated software.

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

## Review rule

A mathematical note should state:

- the objects being defined;
- the assumptions;
- the theorem, lemma or identity being claimed;
- whether it is proved, conjectural or only a working definition;
- where it is used in other repositories.
